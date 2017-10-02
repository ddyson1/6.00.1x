#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:40:08 2017

@author: devinjamesdyson
"""

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
