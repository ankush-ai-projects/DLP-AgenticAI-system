"""
training/train_model.py
Run karo: python training/train_model.py
"""

import spacy
from spacy.training import Example
from spacy.util import minibatch, compounding
import random
import json
from pathlib import Path
from datetime import datetime
import sys

sys.path.append(str(Path(__file__).parent.parent))
from training.train_data import TRAIN_DATA, VAL_DATA

MODEL_OUTPUT_DIR = Path("models/trained/dlp_ner_model")
METRICS_FILE     = Path("models/trained/training_metrics.json")

N_ITER      = 80
DROPOUT     = 0.2       # kam dropout — chhote dataset ke liye
BATCH_START = 2.0
BATCH_STOP  = 8.0       # chhota batch — zyada updates per epoch

LABELS = ["PERSON", "ADDRESS", "AADHAAR", "PAN", "CREDIT_CARD", "EMAIL", "PHONE"]


def validate(nlp_model, val_data):
    tp = fp = fn = 0
    for text, annotations in val_data:
        doc       = nlp_model(text)
        pred_ents = set((e.start_char, e.end_char, e.label_) for e in doc.ents)
        true_ents = set((s, e, l) for s, e, l in annotations["entities"])
        tp += len(pred_ents & true_ents)
        fp += len(pred_ents - true_ents)
        fn += len(true_ents - pred_ents)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1        = (2 * precision * recall / (precision + recall)
                 if (precision + recall) > 0 else 0.0)
    return {
        "precision": float(precision),
        "recall":    float(recall),
        "f1":        float(f1),
    }


def train():
    print("=" * 58)
    print("  DLP Custom NER — Training")
    print(f"  Started : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Examples: {len(TRAIN_DATA)} train / {len(VAL_DATA)} val")
    print("=" * 58)

    # Step 1 — blank model
    nlp = spacy.blank("en")

    # Step 2 — NER pipe
    ner = nlp.add_pipe("ner", last=True)
    for label in LABELS:
        ner.add_label(label)

    # Step 3 — examples banana + position verify
    print(f"\n[1/4] Training examples prepare kar raha hun...")
    train_examples = []
    skipped = 0
    for text, annotations in TRAIN_DATA:
        try:
            # Position verify karo — galat position = skip
            valid = True
            for start, end, label in annotations["entities"]:
                extracted = text[start:end]
                if not extracted.strip():
                    print(f"  BAD POS: '{text[:40]}' pos={start}:{end}")
                    valid = False
                    break
            if not valid:
                skipped += 1
                continue

            doc     = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            train_examples.append(example)
        except Exception as e:
            skipped += 1

    print(f"  {len(train_examples)} ready, {skipped} skipped")

    # Step 4 — training
    print(f"\n[2/4] Training — {N_ITER} epochs, dropout={DROPOUT}, batch={BATCH_START}-{BATCH_STOP}")
    print("-" * 58)

    optimizer   = nlp.begin_training()
    best_f1     = 0.0
    all_metrics = []
    no_improve  = 0

    for epoch in range(N_ITER):
        random.shuffle(train_examples)
        losses  = {}
        batches = minibatch(train_examples,
                            size=compounding(BATCH_START, BATCH_STOP, 1.001))
        for batch in batches:
            nlp.update(batch, drop=DROPOUT, losses=losses)

        metrics  = validate(nlp, VAL_DATA)
        ner_loss = float(losses.get("ner", 0))
        f1       = metrics["f1"]

        saved_marker = ""
        if f1 > best_f1:
            best_f1    = f1
            no_improve = 0
            MODEL_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            nlp.to_disk(MODEL_OUTPUT_DIR)
            saved_marker = " ← SAVED"
        else:
            no_improve += 1

        print(
            f"  Epoch {epoch+1:02d}/{N_ITER} | "
            f"Loss: {ner_loss:7.2f} | "
            f"P: {metrics['precision']:.3f} | "
            f"R: {metrics['recall']:.3f} | "
            f"F1: {f1:.3f}"
            f"{saved_marker}"
        )

        all_metrics.append({
            "epoch":     epoch + 1,
            "loss":      round(ner_loss, 4),
            "precision": round(metrics["precision"], 4),
            "recall":    round(metrics["recall"], 4),
            "f1":        round(f1, 4),
        })

        # Early stop — 15 epochs no improve ke baad
        if no_improve >= 15 and epoch > 25:
            print(f"\n  Early stop at epoch {epoch+1}.")
            break

    # Save metrics
    print("\n[3/4] Metrics save kar raha hun...")
    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(METRICS_FILE, "w") as f:
        json.dump({
            "trained_at": datetime.now().isoformat(),
            "n_train":    len(train_examples),
            "n_val":      len(VAL_DATA),
            "labels":     LABELS,
            "best_f1":    round(float(best_f1), 4),
            "epochs":     all_metrics,
        }, f, indent=2)

    # Sanity check
    print("\n[4/4] Sanity check...")
    trained = spacy.load(str(MODEL_OUTPUT_DIR))
    tests = [
        "Rahul Sharma ka PAN ABCDE1234F hai.",
        "Contact 9876543210 at Sector 14, Gurgaon.",
        "Email priya@gmail.com for Aadhaar 2345 6789 0123.",
        "Deepak Jain used card 4111111111111111 at Connaught Place.",
    ]
    for t in tests:
        doc  = trained(t)
        ents = [(e.text, e.label_) for e in doc.ents]
        print(f"  Input : {t}")
        print(f"  Found : {ents}\n")

    print("=" * 58)
    print(f"  Training complete! Best F1: {best_f1:.4f}")
    print(f"  Model : {MODEL_OUTPUT_DIR}")
    print("=" * 58)


if __name__ == "__main__":
    train()
