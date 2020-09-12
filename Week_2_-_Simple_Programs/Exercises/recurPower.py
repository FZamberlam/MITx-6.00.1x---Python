# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:56:56 2020

@author: Zamberlam
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp <= 0:
        
        return 1
    
    else:
        
        return base * recurPower (base, exp - 1)
    
print(recurPower(5,1))