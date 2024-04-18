import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
PART_TIME_HRS = 4
TOTAL_HRS = HRS_IN_DAY + PART_TIME_HRS

def check_attendance():
    attendance = rm.randint(0,2)
    match attendance :
        case 1 :
            print("Employee is Present")
            cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)
        case 2:
            print("Employee is present and worked parttime")
            part_time_wage(RATE_PER_HR, TOTAL_HRS)
        case _:
            print("Employee is absent")
                  
#UC2
def cal_dalily_wage(wage, hour):
    print("Daily wage of employee is ", wage*hour)

#UC3
def part_time_wage(wage, hour):
    print("Parttime wage of employee is ", wage*hour)

check_attendance()


    

