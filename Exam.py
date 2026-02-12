class Exam:
    platform_name = "Vedantu Online"
    pass_marks = 35

    def __init__(self, student_name, total_marks):
        self.student_name = student_name
        self.total_marks = total_marks
        self.obtained_marks = 0
        self.is_started = False
        self.is_submitted = False

    def start_exam(self):
        if not self.is_started:
            self.is_started = True
            print(f"Exam started for {self.student_name}")
        else:
            print("Exam already started")

    def submit_exam(self, obtained_marks):
        if self.is_started and not self.is_submitted:
            self.obtained_marks = obtained_marks
            self.is_submitted = True
            print("Exam submitted successfully.")
        else:
            print("Exam not started or already submitted.")


    def calculate_score(self):
        if self.is_submitted:
            print("Obtained Marks:", self.obtained_marks)
            if self.obtained_marks >= Exam.pass_marks:
                print("Result: PASS")
            else:
                print("Result: FAIL")
        else:
            print("Exam not submitted yet.")

    @classmethod
    def change_pass_marks(cls, new_pass_marks):
        if new_pass_marks > 0:
            cls.pass_marks = new_pass_marks
            print("Pass marks updated successfully.")
        else:
            print("Invalid pass marks.")
e1 = Exam("Chandini", 90)
e2 = Exam("Manu", 55)

e1.start_exam()
e1.submit_exam(75)
e1.calculate_score()

Exam.change_pass_marks(50)

e2.start_exam()
e2.submit_exam(45)
e2.calculate_score()
