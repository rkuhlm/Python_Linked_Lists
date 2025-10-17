# input will get info from keyboard and will store that info as a string.
name = input("Enter your name: ")
age = int(input("Enter your age {0}: ".format(name)))

print(age)
print()

if age >= 18:
    print("You can vote.")
else:
    print("You can not vote. Wait {0} years to vote.".format(18 - age))

    if age < 18:
        print("You are too young")
    elif age == 900:
        print("You are very old")
print()

