class Solution:
    # @return an integer
    
    ans = []
    M = 0
    N = 0
    def dp(self,  x , y):
        if x < 0 or y < 0 or x >= self.M or y >= self.N:
            return 0
        if self.ans[x][y] != -1:
            return self.ans[x][y]
        self.ans[x][y] = self.dp(x - 1 , y) + self.dp(x , y - 1)
        return self.ans[x][y]
    def uniquePaths(self, m, n):
        self.M = m
        self.N = n
        self.ans = [[-1 for i in range(n)] for j in range(m)]
        self.ans[0][0] = 1
        return self.dp(m - 1 , n - 1)