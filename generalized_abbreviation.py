from os import *
from sys import *
from collections import *
from math import *

def findAbbr(strr):
    # Write your code here.
    res = []
    def solve(ans, count, pos):
        if pos == len(strr):
            if count == 0:
                res.append(ans)
            else:
                res.append(ans+str(count))
            return
        if count>0:
            solve(ans+str(count)+strr[pos],0,pos+1)
        else:
            solve(ans+strr[pos],0,pos+1)
        solve(ans, count+1,pos+1)
    solve("",0,0)
    res.sort()
    return res