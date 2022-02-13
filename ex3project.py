def computepay(hours, rate):
    print("In computepay", hours, rate)

sh=input("Enter Hours: ")
sr=input("Enter Rate: ")
try:
    fh=float(sh)
    fr=float(sr)
    computepay(fh, fr)
except:
    print("That is not a number. Please type a number")
    sh=input("Enter Hours: ")
    sr=input("Enter Rate: ")
    fh=float(sh)
    fr=float(sr)
    computepay(fh, fr)
#Following line is overtime pay
if fh>40:
    print("Overtime: ")
    xp=(fr*40)+(fh-40)*fr*1.5
#following line is normal pay
else:
    print("Regular: ")
    xp=float(fh)*float(fr)
print("Pay:", float(xp))
#fh is hours. Parameter for computepay function
#fr is rate. Parameter for computepay function
