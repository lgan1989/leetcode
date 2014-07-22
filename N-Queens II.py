class Solution:
    # @return an integer
    ans = 0

    def dfs(self,  r , l , v , n , ones):
        if n == 0:
            self.ans += 1
            return

        aval = ones & (~(r | l | v))
        while aval > 0:
            pos = aval & (-aval)
            aval -= pos
            self.dfs((r+pos)>>1 , (l+pos)<<1 , v+pos, n-1 , ones)

    def totalNQueens(self, n):
        self.ans = 0
        ones = (1<<n)-1
        self.dfs(0 , 0 , 0 , n , ones)
        return self.ans