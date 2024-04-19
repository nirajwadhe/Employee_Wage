import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
PART_TIME_HRS = 4
TOTAL_HRS = HRS_IN_DAY + PART_TIME_HRS
DAYS_IN_MONTH = 20


def check_attendance():
    global WORKING_DAYS
    global Total_Wage
    WORKING_DAYS = 0
    Total_Wage = 0
    while WORKING_DAYS != DAYS_IN_MONTH :
        attendance = rm.randint(0,2)
        match attendance :
            case 1 :
                print("Employee is Present")
                WORKING_DAYS+=1
                Total_Wage += cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)

            case 2:
                print("Employee is present and worked parttime")
                WORKING_DAYS+=1
                Total_Wage += part_time_wage(RATE_PER_HR, TOTAL_HRS)

            case _:
                print("Employee is absent")
                  
#UC2
def cal_dalily_wage(wage, hour):
    cal_daily_wage = wage*hour
    return cal_daily_wage

#UC3
def part_time_wage(wage, hour):
    part_time_wages = wage*hour
    return part_time_wages

#UC5
def cal_monthly_wage():
    print("Monthly Wage of Employee is ", Total_Wage)
check_attendance()
cal_monthly_wage()

