# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:55:41 2020

@author: Zamberlam
"""

# Write a Python function that returns a list of keys in aDict with the value 
# target. The list of keys you return should be sorted in increasing order. 
# The keys and values in aDict are both integers. (If aDict does not contain 
# the value target, you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    nlist = []  
    for e in aDict:
        if aDict[e] == target:
            nlist.append(e)
    return sorted(nlist)

Dict = {2:2, 3:3, 4:4, 5:5, 6:5, 7:6, 1:5}

print(keysWithValue(Dict, 5))