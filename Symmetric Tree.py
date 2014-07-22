# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSame(self, r1 , r2):
        if r1 is None and r2 is None:
            return True
        if r1 is None and r2 is not None:
            return False
        if r2 is None and r1 is not None:
            return False
        if r1.val != r2.val:
            return False
        return self.isSame(r1.left , r2.left) and self.isSame(r1.right , r2.right)
    def reverseNode(self , root):
        if root is None:
            return
        self.reverseNode(root.left)
        self.reverseNode(root.right)
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return
        
    def isSymmetric(self, root):
        if root is None:
            return True
        self.reverseNode(root.left)
        return self.isSame(root.left , root.right)
        