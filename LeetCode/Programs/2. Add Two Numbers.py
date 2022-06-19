# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l1Head, l2Head, l1Prev, l2Prev = l1, l2, l1, l2
        while l1 and l2:
            l2.val += (l1.val + carry)
            if l2.val >= 10:
                carry = 1
                l2.val = l2.val % 10
            else:
                carry = 0
            # print(l2.val)
            l1Prev, l2Prev = l1, l2
            l1,l2 = l1.next, l2.next
        if l1:
            l2Prev.next = l1
            l2= l1
        while l2 and carry:
            l2.val += carry
            if l2.val >= 10:
                carry = 1
                l2.val = l2.val % 10
            else:
                carry = 0
            l2Prev = l2
            l2 = l2.next
        if carry and l2:
            l2.next = ListNode(carry)
        elif carry:
            l2Prev.next = ListNode(carry)
        return l2Head