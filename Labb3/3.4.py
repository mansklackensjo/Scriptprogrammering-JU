def highest(listOfNumbers:list):
    
    # for i in len(listOfNumbers):
    #     if listOfNumbers[i] < listOfNumbers[i+1]:
    #         print("first is lower than second")

    highestNr = 0
    for curr in listOfNumbers:
        if curr > highestNr:
            highestNr = curr
        elif curr < highestNr:
            highestNr = highestNr
        else:
            highestNr = curr
    
    return highestNr

print(highest([2, 5, -3, 78, 29, 100, 3, 2, 32]))