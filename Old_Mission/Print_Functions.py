print("Hello Worlds")
print("---------------------------")
print("Hello \nWorlds")
print("---------------------------")
print(len("Hello Worlds"))
print("---------------------------")

mystring = "Hello World"

# indexing
print(mystring[0])
print(mystring[1])
print(mystring[2])
print(mystring[3])
print(mystring[4])
print(mystring[5])
print(mystring[6])
print(mystring[7])
print(mystring[8])
print(mystring[9])
print(mystring[10])
print("---------------------------")
print(mystring[:3])  # print from index 0 up to and NOT including 3
print("---------------------------")
print(mystring[3:])  # print from index 3 INCLUDING 3 to the end of the string
print("---------------------------")
print(mystring[::2])  # print every value in 2 step increments
print("---------------------------")
print(mystring[::-1])  # clever way to reverse a string

# Strings are immutable. They can not be changed with indexing.

print("---------------------------")
print(mystring.upper())