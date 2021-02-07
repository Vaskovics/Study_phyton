def multiply(x: float, y: float) ->float:
    """
        Multiply 2 numbers.

        Although this function is intended to multiply 2 numbers,
        you can also use it to multiply a sequence.  If you pass
        a string, for example, as the first argument, you'll get
        the string repeated `y` times as the returned value.

        :param x: The first number to multiply.
        :param y: The number to multiply `x` by.
        :return: The product of `x` and `y`.
        """
    result = x * y
    return result


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


def is_palindrome(string: str) -> bool:
    """
       Check if a string is a palindrome.

       A palindrome is a string that reads the same forwards as backwards.

       :param string: The string to check.
       :return: True if `string` is a palindrome, False otherwise.
       """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
        Check if a sentence is a palindrome.

        The function ignores whitespace, capitalisation and
        punctuation in the sentence.

        :param sentence: The sentence to check.
        :return: True if `sentence` is a palindrome, False otherwise.
        """
    string = ""

    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    #return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

def fibonacci(n: int) -> int:
    """ Return the `n`th Fibinacci number, to positive `n`"""
    if 0 <= n <=1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 +n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result

def v_fibonacci(n):
    """ Return the `n` th Fibinacci number, to positive `n`"""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0
    result = None

    for i in range(n -1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


def factorial(x):
    """
    Return factorial from number x
    :param x:
    :return:
    """
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc
    :param text: The text to print.
    :param effect: The effect we want. On of the costants
        defined at the start of this module.
    """
    output_string = "{}{}{}".format(effect, text, RESET)
    print(output_string)


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



