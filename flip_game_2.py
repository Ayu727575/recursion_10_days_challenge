import re
from os import *
from sys import *
from collections import *
from math import *

def canNinjaWin(str):
    # Write your code here.
    i, n = 0, len(str) - 1
    is_win = False
    while not is_win and i < n:                                     
        if str[i] == '$':
            while not is_win and i < n and str[i+1] == '$':         
                is_win = not canNinjaWin(str[:i] + '**' + str[i+2:]) 
                i += 1
        i += 1
    return is_win