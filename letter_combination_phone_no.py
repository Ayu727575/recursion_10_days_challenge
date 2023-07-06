def combinations(s):
    digit_map = {"2":"abc",
         "3":"def",
          "4":"ghi",
           "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz"}
    res = []
    def solve(i,str):
        if len(str) == len(s):
            res.append(str)
            return
        for c in digit_map[s[i]]:
            solve(i+1,str+c)
    if s:
        solve(0, "")
    return res
s = input("enter string ")
result = combinations(s)
print(result)
