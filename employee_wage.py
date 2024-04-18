import random as rm

def check_attendance():
    n = rm.randint(0,1)
    if n==1:
        print("Emplpoyee is Present")
    else :
        print("Employee is Present")
        
check_attendance()            

#UC2

def cal_dalily_wage():
    rate_per_hr = 20
    hrs_in_day = 8
    return f"Daily wage of employee is {rate_per_hr*hrs_in_day}"

