# Computing products

# This program computes the product of the integers in a range.
# Enter the lower number of the range: 3
# Enter the upper number of the range: 5
# The product of the integers between 3 and 5 is 60.

start = int(input("Enter lower end: "))
stop = int(input("Enter higer end: "))
product = 1


for i in range(start, stop+1):
    product *= i
    
print(product)