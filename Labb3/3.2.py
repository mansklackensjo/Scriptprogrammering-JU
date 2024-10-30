def closestToZero(a, b):
    if abs(a) < abs(b):
        return a
    
    elif abs(a) > abs(b):
        return b

    else:
        return a


print(closestToZero(2, -5))
print(closestToZero(-3, -2))
print(closestToZero(3, 3))  
print(closestToZero(-8, 8))
