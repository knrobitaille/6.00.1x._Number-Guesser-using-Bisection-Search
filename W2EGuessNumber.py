# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:04:20 2019

@author: u733870
"""


print("Please think of a number between 0 and 100!")
low = 0
high = 100
ans = (high + low) / 2
response = ""
guessed = False

while not guessed:
    print("Is your secret number " + str(int(ans)) + "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'h':
        high = ans
    elif response == 'l':
        low = ans
    elif response == 'c':
        print("Game over. Your secret number was: " + str(int(ans)))
        guessed == True
        break
    else:
         print("Sorry, I did not understand your input.")
         print("Is your secret number " + str(int(ans)) + "?")
         response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")     
         if response == 'c':
             print("Game over. Your secret number was: " + str(int(ans)))
             guessed == True
             break
    ans = int(float((high + low) / 2))
    
#doesnt work when "correct" is typed