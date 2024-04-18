import random as rm

def check_attendance():
    n = rm.randint(0,1)
    if n==1:
        print("Emplpoyee is Present")
    else :
        print("Employee is Present")
        
check_attendance()            

#UC2

rate_per_hr = 20
hrs_in_day = 8
def cal_dalily_wage():
    print(f"Daily wage of employee is {rate_per_hr*hrs_in_day}")
cal_dalily_wage()

# UC3

part_time_hr = 4
def cal_part_wage():
    total = part_time_hr*rate_per_hr 
    print(f"PartTime wage of employee is {total}")
cal_part_wage()

