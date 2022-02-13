def salePersonID():
    global ID
    ID = input("Input Your ID ")
    while ID == str(ID):
        try:
            ID = float(ID)
        except:
            print("Your ID is not valid. Please try again.")
            ID = input("Input Your ID ")
    return


def itemsSold():
    global Items
    global TotalSaleAmount
    Items = input("How many items did you sold? ")
    while Items == str(Items):
        try:
            Items = int(Items)
        except:
            print("Please type in a numerical value (no decimals)")
            Items = input("How many items did you sold? ")             
    TotalSaleAmount = input("What is your sale amaunt? ")
    while TotalSaleAmount == str(TotalSaleAmount):
        try:
                TotalSaleAmount = float(TotalSaleAmount)
        except:
                print("Please type in a numerical value")
                Items = input("What is your sale Amount ")   
    return


def HighOrLowSeller():
    if Items>50 and TotalSaleAmount>2000:
        print("You are a high seller! Congratulations!")
    else:
        print("You are a low Seller. Maybe next time :(")
    return

def main():
    salePersonID()
    itemsSold()
    HighOrLowSeller()
main()

    
    



        

        

        



## Main Function below





