# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:17:51 2020

@author: Zamberlam
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    import string
    
    if len(word) == 1:
        return 0
    else:
        alphabet = list(string.ascii_lowercase)
        alphabet_values = []
        scores = []        
        for letter in word:            
            pos = (alphabet.index(letter.lower()) + 1)
            alphabet_values.append(pos)            
        for i in range(len(alphabet_values)):          
            scores.append(i * alphabet_values[i])
            
        highestScore = max(scores)
        scores.remove(highestScore)
        secondHighestScore = max(scores)
        
        return f(highestScore, secondHighestScore)

def f(x, y):
    return x + y

word = 'abacaxi'
print(score(word, f))