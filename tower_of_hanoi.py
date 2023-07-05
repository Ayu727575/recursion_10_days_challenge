def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    def solve_toh(n,source,auxilary,destination,ans):
        if n==0:
            return
        solve_toh(n-1, source, destination,auxilary, ans)
        ans.append([source, destination])
        solve_toh(n-1, auxilary, source, destination, ans)
    ans = []
    solve_toh(n, 1, 2, 3, ans)
    return ans