class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        c = [0 , 0 , 0]
        for x in A:
            c[x] = c[x] + 1
        del A[:]
        for i in range(3):
            for j in range(c[i]):
                A.append(i)