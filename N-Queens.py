class Solution:
    # @return a list of lists of string
    ans = []

    def dfs(self, r , l , v , n , ones , p , size):
        if n == size:
            board = [['.' for i in range(size)] for j in range(size)]
            for i in range(size):
                board[i][p[i]] = 'Q'
            A = []
            for row in board:
                A.append(''.join(row))
            self.ans.append(A)
            return
        aval = ones & (~(r | l | v))
        while aval > 0:
            pos = aval & (-aval)
            aval -= pos
            tmp = pos
            c = 0
            while tmp > 1:
                tmp >>= 1
                c += 1
            p[n] = c
            self.dfs((r+pos)>>1 , (l+pos)<<1 , v + pos , n + 1 , ones , p , size)

    def solveNQueens(self, n):
        self.ans = []
        ones = (1<<n)-1
        self.dfs(0 , 0 , 0 , 0 , ones , [-1 for i in range(n)] , n)
        return self.ans