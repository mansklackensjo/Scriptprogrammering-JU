def counter(listOfStrings:list, string:str):
    count = 0
    for str in listOfStrings:
        if string == str:
            count += 1
        
    return count

print(counter(["a", "a", "a", "b"], "b"))

