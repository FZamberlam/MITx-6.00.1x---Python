# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:22:01 2020

@author: Zamberlam
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if b == 0:
        
        return a
    
    else:
        
        print(a)
        print(b)
        print('')
        return gcdRecur(b, a % b)
    

print(gcdRecur(2, 12))
print(gcdRecur(6, 12))
print(gcdRecur(9, 12))
print(gcdRecur(17, 12))