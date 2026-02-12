class Library:
    library_name = "Central Library"
    fine_per_day = 15

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False
        self.late = 0


    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print( "Issued successfully")
        else:
            print("Book already issued")

    def return_book(self, late):
        if self.is_issued:
            self.is_issued = False
            self.late =late
            print("returned successfully")
        else:
            print("not issued")


    def calculate_fine(self):
        if self.late > 0:
            total_fine = self.late * Library.fine_per_day
            print("Total Fine:", total_fine)
        else:
            print("No fine")

    @classmethod
    def change_fine_per_day(cls, new_fine):
        if new_fine > 0:
            cls.fine_per_day = new_fine
            print("Fine per day updated successfully.")
        else:
            print("Invalid fine amount.")
b1 = Library("Probability", "Ronaldo", 101)
b2 = Library("Software Engineering", "Pressman", 102)

b1.issue_book()
b1.return_book(3)
b1.calculate_fine()

Library.change_fine_per_day(20)

b2.issue_book()
b2.return_book(2)
b2.calculate_fine()
