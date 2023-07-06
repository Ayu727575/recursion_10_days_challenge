from os import *
from sys import *
from collections import *
from math import *

def backtrack(start, target, factors, combinations, n):
    
    if target == 1:
        
        if len(factors) > 1 or factors[0] != n:
            combinations.append(list(factors))
        return
 
    for i in range(start, target + 1):
        if target % i == 0:
            factors.append(i)  
            backtrack(i, target // i, factors, combinations, n)
            factors.pop() 
def factorCombinations(n):
    # Write your code here.
    combinations = []
    factors = []
    backtrack(2, n, factors, combinations, n)
    return combinations
