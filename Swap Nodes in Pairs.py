# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        ret = None
        pre = None
        if head is None:
            return
        if head.next is None:
            return head
        while head.next is not None:
            if pre is not None:
                pre.next = head.next
            else:
                ret = head.next
            tmp = head.next.next
            head.next.next = head
            head.next = tmp
            pre = head
            head = tmp
            if head is None:
                break
        return ret
            