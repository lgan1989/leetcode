class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer

    
    ans = []
    
    def makeSubset(self , subset , p, l , S):
        for i in range(p + 1 , l):
            if i == p + 1 or S[i] != S[i - 1]:
                s = subset[:]
                s.append(S[i])
                self.ans.append(s)
                self.makeSubset(s , i , l , S)
        return
    
    def subsetsWithDup(self, S):
        S.sort()
        l = len(S)
        self.ans = [[]]
        for i in range(0 , l):
            if i == 0 or S[i] != S[i - 1]:
                self.ans.append([S[i]])
                self.makeSubset([S[i]] , i  , l , S)
        return self.ans