name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 18 < age < 31:
    print("Okay, {} you can go to the Holiday." .format(name))
else:
    print("You are not old enough.")
