"""Offline recognition evaluation. No biometric images, audio or embeddings stored here.

CSV columns: modality,true_id,predicted_id
- true_id: consented enrolled participant ID; blank for an unknown/impostor attempt
- predicted_id: predicted enrolled ID; blank when system rejects the attempt
This script only processes anonymized identifiers and never calls live Supabase.
"""
import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

def evaluate_rows(rows):
    if not rows:
        raise ValueError("Provide at least one labelled attempt")
    groups = defaultdict(list)
    for row in rows:
        modality = (row.get("modality") or "").strip().lower()
        if modality not in {"face","voice"}:
            raise ValueError("modality must be face or voice")
        groups[modality].append({"truth":str(row.get("true_id") or "").strip(),
                                 "predicted":str(row.get("predicted_id") or "").strip()})
    report = {}
    for modality, examples in groups.items():
        genuine = [r for r in examples if r["truth"]]
        unknown = [r for r in examples if not r["truth"]]
        correct = sum(x["truth"] == x["predicted"] for x in genuine)
        false_reject = sum(not x["predicted"] for x in genuine)
        wrong_identity = sum(bool(x["predicted"]) and x["truth"] != x["predicted"] for x in genuine)
        false_accept = sum(bool(x["predicted"]) for x in unknown)
        report[modality] = {
            "total_attempts":len(examples),
            "genuine_attempts":len(genuine),
            "unknown_attempts":len(unknown),
            "correct_identity_accuracy": correct / len(genuine) if genuine else None,
            "false_reject_rate": false_reject / len(genuine) if genuine else None,
            "wrong_identity_rate": wrong_identity / len(genuine) if genuine else None,
            "false_accept_rate": false_accept / len(unknown) if unknown else None,
        }
    return report

def main():
    p = argparse.ArgumentParser(description="Score anonymized, consented SmartClass recognition attempts")
    p.add_argument("--input", required=True)
    p.add_argument("--output", default="evaluation/results.json")
    args = p.parse_args()
    with open(args.input, newline="", encoding="utf-8") as handle:
        result = evaluate_rows(csv.DictReader(handle))
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result,indent=2), encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__ == "__main__":
    main()
