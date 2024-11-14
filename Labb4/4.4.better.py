# Calculator Operations
def add(memory, n):
    return memory + n

def subtract(memory, n):
    return memory - n

def multiply(memory, n):
    return memory * n

def divide(memory, n):
    if n == 0:
        print("Cannot divide by zero.")
        return memory
    return memory / n

# Main Calculator Function
def calculator():
    print("Press enter to start...")
    memory = float(input("Enter start value: "))
    memory_history = [memory]
    
    # Map operation strings to functions
    operations = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide
    }
    
    while True:
        operation = input("Enter operation (add/sub/mul/div/undo/quit): ")

        if operation == "quit":
            print("Quitting...")
            break

        elif operation == "undo":
            if len(memory_history) > 1:
                memory_history.pop()  # Remove last entry
                memory = memory_history[-1]
                print(f"Undo successful. Current value: {memory}")
            else:
                print("Nothing to undo.")
                
        elif operation in operations:
            try:
                n = float(input(f"{memory} {operation} "))
            except ValueError:
                print("Invalid input, please enter a number.")
                continue
            
            # Execute the operation function
            memory = operations[operation](memory, n)
            memory_history.append(memory)
            print(f"= {memory}")
            
        else:
            print("Invalid operation. Please choose add/sub/mul/div/undo/quit.")

# Run the calculator
calculator()


