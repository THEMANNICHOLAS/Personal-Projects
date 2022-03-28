deptSalary= [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
deptList = ["Personnel", "Marketing", "Manufacturing", "Computer Services", "Sales", "Accounting", "Shipping"]
def printDeptList(deptSalary, deptList):
    print("Salary by department:\n" + str(deptSalary))
    print(deptList)
    print("1 - Personnel")
    print("2 - Marketing")
    print("3 - Manufacturing")
    print("4 - Computer Services")
    print("5 - Sales")
    print("6 - Accounting")
    print("7 - Shipping")
    
def validateDept(dept):
    global DeptNumber
    DeptNumber = input("Input department number.\n")
    while DeptNumber == str(DeptNumber):
        try:
            DeptNumber = int(DeptNumber)
        except:
            DeptNumber = input("That is not a valid department number.\n Try again.")
        
    while DeptNumber > 7 or DeptNumber < 0:
        DeptNumber = input("That is not a valid department number.\n Try again.")
        try:
            DeptNumber = int(DeptNumber)
        except:
            DeptNumber = input("That is not a valid department number.\nTry again.")
    return

def validateHours():
    global hours
    hours = input("How many hours worked for the week?\n")
    try:
        hours = float(hours)
    except:
        hours = input("Enter a numerical value")
        



def validateRate():
    global hourlySalary
    hourlySalary = input("What is your hourly salary?\n")
    try:
        hourlySalary = float(hourlySalary)
    except:
        hourlySalary = input("Enter a numerical value")
        
        

def deptWages(DeptNumber, hours, hourlySalary, deptSalary):
    wage = hours * hourlySalary
    
    if DeptNumber == 1:
        deptSalary[0] = deptSalary[0] + hourlySalary
    elif DeptNumber == 2:
        deptSalary[1] = deptSalary[1] + hourlySalary
    elif DeptNumber == 3:
        deptSalary[2] = deptSalary[2] + hourlySalary
    elif DeptNumber == 4:
        deptSalary[3] = deptSalary[3] + hourlySalary
    elif DeptNumber == 5:
        deptSalary[4] = deptSalary[4] + hourlySalary
    elif DeptNumber == 6:
        deptSalary[5] = deptSalary[5] + hourlySalary
    elif DeptNumber == 7:
        deptSalary[6] = deptSalary[6] + hourlySalary
        
        
def printTotalSalary(deptSalary):
    print(deptSalary)
 
def main():
    again = "Y"
    dept = 0
    while again.upper() == "Y":
        print("You will need to enter the employee's department number, hours worked and hourly salary")
        printDeptList(deptSalary, deptList)     
        #Get valid input
        validateDept(dept)
        validateHours()
        validateRate()
      #add to correct department list  
        deptWages(DeptNumber,hours,hourlySalary, deptSalary)
        printTotalSalary(deptSalary)
    
        again = input("Enter Y to continue")
        
main()
