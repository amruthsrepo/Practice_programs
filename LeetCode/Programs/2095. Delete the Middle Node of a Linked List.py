# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        end, half, prevHalf = head, head, head
        while end.next and end.next.next:
            end = end.next.next
            prevHalf = half
            half = half.next
        if half.next:
            if end.next:
                half.next = half.next.next
                return head
            prevHalf.next = prevHalf.next.next
            return head
        return None