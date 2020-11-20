# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:17:55 2020

@author: Zamberlam
"""

# Write a function called longestRun, which takes as a parameter a list of integers 
# named L (assume L is not empty). This function returns the length of the longest 
# run of monotonically increasing numbers occurring in L. A run of monotonically 
# increasing numbers means that a number at position k+1 in the sequence is 
# either greater than or equal to the number at position k in the sequence.

# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should 
# return the value 5 because the longest run of monotonically increasing 
# integers in L is [3, 4, 5, 7, 7].

def longestRun(L):
    
    current_run = []
    longest_run = []
    
    for n in range(len(L)):
        
        if (L[n] >= L[n-1]):
            current_run.append(L[n])
            
        else:
            current_run = [L[n]]
            
        if len(current_run) > len(longest_run):
            longest_run = current_run[:]
            
            
    return len(longest_run)

