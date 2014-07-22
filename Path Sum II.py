# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    ans = []
    def work(self, node , sum , A):
        if node is None:
            return
        B = A[:]
        B.append(node.val)
        if node.left is None and node.right is None:
            if sum == 0:
                self.ans.append(B)
            return
        if node.left is not None:
            self.work(node.left , sum - node.left.val , B)
        if node.right is not None:
            self.work(node.right , sum - node.right.val , B)
    def pathSum(self, root, sum):
        self.ans = []
        if root is None:
            return []
        self.work(root , sum - root.val , [])
        return self.ans
        