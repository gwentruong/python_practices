#!/bin/env/python3

import random

count = 7
secret_number = random.randint(1, 100)

print("Welcome to GUESS A NUMBER!")
print("The computer just generated a secret number between 1 and 100, you have 7 turns to guess the secret number")

while count > 0:
    try:
        print("What is the secret number?")
        guessed_number = int(input())
    except ValueError:
        print("Invalid input. Please input an integer.")
        continue
    else:
        if guessed_number == secret_number:
            break;
        elif guessed_number<1 or guessed_number>100:
            print("Your guess is out of range. Try to guess from 1 to 100.")
        elif guessed_number < secret_number:
            print("Your guess is too low.")
        elif guessed_number > secret_number:
            print("Your guess is too high.")

    if (count-1) > 1:
        print("Try again. You have {} guesses left.".format(count-1))
    elif (count-1) == 1:
        print("You only have 1 guess left! Choose correctly!")

   # count -= 1
   count = count - 1

if count == 0:
    print("You ran out of turns. Try again next time!")
else:
    print("You guess is correct!")

print("The secret number is {}.".format(secret_number)) 

