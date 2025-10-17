# Sets (set) = Unordered collection of unique objects EX: {"a", "b"}
mySet = set()
print(mySet)
print("--------------------------------------------------------------")
mySet.add(1)
mySet.add(2)
mySet.add(2)
mySet.add(3)
print(mySet)
# Sets are great for taking lists and casting them as unique sets
myList = [1, 1, 1, 2, 2, 3, 1, 2, 2, 3, 4]
print("--------------------------------------------------------------")
print(myList)
print(set(myList))
unquieList = set(myList)
print(unquieList)
