def fizz_buzz(num=int) -> str:
    """
    fizz_buzz
    :param num: 
    :return:
    """
    if num % 3 == 0 and num % 5 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)


for i in range(1, 101):
    print(i, fizz_buzz(i))

