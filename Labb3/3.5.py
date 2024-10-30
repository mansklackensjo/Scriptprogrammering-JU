def counter(listOfStrings:list, string:str):
    count = 0
    for i in listOfStrings:
        if string == i:
            count += 1
        
    return count

print(counter(["a", "a", "a", "b"], "b"))

