class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        lst = []
        for x in matrix:
            lst += x
        high = len(lst) - 1
        low = 0
        for i in range(30):
            mid = (high + low)/2
            if lst[mid] < target:
                low = mid + 1
            elif lst[mid] > target:
                high = mid - 1
            else:
                return True
        return False