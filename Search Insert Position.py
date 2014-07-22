class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        low = 0
        high = len(A) - 1
        mid = 0
        while low < high:
            mid = (low + high) / 2
            if A[mid] < target:
                low = mid  + 1
            elif A[mid] > target:
                high = mid
            else :
                return mid
        if A[high] < target:
            high = high + 1
        return high
        