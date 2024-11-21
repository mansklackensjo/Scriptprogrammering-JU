import xml.etree.ElementTree as ET

def store_calculator(memoryValueList) -> None:
    memoryValueList_element = ET.Element('memoryValueList')
    for memoryValue in memoryValueList:
        memoryValue_element = ET.SubElement(memoryValueList_element, 'memoryValue')
        memoryValue_element.text = str(memoryValue)
    
    xml_string_memoryValueList = ET.tostring(memoryValueList_element,encoding="unicode")

    with open('Labb5/storedCalculator.xml', 'w') as xml_file:
        xml_file.write(xml_string_memoryValueList)


def load_calculator():
    memoryValueList = []
    with open('Labb5/storedCalculator.xml', 'r') as xml_file:
        xml_string_memoryValueList = xml_file.read()
        memoryValueList_element = ET.fromstring(xml_string_memoryValueList)
        for memoryValue_element in memoryValueList_element:
            memoryValueList.append(float(memoryValue_element.text))
    
    return memoryValueList
    
    

## Calculator
print("Press enter to start...")
memory = float(input("Enter start value: "))
memoryValueList = [memory]
operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))

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
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
    
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
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
    
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
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
    
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
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))

    elif operation == "undo":
        if len(memoryValueList) > 1:  # Ensure there's something to undo
            memoryValueList.pop()      # Remove the last memory value
            memory = memoryValueList[-1]  # Set memory to the previous value
            print(f"Undo successful. Current memory: {memory}")
            operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
        else:
            print("Nothing to undo.")

    elif operation == "store":
        store_calculator(memoryValueList)
        print("memory values is stored to xml file.")
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
            

    elif operation == "load":
        loaded_memory = load_calculator()
        if loaded_memory:
            memoryValueList = loaded_memory
            memory = memoryValueList[-1]
            print("memory values is restored to memory.")
        else:
            print("failed to restore memory values")

        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))

    elif operation == "show memory":
        print(memoryValueList)
        operation = (input("Enter operation (add/sub/mul/div/undo/store/load/quit): "))
        

    else:
       operation = (input("Wrong operation enter one of the following (add/sub/mul/div/undo/store/load/quit): "))

print("Quiting...")