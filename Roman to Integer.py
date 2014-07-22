class Solution:
    # @return an integer
    def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        roman_ixc = {'I':5, 'X':50, 'C':500}
        ret = 0
        for i in s[::-1]:
            if i in roman_ixc and ret >= roman_ixc[i]:
                ret -= roman_dict[i]
            else:
                ret += roman_dict[i]
        return ret