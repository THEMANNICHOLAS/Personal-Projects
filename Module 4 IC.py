### Ask user to input their first primary color
Color1 = input("Input your first color (Red, Blue, or Yellow)\n")
Color1 = Color1.upper()
while Color1==str(Color1):
    if Color1!="BLUE" and Color1!="RED" and Color1!="YELLOW":
       print("That is not a valid primary color")
       Color1 = input("Input your first color (Red, Blue, or Yellow)\n")
    else:
        print("ok")
        break
    
    
print("What is your next color?")

### Asks user to input second primary color
Color2 = input("Input your second color (Red, Blue, or Yellow)\n")
Color2 = Color2.upper()
while Color1==str(Color2):
    if Color2!="BLUE" and Color2!="RED" and Color2!="YELLOW":
       print("That is not a valid primary color or you typed in the same color")
       Color2 = input("Input your second color (Red, Blue, or Yellow)\n")
    else:
        print("ok")
        break
    
if Color1=="BLUE" and Color2=="YELLOW":
    print("Your color is Green")
     
elif Color1=="BLUE" and Color2=="RED":
    print("Your color is Purple")
    
elif Color1=="BLUE" and Color2=="GREEN":
    print("Your color is Blue-Green")
    
elif Color1=="RED" and Color2=="YELLOW":
    print("Your color is Orange")
    
elif Color1=="RED" and Color2=="GREEN":
    print("Your color is Brown")
    
elif Color1=="YELLOW" and Color2=="GREEN":
    print("Your color is Light Green")


#Reversed the colors for the variables. Please tell me if there is a faster way to do this.
    
if Color1=="YELLOW" and Color2=="BLUE":
    print("Your color is Green")
     
elif Color1=="RED" and Color2=="BLUE":
    print("Your color is Purple")
    
elif Color1=="GREEN" and Color2=="BLUE":
    print("Your color is Blue-Green")
    
elif Color1=="YELLOW" and Color2=="RED":
    print("Your color is Orange")
    
elif Color1=="GREEN" and Color2=="RED":
    print("Your color is Brown")
    
elif Color1=="GREEN" and Color2=="YELLOW":
    print("Your color is Light Green")



    
    

