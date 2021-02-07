def sum_numbers(*x: float) -> float:
    """
    The function calculate the sum of all numbers of all arguments in sequences
    :param x:sequences of int
    :return:sum of all int sequences
    """
    result = sum(x)
    return result


print(sum_numbers(1.1, 2.2, 5.5))