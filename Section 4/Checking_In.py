parrot = "Norwegian Blue"

letter = input("Enter a letter: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont need that letter.")

activity = input("What do you wanna do today? ")

# casefold allows for the use of capitalized and not capitalized letters to be matched together

if "cinema" not in activity.casefold():
    print("But I want to go to Cinema.")
