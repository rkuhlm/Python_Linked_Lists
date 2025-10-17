my_iterable = [1, 2, 3]

# In the FOR loop, the my_iterable is the object that we want to iterate through.
# in the FOR loop, the item_name is the name of each object as we iterate through the iterable object.
for item_name in my_iterable:
    print(item_name)

print("-------------------------------------------------------------------")

my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_List:
    print(num)

print("-------------------------------------------------------------------")
for evens in my_List:
    # Checking for even numbers in my_List
    if evens % 2 == 0:
        print(evens)

print("-------------------------------------------------------------------")
for odds in my_List:
    # Checking for odd numbers in my_List
    if odds % 2 != 0:
        print(odds)

print("-------------------------------------------------------------------")
# This will print the sum of all integers in the list
my_ListSum = 0
for nums in my_List:
    my_ListSum = my_ListSum + nums

print(my_ListSum)

print("-------------------------------------------------------------------")
# This is a list of tuples. We can each tuple like this.
tup_List = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
for item in tup_List:
    print(item)

print("-------------------------------------------------------------------")
# We can print/retrieve an object inside the tuples by doing this.
for a, b, c in tup_List:
    print(b)

print("-------------------------------------------------------------------")
# This will only print the keys in the dict
my_dict = {'Key1': 1, 'Key2': 2, "Key3": 3}
for key in my_dict:
    print(key)
print("-------------------------------------------------------------------")
# This will give you each Key Value pair in your dict as a tuple
for t in my_dict.items():
    print(t)
print("-------------------------------------------------------------------")
# This will retrieve each key and each value
for k, v in my_dict.items():
    print(k)
    print(v)
print("-------------------------------------------------------------------")
word = "ABCDEFG"
for index, value in enumerate(word):
    print("The index is", index, "The value is", value)