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


input("Play Fizz Buzz.   Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    #player_answer = input('You go: ')
    player_answer = correct_answer
    if player_answer != correct_answer:
        print(f'You lose, the correct answer was {correct_answer}')
        break
else:
    print(f"Well done, you raached {next_number}")