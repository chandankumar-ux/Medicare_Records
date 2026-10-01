"""The Patient class — the OOP heart of the project.

Two OOP ideas to demonstrate (only two, on purpose):
1. ENCAPSULATION — consultation_fee guarded by @property (Module 6).
2. FACTORY CLASSMETHOD — Patient.from_csv_row() builds a validated
Patient from a messy CSV row (Module 5 + Module 8 together).
"""

from clinic import validators


class Patient:
    """One validated patient visit record."""

    def __init__(self, patient_id: str, name: str, age: int,department: str, consultation_fee: float, visit_date: str):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.department=department
        self.consultation_fee=consultation_fee
        self.visit_date=visit_date
            
        

    # ----- encapsulation: a guarded attribute -----
    @property
    def consultation_fee(self) -> float:
        return self._consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value: float):
        if value < 0:
            raise ValueError("value should be non-negative")
        self.consultation_fee=value

    # ----- factory: build a Patient from one raw CSV row (a dict) -----
    @classmethod
    def from_csv_row(cls, row: dict) -> "Patient":
        return cls(
        patient_id=row["patient_id"].strip(),
        name=validators.clean_name(row["name"]),
        age=validators.parse_age(row["age"]),
        department=validators.clean_department(row["department"]),
        consultation_fee=validators.parse_fee(row["consultation_fee"]),
        visit_date=row["visit_date"].strip(),
    )

    def to_dict(self) -> dict:
        return {
        "patient_id": self.patient_id,
        "name": self.name,
        "age": self.age,
        "department": self.department,
        "consultation_fee": self.consultation_fee,
        "visit_date": self.visit_date,
    }
    def __repr__(self) -> str:
        return f"Patient({self.patient_id}, {self.name}, {self.department})"


if __name__ == "__main__":
    # Self-test (Module 7 pattern) — works once TODOs 5-7 are done
    demo = Patient("P999", "Test Person", 30, "General", 500.0, "2026-08-12")
    print("Self-test:", demo)
