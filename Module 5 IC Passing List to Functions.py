def addToList():
    global food
    food = str(input("Input a food item: "))
#####^^^^ asks for a new food item to add to the list    


def printList(food):
    global myList
    myList = ["apple", "orange", "grape"]
    myList.append(food)
    ###^^^ adds the food item from function addToList() to the list
    print(myList)
    
def removeFromList(myList):
    RemoveItem = int(input("Pick an item to remove from the list (first item is 0)"))
    myList.pop(RemoveItem)
    print(myList)


addToList()
printList(food)
removeFromList(myList)
    
    