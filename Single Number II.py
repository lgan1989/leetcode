class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        threes = ~0
        for a in A:
            z = threes
            threes = (threes & ~a) | (twos & a)
            twos = (twos & ~a) | (ones & a)
            ones = (ones & ~a) | (z & a)
        return ones