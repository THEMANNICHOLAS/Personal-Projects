monthlist = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
salesnum = [103,104,201,319,267,388,435]
salesname = ["Darwin", "Kratz", "Shulstad","Fortune","Wickert","Miller","Vick"]

userNumber = input("Input your your saleperson number\n")

def validateUser(salesnum, userNumber):
try:
    userNumber = int(userNumber)
except:
    print("Invalid user number")


    for number in salesnum:
        while salesnum != number:
            print("Invalid user number")
            userNumber = input("Input your your saleperson number\n")
    if salesnum == num:
        return


def validateUserName(salesname):
    global salesName
    for name in salesname:
        while salesname != name:
            print("Invalid user name")
            salesname = input("Input your name\n")
    if salesname == name:
        return

def inputSalesDate(monthlist):
    saleDate = input("Input the month of sale transaction")
    for month in monthlist:
        while saleDate != month:
            print("Invalid sale date")
            saleDate = input("Input a month.\n")    
    if saleDate == month:
        saleDate = [saleDate]
        print(saleDate)
        return


validateUser(salesnum, userNumber)   
validateUserName(salesname) 


