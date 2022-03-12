import sys
userNumber = input("Type in whatver number you want, as many as you want whether negative or positive\nType '0' to cancel.\n")


if userNumber == "0":
    sys.exit()

while userNumber == str(userNumber):
    try:
        userNumber = int(userNumber)
    except:
        print("That is not a number. Please try again")
    userNumber = input("Type in whatver number you want, as many as you want whether negative or positive\nType '0' to cancel.\n")



numberList = []
numberList.append(userNumber)




print("Do you want to continue? Type 'Y' for yes or 'N' for no.\n")
toContinue = str(input())
toContinue = toContinue.upper()

while toContinue != "Y" and toContinue == "N":
    print("That is not a valid value. Please try again\n")
    toContinue = input("Do you want to continue? Type 'Y' for yes or 'N' for no.\n")
    toContinue = toContinue.upper()

while toContinue == "Y":
        print("What is your next number?")
        userNumber = input()
        numberList.append(userNumber)
        print("Continue?")
        toContinue = str(input())
        toContinue = toContinue.upper()
        print(numberList)

while toContinue == "N":
    print("Ok")
    break





### Converts all value in the list to integers
for i in range(0, len(numberList)):
    numberList[i] = int(numberList[i])


def addNegativeNumbers(numberList):
    total = 0

    ### Makes and sorts out numberList to just values below 0
    numberList2 = [x for x in numberList if x < 0]

    ### Adds all values in numberList2, which are already sorted
    for value in range(0, len(numberList2)):
        total = total + numberList2[value]
    print(total)  


def addPositiveNumbers(numberList):
    total = 0

    numberList3 = [x for x in numberList if x > 0]
    for value in range(0, len(numberList3)):
        total = total + numberList3[value]
    print(total)

def allNumbers(numberList):
    total = 0
    for x in range(0, len(numberList)):
        total = total + numberList[x]
    print(total)



addNegativeNumbers(numberList)
addPositiveNumbers(numberList)    
allNumbers(numberList)
