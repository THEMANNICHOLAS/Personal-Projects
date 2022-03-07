
# importing time module
import time
statement = str(input())



def message(statement):
    
    for i in statement:
        
        # printing each character of the message
        print(i, end="")
          
        # adding time delay of half second
        time.sleep(0.05)
  
  
# main function
if __name__ == '__main__':
    statement = statement
      
    # calling the function for printing the 
    # characters with delay
    message(statement)