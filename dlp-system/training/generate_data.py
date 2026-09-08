"""
training/generate_data.py

Run karo: python training/generate_data.py
Yeh script automatically sahi character positions calculate karke
train_data.py generate karta hai — manually count karne ki zarurat nahi.
"""

from pathlib import Path

# ── Raw examples — sirf text aur entity string do ────────────────────
# Format: (sentence, [(entity_text, label), ...])
# Script automatically start/end positions calculate karega

RAW_EXAMPLES = [

    # PERSON
    ("Please send the report to Rahul Sharma by Friday.",
     [("Rahul Sharma", "PERSON")]),

    ("The account belongs to Priya Singh and her husband.",
     [("Priya Singh", "PERSON")]),

    ("Customer Amit Kumar called regarding his loan.",
     [("Amit Kumar", "PERSON")]),

    ("Dr. Sunita Verma is the primary account holder.",
     [("Sunita Verma", "PERSON")]),

    ("Please verify the identity of Mohammad Iqbal before proceeding.",
     [("Mohammad Iqbal", "PERSON")]),

    ("Ananya Krishnamurthy submitted the KYC documents.",
     [("Ananya Krishnamurthy", "PERSON")]),

    ("Contact Ravi Shankar at the branch office.",
     [("Ravi Shankar", "PERSON")]),

    ("The loan was sanctioned to Deepika Nair last month.",
     [("Deepika Nair", "PERSON")]),

    ("Suresh Patel and Meena Patel are joint account holders.",
     [("Suresh Patel", "PERSON"), ("Meena Patel", "PERSON")]),

    ("Vikram Malhotra PAN card was not verified.",
     [("Vikram Malhotra", "PERSON")]),

    ("The patient Sanjay Gupta visited the clinic yesterday.",
     [("Sanjay Gupta", "PERSON")]),

    ("Please contact Nisha Agarwal for further details.",
     [("Nisha Agarwal", "PERSON")]),

    ("Account opened by Rohit Mehta on 5th March.",
     [("Rohit Mehta", "PERSON")]),

    ("Kavya Reddy submitted her application form.",
     [("Kavya Reddy", "PERSON")]),

    ("The nominee is Arun Joshi as per the records.",
     [("Arun Joshi", "PERSON")]),

    ("Residence proof of Pooja Sharma was verified.",
     [("Pooja Sharma", "PERSON")]),

    ("Mr. Harish Nair called to update his address.",
     [("Harish Nair", "PERSON")]),

    ("Beneficiary name is Leela Krishnan in this account.",
     [("Leela Krishnan", "PERSON")]),

    ("Kiran Bedi applied for a new credit card.",
     [("Kiran Bedi", "PERSON")]),

    ("Please call Manoj Tiwari at the earliest.",
     [("Manoj Tiwari", "PERSON")]),

    ("Salary credited to Geeta Rani account.",
     [("Geeta Rani", "PERSON")]),

    ("Shruti Desai is the registered mobile owner.",
     [("Shruti Desai", "PERSON")]),

    ("The applicant Neha Joshi provided her documents.",
     [("Neha Joshi", "PERSON")]),

    ("Tarun Khanna has not completed KYC yet.",
     [("Tarun Khanna", "PERSON")]),

    ("Insurance policy issued to Rekha Iyer.",
     [("Rekha Iyer", "PERSON")]),

    ("Dinesh Rao is the primary borrower on this account.",
     [("Dinesh Rao", "PERSON")]),

    ("Sundar Pichai attended the annual general meeting.",
     [("Sundar Pichai", "PERSON")]),

    ("Loan application by Farhan Akhtar is under review.",
     [("Farhan Akhtar", "PERSON")]),

    ("Notify Pallavi Joshi once the transfer is complete.",
     [("Pallavi Joshi", "PERSON")]),

    ("The guarantor is Ramesh Babu as per the agreement.",
     [("Ramesh Babu", "PERSON")]),

    # ADDRESS
    ("The customer lives at Sector 14, Gurgaon, Haryana.",
     [("Sector 14, Gurgaon, Haryana", "ADDRESS")]),

    ("Delivery address is Flat 302, Sunflower Apartments, Andheri West, Mumbai.",
     [("Flat 302, Sunflower Apartments, Andheri West, Mumbai", "ADDRESS")]),

    ("Branch located at MG Road, Bangalore 560001.",
     [("MG Road, Bangalore 560001", "ADDRESS")]),

    ("Please ship to 45 Park Street, Kolkata, West Bengal.",
     [("45 Park Street, Kolkata, West Bengal", "ADDRESS")]),

    ("The registered office is at Connaught Place, New Delhi 110001.",
     [("Connaught Place, New Delhi 110001", "ADDRESS")]),

    ("Customer address: Plot 7, MIDC Industrial Area, Pune 411019.",
     [("Plot 7, MIDC Industrial Area, Pune 411019", "ADDRESS")]),

    ("Permanent address is Village Rampur, District Sitapur, UP.",
     [("Village Rampur, District Sitapur, UP", "ADDRESS")]),

    ("The property is situated at Koramangala 5th Block, Bengaluru.",
     [("Koramangala 5th Block, Bengaluru", "ADDRESS")]),

    ("Send documents to House No. 12, Rajouri Garden, New Delhi.",
     [("House No. 12, Rajouri Garden, New Delhi", "ADDRESS")]),

    ("Send the courier to 23 Linking Road, Bandra, Mumbai 400050.",
     [("23 Linking Road, Bandra, Mumbai 400050", "ADDRESS")]),

    ("Office address: Tower B, Cyber City, Gurgaon 122002.",
     [("Tower B, Cyber City, Gurgaon 122002", "ADDRESS")]),

    ("The flat is at 7A, Green Park Extension, New Delhi.",
     [("7A, Green Park Extension, New Delhi", "ADDRESS")]),

    ("Deliver to Shop 4, Commercial Street, Bangalore 560001.",
     [("Shop 4, Commercial Street, Bangalore 560001", "ADDRESS")]),

    ("Current address: Pocket C, Mayur Vihar Phase 1, Delhi.",
     [("Pocket C, Mayur Vihar Phase 1, Delhi", "ADDRESS")]),

    ("Registered at B-12, Vasant Kunj, New Delhi 110070.",
     [("B-12, Vasant Kunj, New Delhi 110070", "ADDRESS")]),

    ("Located near Hiranandani Gardens, Powai, Mumbai.",
     [("Hiranandani Gardens, Powai, Mumbai", "ADDRESS")]),

    ("Property at Survey No 45, Hadapsar, Pune 411028.",
     [("Survey No 45, Hadapsar, Pune 411028", "ADDRESS")]),

    # AADHAAR
    ("Aadhaar number 2345 6789 0123 was submitted.",
     [("2345 6789 0123", "AADHAAR")]),

    ("Verify UID 3456 7890 1234 for KYC completion.",
     [("3456 7890 1234", "AADHAAR")]),

    ("The Aadhaar 5678 9012 3456 linked to the account.",
     [("5678 9012 3456", "AADHAAR")]),

    ("Customer provided Aadhaar: 8901 2345 6789.",
     [("8901 2345 6789", "AADHAAR")]),

    ("UIDAI number 9012 3456 7890 not found in database.",
     [("9012 3456 7890", "AADHAAR")]),

    ("Her Aadhaar 3456 7890 1234 was used for KYC.",
     [("3456 7890 1234", "AADHAAR")]),

    ("UID 7890 1234 5678 linked to mobile number.",
     [("7890 1234 5678", "AADHAAR")]),

    ("Aadhaar verification pending for 6543 2109 8765.",
     [("6543 2109 8765", "AADHAAR")]),

    ("Aadhaar 9876 5432 1098 belongs to the customer.",
     [("9876 5432 1098", "AADHAAR")]),

    ("Please link Aadhaar 4321 0987 6543 to this account.",
     [("4321 0987 6543", "AADHAAR")]),

    # PAN
    ("PAN card ABCDE1234F needs to be verified.",
     [("ABCDE1234F", "PAN")]),

    ("Income tax filed under PQRST9876Y for FY 2023-24.",
     [("PQRST9876Y", "PAN")]),

    ("The PAN MNOPQ5432Z was rejected due to mismatch.",
     [("MNOPQ5432Z", "PAN")]),

    ("Linking Aadhaar with PAN XYZAB6543W is mandatory.",
     [("XYZAB6543W", "PAN")]),

    ("TDS deducted against LMNOP2109K for this quarter.",
     [("LMNOP2109K", "PAN")]),

    ("PAN GHIJK5678L submitted for ITR filing.",
     [("GHIJK5678L", "PAN")]),

    ("Tax deducted under UVWXY9012Z this quarter.",
     [("UVWXY9012Z", "PAN")]),

    ("Invalid PAN RSTUV3456W entered by customer.",
     [("RSTUV3456W", "PAN")]),

    ("Form 16 issued against PAN CDEFG8901H.",
     [("CDEFG8901H", "PAN")]),

    ("PAN verification failed for HIJKL3210M.",
     [("HIJKL3210M", "PAN")]),

    # CREDIT CARD
    ("Transaction on card 4111111111111111 was declined.",
     [("4111111111111111", "CREDIT_CARD")]),

    ("Charge card number 5500005555555559 for INR 2000.",
     [("5500005555555559", "CREDIT_CARD")]),

    ("Card 4012888888881881 reported stolen by customer.",
     [("4012888888881881", "CREDIT_CARD")]),

    ("New card 5105105105105100 issued to customer.",
     [("5105105105105100", "CREDIT_CARD")]),

    ("Disputed transaction on 4000056655665556 last week.",
     [("4000056655665556", "CREDIT_CARD")]),

    ("Card ending 4111111111111111 was used abroad.",
     [("4111111111111111", "CREDIT_CARD")]),

    ("Block card number 5500005555555559 immediately.",
     [("5500005555555559", "CREDIT_CARD")]),

    # EMAIL
    ("Send OTP to rahul.sharma@gmail.com immediately.",
     [("rahul.sharma@gmail.com", "EMAIL")]),

    ("User registered with priya.singh@hdfc.co.in last week.",
     [("priya.singh@hdfc.co.in", "EMAIL")]),

    ("Statement sent to amit.kumar@yahoo.in successfully.",
     [("amit.kumar@yahoo.in", "EMAIL")]),

    ("Reach out at sunita.rao@outlook.com for queries.",
     [("sunita.rao@outlook.com", "EMAIL")]),

    ("OTP sent to mohan.das@rediffmail.com successfully.",
     [("mohan.das@rediffmail.com", "EMAIL")]),

    ("Account linked to neha.joshi@icicibank.com.",
     [("neha.joshi@icicibank.com", "EMAIL")]),

    ("Send statement to kiran.kumar@sbi.co.in.",
     [("kiran.kumar@sbi.co.in", "EMAIL")]),

    ("Email vikram.nair@axis.com about the transaction.",
     [("vikram.nair@axis.com", "EMAIL")]),

    # PHONE
    ("Call customer at 9876543210 for verification.",
     [("9876543210", "PHONE")]),

    ("Registered mobile number is +91-9123456789.",
     [("9123456789", "PHONE")]),

    ("Contact 8800112233 for further assistance.",
     [("8800112233", "PHONE")]),

    ("Mobile 7788991234 registered with this account.",
     [("7788991234", "PHONE")]),

    ("Alternate number +91-8899001122 added to profile.",
     [("8899001122", "PHONE")]),

    ("Customer OTP sent to 9988776655.",
     [("9988776655", "PHONE")]),

    ("Please call 7007001234 to confirm your appointment.",
     [("7007001234", "PHONE")]),

    ("New mobile 9654321078 linked to your account.",
     [("9654321078", "PHONE")]),

    # MIXED
    ("Rahul Sharma from Sector 14, Gurgaon called about his Aadhaar 2345 6789 0123.",
     [("Rahul Sharma", "PERSON"), ("Sector 14, Gurgaon", "ADDRESS"), ("2345 6789 0123", "AADHAAR")]),

    ("Priya Singh with PAN ABCDE1234F lives at Andheri West, Mumbai.",
     [("Priya Singh", "PERSON"), ("ABCDE1234F", "PAN"), ("Andheri West, Mumbai", "ADDRESS")]),

    ("Card 4111111111111111 used by Deepak Jain at Connaught Place.",
     [("4111111111111111", "CREDIT_CARD"), ("Deepak Jain", "PERSON"), ("Connaught Place", "ADDRESS")]),

    ("Aadhaar 9876 5432 1098 belongs to Meera Nair, contact 9001122334.",
     [("9876 5432 1098", "AADHAAR"), ("Meera Nair", "PERSON"), ("9001122334", "PHONE")]),

    ("Rohit Sharma ka email rohit.sharma@gmail.com aur mobile 9876543210 hai.",
     [("Rohit Sharma", "PERSON"), ("rohit.sharma@gmail.com", "EMAIL"), ("9876543210", "PHONE")]),

    ("Arjun Kapoor from MG Road, Pune applied for a loan with PAN FGHIJ2345K.",
     [("Arjun Kapoor", "PERSON"), ("MG Road, Pune", "ADDRESS"), ("FGHIJ2345K", "PAN")]),

    ("Sneha Pillai at sneha.pillai@gmail.com lives in Powai, Mumbai.",
     [("Sneha Pillai", "PERSON"), ("sneha.pillai@gmail.com", "EMAIL"), ("Powai, Mumbai", "ADDRESS")]),

    ("Vikram Nair, Flat 5B Worli Mumbai, PAN PQRST6789U, Aadhaar 2109 8765 4321.",
     [("Vikram Nair", "PERSON"), ("Flat 5B Worli Mumbai", "ADDRESS"), ("PQRST6789U", "PAN"), ("2109 8765 4321", "AADHAAR")]),

    ("Tarun Mehta called from 9812345670 about his card 5500005555555559.",
     [("Tarun Mehta", "PERSON"), ("9812345670", "PHONE"), ("5500005555555559", "CREDIT_CARD")]),

    ("Salary slip sent to pooja.sharma@outlook.com for Pooja Sharma.",
     [("pooja.sharma@outlook.com", "EMAIL"), ("Pooja Sharma", "PERSON")]),

    ("Kiran Kumar, email kiran.kumar@sbi.co.in, mobile 9001234567, PAN KLMNO6789P.",
     [("Kiran Kumar", "PERSON"), ("kiran.kumar@sbi.co.in", "EMAIL"), ("9001234567", "PHONE"), ("KLMNO6789P", "PAN")]),
]

# ── Validation examples ───────────────────────────────────────────────
RAW_VAL = [
    ("The applicant Neha Joshi provided her Aadhaar 6789 0123 4567.",
     [("Neha Joshi", "PERSON"), ("6789 0123 4567", "AADHAAR")]),

    ("Registered address: C-45, Defence Colony, New Delhi 110024.",
     [("C-45, Defence Colony, New Delhi 110024", "ADDRESS")]),

    ("PAN DEFGH7890I linked with Aadhaar 3456 7890 1234.",
     [("DEFGH7890I", "PAN"), ("3456 7890 1234", "AADHAAR")]),

    ("Kiran Kumar email is kiran.kumar@sbi.co.in.",
     [("Kiran Kumar", "PERSON"), ("kiran.kumar@sbi.co.in", "EMAIL")]),

    ("Flat 501, Bandra West, Mumbai 400050 is the billing address.",
     [("Flat 501, Bandra West, Mumbai 400050", "ADDRESS")]),

    ("Tarun Mehta called from 9812345670 about his card 5500005555555559.",
     [("Tarun Mehta", "PERSON"), ("9812345670", "PHONE"), ("5500005555555559", "CREDIT_CARD")]),

    ("Salary slip sent to pooja.sharma@outlook.com for Pooja Sharma.",
     [("pooja.sharma@outlook.com", "EMAIL"), ("Pooja Sharma", "PERSON")]),

    ("Contact Ravi Nair at 9900112233 or ravi.nair@gmail.com.",
     [("Ravi Nair", "PERSON"), ("9900112233", "PHONE"), ("ravi.nair@gmail.com", "EMAIL")]),
]


def make_spacy_data(raw_examples):
    """
    Entity string se automatically character positions calculate karo.
    Agar sentence mein entity nahi mili toh skip karo.
    """
    spacy_data = []
    errors     = []

    for text, entity_pairs in raw_examples:
        entities = []
        ok       = True

        for entity_text, label in entity_pairs:
            # find() se exact position milegi
            start = text.find(entity_text)
            if start == -1:
                errors.append(f"NOT FOUND: '{entity_text}' in '{text[:50]}...'")
                ok = False
                break
            end = start + len(entity_text)
            entities.append((start, end, label))

        if ok:
            spacy_data.append((text, {"entities": entities}))

    return spacy_data, errors


def verify_positions(spacy_data):
    """Generated positions verify karo — print karke confirm karo."""
    print("\nPosition verification (first 10):")
    print("-" * 50)
    for text, ann in spacy_data[:10]:
        print(f"Text: {text[:60]}")
        for start, end, label in ann["entities"]:
            extracted = text[start:end]
            status = "✓" if extracted else "✗"
            print(f"  {status} [{label}] pos={start}:{end} → '{extracted}'")
        print()


def write_train_data_file(train_data, val_data, output_path):
    """Generated data ko train_data.py file mein likhao."""
    lines = ['"""', 'training/train_data.py', 'Auto-generated by generate_data.py — positions verified.',
             f'Total: {len(train_data)} train + {len(val_data)} val examples', '"""', '', 'TRAIN_DATA = [']

    for text, ann in train_data:
        lines.append(f'    ({repr(text)},')
        lines.append(f'     {{"entities": {ann["entities"]}}}),')
        lines.append('')

    lines.append(']')
    lines.append('')
    lines.append('VAL_DATA = [')

    for text, ann in val_data:
        lines.append(f'    ({repr(text)},')
        lines.append(f'     {{"entities": {ann["entities"]}}}),')
        lines.append('')

    lines.append(']')

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\nFile written: {output_path}")


if __name__ == "__main__":
    print("Positions calculate kar raha hun...")

    train_data, train_errors = make_spacy_data(RAW_EXAMPLES)
    val_data,   val_errors   = make_spacy_data(RAW_VAL)

    all_errors = train_errors + val_errors
    if all_errors:
        print(f"\nErrors ({len(all_errors)}):")
        for e in all_errors:
            print(f"  {e}")

    print(f"\nTrain: {len(train_data)} examples ready ({len(train_errors)} skipped)")
    print(f"Val  : {len(val_data)} examples ready ({len(val_errors)} skipped)")

    verify_positions(train_data)

    output = Path(__file__).parent / "train_data.py"
    write_train_data_file(train_data, val_data, output)
    print("\nAb chalao: python training/train_model.py")
