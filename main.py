"""MediCare Patient Records Manager — entry point.

Business problem: reception exports a messy patients CSV every week.
The clinic needs it validated, stored cleanly, and summarised.

Run from the project folder (with the venv active):
    python main.py

This file is COMPLETE — no TODOs here. Once your clinic package works,
this program works. Read it top to bottom before you start coding:
it shows you exactly how your functions and class will be used.
"""

from pathlib import Path

from tabulate import tabulate            # third-party: installed via pip

from clinic import storage

RAW_FILE = Path("data") / "patients_raw.csv"
CLEAN_FILE = Path("reports") / "patients_clean.json"
SUMMARY_FILE = Path("reports") / "summary.json"


def main() -> None:
    print("=" * 60)
    print("MediCare Patient Records Manager")
    print("=" * 60)

    # 1. Load + validate (bad rows are collected, not fatal)
    patients, errors = storage.load_patients(RAW_FILE)

    # 2. Persist the clean data and the summary
    storage.write_clean_json(patients, CLEAN_FILE)
    summary = storage.write_summary(patients, errors, SUMMARY_FILE)

    # 3. Show the clean records as a table (tabulate = why we have a venv!)
    table = [[p.patient_id, p.name, p.age, p.department,
            f"{p.consultation_fee:,.2f}"] for p in patients]
    print(tabulate(table,
                headers=["ID", "Name", "Age", "Department", "Fee (INR)"],
                tablefmt="rounded_outline"))

    # 4. Report what was rejected, and why (never hide data loss!)
    print(f"\nValid records : {summary['valid_records']}")
    print(f"Rejected rows : {summary['rejected_rows']}")
    for message in errors:
        print(f"  - {message}")

    print(f"\nTotal revenue : INR {summary['total_revenue']:,.2f}")
    print("Revenue by department:")
    for dept, revenue in summary["revenue_by_department"].items():
        print(f"  {dept:<14} INR {revenue:>10,.2f}")

    print(f"\nSaved: {CLEAN_FILE} and {SUMMARY_FILE}")


if __name__ == "__main__":
    main()
