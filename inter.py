# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:32:43 2023

@author: Regi
"""

from pylab import*

def interest(P,i,n):
    return int(P*i*n/100)

Principal =int(input("Enter principal: ",))
rate = int(input("Enter interest: ",))
Period = int(input("Enter period: ",))

amount = Principal + interest(Principal,rate,Period)

print("The amount accrued= R", amount)
