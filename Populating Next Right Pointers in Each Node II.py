# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    
    def lvl_connect(self , root):
        if root is None:
            return
        node = root.right if root.right is not None else root.left
        if root.left is not None and root.right is not None:
            root.left.next = root.right    
         
        if node is not None and root.next is not None:
            tmp = root.next
            next_node = None
            while tmp is not None:
                next_node = tmp.left if tmp.left is not None else tmp.right
                if next_node is not None:
                    break
                tmp = tmp.next
            node.next = next_node    
    def work(self, root):
        if root is None:
            return
        self.lvl_connect(root)
        node = root.next
        if node is not None:
            while node is not None:
                self.lvl_connect(node)
                node = node.next
        node = root
        first = node.left
        while node is not None:
            first = node.left if node.left is not None else node.right
            if first is None:
                node = node.next
            else:
                break
        self.work(first)

    def connect(self, root):
        if root is None:
            return
        self.work(root)

        
     
     