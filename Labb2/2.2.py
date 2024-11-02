def sums(list):
    sum = 0
    for number in list:
        sum += number
    
    return sum

def average(listOfNumbers):
    return sums(listOfNumbers)/len(listOfNumbers)

print(average([2, 4, 6]))