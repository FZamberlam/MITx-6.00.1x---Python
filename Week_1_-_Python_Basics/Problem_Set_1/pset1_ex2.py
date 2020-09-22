# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 05:40:33 2020

@author: Zamberlam
"""

# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2

s = 'azcbobobegghakl'
occurrences = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        occurrences += 1
        
print("Number of times 'bob' occurs is:", occurrences)