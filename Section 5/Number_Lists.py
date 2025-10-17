even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

numbers = even + odd
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print()
# len is length
print(len(even))
print(len(odd))
print()
print("mississippi".count("s"))


# extend will add the lists together.
# this will pass the odd list into the even list.
# it will add the list onto the end of the even list
even.extend(odd)
print(even)
# sort will sort the list
even.sort()
print(even)
# sort the list in reverse order
even.sort(reverse=True)
print(even)
