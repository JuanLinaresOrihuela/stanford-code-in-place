import random

# First make the Code choose a random number.
secret_number = random.randint(1,99)
print("I am thinking of a number between 1 and 99... ")

# User enters a guess between 1 and 99.
guess = int(input("Enter a guess: "))

# True if guess is not equal to secret number.
while guess != secret_number:
    # True if guess if less than secret number.
    if guess < secret_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input("Enter a new guess: "))

print("Congrats! The number was: " + str(secret_number))