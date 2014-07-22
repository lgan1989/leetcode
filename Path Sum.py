# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        b1 = False
        b2 = False
        if root.left is not None:
            b1 = self.hasPathSum(root.left , sum - root.val)
        if root.right is not None:
            b2 = self.hasPathSum(root.right , sum - root.val)
        if b1 == True or b2 == True:
            return True
        if root.left is None and root.right is None:
            return root.val == sum
        return False