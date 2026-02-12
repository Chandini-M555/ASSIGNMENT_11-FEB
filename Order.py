import logging
logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Order:
    Order_platform="Amazon"
    tax_percent=5
    def __init__(self,orderid,cname):
        self.orderid=orderid
        self.cname=cname
        self.products=[]
        self.placed=False
        self.cancelled=False
        logging.info("orderid:%d \n cname:%s ",self.orderid,self.cname)
    def place_order(self, product, cost, quantity):
        if self.cancelled:
            logging.warning("Cannot place order. Order is cancelled.")
            return

        self.products.append((product, cost, quantity))
        logging.info("Product: %s \n Cost: %d \n Quantity: %d",
                     product, cost, quantity)
    
    def cancel_order(self):
        if not self.cancelled:
            self.cancelled=True
            logging.info("Your order has been cancelled")
        else:
            logging.warning("Already cancelled")
    def total_price(self):
        if self.cancelled:
            logging.warning("order is cancelled")
        else:
            subtotal=sum(cost*quantity for product,cost,quantity in self.products)
            tax=subtotal*(Order.tax_percent/100)
            totalprice=subtotal+tax
            logging.info("totalprice:%d",totalprice)
    @classmethod
    def change_tax_percent(cls,new_tax):
        cls.tax_percent=new_tax
        logging.info("new_tax:%d",new_tax)
c1=Order(101,"Chandini")
c2=Order(102,"Madhuri")
c1.place_order("Laptop",50000,1)
c1.place_order("Mouse",1000,2)
c1.total_price()
c2.place_order("Mobile",70000,1)
Order.change_tax_percent(7)
c1.total_price()
c2.cancel_order()
c2.cancel_order()

