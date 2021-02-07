low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Please press ENTER to start")

guesses = 1
while low != high :
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low)//2
    high_low = input("Me guess is {}. Shoul I guess higher or lower ?"
                     "Enter h or l, or c if my guess was correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low== 'c':
        print("I got it in {} guesses!".format(guesses))
        break
    guesses += 1
else:
    print("You thought the number {}".format(low))
    print('I got it in {} guesses'.format(guesses))


