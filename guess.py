# This is a 'guess the number' game.

import random


# Use a breakpoint in the code line below to debug your script.

def isdigit(str):
    return str.isdigit()


guessesTaken = 0

print('what is your name?')
myName = input()

number = random.randint(1, 20)
print('well,' + myName + ' I am thinking about a number between 1 and 20.')

guessesTaken = 0

while True:
    if guessesTaken > 5:
        break

    print('take a guess.')
    guess = input()

    if not isdigit(guess):
        guessesTaken = (guessesTaken - 1)
        print('You have to put a number.')
        continue
    guessesTaken = guessesTaken + 1
    guess = int(guess)

    if guess < number:
        print('your guess is too low.')

    if guess > number:
        print('your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('congratuations, ' + myName + '! You guessed my number in ' + guessesTaken + 'th try!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking was ' + number + '.')
