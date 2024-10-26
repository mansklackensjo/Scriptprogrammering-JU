# Enter multiplication table: 5
# Enter number of questions: 3
# What is 5 * 6?
# Enter answer: 20
# Correct answer is 30.
# What is 5 * 2?
# Enter answer: 10
# Correct answer is 10.
# What is 5 * 8?
# Enter answer: 45
# Correct answer is 40.

import random
tableNumber = int(input("Enter a multiplication table: "))
numberOfQuestions = int(input("Enter number of questions: "))
print()
for i in range(numberOfQuestions):
    randy = random.randint(0, 9)
    print(f"What is {tableNumber} * {randy}" )
    answer = int(input("Enter answer: " ))
    print(f"Correct answer is {tableNumber * randy}")
    print()

