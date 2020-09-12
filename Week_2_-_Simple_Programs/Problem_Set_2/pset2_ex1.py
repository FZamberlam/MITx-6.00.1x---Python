# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 19:47:45 2020

@author: Zamberlam
"""

"""

Balance = Unpaid + Interest
Minimum = Balance * 0.02
Unpaid = Balance - Minimum
Interest = 0.18/12.0 * Unpaid

Month    Balance    Minimum    Unpaid      Interest
0        5000.00    100        4900        73.50
1        4973.50    99.47      4874.03     73.11
2        4947.14    98.94      4848.20     72.72

"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

month = 1

while month <= 12:
    
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    month += 1
    
print("Remaining balance:", round(balance, 2))