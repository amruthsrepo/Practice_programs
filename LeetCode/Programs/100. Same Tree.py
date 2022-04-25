# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False
        sameLeft = sameRight = False
        sameVal = p.val == q.val
        if p.left and q.left:
            sameLeft = self.isSameTree(p.left,q.left)
        elif not p.left and not q.left:
            sameLeft = True
        if p.right and q.right:
            sameRight = self.isSameTree(p.right,q.right)
        elif not p.right and not q.right:
            sameRight = True
        if sameLeft and sameRight and sameVal:
            return True
        return False
