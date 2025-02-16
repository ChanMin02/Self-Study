import random

"""

Write a program that
 Saves a secret number in a variable.
 Asks the user for a number guess.
 Prints a bool False or True depending on whether the guess
matches the secret.

"""

secret_number = int(random.randrange(1,10000))

guess = int(input("Guess a number: "))


print(secret_number,guess)
print(secret_number == guess)