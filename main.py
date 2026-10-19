
class Patient:
    
    def __init__(self, patient_id, name, age, condition):
        if not self.valid_age(age):
            raise ValueError("Age must be between 0 and 120.")
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition
        self.notes = []

    def add_note(self, note):
        if note.strip():
            self.notes.append(note.strip())
            return True
        return False

    def update_condition(self, new_condition):
        if new_condition.strip():
            self.condition = new_condition.strip()
            return True
        return False

    def display_record(self):
        print("ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Condition:", self.condition)
        print("Notes:", "; ".join(self.notes) if self.notes else "None")
        print("-" * 35)

    @staticmethod
    def valid_age(age):
        return type(age) is int and 0 <= age <= 120


class PatientRecordSystem:
    """Stores multiple Patient objects in one dictionary."""
    facility_name = "Community Health Learning Demo"

    def __init__(self):
        self.patients = {}  # One required data structure: dictionary

    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            return False
        self.patients[patient.patient_id] = patient
        return True

    def find_patient(self, patient_id):
        return self.patients.get(patient_id)

    def display_all(self):
        if not self.patients:
            print("No records found.")
            return
        for patient in self.patients.values():
            patient.display_record()

    @classmethod
    def display_facility(cls):
        print("Facility:", cls.facility_name)


def main():
    print("PATIENT RECORD SYSTEM - FICTIONAL DEMO")
    PatientRecordSystem.display_facility()
    system = PatientRecordSystem()
    first = Patient("P001", "Aminata Example", 27, "Routine check-up")
    second = Patient("P002", "Joseph Example", 34, "Follow-up visit")
    print("Added P001:", system.add_patient(first))
    print("Added P002:", system.add_patient(second))
    print("Duplicate P001 rejected:", not system.add_patient(first))
    first.add_note("Attended scheduled consultation")
    second.update_condition("Routine review completed")
    print("\nALL PATIENT RECORDS")
    system.display_all()
    print("LOOKUP P002")
    found = system.find_patient("P002")
    if found:
        found.display_record()
    print("Valid age 25:", Patient.valid_age(25))
    print("Valid age -2:", Patient.valid_age(-2))


if __name__ == "__main__":
    main()
