# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    ans = []
    def work(self , lvl , node):
        if node is None:
            return
        if lvl >= len(self.ans):
            self.ans.append([])
        self.ans[lvl].append(node.val)
        self.work(lvl + 1 , node.left)
        self.work(lvl + 1 , node.right)
    def levelOrder(self, root):
        del self.ans[:]
        self.work(0 , root)
        return self.ans