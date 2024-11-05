## Calculator
def calcOpening():
    memory = int(input("Enter start value: "))
    operation = (input(f"Enter operation (add/sub/mul/div/quit): "))

    return memory, operation


print("Press enter to start...")
memory = float(input("Enter start value: "))
operation = (input("Enter operation (add/sub/mul/div/quit): "))

while operation != "quit":
    if operation == "add":
        try:
            n = float(input(f"{memory} + "))
        except:
            print("Wrong input")
            continue
        memory += n
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/quit): "))
    
    elif operation == "sub":
        try:
            n = float(input(f"{memory} - "))
        except:
            print("Wrong input")
            continue
        memory -= n
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/quit): "))
    
    elif operation == "mul":
        try:
            n = float(input(f"{memory} * "))
        except:
            print("Wrong input")
            continue
        memory *= n
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/quit): "))
    
    elif operation == "div":
        try:
            n = float(input(f"{memory} / "))
        except:
           print("Wrong input")
           continue
        memory /= n
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/quit): "))

    else:
       operation = (input("Wrong operation enter one of the following (add/sub/mul/div/quit): "))

print("Quiting...")


