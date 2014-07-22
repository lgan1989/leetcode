# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def depth(self , node):
        if node is None:
            return 0
        node.val = max(self.depth(node.left) , self.depth(node.right)) + 1
        return node.val
    def check(self , root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is None and root.right.val > 1:
            return False
        if root.right is None and root.left.val > 1:
            return False
        if self.check(root.left) == False:
            return False
        if self.check(root.right) == False:
            return False
        if root.left is not None and root.right is not None and abs(root.left.val - root.right.val) > 1:
            return False
        return True
    def isBalanced(self, root):
        self.depth(root)
        return self.check(root)
    