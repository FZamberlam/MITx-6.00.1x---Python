# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:22:46 2020

@author: Zamberlam
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if aStr == '':
        
        return False
    
    if len(aStr) == 1:
        
        return aStr == char
    
    midpos = len(aStr) // 2
    midchar = aStr[midpos]
    
    if char == midchar:
        
        return True

    elif char < midchar:
            
        return isIn(char, aStr[:midpos])
        
    else:
            
        return isIn(char, aStr[midpos:])