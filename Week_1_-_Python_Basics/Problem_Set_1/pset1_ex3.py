# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 01:15:53 2020

@author: Zamberlam
"""

# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters 
# occur in alphabetical order. For example, if s = 'azcbobobegghakl', then 
# your program should print

# Longest substring in alphabetical order is: beggh

s = 'azcbobobegghakl'

current = ''
longest = ''

for i in range(len(s)):
    
    if (s[i] >= s[i-1]):
            
        current += s[i]
 
    else:
  
        current = s[i]
 
    if len(current) > len(longest):
        
        longest = current
        
print("Longest substring in alphabetical order is: " + longest)

