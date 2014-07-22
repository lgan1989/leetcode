class Solution:
    # @return a list of integers
    n_len = 0
    h = {}
    ret = []
    def work(self , val):
        for i in range(0 , self.n_len):
            next = (1<<i) ^ val
            if next not in self.h:
                self.h[next] = 1
                self.ret.append(next)
                self.work(next)
    def grayCode(self, n):
        self.n_len = n
        self.h = {}
        self.h[0] = 1
        self.ret = [0]
        self.work(0)
        return self.ret