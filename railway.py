import logging

logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:
    Railway="Indian Railways"
    basefare_for_km = 5  

    def __init__(self, ticket_id, passenger_name, distance_km):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.distance_km = distance_km
        self.isbooked = False
        self.iscancelled = False
        logging.info("ticket_id:%d \n passenger_name:%s \n distance_km:%d",
                     self.ticket_id, self.passenger_name, self.distance_km)

    def book_ticket(self):
        if self.iscancelled:
            logging.warning("Ticket was cancelled")
        elif self.isbooked:
            logging.warning("Ticket already booked")
        else:
            self.isbooked = True
            logging.info("Ticket %d booked successfully",self.ticket_id)


    def cancel_ticket(self):
        if not self.isbooked:
            logging.warning(" Ticket not booked ")

        elif self.iscancelled:
            logging.warning("Ticket already cancelled")

        self.iscancelled = True
        logging.info("Ticket %d has been cancelled", self.ticket_id)

    def cal_fare(self):
        if not self.isbooked or self.iscancelled:
            logging.warning("Fare cannot be calculated")
        else:
            fare = self.distance_km * Ticket.basefare_for_km
            logging.info("Fare for Ticket %d: %.2f", self.ticket_id, fare)

    @classmethod
    def change_basefare_for_km(cls, new_fare):
        cls.basefare_for_km = new_fare
        logging.info("Base fare updated to %.2f for km", new_fare)
p1 = Ticket(301, "Chandini", 500)
p2 = Ticket(302, "Madhuri", 300)
p1.book_ticket()
p1.cal_fare()
Ticket.change_basefare_for_km(3)
p1.cal_fare()
p2.book_ticket()
p2.cancel_ticket()
p2.cal_fare()

