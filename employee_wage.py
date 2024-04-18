import random as rm

def check_attendance():
    attendance = rm.randint(0,1)
    if attendance==1:
        print("Emplpoyee is Present")
    else :
        print("Employee is Present")
        
check_attendance()            


