import random as rm
RATE_PER_HR = 20
HRS_IN_DAY = 8
PART_TIME_HRS = 4
TOTAL_HRS = HRS_IN_DAY + PART_TIME_HRS
DAYS_IN_MONTH = 20

TOTAL_HRS_WORKED = 0
TOTAL_DAYS_WORKED = 0

WAGES_RECORD = []
TOTAL_WAGES = []
DAYWISE_WAGE = {}

def check_attendance():
        global TOTAL_HRS_WORKED 
        global TOTAL_DAYS_WORKED
        while TOTAL_HRS_WORKED<100 or TOTAL_DAYS_WORKED < 20 :
            attendance = rm.randint(0,2)
            match attendance :
                case 1 :
                    print("Employee is Present")
                    wage = cal_dalily_wage(RATE_PER_HR, HRS_IN_DAY)
                    TOTAL_DAYS_WORKED+=1
                    TOTAL_HRS_WORKED+=8
                    DAYWISE_WAGE[TOTAL_DAYS_WORKED] = wage
                    cal_monthly_wage(RATE_PER_HR,TOTAL_DAYS_WORKED,TOTAL_HRS_WORKED)

                case 2:
                    print("Employee is present and worked parttime")
                    wage = part_time_wage(RATE_PER_HR, TOTAL_HRS)
                    TOTAL_DAYS_WORKED+=1
                    TOTAL_HRS_WORKED+=12
                    DAYWISE_WAGE[TOTAL_DAYS_WORKED] = wage
                    cal_monthly_wage(RATE_PER_HR,TOTAL_DAYS_WORKED,TOTAL_HRS_WORKED)
                
                case _:
                    DAYWISE_WAGE[TOTAL_DAYS_WORKED] = "absent"

            print(TOTAL_HRS_WORKED)    
#UC2
def cal_dalily_wage(wage, hour):
    daily_wages = wage*hour
    WAGES_RECORD.append(daily_wages)
    return daily_wages

#UC3
def part_time_wage(wage, hour):
    daily_wages = wage*hour
    WAGES_RECORD.append(daily_wages)
    return daily_wages

#UC5
def cal_monthly_wage(wage, hour, day):
    total_wage = wage*hour*day
    TOTAL_WAGES.append(total_wage)
    return total_wage

#UC7
def view_total_work_hrs() :
    print("Total HRS of the Employee is - ",TOTAL_HRS_WORKED)

check_attendance()
view_total_work_hrs()
print(WAGES_RECORD)
print(TOTAL_WAGES)
print(DAYWISE_WAGE)