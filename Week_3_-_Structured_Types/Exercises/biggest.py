# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:29:31 2020

@author: Zamberlam
"""

animals = {'a': ['aardvark'], 
           'b': ['baboon'], 
           'c': ['coati'], 
           'd': ['donkey', 'dog', 'dingo']}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result 

    