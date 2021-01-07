# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self):
        super().__init__()
        self.las = None
        self.fis = None
        self.ret = None
    def reverseList(self, head: ListNode) -> ListNode:
        if(head != None):
            if(head.next != None):
                if(head.next.next != None):
                    self.fis = self.reverseList(head.next)
                    self.las.next = head
                    head.next = None
                    self.las = head
                    return self.fis
                else:
                    head.next.next = head
                    self.ret = head.next
                    head.next = None
                    self.las = head
                    return self.ret
            else:
                return head
        else:
            return head
