# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 08:14:45 2021

@author: simone.rossi
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    
    lengths = [len(word) for word in L]
    mean = sum(lengths)/len(lengths)
    
    somma = 0
    
    for x in lengths:
        somma += (x - mean)**2
    dev = (somma / len(lengths))**.5
    
    return dev
    

L = ['k', 'l', 'h', 'g']
print(stdDevOfLengths(L))