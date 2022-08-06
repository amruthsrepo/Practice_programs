# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root, strVal = ''):
        """
        :type root: TreeNode
        :rtype: str
        """
        root.val = chr(97 + root.val)
        if root.left and root.right:
            leftVal = self.smallestFromLeaf(root.left, root.val + strVal)
            rightVal = self.smallestFromLeaf(root.right, root.val + strVal)
            return leftVal if leftVal < rightVal else rightVal
        if root.left:
            return self.smallestFromLeaf(root.left, root.val + strVal)
        if root.right:
            return self.smallestFromLeaf(root.right, root.val + strVal)
        return root.val + strVal