class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        l = 0
        h = len(A) - 1
        ans = [-1 , -1]
        while l <= h:
            mid = (l + h) >> 1
            if A[mid] < target:
                l = mid + 1
            elif A[mid] > target:
                h = mid - 1
            else:
                ans[0] = mid
                h = mid - 1
        l = 0
        h = len(A) - 1
        while l <= h:
            mid = (l + h) >> 1
            if A[mid] < target:
                l = mid + 1
            elif A[mid] > target:
                h = mid - 1
            else:
                ans[1] = mid
                l = mid + 1
        return ans