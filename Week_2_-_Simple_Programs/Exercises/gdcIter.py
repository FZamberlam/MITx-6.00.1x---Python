# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:16:34 2020

@author: Zamberlam
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    lowest = min(a, b)
    greatest = max(a, b)
    
    
    if greatest % lowest == 0:
        
        return lowest
    
    else:
        
        divisor = lowest
        
        while divisor >= 1:
            
            if a % divisor == 0 and b % divisor == 0:
                
                return divisor
            
            else:
                
                divisor -= 1

                
print(gcdIter(2, 12))
print(gcdIter(6, 12))
print(gcdIter(9, 12))
print(gcdIter(17, 12))