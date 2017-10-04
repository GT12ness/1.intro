# This is a guess the number game.
import random
from builtins import input  # needed for python 2


guesses_taken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

while guesses_taken < 6:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guesses_taken = guesses_taken + 1

    if guess < number:
        print('Your guess is too low.')  # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

    if guess == number:
        guesses_taken = str(guesses_taken)
        print('Good job, ' + name + '! You guessed my number in ' + guesses_taken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number I was thinking of was ' + number)
