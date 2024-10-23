#LOWER AND UPPER BOUND MULTIPLICATION TABLE

table_number = int(input("which table do you want to see? "))
lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))


for i in range(lower_bound, upper_bound + 1):
    answer = i * table_number
    print(str(i) + " * " + str(table_number) + " = " + str(answer))

