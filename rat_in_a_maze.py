def isSafe( maze, x, y, N ):
     
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
        return True
    return False

def solveMazeUtil(maze, x, y, sol, N):
     
    if x == N - 1 and y == N - 1:
        sol[x][y] = 1
        return True
         
    if isSafe(maze, x, y, N) == True:
        sol[x][y] = 1
         
        if solveMazeUtil(maze, x + 1, y, sol, N) == True:
            return True
             
        
        if solveMazeUtil(maze, x, y + 1, sol, N) == True:
            return True
         
        sol[x][y] = 0
        return False

def ratInAMaze( maze, n ):
     
    sol = [ [ 0 for j in range(n) ] for i in range(n) ]
     
    solveMazeUtil(maze, 0, 0, sol, n)
    return sol

n = int(input())
maze = n*[0]

for i in range(0 , n):
    maze[i]=input().split()
    maze[i]=[int(j) for j in maze[i]]
    
print(ratInAMaze(maze , n)) 
        