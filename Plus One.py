class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        digits = digits[::-1]
        i = 0
        l = len(digits)
        while i < l and digits[i] + 1 > 9:
            digits[i] = 0
            i = i + 1
        if i == l:
            digits.append(1)
        else:
            digits[i] = digits[i] + 1
        return digits[::-1]