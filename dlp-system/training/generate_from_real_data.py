"""
training/generate_from_real_data.py

Tumhara real CSV data se training examples banata hai.
Run karo: python training/generate_from_real_data.py

Kya karta hai:
1. UP + Delhi addresses → ADDRESS training examples
2. Gmail IDs → EMAIL training examples  
3. PCI data → CREDIT_CARD training examples (real numbers generate karke)
4. Sab combine karke train_data.py generate karta hai
"""

import pandas as pd
import random
import re
from pathlib import Path

# ── File paths ────────────────────────────────────────────────────────
UP_ADDR_FILE    = "data/uttar_pradesh_75_districts_places.csv"
DELHI_ADDR_FILE = "data/Delhi_districts_places.csv"
EMAIL_FILE      = "data/valid_gmails_100k.csv"
PCI_FILE        = "data/pci_test_data_50k.txt"
OUTPUT_FILE     = "training/train_data.py"

# ── Kitne examples lene hain ──────────────────────────────────────────
N_ADDRESS     = 300   # address examples
N_EMAIL       = 300   # email examples
N_CREDIT_CARD = 200   # credit card examples
N_MIXED       = 150   # mixed (multiple entities ek sentence mein)

# ── Sentence templates ────────────────────────────────────────────────
ADDRESS_TEMPLATES = [
    "Customer lives at {addr}.",
    "Delivery address is {addr}.",
    "Please ship to {addr}.",
    "Registered address: {addr}.",
    "Send documents to {addr}.",
    "The property is located at {addr}.",
    "Branch office at {addr}.",
    "Permanent address: {addr}.",
    "Contact at {addr} for further details.",
    "Invoice to be sent at {addr}.",
]

EMAIL_TEMPLATES = [
    "Send OTP to {email} immediately.",
    "User registered with {email}.",
    "Statement sent to {email} successfully.",
    "Account linked to {email}.",
    "Please contact {email} for queries.",
    "OTP sent to {email}.",
    "Email {email} is not verified.",
    "Send report to {email}.",
    "Notification sent to {email}.",
    "Recovery email set to {email}.",
]

CARD_TEMPLATES = [
    "Transaction on card {card} was declined.",
    "Card {card} reported stolen.",
    "Charge card number {card} for INR 2000.",
    "New card {card} issued to customer.",
    "Disputed transaction on {card}.",
    "Card {card} was used at an ATM.",
    "Block card {card} immediately.",
    "Card {card} linked to this account.",
]

MIXED_TEMPLATES = [
    ("Customer {name} lives at {addr}. Contact: {email}.",
     ["PERSON", "ADDRESS", "EMAIL"]),
    ("{name} used card {card} at {addr}.",
     ["PERSON", "CREDIT_CARD", "ADDRESS"]),
    ("Send statement to {email} for {name}.",
     ["EMAIL", "PERSON"]),
    ("Card {card} linked to {email}.",
     ["CREDIT_CARD", "EMAIL"]),
    ("{name} at {addr}, email {email}.",
     ["PERSON", "ADDRESS", "EMAIL"]),
]

# ── Indian names for mixed examples ──────────────────────────────────
INDIAN_NAMES = [
    "Rahul Sharma", "Priya Singh", "Amit Kumar", "Sunita Verma",
    "Ravi Shankar", "Deepika Nair", "Suresh Patel", "Meena Patel",
    "Vikram Malhotra", "Ananya Krishnamurthy", "Kiran Bedi",
    "Manoj Tiwari", "Geeta Rani", "Shruti Desai", "Neha Joshi",
    "Tarun Khanna", "Rekha Iyer", "Dinesh Rao", "Pallavi Joshi",
    "Ramesh Babu", "Sanjay Gupta", "Nisha Agarwal", "Rohit Mehta",
    "Kavya Reddy", "Arun Joshi", "Pooja Sharma", "Harish Nair",
    "Leela Krishnan", "Farhan Akhtar", "Arjun Kapoor",
]


def generate_visa_card():
    """Valid Visa card number generate karo (Luhn algorithm)."""
    prefix = "4"
    number = prefix + "".join([str(random.randint(0, 9)) for _ in range(14)])
    # Luhn checksum
    total = 0
    reverse = number[::-1]
    for i, digit in enumerate(reverse):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    check = (10 - (total % 10)) % 10
    return number + str(check)


def generate_mastercard():
    """Valid Mastercard number generate karo."""
    prefix = random.choice(["51", "52", "53", "54", "55"])
    number = prefix + "".join([str(random.randint(0, 9)) for _ in range(13)])
    total = 0
    reverse = number[::-1]
    for i, digit in enumerate(reverse):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    check = (10 - (total % 10)) % 10
    return number + str(check)


def clean_address(addr: str) -> str:
    """Address clean karo — too long na ho."""
    addr = str(addr).strip()
    # India suffix hata do
    addr = re.sub(r",?\s*India\s*$", "", addr).strip()
    # 80 chars max
    if len(addr) > 80:
        # Last comma tak truncate karo
        parts = addr[:80].rsplit(",", 1)
        addr = parts[0].strip()
    return addr


def make_example(text: str, entity_text: str, label: str):
    """Ek spaCy training example banao — position auto-calculate."""
    start = text.find(entity_text)
    if start == -1:
        return None
    end = start + len(entity_text)
    return (text, {"entities": [(start, end, label)]})


def make_multi_example(text: str, entities: list):
    """Multiple entities wala example banao."""
    ents = []
    for entity_text, label in entities:
        start = text.find(entity_text)
        if start == -1:
            return None
        end = start + len(entity_text)
        # Overlap check
        overlap = any(not (end <= s or start >= e) for s, e, _ in ents)
        if overlap:
            return None
        ents.append((start, end, label))
    return (text, {"entities": ents})


def load_addresses(n: int) -> list:
    """Real addresses load karo."""
    print(f"  Loading addresses (n={n})...")
    dfs = []
    for fpath in [UP_ADDR_FILE, DELHI_ADDR_FILE]:
        if Path(fpath).exists():
            df = pd.read_csv(fpath, usecols=["Full_Address"])
            dfs.append(df)
        else:
            print(f"  WARNING: {fpath} nahi mila — data/ folder mein rakho")

    if not dfs:
        return []

    all_df = pd.concat(dfs, ignore_index=True)
    addresses = all_df["Full_Address"].dropna().tolist()
    random.shuffle(addresses)
    return [clean_address(a) for a in addresses[:n] if len(str(a)) > 10]


def load_emails(n: int) -> list:
    """Real Gmail IDs load karo."""
    print(f"  Loading emails (n={n})...")
    fpath = EMAIL_FILE
    if not Path(fpath).exists():
        print(f"  WARNING: {fpath} nahi mila")
        return []
    df = pd.read_csv(fpath, usecols=["email"], nrows=n * 2)
    emails = df["email"].dropna().tolist()
    random.shuffle(emails)
    return emails[:n]


def generate_cards(n: int) -> list:
    """Credit card numbers generate karo."""
    print(f"  Generating {n} card numbers...")
    cards = []
    for _ in range(n):
        if random.random() < 0.5:
            cards.append(generate_visa_card())
        else:
            cards.append(generate_mastercard())
    return cards


def build_training_data(addresses, emails, cards):
    """Sab data se training examples banao."""
    examples = []
    errors = 0

    # ADDRESS examples
    print(f"  Building {N_ADDRESS} ADDRESS examples...")
    for addr in addresses[:N_ADDRESS]:
        template = random.choice(ADDRESS_TEMPLATES)
        text = template.format(addr=addr)
        ex = make_example(text, addr, "ADDRESS")
        if ex:
            examples.append(ex)
        else:
            errors += 1

    # EMAIL examples
    print(f"  Building {N_EMAIL} EMAIL examples...")
    for email in emails[:N_EMAIL]:
        template = random.choice(EMAIL_TEMPLATES)
        text = template.format(email=email)
        ex = make_example(text, email, "EMAIL")
        if ex:
            examples.append(ex)
        else:
            errors += 1

    # CREDIT_CARD examples
    print(f"  Building {N_CREDIT_CARD} CREDIT_CARD examples...")
    for card in cards[:N_CREDIT_CARD]:
        template = random.choice(CARD_TEMPLATES)
        text = template.format(card=card)
        ex = make_example(text, card, "CREDIT_CARD")
        if ex:
            examples.append(ex)
        else:
            errors += 1

    # MIXED examples
    print(f"  Building {N_MIXED} MIXED examples...")
    addr_pool  = addresses[N_ADDRESS:]
    email_pool = emails[N_EMAIL:]
    card_pool  = cards[N_CREDIT_CARD:]

    for i in range(N_MIXED):
        name  = random.choice(INDIAN_NAMES)
        addr  = addr_pool[i % len(addr_pool)] if addr_pool else "Sector 14, Gurgaon"
        email = email_pool[i % len(email_pool)] if email_pool else "user@gmail.com"
        card  = card_pool[i % len(card_pool)] if card_pool else generate_visa_card()

        template, labels = random.choice(MIXED_TEMPLATES)

        # Template fill karo
        text = template.format(
            name=name, addr=addr, email=email, card=card
        )

        # Entity pairs banao
        entity_pairs = []
        for label in labels:
            if label == "PERSON":
                entity_pairs.append((name, "PERSON"))
            elif label == "ADDRESS":
                entity_pairs.append((addr, "ADDRESS"))
            elif label == "EMAIL":
                entity_pairs.append((email, "EMAIL"))
            elif label == "CREDIT_CARD":
                entity_pairs.append((card, "CREDIT_CARD"))

        ex = make_multi_example(text, entity_pairs)
        if ex:
            examples.append(ex)
        else:
            errors += 1

    print(f"  Total: {len(examples)} examples built ({errors} skipped)")
    return examples


def split_train_val(examples, val_ratio=0.15):
    """Train/Val split karo."""
    random.shuffle(examples)
    val_size = int(len(examples) * val_ratio)
    return examples[val_size:], examples[:val_size]


def write_output(train_data, val_data, output_path):
    """train_data.py file generate karo."""
    lines = [
        '"""',
        'training/train_data.py',
        f'Auto-generated from real data by generate_from_real_data.py',
        f'Train: {len(train_data)} examples | Val: {len(val_data)} examples',
        '"""',
        '',
        'TRAIN_DATA = [',
    ]

    for text, ann in train_data:
        # Safe repr
        safe_text = text.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    ("{safe_text}",')
        lines.append(f'     {{"entities": {ann["entities"]}}}),')
        lines.append('')

    lines.append(']')
    lines.append('')
    lines.append('VAL_DATA = [')

    for text, ann in val_data:
        safe_text = text.replace("\\", "\\\\").replace('"', '\\"')
        lines.append(f'    ("{safe_text}",')
        lines.append(f'     {{"entities": {ann["entities"]}}}),')
        lines.append('')

    lines.append(']')

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\n  File written: {output_path}")


if __name__ == "__main__":
    print("=" * 55)
    print("  Real Data → Training Examples Generator")
    print("=" * 55)

    # Data load karo
    addresses = load_addresses(N_ADDRESS + N_MIXED + 50)
    emails    = load_emails(N_EMAIL + N_MIXED + 50)
    cards     = generate_cards(N_CREDIT_CARD + N_MIXED + 50)

    if not addresses:
        print("\nERROR: CSV files 'data/' folder mein rakho!")
        print("  data/uttar_pradesh_75_districts_places.csv")
        print("  data/Delhi_districts_places.csv")
        print("  data/valid_gmails_100k.csv")
        exit(1)

    # Examples banao
    print("\nExamples build kar raha hun...")
    examples = build_training_data(addresses, emails, cards)

    # Split karo
    train_data, val_data = split_train_val(examples)
    print(f"\nSplit: {len(train_data)} train / {len(val_data)} val")

    # File likhao
    write_output(train_data, val_data, OUTPUT_FILE)

    print("\n" + "=" * 55)
    print("  Done! :")
    print("  python training/train_model.py")
    print("=" * 55)
