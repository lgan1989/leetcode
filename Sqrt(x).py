class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        l = 0
        h = x
        last = 0 
        mid = 1
        while abs(mid - last) > 0.000000001:
            last = mid
            s = mid * mid
            if abs(s - x ) < 0.000000001:
                return mid
            elif s > x:
                h = mid
            else:
                l = mid
            mid = (l + h) >> 1
        return mid