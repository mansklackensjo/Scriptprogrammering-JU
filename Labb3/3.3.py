def closestToZero(a, b):
    if abs(a) < abs(b):
        return a
    
    elif abs(a) > abs(b):
        return b

    else:
        return a
    
def closestToZero4(a, b, c, d):
    return closestToZero(closestToZero(a, b), closestToZero(c, d))

print(closestToZero4(-6, 6, -4, 38))