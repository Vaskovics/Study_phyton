def mile_converter(x):
    """
    function is convert distance in kilometers into miles
    :param x: convert kilometers into miles
    :return: get miles
    """
    distance = x / 1.60934
    return round(distance)


a = int(input('Please enter the distanec: '))
x = mile_converter(a)
print(x)