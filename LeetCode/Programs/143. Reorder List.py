# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.listQ = []
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head.next:
            self.reOrderListUtil(head, head.next)

    def reOrderListUtil(self, head, currentNode):
        listQ = self.listQ
        if currentNode.next:
            listQ.insert(0, currentNode)
            tail = self.reOrderListUtil(head, currentNode.next)
            if tail:
                tail.next = listQ.pop()
                if tail is tail.next:
                    tail.next = None
                    del listQ
                    return
                tail = tail.next
                tail.next = currentNode
                if tail is tail.next:
                    tail.next = None
                    del listQ
                    return
                return currentNode
        else:
            head.next = currentNode
            return currentNode