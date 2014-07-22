# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    
    def toList(self, root):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return root
        if root.left is None:
            return self.toList(root.right)
        if root.right is None:
            root.right = root.left
            root.left = None
            return self.toList(root.right)
        tmp = root.right
        lastNode = self.toList(root.left)
        root.right = root.left
        root.left = None
        lastNode.right = tmp
        return self.toList(tmp)
        
    def flatten(self, root):
        self.toList(root)
        