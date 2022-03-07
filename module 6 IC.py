import sys
userSign = input("Create a sign with a max number of 8 characters\n")
if len(userSign)>8:
    print("Error, that is more than 8 characters.")
    sys.exit()
    
numChar = len(userSign)

color = input("Choose a color: gold (type g) or silver (type s).\n")
wood = input("Would you like oak wood? It will be $20 extra (Type Y for yes or N for no)\n")



def CalcChar(numChar):
    global cost
    cost = numChar * 20

def CalcColors(color, numChar):
    global colorCost
    color = color.upper()
    if color == "G":
        colorCost = numChar * 8
    elif color == "S":
        colorCost = numChar * 9

def WoodType(wood, cost):
    global woodCost
    wood = wood.upper()
    if wood == "Y":
        woodCost = cost + 20
    elif wood == "N":
        woodCost = cost + 0


CalcChar(numChar)
CalcColors(color, numChar)
WoodType(wood, cost)

totalCost = cost + colorCost + woodCost
print("$" + str(totalCost))