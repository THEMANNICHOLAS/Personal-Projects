# Computation.py - This program calculates sum, difference, and product of two values.
# Input: Interactive
# Output: Sum, difference, and product of two values. 

# Write calculateSum function here
def calculateSum(value1, value2):
    ssum = value1 + value2
    print(ssum)
     
# Write calculateDifference function here
def calculateDifference(value1, value2):
    difference = value1 - value2
    print(difference)

# Write calculateProduct function here
def calculateProduct(value1, value2):
    product = value1 * value2
    print(product)

value1 = int(input("Enter first numeric value: "))
value2 = int(input("Enter second numeric value: "))
      
# Call calculateSum
calculateSum(value1, value2)
# Call calculateDifference
calculateDifference(value1, value2)
# Call calculateProduct
calculateProduct(value1, value2)