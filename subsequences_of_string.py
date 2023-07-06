from os import *
from sys import *
from collections import *
from math import *

def subsequences(str):

    # Write your code here
    def subseq(ind, strr, res, n):
        if ind>=n:
            if len(strr)>0:
                res.append(strr)
            return
        subseq(ind+1, strr+str[ind], res, n)
        subseq(ind+1, strr, res, n)
    res = []
    subseq(0, "", res, len(str))
    return res