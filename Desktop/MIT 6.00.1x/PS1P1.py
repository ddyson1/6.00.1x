#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:53:35 2017

@author: devinjamesdyson
"""

#Week 1: Python Basics Problem Set 1 > Problem 1

s = 'azcbobobegghakl'
ans = 0

for n in s:
    if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
        ans += 1
print('Number of vowels:',ans)
    
    