import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
PART_TIME_HRS = 4
TOTAL_HRS = HRS_IN_DAY + PART_TIME_HRS
DAYS_IN_MONTH = 20
def check_attendance():
    attendance = rm.randint(0,2)

    TOTAL_HRS_WORKED = 0
    TOTAL_DAYS_WORKED = 0

    while TOTAL_HRS_WORKED<100 or TOTAL_DAYS_WORKED < 20 :
        TOTAL_DAYS_WORKED+=1
        TOTAL_HRS_WORKED+=8
    match attendance :
        case 1 :
            print("Employee is Present")
            cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)

            while TOTAL_HRS_WORKED<100 or TOTAL_DAYS_WORKED < 20 :
                TOTAL_DAYS_WORKED+=1
                TOTAL_HRS_WORKED+=8
            cal_monthly_wage(RATE_PER_HR,TOTAL_DAYS_WORKED,TOTAL_HRS_WORKED)

        case 2:
            print("Employee is present and worked parttime")
            part_time_wage(RATE_PER_HR, TOTAL_HRS)

            while TOTAL_HRS_WORKED<100 or TOTAL_DAYS_WORKED < 20 :
                TOTAL_DAYS_WORKED+=1
                TOTAL_HRS_WORKED+=12

            cal_monthly_wage(RATE_PER_HR,TOTAL_HRS_WORKED,TOTAL_DAYS_WORKED)
        
        case _:
            print("Employee is absent")
                  
#UC2
def cal_dalily_wage(wage, hour):
    print("Daily wage of employee is ", wage*hour)

#UC3
def part_time_wage(wage, hour):
    print("Parttime wage of employee is ", wage*hour)

#UC5
def cal_monthly_wage(wage, hour, day):
    print("Monthly Wage of Employee is ", wage*hour*day)
check_attendance()

