def validParenthesis(n: int) -> int:
    # Write your code here.
    stack = []
    res = []
    def back_track(i,j):
        if i==j==n:
            res.append("".join(stack))
            return
        if i<n:
            stack.append("(")
            back_track(i+1,j)
            stack.pop()
        if j<i:
            stack.append(")")
            back_track(i,j+1)
            stack.pop()
    back_track(0,0)
    return res