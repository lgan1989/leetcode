# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    
    def sortedArrayToBST(self, num):
        l = len(num)
        if l == 0:
            return None
        node = TreeNode(num[l/2])
        if l == 1:
            return node
        leftNode = self.sortedArrayToBST(num[0:l/2:1])
        rightNode = self.sortedArrayToBST(num[l/2 + 1 : l : 1])
        node.left = leftNode
        node.right = rightNode
        return node
        
        