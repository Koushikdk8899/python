# Problem 2: Number Guessing Game
# Write a Python program that generates a random number between 1 and 100.
# The user should repeatedly guess the number until the correct number is found.
#
# Requirements:
# 1. Use the random module.
# 2. Tell the user whether the guess is too high or too low.
# 3. Count and display the number of attempts.

import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        print("Number of attempts:", attempts)
        break
