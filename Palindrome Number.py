class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        tmp = x
        k = 1
        while tmp / 10 > 0:
            k *= 10
            tmp = int(tmp/10)
        while x > 0 and k > 0:
            a = x % 10
            b = int(x / k)
            if a != b:
                return False
            x = x - b * k
            x = int(x / 10)
            k = int(k / 100)

        return True
