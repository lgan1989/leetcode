# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        n1 = head
        n2 = head
        while True:
            if n1 is None or n2 is None:
                return None
            n1.val = 1
            n1 = n1.next
            n2 = n2.next
            if n2 is not None:
                n2 = n2.next
            if n1 is not None and n2 is not None and n1 == n2:
                while n1.val != -1:
                    n1.val = -1
                    n1 = n1.next
                ret = head
                while ret.val != -1:
                    ret = ret.next
                return ret
        return None