def fizz_buzz(x:int) -> int:
    """
    Fuction is playing fizz buzz game
    if `x` divisible 3 or 5 is printin "fizz" or "buzz"
    if `x` divisible for 3 and 5 is printin "fizz buzz"
    :param x: int
    :return: str `x` if number is divisible for 3 and 5
    """
    if x % 3 == 0 and  x % 5 == 0:
        return 'fizz buzz'
    elif x % 5 == 0:
        return 'buzz'
    elif x % 3 == 0:
        return 'fizz'
    else:
        return str(x)

input('Please press ENTER to play fizz buzz')
for i in range(1, 101):
    print(i, fizz_buzz(i))