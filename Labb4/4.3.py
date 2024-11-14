def sums(list):
    result = {
        "odd": 0,
        "even": 0,
        "all": 0
    }

    for number in list:
        result["all"] += number

        if number % 2 == 0:
            result["even"] += number

        else:
            result["odd"] += number

    return result



print(sums([1, 2, 3, 4, 5]))
print(sums([5,10,15,20]))