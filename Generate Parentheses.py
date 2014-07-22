class Solution:
    # @param an integer
    # @return a list of string
    ret = []
    def work(self , n , l , s):
        if len(s) == 2 * n:
            if l == 0:
                self.ret.append(s)
            return
        if l > 0:
            if l + 1 <= n:
                self.work(n , l + 1 , s + "(")
            self.work(n , l - 1 , s + ")")
        else:
            self.work(n , l + 1 , s + "(")
        
    def generateParenthesis(self, n):
        del self.ret[:]
        if n == 0:
            return []
        if n == 1:
            return ["()"]
        self.work(n , 0 , "")
        return self.ret