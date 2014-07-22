class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        r = len(obstacleGrid)
        if r == 0:
            return 0
        c = len(obstacleGrid[0])
        
        ans = [ [0 for i in range(c)] for j in range(r)]
        
        ans[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(0 , r):
            for j in range(0 , c):
                ni = i + 1
                nj = j
                if ni >= 0 and ni < r and nj >= 0 and nj < c and obstacleGrid[ni][nj] != 1:
                    ans[ni][nj] += ans[i][j]
                ni = i
                nj = j + 1
                if ni >= 0 and ni < r and nj >= 0 and nj < c and obstacleGrid[ni][nj] != 1:
                    ans[ni][nj] += ans[i][j]
                
        return ans[r - 1][c - 1]