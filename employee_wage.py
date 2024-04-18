import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
def check_attendance():
    attendance = rm.randint(0,1)
    if attendance==1:
        print("Emplpoyee is Present")
        cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)
    else :
        print("Employee is Present")
                  
#UC2
def cal_dalily_wage(wage, hour):
    print("Daily wage of employee is ", wage*hour)

check_attendance()
    

