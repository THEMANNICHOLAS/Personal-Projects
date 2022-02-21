#Creates a list
fruits = []
print(fruits)


#Prints the list
fruits = ["Apples", "Oranges", "Grapes", "Strawberries", "Pineapple", "Mango"]
print(fruits)


#Adds the word "Peach" to the end of the list
fruits.append("Peach")
print(fruits)


#Inserts the word "Pear" at position 3
fruits.insert(3, "Pear")
print(fruits)


#Prints out value of "Oranges" in the list
print(fruits.index('Oranges'))


#Removes the word "Pineapple" from the list
fruits.remove("Pineapple")
print(fruits)


#Sorts list alphabetically
fruits.sort()
print(fruits)


#Oppoiste of alpabetize
fruits.reverse()
print(fruits)

#Finds value of "Grapes" and removes it. fruits.pop() otherwise would remove the last item in the list
x = fruits.index("Grapes")
fruits.pop()
print(fruits)


