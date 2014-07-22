class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float

    def do(self , x , n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n % 2 == 0:
            res = self.do(x , n/2)
            res = res * res
        else:
            res = self.do(x , n/2) 
            res = res * res * x
        return res

    def pow(self, x, n):

        res = self.do(x , abs(n))
        if n < 0:
            res = 1.0/res
        return res