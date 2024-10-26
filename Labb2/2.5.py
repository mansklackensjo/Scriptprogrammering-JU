def stringWithNumbers(lastNumber):
    result = "1"
    for i in range(2, lastNumber + 1):
        result = result + "_" + str(i)

    print(result)

stringWithNumbers(11)