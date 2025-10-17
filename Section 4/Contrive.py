numbers = [1, 45, 32, 12, 60]
# checking to see if one number is divisible by 8.
# If it is then we break the loop and print.
# we can add an else block onto for loops.
for num in numbers:
    if num % 8 == 0:
        print("The numbers are unacceptable.")
        break
else:
    print("All those numbers are fine.")
