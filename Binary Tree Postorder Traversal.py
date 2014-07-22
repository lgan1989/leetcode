# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    ans = []
    def travel(self , node):
        if node is None:
            return
        self.travel(node.left)
        self.travel(node.right)
        self.ans.append(node.val)
    def postorderTraversal(self, root):
        del self.ans[:]
        self.travel(root)
        return self.ans