# def xxx(lastNumber:int):
#     summa = 1
#     for i in range(2, lastNumber + 1):
#         summa += i*i

#     return summa

# print(xxx(3))


def xxx(lastNumber:int):
    summa = 0
    for i in range(1, lastNumber + 1):
        summa += i*i

    return summa

print(xxx(3))