# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 05:31:19 2020

@author: Zamberlam
"""

# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
# if s = 'azcbobobegghakl', your program should print:
    
# Number of vowels: 5

s = 'azcbobobegghakl'

nVowels = 0
vowels = "AaEeIiOoUu"

for letter in s:
    if letter in vowels:
        nVowels += 1

print("Number of vowels:", nVowels)
        