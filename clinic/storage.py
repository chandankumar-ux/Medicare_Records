"""Reading raw CSV data and writing clean outputs (Module 8 skills)."""

import csv
import json
from pathlib import Path

from clinic.models import Patient
from clinic.validators import InvalidRecordError


def load_patients(csv_path: Path) -> tuple[list[Patient], list[str]]:
    patients: list[Patient] = []
    errors: list[str] = []
    seen_ids: set[str] = set()

    with open(csv_path, "r", newline="", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for line_no, row in enumerate(reader, start=2):

        try:
            patient = Patient.from_csv_row(row)

            if patient.patient_id in seen_ids:
                errors.append(f"line {line_no}: duplicate patient id")
                continue

            seen_ids.add(patient.patient_id)

            patients.append(patient)

        except InvalidRecordError as e:
            errors.append(f"line {line_no}: {e}")

def write_clean_json(patients: list[Patient], out_path: Path) -> None:
    """Save the validated records as human-readable JSON."""

    out_path.parent.mkdir(exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as file:
        json.dump(
            [patient.to_dict() for patient in patients],
            file,
            indent=2
        )

def write_summary(patients: list[Patient], errors: list[str],
                out_path: Path) -> dict:
    """Compute the business summary, save it as JSON, and return it."""

    total_revenue = round(
        sum(patient.consultation_fee for patient in patients),
        2
    )

    revenue_by_department = {}

    for patient in patients:
        department = patient.department

        revenue_by_department[department] = round(
            revenue_by_department.get(department, 0)
            + patient.consultation_fee,
            2
        )

    summary = {
        "valid_records": len(patients),
        "rejected_rows": len(errors),
        "total_revenue": total_revenue,
        "revenue_by_department": revenue_by_department,
    }

    out_path.parent.mkdir(exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as file:
        json.dump(summary, file, indent=2)

    return summary
