import logging
logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MovieTicket:
    Movie_theatre="Asian movies"
    base_price = 200   
    def __init__(self, ticket_id, movie_name, seat_no):
        self.ticket_id = ticket_id
        self.movie_name = movie_name
        self.seat_no = seat_no
        self.is_booked = False

        logging.info("ticket_id: %d \n Movie: %s \n Seat: %s",
                     self.ticket_id, self.movie_name, self.seat_no)

    def book_seat(self):
        if self.is_booked:
            logging.warning("Seat %s already booked.", self.seat_no)
        else:
            self.is_booked = True
            logging.info("Seat %s booked successfully ",
                     self.seat_no)

    def cancel_booking(self):
        if not self.is_booked:
            logging.warning("Seat %s is not booked yet", self.seat_no)
        else:
            self.is_booked = False
            logging.info("cancelled for seat %s", self.seat_no)

    def cal_ticket_price(self, is_weekend=False, spcl=False):
        if not self.is_booked:
            logging.warning("Ticket not booked")
            return 0   
        price = MovieTicket.base_price
        if is_weekend:
            price += 50   
        if spcl:
            price += 100  
        logging.info("Ticket Price for Movie: %s \n Seat: %s \n Price: %d",
                 self.movie_name, self.seat_no, price)
        return price

    @classmethod
    def change_ticket_price(cls, new_price):
        cls.base_price = new_price
        logging.info("Base price updated to %d", new_price)

t1 = MovieTicket(401, "Bahubali", "A10")
t2 = MovieTicket(402, "Salaar", "B5")
t1.book_seat()
print(t1.cal_ticket_price(is_weekend=True, spcl=True))
MovieTicket.change_ticket_price(250)
print(t1.cal_ticket_price())
t2.book_seat()
t2.cancel_booking()
t2.cal_ticket_price()


