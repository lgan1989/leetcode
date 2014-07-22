# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    
    def valid(self, root , min_val , max_val):
        if root is None:
            return True

        b = root.val < min_val and root.val > max_val
        b = b and self.valid(root.left , min(min_val , root.val) , max_val)
        b = b and self.valid(root.right , min_val , max(max_val , root.val))
        return b
        
    def isValidBST(self, root):

        return self.valid(root , 9223372036854775807 , -9223372036854775807)
        
