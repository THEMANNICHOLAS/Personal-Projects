# Calculator.py - This program performs arithmetic, ( +. -, *. / ) on two numbers.
# Input:  Interactive
# Output:  Result of arithmetic operation

# Write performOperation function here
def performOperation(numberOne, numberTwo, operation):
    global result
    if operation == "*":
        result = numberOne * numberTwo
    elif operation == "+":
        result = numberOne + numberTwo
    elif operation == "/":
        result = numberOne / numberTwo
    elif operation == "-":
        result = numberOne - numberTwo
    
    
    

numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
operation = input("Enter an operator (+ - * /): ")

# Call performOperation method here and store the value in "result"
performOperation(numberOne, numberTwo, operation)


print(str(numberOne) + " " + operation + " " + str(numberTwo) + " = " + str(result))
