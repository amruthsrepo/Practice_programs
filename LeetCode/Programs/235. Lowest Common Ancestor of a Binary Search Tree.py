# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root.val == p.val or root.val == q.val:
            return root
        return self.lowestCommonAncestorUtil(root, p.val, q.val)[2]
    
    def lowestCommonAncestorUtil(self, root, p, q):
        foundP, foundQ = root.val == p, root.val == q
        foundNode = None
        if root.left:
            foundPLeft, foundQLeft, foundNode = self.lowestCommonAncestorUtil(root.left, p, q)
            if foundNode:
                return True, True, foundNode
            foundP = foundP or foundPLeft
            foundQ = foundQ or foundQLeft
        if root.right:
            foundPRight, foundQright, foundNode = self.lowestCommonAncestorUtil(root.right, p, q)
            if foundNode:
                return True, True, foundNode
            foundP = foundP or foundPRight
            foundQ = foundQ or foundQright
        if foundQ and foundP and not foundNode:
            foundNode = root
        print(p,q,foundP,foundQ,root.val)
        return foundP, foundQ, foundNode