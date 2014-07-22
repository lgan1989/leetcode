class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        c = int(a , 2) + int(b , 2)
        return "{0:b}".format(c)
        