# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        toAdd = l1.val + l2.val
        carry = int(toAdd/10)
        newList = retList = ListNode(toAdd % 10)
        l1, l2 = l1.next, l2.next
        while l1 or l2:
            if l1 and l2:
                toAdd = l1.val + l2.val + carry
                carry = int(toAdd/10)
                newList.next = ListNode(toAdd % 10)
                newList = newList.next
                l1, l2 = l1.next, l2.next
            elif l1:
                toAdd = l1.val + carry
                carry = int(toAdd/10)
                newList.next = ListNode(toAdd % 10)
                newList = newList.next
                l1 = l1.next
            elif l2:
                toAdd = l2.val + carry
                carry = int(toAdd/10)
                newList.next = ListNode(toAdd % 10)
                newList = newList.next
                l2 = l2.next
        if carry > 0:
            newList.next = ListNode(carry)
        return retList
