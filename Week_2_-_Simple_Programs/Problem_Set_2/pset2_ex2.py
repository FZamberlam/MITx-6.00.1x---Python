# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 00:08:03 2020

@author: Zamberlam
"""

balance = 4773
annualInterestRate = 0.2    
    
def lowestPayment(balance, annualInterestRate, minimumMonthlyPayment = 10):
    
    '''
    balance: int or float
    annualInterestRate: float
    minimumMonthlyPayment: int, if not specified, default value is 10
    
    return minimumMonthlyPayment to pay off debt in a year
    '''
    
    temp = balance
    month = 1
    
    monthlyInterestRate = annualInterestRate / 12.0
    
    while month <= 12:
        
        balance = round(balance, 2)
        
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        
        month += 1
        
    if monthlyUnpaidBalance <= 0:
        
        return minimumMonthlyPayment
    
    else:
        
        balance = temp
        return lowestPayment(balance, annualInterestRate, minimumMonthlyPayment + 10)
      
print(lowestPayment(balance, annualInterestRate))
    
    