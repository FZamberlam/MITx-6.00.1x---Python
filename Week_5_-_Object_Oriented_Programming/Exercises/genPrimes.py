# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:20:48 2020

@author: Zamberlam
"""

def genPrimes():
    
    primes = []
    guess = 2
    
    while True:
        if all(guess % x != 0 for x in primes):
            primes.append(guess)
            yield guess
        guess += 1
            
    