class Solution:
    # @param grid, a list of lists of integers
    # @return an integer

        
    def minPathSum(self, grid):
        M = len(grid)
        N = len(grid[0])
        ans = [[1000000000 for i in range(N + 1)] for j in range(M + 1)]
        ans[0][0] = grid[0][0]
        for i in range(M):
            for j in range(N):
                if i + 1 < M:
                    ans[i + 1][j] = min(ans[i + 1][j] , ans[i][j] + grid[i + 1][j])
                if j + 1 < N:
                    ans[i][j + 1] = min(ans[i][j + 1] , ans[i][j] + grid[i][j + 1])
        return ans[M-1][N-1]