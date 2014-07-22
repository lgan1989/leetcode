class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        pos = 0
        for i in A:
            if i == target:
                return pos
            pos += 1
        return -1