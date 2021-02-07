def fibonacci(n):
    """ Return the `n`th Fibinacci number, to positive `n`"""
    if 0 <= n <=1:
        return n

    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result

for i in range(40):
    print(i, fibonacci(i))