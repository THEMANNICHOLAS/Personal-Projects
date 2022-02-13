number1 = input("Input number 1 ")
while number1==str(number1):
    try:
        number1 = float(number1)
    except:
        print("That is not a valid number. Please try again.")
        number1 = input("Input number 1 ")

number2 = input("Input number 2 ")
while number2==str(number2):
    try:
        number2 = float(number2)
    except:
        print("That is not a valid number. Please try again.")
        number2 = input("Input number 2 ")

number3 = input("Input number 3 ")
while number3==str(number3):
    try:
        number3 = float(number3)
    except:
        print("That is not a valid number. Please try again.")
        number3 = input("Input number 3 ")

number4 = input("Input number 4 ")
while number4==str(number4):
    try:
        number4 = float(number4)
    except:
        print("That is not a valid number. Please try again.")
        number4 = input("Input number 4 ")

number5 = input("Input number 5 ")
while number5==str(number5):
    try:
        number5 = float(number5)
    except:
        print("That is not a valid number. Please try again.")
        number5 = input("Input number 5 ")
numberTotal = number1 + number2 + number3 + number4 + number5
print(numberTotal)


#This is the second half of OYO Exercise.

mystring = "I am studying Computer Programming"
myStringCapital = mystring.upper()
print(myStringCapital)

myStringLower = mystring.casefold()
print(myStringLower)

myStringTitle = mystring.title()
print(myStringTitle)

myStringLetterM = mystring.count("m")
print(myStringLetterM)

myStringSwapCase = mystring.swapcase()
print(myStringSwapCase)