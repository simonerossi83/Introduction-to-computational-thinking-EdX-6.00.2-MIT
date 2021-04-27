#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:31:49 2021

@author: simon
"""

import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    threeEquals = 0
    for i in range(numTrials):
        bucket = 3*['red'] + 3*['green']
        for j in range(3):
            result = random.choice(bucket)
            bucket.remove(result)
        if all(x=='red' for x in bucket) or all(x=='green' for x in bucket):
            threeEquals += 1
    return threeEquals/numTrials
            

print(noReplacementSimulation(50000))