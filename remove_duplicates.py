def removeDuplicate(n, s):
	
	def solve(i,res):
		if i==n-1:
			res+=s[i]
			return res
		if s[i] != s[i+1]:
			res+=s[i]
			return solve(i+1,res)
		if s[i] == s[i+1]:
			return solve(i+1,res)
	res = ""
	return solve(0,res)