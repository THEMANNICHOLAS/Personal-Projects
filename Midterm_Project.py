rating = input("Input a rating 1 to 4. Enter -1 to quit.\n")


while rating == rating:
    if rating == str(rating):
        try:
            rating = int(rating)
        except:
            print("That is an invalid value.")
            rating = input("Input a rating 1 to 4. Enter -1 to quit.\n")
        else:
            if rating != 1 and rating != 2 and rating != 3 and rating != 4 and rating != -1:
                print("That is an invalid value.")
                rating = input("Input a rating 1 to 4. Enter -1 to quit.\n")
            elif rating == -1:
                    quit
            elif rating == 1 or rating == 2 or rating == 3 or rating != 4:
                print("Average Star Rating: 3.5.")
