# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        searchFrom = [root]
        while searchFrom:
            rootStart = self.findRootNode(searchFrom.pop(), subRoot.val)
            if rootStart:
                if self.isSameTree(rootStart, subRoot):
                    return True
            else:
                continue
            if rootStart.left:
                searchFrom.insert(0, rootStart.left)
            if rootStart.right:
                searchFrom.insert(0, rootStart.right)
        return False
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False

    def findRootNode(self, root, val):
        if root.val == val:
            return root
        if not root.left and not root.right:
            return None
        if root.left:
            left = self.findRootNode(root.left, val)
            if left:
                return left
        if root.right:
            right = self.findRootNode(root.right, val)
            if right:
                return right
        return None


# BruteForce
# class Solution(object):
#     def isSubtree(self, root, subRoot):
#         if not subRoot: return True
#         if not root: return False
#         if self.isSameTree(root, subRoot): return True
#         return (self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot))
        
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True
#         if p and q and p.val == q.val:
#             return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
#         return False