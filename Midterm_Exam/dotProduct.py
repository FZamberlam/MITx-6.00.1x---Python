# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:46:17 2020

@author: Zamberlam
"""

# Write a Python function that returns the sum of the pairwise products of 
# listA and listB. You should assume that listA and listB have the same length 
# and are two lists of integer numbers. For example, if listA = [1, 2, 3] and 
# listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function 
# should return: 32

# This function takes in two lists of numbers and returns a number.

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    for n in range(len(listA)):
        result += listA[n] * listB[n]
    return result

listaA = [1, 2, 3]
listaB = [4, 5, 6]

print(dotProduct(listaA, listaB))