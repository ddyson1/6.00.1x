#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:20:24 2017

@author: devinjamesdyson
"""

s = 'azcbobobegghakl'
count = 0

for n in range(len(s) - 2):
    if s[n] == 'b' and s[n + 1] == 'o' and s[n + 2] == 'b':
        count += 1
        
print('Number of times bob occurs is:',count)