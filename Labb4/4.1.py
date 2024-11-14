def areEqual(listA, listB):
    if len(listA) != len(listB):
        return "Not equal"
    
    for i in range(len(listA)):
        if listA[i] != listB[i]:
            return "Not equal"       
    return "Equal"



print(areEqual([1,2,3], [1,2,3]))
print(areEqual([1,2,3], [1,2]))
print(areEqual([1,2,3], [1,2,5]))