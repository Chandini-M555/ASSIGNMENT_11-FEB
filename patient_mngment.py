class Patient:
    hospital_name = "Apollo"
    consultation_fee = 500

    def __init__(self,name,age,disease,admitted_days):
        self.name = name
        self.age = age
        self.disease = disease
        self.admitted_days = admitted_days
        self.is_admitted = False
    def admit(self):
        if not self.is_admitted:
            self.is_admitted = True
            print( "Admitted successfully")
        else:
            print("Patient already admitted")

    def discharge(self):
        if self.is_admitted:
            self.is_admitted = False
            print("discharged successfully")
        else:
            print("Patient is not admitted")

    def bill(self):
        if self.is_admitted:
            room_charge = 2000
            total_bill = (room_charge * self.admitted_days) + Patient.consultation_fee
            print("Total Bill:", total_bill)
        else:
            print(" No bill")

    @classmethod
    def change_consultation_fee(cls, new_fee):
        if new_fee > 0:
            cls.consultation_fee = new_fee
            print("Consultation fee updated successfully")
        else:
            print("Invalid consultation fee")
p1 = Patient("Chandini",20, "Fever", 2)
p2 = Patient("Madhuri",16, "Fracture", 5)

p1.admit()
p1.bill()
p1.discharge()

Patient.change_consultation_fee(800)

p2.admit()
p2.bill()
