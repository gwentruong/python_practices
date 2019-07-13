#!/bin/env/python3

a = 0
b = 100

print("Hello, do you belive that a computer can read your mind?")
print("Think of a integer between 0 and 100, remember it.\n \
        I'll figure out the number you are thinking about in 7 turns.")
print("Please answer question with (Y)es or (N)o.")

yeses = ["Y", "Yes", "YES", "y", "yes"]
noes  = ["N", "No", "NO", "n", "no"]
i = 0

while i < 6:
    m = a + int((b-a) / 2)
    
    print("Is it larger than %i ?" % m)
    response = input()

    if (response not in yeses) and (response not in noes):
        print("Invalid response. Please answer (Y)es or (N)o")
        continue
 
    if response in yeses:
        a = m + 1
        b = b
    elif response in noes:
        a = a
        b = m
    i += 1

print("Is it larger than %i ?" % a)
response = input()

while True:
    if response in yeses:
        result = b
        break
    elif response in noes:
        result = a
        break
    else:
        print("Invalid response. Please answer (Y)es or (N)o")
        continue

print("You are thinking about number %i." % result)
