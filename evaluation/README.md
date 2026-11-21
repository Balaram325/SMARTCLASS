# SmartClass face and voice recognition evaluation

**No verified recognition accuracy is currently reported.** This folder contains a small **offline** evaluation utility, not changes to deployed student authentication.

Use **consenting test participants only**. Record one row per attempt with a known truth label and observed prediction. Do not put images, audio, embeddings, passwords, email addresses, real student IDs, or other personal data into the repository.

Create a local `evaluation/attempts.csv` (gitignored) with three fields:

```csv
modality,true_id,predicted_id
face,pseudonym_A,pseudonym_A
face,pseudonym_B,
face,,pseudonym_A
voice,pseudonym_A,pseudonym_A
```

*The rows above are illustrative examples only and do not represent measured SmartClass performance.*

Evaluate:

```powershell
python -m evaluation.metrics --input evaluation/attempts.csv
python -m unittest discover -s tests
```

The report provides correct identity rate for enrolled participant attempts, **false rejection rate** for enrolled attempts, **wrong-identity rate** for enrolled attempts, and **false acceptance rate** for unknown/impostor attempts. Empty groups produce null (not zero), and sample counts are reported. For meaningful results, collect varied consented attempts and unknown-person tests in controlled conditions; disclose sample size and thresholds.

## Biometric privacy before production use

- Obtain meaningful consent, explain recording/storage and allow revocation.
- Restrict embeddings and attendance records using authenticated server-side authorisation and Supabase Row Level Security.
- Provide deletion and retention procedures; do not publish the real biometric dataset.
- Test spoofing/liveness risks; facial similarity alone is not robust proof of identity.
- Do not use recognition outcomes as the sole basis for adverse attendance decisions without a correction mechanism.

**Important:** This evaluation script neither verifies Supabase RLS nor fixes live biometric authentication security. Do not claim the application is secure solely because this script exists.
