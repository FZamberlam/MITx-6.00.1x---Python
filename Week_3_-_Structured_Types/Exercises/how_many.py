# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:42:07 2020

@author: Zamberlam
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    
    count = 0
    
    for i in aDict.values():
        
        count += len(i)
        
    return count
    
    
print(how_many(animals))