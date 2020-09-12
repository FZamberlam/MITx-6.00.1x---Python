# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:33:58 2020

@author: Zamberlam
"""

balance = 999999
annualInterestRate = 0.18

def bisectionPaymentSearch(balance, annualInterestRate, lower = 0, upper = 0):
    
    initialBalance = balance
    monthlyInterestRate = annualInterestRate / 12
    epsilon = 0.03
    
    if lower == 0:
        lower = initialBalance / 12
    
    if upper == 0:
        upper = (initialBalance * (1 + monthlyInterestRate) ** 12) / 12.0
        
    while abs(balance) > epsilon:
        monthlyPayment = (upper + lower) / 2
        balance = initialBalance
        
        for i in range(12):
            
            monthlyUnpaidBalance = balance - monthlyPayment
            balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
            
        if balance > epsilon:
            
            lower = monthlyPayment
        
        elif balance < -epsilon:
            
            upper = monthlyPayment
        
        else:
            
            return monthlyPayment
        
print(round(bisectionPaymentSearch(balance, annualInterestRate), 2))