# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        if not root:
            return True
        return self.isBalancedUtil(root)[1]
        
    def isBalancedUtil(self, root):
        if not root.left and not root.right:
            return [1, True]
        left = right = 0
        leftBalanced = rightBalanced = True
        if root.left:
            left, leftBalanced = self.isBalancedUtil(root.left)
        if root.right:
            right, rightBalanced = self.isBalancedUtil(root.right)
        if rightBalanced and leftBalanced and abs(right-left) < 2:
            return [1+max(left,right), True]
        return [0, False]
