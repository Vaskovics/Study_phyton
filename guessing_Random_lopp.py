import random

def  get_integer(prompt):
    """
    Get an integer from Standart Input (stdin).
    Tht function will continue looping, and promting
    the user, until walid 'int' is enterd.

    :param prompt: The string that user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else:
        print(f"{temp} is not a valid number")


highest = 1000
answer = random.randint(1, highest)
print(answer)
print("Please guess number between 1 and {}".format(highest))
guess = 0

while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("Well done you guessed it ")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        elif guess > answer:
            print("Please guess lower")


