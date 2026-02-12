import logging
logging.basicConfig(
    filename="results.log",
    level=logging.INFO,
    format="%(asctime)s-%(levelname)s-%(message)s"
)

class Employee:
    Companyname="xyz"
    location="Hyderabad"
    hra_percent=25
    def __init__(self,emp_id,emp_name,sal):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.sal=sal
        self.leave_ded=0
        logging.info("emp_id:%d\n emp_name:%s \n sal:%d",self.emp_id,self.emp_name,self.sal)
    def cal_sal(self):
        hra=self.sal*(Employee.hra_percent)/100
        total_sal=hra+self.sal-self.leave_ded
        logging.info("total_sal:%d",total_sal)
    def apply_leave_ded(self,leave_days):
        sal_per_day=(self.sal)/30
        self.leave_ded=leave_days*sal_per_day
        logging.info("Leave deduction applied for emp_name:%s for leave_days:%d",self.emp_name,leave_days)
    def display_payslip(self):
        hra=self.sal*(Employee.hra_percent)/100
        total_sal=hra+self.sal-self.leave_ded
        logging.info("emp_id:%d\n emp_name:%s\n total_sal:%d \n leave_ded:%d",self.emp_id,self.emp_name,total_sal,self.leave_ded)
    @classmethod
    def change_hra_percent(cls,new_hra):
        cls.hra_percent=new_hra
        logging.info("hra updated with new_hra:%d",new_hra)
e1=Employee(1,"Chandini",35000)
e2=Employee(2,"Ramani",40000)
e1.apply_leave_ded(3)
e1.cal_sal()
e1.display_payslip()
Employee.change_hra_percent(10)
e2.cal_sal()
e2.display_payslip()



    
    