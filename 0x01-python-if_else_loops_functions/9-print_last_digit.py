st_digit(number):
    if number < 0:
        number *= -1
    num = number % 10
    print("{}".format(num), end='')
    return num
