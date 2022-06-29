# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: boolsc
        """
        return self.isValidBSTutil(root)
        
    def isValidBSTutil(self, root, lowThan=float('inf'), highThan=float('-inf')):
        if root.val >= lowThan or root.val <= highThan:
            return False
        left,right = True,True
        if root.left:
            left = self.isValidBSTutil(root.left, root.val, highThan)
        if root.right:
            right = self.isValidBSTutil(root.right, lowThan, root.val)
        return (left and right)