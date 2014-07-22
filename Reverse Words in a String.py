class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        wordList = s.split(" ")
        newWordList = []
        for word in wordList:
            if (word.strip() != "" and word.strip() != " "):
                newWordList.append(word)
        if (s != ""):
            newWordList.reverse()
            return ' '.join(newWordList)
        else:
            return s