# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = '', ''
        while l1 or l2:
            if l1 and l2:
                n1 += repr(l1.val)
                n2 += repr(l2.val)
                l1, l2 = l1.next, l2.next
            elif l1:
                n1 += repr(l1.val)
                l1 = l1.next
            elif l2:
                n2 += repr(l2.val)
                l2 = l2.next
        ans = repr(int(n1) + int(n2))
        del l1, l2, n1, n2
        retList = copy = ListNode(ans[0])
        for i in range(1, len(ans)):
            copy.next = ListNode(ans[i])
            copy = copy.next
        return retList