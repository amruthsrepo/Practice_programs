"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        rootCopy = root
        currentLevel = [root] if root else []
        while currentLevel:
            nextLevel = []
            rightNode = None
            for node in currentLevel:
                node.next = rightNode
                rightNode = node
                if node.right:
                    nextLevel.append(node.right)
                if node.left:
                    nextLevel.append(node.left)
            currentLevel = nextLevel
        return rootCopy