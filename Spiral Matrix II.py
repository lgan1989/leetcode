class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        ret = [[0 for i in range(n)] for j in range(n)]
       
        c = 0
        val = 1
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        pi = 0
        pj = 0
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        ret[0][0] = 1
        for i in range(n * n - 1):
            ni = pi + dir[c][0]
            nj = pj + dir[c][1]
            if ni < 0 or nj < 0 or ni >= n or nj >= n or ret[ni][nj] != 0:
                c = (c + 1) % 4
                ni = pi + dir[c][0]
                nj = pj + dir[c][1]
            pi = ni
            pj = nj
            val = val + 1
            ret[pi][pj] = val
        return ret
        