"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        headCopy = head
        retListHead = copyNode = Node(head.val)
        # retListHead = copyNode
        prevHead = retListHead
        # head.copyNode = copyNode
        setattr(head, 'copyNode', copyNode)
        head = head.next
        while head:
            copyNode = Node(head.val)
            prevHead.next = copyNode
            setattr(head, 'copyNode', copyNode)
            # head.copyNode = copyNode
            head = head.next
            prevHead = copyNode
        head = headCopy
        copyNode = retListHead
        while head:
            if head.random:
                copyNode.random = head.random.copyNode
            copyNode = copyNode.next
            head = head.next
        return retListHead