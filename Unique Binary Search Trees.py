class Solution:
    # @return an integer
    def numTrees(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        ret = 0
    
        for i in range(n):
            ret = ret + self.numTrees(i) * self.numTrees(n-1-i)
        return ret
        