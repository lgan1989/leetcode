class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.strip()
        wordList = s.split(' ')
        if len(wordList) > 0:
            return len(wordList[-1])