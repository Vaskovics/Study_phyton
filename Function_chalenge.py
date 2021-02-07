def sum_eo():
    n = int(input('Please enter the number: '))
    t = input('Please enteer "e" for evan or "o" for odd: ')
    result = 0
    if t == "e":
        for numbers in range(0, n):
            if numbers % 2 == 0:
                result += numbers
        print(result)
    elif t == "o":
        for numbers in range(0, n):
            if numbers % 2 != 0:
                result += numbers
        print(result)
    else:
        print(-1)

sum_eo()
