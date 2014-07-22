# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        n1 = head
        n2 = head
        if head is None:
            return False    
        while True:
            n1 = n1.next
            n2 = n2.next

            if n1 is None or n2 is None:
                return False
            n2 = n2.next
            if n2 is None:
                return False
            if n1 == n2:
                return True
        