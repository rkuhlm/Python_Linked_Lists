def sum_numbers(*val):
    result = 0
    for nums in val:
        result += nums
    return result


print(sum_numbers(1, 2, 3.0))

