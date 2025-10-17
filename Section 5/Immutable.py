result = True
another_result = result
print(id(result))
print(id(another_result))
print(id(True))

result = False
print(id(result))