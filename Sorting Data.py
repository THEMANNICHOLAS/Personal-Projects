import statistics


def inputScore():
    global testScoreList
    testScoreList = []  
    toContinue = "Y"

    while toContinue == "Y":
        score = input("Input a score\n")
        testScoreList.append(score)
        print(testScoreList)
        toContinue = input("Continue?\n")
        toContinue = toContinue.upper()

        if len(testScoreList) > 9:   
            print("""You exceeded the 10 score limit. Every score inputted after
            first 10 does not count.""")
            return testScoreList

    if toContinue =="N":
        return testScoreList


def calculateMeanAndMedian(array):
    array = [int(i) for i in array]

    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print("Sorted array is: ", array)
    print("Mean is " + str(statistics.mean(array)))
    print("Median is " + str(statistics.median(array)))
    
    array.pop(0)
    array.pop(0)
    array.pop(0)
    array.pop(0)
    
    print("6 Highest Scores Mean and Median: ")
    print("6 Highest Sorted array is: ", array)
    print("Mean is " + str(statistics.mean(array)))
    print("Median is " + str(statistics.median(array)))

name = input("Input your name.\n")
print("Would you like to enter your scores? Y for yes, N for no.\n")
toContinue = input()
toContinue = toContinue.upper()

while toContinue == "Y":
    inputScore()
    print(name)
    print("The result is: ")
    calculateMeanAndMedian(testScoreList)



