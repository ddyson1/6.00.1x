#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 19:33:25 2017

@author: devinjamesdyson
"""

#In this problem, you'll create a program that guesses a secret number!

#The program works as follows: you (the user) thinks of an integer between 
#0 (inclusive) and 100 (not inclusive). The computer makes guesses, 
#and you give it input - is its guess too high or too low? 
#Using bisection search, the computer will guess the user's secret number!
 
#Please think of a number between 0 and 100!
#Is your secret number 50?
#Enter 'h' to indicate the guess is too high. 
#Enter 'l' to indicate the guess is too low.
#Enter 'c' to indicate I guessed correctly. 

x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x

ans = (high + low)/2.0

while abs (ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square toot of ' + str(x))
