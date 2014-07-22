# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        stack = []
        if root is None:
            return res
        stack.append(root)
        while len(stack) > 0:
            tmp = stack[-1]
            if tmp.left is None or tmp.left.val is None:
                res.append(tmp.val)
                tmp.val = None
                stack.pop()
                if tmp.right is not None:
                    stack.append(tmp.right)
            else:
                while tmp.left is not None and tmp.left.val is not None:
                    tmp = tmp.left
                    stack.append(tmp)
        return res