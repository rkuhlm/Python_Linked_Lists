shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
print(shopping_list)
print()

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print()
print(shopping_list)
print(id(shopping_list))
print()

a = b = c = d = e = f = another_list
print(a)
print()
print("adding cream to list....")
b.append("cream")
print(b)
print(c)