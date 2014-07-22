# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    lst = []
    def work(self , node , lvl):
        if node is None:
            return
        if lvl >= len(self.lst):
            self.lst.append([])
        self.lst[lvl].append(node.val)
        self.work(node.left , lvl + 1)
        self.work(node.right , lvl + 1)
    def levelOrderBottom(self, root):
        del self.lst[:]
        if root is None:
            return []
        self.work(root , 0)
        return self.lst[::-1]