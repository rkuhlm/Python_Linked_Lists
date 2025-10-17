even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

numbers = even + odd
print(numbers)

# This will create a list of lists.
# In this case, we have a list containing two lists.
# The list EVEN and the list ODD join to create a list of lists named NUMBERS
numbers = [even, odd]
print(numbers)

# we can use nested for loops to loop through items within a listed list.

for i in numbers:
    print(i)  # i will be the list inside the NUMBERS list. EVEN and then ODD

    for j in i:
        print(j)  # j will be the value of the item at each index within the EVEN and then ODD list
