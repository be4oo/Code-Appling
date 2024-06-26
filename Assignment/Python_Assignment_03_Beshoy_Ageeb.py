#!/usr/bin/env python
# coding: utf-8

# ### Python_Assignment_03
# ` By: Beshoy Ageeb `

# Task is to build a game to play with the computer a guessing number game
# 
# Consists of 3 levels
# - In the first level, you have `3` trials to guess the number that the computer randomly has in a range from `1:10`
# - In the second level, you have `7` trials to guess the number that the computer randomly has in a range from `1:100`
# - In the third level, you have `15` trials to guess the number that the computer randomly has in a range from `1:1000`
# 
# 

# In[16]:


# Flags for the game

easy = medium = hard = False

guessedRight = False

# Make the user choose the level

print("Welcome to the Guessing Number Game")
print("Please choose the level you want to play")
print("1. Easy")
print("2. Medium")
print("3. Hard")
print("Please enter the number of the level?")

level = int(input())

if level == 1:
    easy = True
    print("Thank you, you choose number 1 which is the easy level")
elif level == 2:
    medium = True
    print("Thank you, you choose number 2 which is the medium level")
elif level == 3:
    hard = True
    print("Thank you, you choose number 3 which is the hard level")
else:
    print("Invalid level")
    
# Make the computer choose a random number

import random

if easy:
    number = random.randint(1, 10)
    print("Now, I have put my number in my mind, try to put your first guess")
elif medium:
    number = random.randint(1, 100)
    print("Now, I have put my number in my mind, try to put your first guess")
elif hard:
    number = random.randint(1, 1000)
    print("Now, I have put my number in my mind, try to put your first guess")

# print(number)

# Get the user's guessing number

if easy:
    for i in range (1,4):
        guess = int(input())
        print("Your guess is " + str(guess))
        if guess == number:
            print("Congratulation, you have guessed the number right")
            guessedRight = True
            break
        elif guess > number:
            print("Sorry, you have guessed bigger number")
        else:
            print("Sorry, you have guessed smaller number")
elif medium:
    for i in range (1,7):
        guess = int(input())
        print("Your guess is " + str(guess))
        if guess == number:
            print("Congratulation, you have guessed the number right")
            guessedRight = True
            break
        elif guess > number:
            print("Sorry, you have guessed bigger number")
        else:
            print("Sorry, you have guessed smaller number")
elif hard:
    for i in range (1,15):
        guess = int(input())
        print("Your guess is " + str(guess))
        if guess == number:
            print("Congratulation, you have guessed the number right")
            guessedRight = True
            break
        elif guess < number:
            print("Sorry, you have guessed bigger number")
        else:
            print("Sorry, you have guessed smaller number")

# If the user fails to guess it right in his trials tell him your number

if not guessedRight:
    print("Sorry, you have failed to guess the number")
    print("My number was " + str(number))


# In[ ]:




