import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
PART_TIME_HRS = 4
TOTAL_HRS = HRS_IN_DAY + PART_TIME_HRS

def check_attendance():
    attendance = rm.randint(0,2)
    if attendance==1:
        print("Emplpoyee is Present")
        cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)
    elif attendance == 2:
        print("employee is present")
        part_time_wage(RATE_PER_HR,TOTAL_HRS)
    else :
        print("Employee is Absent")
                  
#UC2
def cal_dalily_wage(wage, hour):
    print("Daily wage of employee is ", wage*hour)

#UC3
def part_time_wage(wage, hour):
    print("Parttime wage of employee is ", wage*hour)

check_attendance()


    

