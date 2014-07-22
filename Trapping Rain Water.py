class Solution:
    # @param A, a list of integers
    # @return an integer


    def trap(self, A):

        #print A
        l = len(A)
        if l <= 1:
            return 0
        max_h = -1
        sec_h = -1
        p_max = -1
        p_sec = -1
        for i in range(0 , l):
            if A[i] > max_h:
                max_h = A[i]
                p_max = i

        for i in range(0 , l):
            if A[i] <= max_h and i != p_max:
                if A[i] > sec_h:
                    sec_h = A[i]
                    p_sec = i

        s = min(p_sec , p_max)
        e = max(p_sec , p_max)
        #print 'from ' , s , ' to ' , e

        tmp = 0
        if e - s == 1:
            tmp = 0
        else:
            for i in range(s + 1 , e):
                tmp += sec_h - A[i]
        #print max_h , sec_h , tmp
        sl = self.trap(A[:s+1])
        sr = self.trap(A[e:])

        return tmp + sl + sr