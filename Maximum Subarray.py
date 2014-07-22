class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        l = len(A)
        mid = l/2
        if l == 0:
            return 0
        if l == 1:
            return A[0]
        v1 = self.maxSubArray(A[0 : mid : 1])
        v2 = self.maxSubArray(A[mid : l : 1])
        lsum = 0
        lmax = 0
        idx = mid - 1
        while idx >= 0:
            lsum += A[idx]
            lmax = max(lmax , lsum)
            idx = idx - 1
        rsum = A[mid]
        rmax = A[mid]
        idx = mid + 1
        while idx < l:
            rsum += A[idx]
            rmax = max(rmax , rsum)
            idx = idx + 1
        return max( max(v1 , v2) ,  rmax + lmax)
        
            
            