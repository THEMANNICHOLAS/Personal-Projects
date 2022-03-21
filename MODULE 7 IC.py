import sys

def reservation():
    global name
    name = input("What is your name?\n")
    name = [name]
    print("There are three reservation times available.")
    print("One is at 6:00 p.m, one at 7:00 p.m, and one at 8:00 p.m")
    print("Type in the number for the time you want (i.e 6, 7, 8) or type 0 to cancel")
    time = input()
    time = str(time)

    while time != "6" and time != "7" and time != "8" and time != "0":
        time = input("That is not a valid number. What is your reservation time?\n")
   
    time = str(time)
    if time == "0":
        sys.exit()
    
    elif time == "6":
        time = "6:00"
        name.append(time)
    
    elif time == "7":
        time = "7:00"
        name.append(time)

    elif time == "8":
        time = "8:00"
        name.append(time)
   
   
    print(name)
######################################
######################################
######################################
def addPerson(name):
    newPerson = input("What is the name of this person?")
    name.insert(0, newPerson)
    print(name)




reservation()     

print("Would you like to add another person? Type Y/Yes or N/No")
validate = input()
validate = validate.upper()
while validate == validate:
    if validate == "Y":
        addPerson(name)
        validate = input("Would you like to add another person? Type Y/Yes or N/No")
        validate = validate.upper()
    if validate == "N" or validate != "N":
        sys.exit()
        
   





