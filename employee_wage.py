import random as rm

class Employee :

    def __init__(self) -> None:
        self.RATE_PER_HR = 20
        self.HRS_IN_DAY = 8
        self.PART_TIME_HRS = 4
        self.TOTAL_HRS = self.HRS_IN_DAY + self.PART_TIME_HRS
        self.DAYS_IN_MONTH = 20

        self.TOTAL_HRS_WORKED = 0
        self.TOTAL_DAYS_WORKED = 0

    def check_attendance(cls):
            while cls.TOTAL_HRS_WORKED<100 and cls.TOTAL_DAYS_WORKED < 20 :
                attendance = rm.randint(0,2)
                match attendance :
                    case 1 :
                        print("Employee is Present")
                        cls.TOTAL_DAYS_WORKED+=1
                        cls.TOTAL_HRS_WORKED+=8
                        cls.cal_dalily_wage(cls.RATE_PER_HR, cls.HRS_IN_DAY)

                    case 2:
                        print("Employee is present and worked parttime")
                        cls.TOTAL_DAYS_WORKED+=1
                        cls.TOTAL_HRS_WORKED+=4
                        cls.part_time_wage(cls.RATE_PER_HR, cls.PART_TIME_HRS)

                    case _:
                        print("Employee is absent")
                        cls.TOTAL_DAYS_WORKED+=1
                        cls.TOTAL_HRS_WORKED+=0
            cls.cal_monthly_wage(cls.RATE_PER_HR, cls.TOTAL_HRS_WORKED, cls.TOTAL_DAYS_WORKED)
            cls.view_total_work_hrs(cls.TOTAL_HRS_WORKED)

    #UC2
    def cal_dalily_wage(self, wage, hours):
        print("Daily wage of employee is ", wage * hours)

    #UC3
    def part_time_wage(self, wage, hour):
        print("Part time wage of employee is ", wage*hour)

    #UC5
    def cal_monthly_wage(self, wage, hour, day):
        print("Monthly Wage of Employee is ", wage*hour*day)

    #UC7
    def view_total_work_hrs(self, hours) :
        print("Total HRS of the Employee is - ",hours)

Niraj = Employee()
print("\t Niraj Wage Details \n\n")
print(Niraj.check_attendance())

Rohit = Employee()
print("\t Rohit Wage Details \n\n")
print(Rohit.check_attendance())

Mohit = Employee()
print("\t Mohit Wage Details \n\n")
print(Mohit.check_attendance())


