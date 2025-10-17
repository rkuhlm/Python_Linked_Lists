import random
answer = random.randint(1, 10) # 1 to 10 including 10


print("Guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You guessed the number on the first try.")
else:
    while guess != answer:
        if guess < answer:
            print("Guess a higher number.")
            guess = int(input())
        elif guess > answer:
            print("Guess a lower number.")
            guess = int(input())

    print("You guessed the correct number.")
