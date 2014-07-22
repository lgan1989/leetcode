class Solution:
    # @return an integer
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        s = str(x)
        ret = int(s[::-1]) * flag
        return ret