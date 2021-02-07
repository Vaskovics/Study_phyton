def sum_numbers(*x: float) -> float:
    res = 0
    for number in x:
        res += number
    return res


print(sum_numbers(2,3,4,5))