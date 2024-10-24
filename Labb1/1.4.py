#MULTIPLICATION TABLE

print("This program displays a multiplication table between 0 to 9")
table_number = int(input("which table do you want to see? "))

if table_number < 9 and table_number > 0:
    for i in range(11):
        answer = i * table_number
        print(str(i) + " * " + str(table_number) + " = " + str(answer))

else:
    print("Value entered was not between 0 and 9")