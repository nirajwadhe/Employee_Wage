import random as rm
attendance = {}
def rmdm_attnd(attendance):
    for i in range(1,31):
        attendance[i] = rm.randint(0,1)

n = int(input("Enter a day: "))

def check_attendance(n,attendance):
    if attendance[n]==1:
        print("Employee is Present")
    else :
        print("Employee is asbent")    

rmdm_attnd(attendance)       
check_attendance(n,attendance)


