class Solution:
    # @return a string

    ans = 0
    ans_str = ""
    class Trie:
        next = None
        val = None
        cnt = 0
        def __init__(self , c):
            self.val = c
            self.next = [None for i in range(0,26)]
            self.cnt = 0

    def build(self , node , s):
        if node.val != '$':
            node.cnt += 1
        if len(s) == 0:
            return

        c = s[0]
        idx = int(ord(c) - ord('a'))
        if node.next[idx] is None:
            node.next[idx] = self.Trie(c)
            node.next[idx].val = str(node.val) + c
        self.build(node.next[idx] , s[1:])

    def get(self , node , t):
        #print node.val , node.cnt
        if node.cnt == t:

            if (node.val != '$'):
                if self.ans < len(node.val):
                    self.ans = len(node.val)
                    self.ans_str = node.val


        for i in range(0,26):
            if node.next[i] is not None:
                self.get(node.next[i] , t)

    def longestCommonPrefix(self, strs):
        root = self.Trie('$')
        l = len(strs)
        for s in strs:
            self.build(root , s)
        self.ans = 0
        self.ans_str = ""
        self.get(root , l)

        return self.ans_str[1:]