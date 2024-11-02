def xxx(lastNumber:int):
    summa = 0     
    for i in range(1, lastNumber + 1):
        summa += i*i

    return summa

print(xxx(2))