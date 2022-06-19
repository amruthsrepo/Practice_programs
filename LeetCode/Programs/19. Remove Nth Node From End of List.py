# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        toRemove, tail = head, head
        while n > 0:
            tail = tail.next
            n -= 1
        while tail and tail.next:
            toRemove = toRemove.next
            tail = tail.next
        if toRemove.next:
            if tail:
                toRemove.next = toRemove.next.next
                return head
            return head.next
        return None