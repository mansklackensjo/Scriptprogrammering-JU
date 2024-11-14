## Calculator
print("Press enter to start...")
memory = float(input("Enter start value: "))
memoryValueList = [memory]
operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))

while operation != "quit":
    if operation == "add":
        try:
            n = float(input(f"{memory} + "))
        except:
            print("Wrong input")
            continue
        memory += n
        memoryValueList.append(memory)
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))
    
    elif operation == "sub":
        try:
            n = float(input(f"{memory} - "))
        except:
            print("Wrong input")
            continue
        memory -= n
        memoryValueList.append(memory)
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))
    
    elif operation == "mul":
        try:
            n = float(input(f"{memory} * "))
        except:
            print("Wrong input")
            continue
        memory *= n
        memoryValueList.append(memory)
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))
    
    elif operation == "div":
        try:
            n = float(input(f"{memory} / "))
        except:
           print("Wrong input")
           continue
        memory /= n
        memoryValueList.append(memory)
        print(f"= {memory}")
        print(f"{memory} is stored in memory.")
        operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))

    elif operation == "undo":
        if len(memoryValueList) > 1:  # Ensure there's something to undo
            memoryValueList.pop()      # Remove the last memory value
            memory = memoryValueList[-1]  # Set memory to the previous value
            print(f"Undo successful. Current memory: {memory}")
            operation = (input("Enter operation (add/sub/mul/div/undo/quit): "))
        else:
            print("Nothing to undo.")
            

    else:
       operation = (input("Wrong operation enter one of the following (add/sub/mul/div/undo/quit): "))

print("Quiting...")