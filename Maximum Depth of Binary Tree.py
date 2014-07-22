# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        l1 = self.maxDepth(root.left)
        l2 = self.maxDepth(root.right)
        return max(l1 + 1 , l2 + 1)
        