import math


def factorial(num) -> int:
    """
    Takes `num`  number and computes the factorial for `num`.
    :param num:
    :return:
    """
    result = math.factorial(num)
    return result


for i in range(36):
    print(i, factorial(i))
