
a = int(input("Enter a number: "))
b = int(input("Enter a number higher than the first one: "))
if a < b:
    sumOfEvens = 0
    for number in range(a, b +1):
        if number % 2 == 0:
            sumOfEvens += number
            
    print(f"This is the total sum of the even numbers in the range: {sumOfEvens}")
else:
    print("Did not follow the instructions!")


