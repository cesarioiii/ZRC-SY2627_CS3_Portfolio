class Patient:
    def __init__(self, name, bill_amount : float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def __init__(self, name, bill_amount : float):
        self.__name = name
        self.__bill_amount = bill_amount
        self.__discount = 0.20

    def calculate_bill(self):
        discounted_amount = self.__bill_amount * (1 - self.__discount)
        return discounted_amount

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount : float):
        self.__name = name
        self.__bill_amount = bill_amount
        self.__discount = 0.15

    def calculate_bill(self):
        discounted_amount = self.__bill_amount * (1 - self.__discount)
        return discounted_amount

regular_patient = Patient("Juan dela Cruz", 15000.00)
senior_patient = SeniorPatient("Maria Santos", 15000.00)
philhealth_patient = PhilHealthPatient("Pedro Pablo", 15000.00)

print("Patient Name:", regular_patient.get_name())
print("Original Bill:", regular_patient.calculate_bill())
print("Final Bill:", regular_patient.calculate_bill())

print("Patient Name:", senior_patient.get_name())
print("Original Bill:", senior_patient.calculate_bill())
print("Final Bill:", senior_patient.calculate_bill())

print("Patient Name:", philhealth_patient.get_name())
print("Original Bill:", philhealth_patient.calculate_bill())
print("Final Bill:", philhealth_patient.calculate_bill())