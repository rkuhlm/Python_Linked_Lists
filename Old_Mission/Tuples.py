# Tuples (tup) = Ordered immutable (not changeable) sequence of objects EX: (10, "hello", 200.3)
# Very simple to lists except tuples can not be changed
t = (1, 2, 3)
print(t)
print(type(t))
print("-------------------------------------------------------------------")
my_List = [1, 2, 3]
print(my_List)
print(type(my_List))
print("-------------------------------------------------------------------")
my_tuple = ('a', 'a', 'b', 'c', 'd', 'd')
print(my_tuple)
print(my_tuple.count('a'))  # returns total number of occurrences of a
print(my_tuple.index('c'))  # returns index location
