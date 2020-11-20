# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 16:40:42 2020

@author: Zamberlam
"""

def sum_digits(s):
    """
    assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception. 
    """
    
    numbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    total = 0
    
    if s.isalpha() == True:
        raise ValueError
    else:  
        for letter in s:
            if letter in numbers:
                total += numbers[letter]

    return total
