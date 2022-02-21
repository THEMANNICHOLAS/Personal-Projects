import math

# Write sums() function here.
def sums(number):
    sum = 0
    for num in range(1, number + 1, 1):
        sum = sum + num
    print("Sum of first ", number, "numbers is: ", sum)
            


# Write products() function here
def products(number):
    print(math.factorial(number))
#Importing math and using .factorial() attribute finds factorial



numberString = input("Enter a positive integer, or enter 0 to quit: ")
number = int(numberString)

    
while number != 0:
    # Call sums() function here.
    sums(number)
    products(number)
    break
    
    # Call products() function here.

    
    
    
