# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        after = head.next
        head.next = None
        while after != None:
            temp = after.next
            after.next = head
            head = after
            after = temp
        return head
