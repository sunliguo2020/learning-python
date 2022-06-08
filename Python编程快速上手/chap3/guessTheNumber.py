# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2020/11/29 13:12
"""
# This is a guess the number game.
import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('You guess is too low')
    elif guess > secretNumber:
        print('You guess is too high')
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! you guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thing of was ' + str(secretNumber))
