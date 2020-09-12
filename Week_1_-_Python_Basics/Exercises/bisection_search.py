# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 06:23:30 2020

@author: Zamberlam
"""
print('Please think of a number between 0 and 100!')
  
low = 0
high = 100
guess = False

while not guess:
    
    ans = (high + low) // 2
    
    print('\nIs your secret number ' + str(ans) + '?')
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if user_input == 'c':
        
        guess = True
        
    elif user_input == 'l':
        
        low = ans
        
    elif user_input == 'h':
        
        high = ans
        
    else:
        
        print('Sorry, I did not understand your input.')


print('\nGame Over. Your secret number was: ' + str(ans))
    
