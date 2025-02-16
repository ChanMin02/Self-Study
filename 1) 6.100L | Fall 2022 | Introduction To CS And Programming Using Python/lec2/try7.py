"""

 Write a program that
 Saves a secret number.
 Asks the user for a number guess.
 Prints whether the guess is too low, too high, or the same as the secret.

"""

secret_number = int(input(('Enter a secret number: ')))

guess = int(input('Guess the secret number: '))

if guess < secret_number:
    print('Too low!')
elif guess > secret_number:
    print('Too high!')
else:
    print('Congratulations! You guessed it!')