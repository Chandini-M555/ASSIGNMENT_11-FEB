import logging

logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Hostel:
    Hostel_name="Seetha Womens Hostel"
    loc="Nizampet"
    rent= 5000   

    def __init__(self,room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.isallocated= False
        self.student_name = None
        logging.info("room_no:%d \n room_type:%s ",self.room_no,self.room_type)

    def allocate_room(self,student_name):
        if self.isallocated:
            logging.warning("Room %d already allocated", self.room_number)
        else:
            self.isallocated = True
            self.student_name=student_name
            logging.info("Room %d allocated to %s",self.room_no, self.student_name)

    def vacate_room(self):
        if not self.isallocated:
            logging.warning("Room %d is already vacant", self.room_number)
        else:
            logging.info("Room %d vacated by %s",self.room_no, self.student_name)
            self.isallocated = False
            self.student_name=None

    def cal_monthly_fee(self, months):
        if not self.isallocated:
            logging.warning("Room %d is not allocated",self.room_no)
        else:
            total_fee = Hostel.rent * months
            logging.info("room_no:%d \n student_name:%s \n months:%d \n total_fee:%d",
                     self.room_no, self.student_name, months, total_fee)
            return total_fee

    @classmethod
    def change_rent(cls, new_rent):
        cls.rent = new_rent
        logging.info("Room rent updated to %d per month", new_rent)
s1 = Hostel(101, "Single")
s2 = Hostel(102, "Double")
s1.allocate_room("Chandini")
s1.cal_monthly_fee(3)
Hostel.change_rent(6000)
s1.cal_monthly_fee(3)
s2.allocate_room("Madhuri")
s2.vacate_room()
s2.cal_monthly_fee(2)
