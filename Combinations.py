class Solution:
    # @return a list of lists of integers

    ret = []

    def gk(self, x , k , n , combo):

        if k == 0:
            self.ret.append(combo)
            return
        for i in range(x + 1 , n + 1):
            temp = combo[:]
            temp.append(i)
            self.gk(i , k - 1 , n , temp)

    def combine(self, n, k):
        self.ret = []
        for i in range(1 , n + 1):
            self.gk(i , k - 1 , n , [i])

        return self.ret
