# Lists (list) = Ordered sequence of objects EX: [10, "hello", 20.3]
# List are mutable, so we can change them
my_List = ['one', 'two', 'three', 'four', 'five']
print(my_List[1])
print(my_List[1:])
print("-------------------------------------------------------------------")
my_List[0] = 1
print(my_List)
print("-------------------------------------------------------------------")
num_List = [3, 4, 8, 2, 56, 12, 5]
print(num_List)
num_List.sort()
print(num_List)
print("-------------------------------------------------------------------")
print(num_List)
num_List.reverse()
print(num_List)
num_List.append([6, 7])
print(num_List)
