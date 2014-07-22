
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers

    def work(self , num):
        if len(num) == 0:
            return []
        if len(num) == 1:
            return [num]
        if len(num) <= 2:
            return [ num , num[::-1] ]
        else:
            rst = self.work(num[1:])
            lst = []
            l = len(num)
            for x in rst:
                for p in range(l):
                    tmp = x[:]
                    tmp.insert(p , num[0])
                    lst.append(tmp)
            return lst
    def permute(self, num):

        ret = self.work(num)
        ret.sort()
  
        return ret