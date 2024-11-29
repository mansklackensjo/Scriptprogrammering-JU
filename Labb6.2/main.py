from lab_06_calculator import Calculator

input("Press enter to start...")
initial_memory_value = (input("Enter initial memory value: "))
if initial_memory_value.isdigit() == True:

    calculator = Calculator(int(initial_memory_value))
    operation = ""

else:
    print("wrong input!")
    operation = "quit"

while operation != "quit":
    
    operation = input("Enter operation (add/sub/mul/div/undo/quit): ")

    if operation in ["add", "sub", "mul", "div"]:

        operand = int(input("Enter operand: "))

        if operation == "add":
            calculator.add(operand)
        if operation == "sub":
            calculator.subtract(operand)
        if operation == "mul":
            calculator.multiply(operand)
        if operation == "div":
            calculator.divide(operand)
        
        print(calculator.get_memory_value())
    
    elif operation == "undo":
        if calculator.can_undo() == False:
            print("Nothing to undo")
        
        else:
            calculator.undo()
            print(f"memoryvalue is set to previous ({calculator.get_memory_value()})")

    elif operation == "history":

        print(calculator.get_history())

    else:
        print("Wrong operation, try again!")

    



	 
	

