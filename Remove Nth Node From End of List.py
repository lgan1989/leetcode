# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        
        pre_node = ListNode(-1)
        root = pre_node
        cur_node = head
        temp_node = cur_node
        
        pre_node.next = temp_node
        if cur_node is None:
            return None
        c = n
        while True:
            c -= 1
            if c == 0:
                if cur_node is not None and cur_node.next is not None:
                    pre_node = temp_node
                    temp_node = temp_node.next
                    c += 1
                elif cur_node is not None and cur_node.next is None:
                    pre_node.next = temp_node.next
                    break
       
            cur_node = cur_node.next
            
        return root.next
            
                