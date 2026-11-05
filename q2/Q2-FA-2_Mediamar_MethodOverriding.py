class Patient:
    def __init__(self, name, bill_amount: float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        return "Regular Patient"


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount: float):
        super().__init__(name, bill_amount)
        self.__discount = 0.20

    def calculate_bill(self):
        return self.get_bill_amount() * (1 - self.__discount)

    def display_patient_type(self):
        return "Senior Patient"


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount: float):
        super().__init__(name, bill_amount)
        self.__discount = 0.15

    def calculate_bill(self):
        return self.get_bill_amount() * (1 - self.__discount)

    def display_patient_type(self):
        return "PhilHealth Patient"


regular_patient = Patient("Juan dela Cruz", 15000.00)
senior_patient = SeniorPatient("Maria Santos", 15000.00)
philhealth_patient = PhilHealthPatient("Pedro Pablo", 15000.00)

print("Hospital Billing System")
print("----------------------------------")
print("Patient Name:", regular_patient.get_name())
print("Patient Type:", regular_patient.display_patient_type())
print("Original Bill:", regular_patient.calculate_bill())
print("Final Bill:", regular_patient.calculate_bill())

print("                                  ")

print("Patient Name:", senior_patient.get_name())
print("Patient Type:", senior_patient.display_patient_type())
print("Original Bill:", senior_patient.calculate_bill())
print("Final Bill:", senior_patient.calculate_bill())

print("                                  ")

print("Patient Name:", philhealth_patient.get_name())
print("Patient Type:", philhealth_patient.display_patient_type())
print("Original Bill:", philhealth_patient.calculate_bill())
print("Final Bill:", philhealth_patient.calculate_bill())
print("----------------------------------")