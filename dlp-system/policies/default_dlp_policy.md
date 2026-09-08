# Default DLP Policy

## Payment card data

Validated payment-card data must be encrypted or tokenized at rest. Access must be restricted to approved roles, every access must be auditable, and storage must be minimized. Critical findings require analyst review before remediation.

## Government identifiers

Aadhaar and PAN data must be collected only for an approved business purpose. Access must be least-privilege, values must be masked in reports, and retention must follow the organization's approved schedule.

## Personal contact data

Email addresses, phone numbers, names, and addresses are personal data. Systems must document their purpose, restrict access, encrypt data in transit and at rest, and support deletion according to retention policy.

## Remediation and verification

After access controls, masking, encryption, tokenization, or deletion are applied, the affected asset must be re-scanned. The remediation ticket must link the original finding, approving analyst, change record, and verification scan.
