class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        p = 0
        l = len(A)
        ans = [999999999999999 for i in range(l)]
        ans[0] = 0
        for i in range(1 , l):
            if i - p <= A[p]:
                ans[i] = min(ans[i] , ans[p] + 1)
            else:
                while p < l and i - p > A[p]:
                    p = p + 1
                if p >= l:
                    break
                ans[i] = min(ans[i] , ans[p] + 1)
        return ans[l - 1]