from datetime import timedelta
import sys
name = input("What is your name?")
name = [name]
print("There are three reservation times available.")
print("One is at 6:00 p.m, one at 7:00 p.m, and one at 8:00 p.m")
print("Type in the number for the time you want (i.e 6, 7, 8) or type 0 to cancel")
time = input()
while time == str(time):
    try:
        time = int(time)
    except:
        print("That is not a number. Please try again.")
        print("What is your reservation time?")
        time = input()

if time == "0":
    sys.quit()

elif time == "6":
    time = "6:00"
    time = [time]

elif time == "7":
    time = "7:00"
    time = [time]

elif time == "8":
    time = "8:00"
    time = [time]

reservation = name + str(time)
print(reservation)

