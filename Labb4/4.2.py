def highestNum(list):
    highest = list[0]
    for curr in list:
        if curr > highest:
            highest = curr
    
    return highest
            
        
def changeToHighest(list):
    for i in range(len(list)):
        list[i] = highestNum(list[i])


theList = [
    [1, 2, 3],
    [5, 4, 3],
    [2, 7, 6]
]


print(theList)
changeToHighest(theList)
print(theList)