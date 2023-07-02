def kthChildNthGeneration(n, k):
    # Write your code here
    def solve(k):
        if k==1:
            return 1
        if k%2==0:
            return 1 - solve((k+1)//2)
        else:
            return solve((k+1)//2)
    if solve(k):
        return "Male"
    else:
        return "Female"