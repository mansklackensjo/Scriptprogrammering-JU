# 1.3 the average of x numbers


# With a list that loops the amount that the user wants, to then summarize with built
# in function and calculate the average nunmber then print it.


number_amount = int(input("How many numbers do you wanna enter? "))

list_of_numbers =[int(input("Type a number: ")) for _ in range(number_amount)]
    
summary = sum(list_of_numbers)

average = summary/number_amount

print("This is the average number: " + str(average))