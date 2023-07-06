from os import *
from sys import *
from collections import *
from math import *

from os import *
from sys import *
from collections import *
from math import *


def printPermutations(s):
	# Write your code here.
	def all_permutation(s, ds, ans, freq):
		if len(ds) == len(s):
			ans.append(ds)
			return
		for i in range(len(s)):
			if not freq[i]:
				freq[i] = True
				all_permutation(s, ds+s[i], ans, freq)
				freq[i] = False
	ans = []
	freq = [False for i in range(len(s))]
	all_permutation(s,"",ans,freq)
	return ans

s = input("enter string")
result = printPermutations(s)
print(result)