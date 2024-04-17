# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:44:53 2019

@author: azeng

Class: PGRM1000

Title: Assignment 8 - Making Decisions 
"""
import random

rand1 = random.randint(1,6)
rand2 = random.randint(1,6)
i = 1
Total = rand1 + rand2
print(Total)
UserGuess = input("We have rolled 2 dice. \nPlease guess the sum of the 2 dice: ")
guess = int(UserGuess)

while(i < 4):
    if((guess <= 1)or(guess >= 13)):
        print("Invalid guess!")
        break
    elif((guess < Total) and (guess >= 2)):
        print("\nYour guess is too low. Try again.")
        UserGuess = input("Please guess the sum of the 2 dice: ")
        guess = int(UserGuess)
        i += 1
    elif((guess > Total) and (guess <= 12)):
        print("\nYour guess is too high. Try again.")
        UserGuess = input("Please guess the sum of the 2 dice: ")
        guess = int(UserGuess)
        i += 1
    elif(guess == Total):
        print("Correct!")
        break

if(i > 4):
    print("Out of guesses.")
    