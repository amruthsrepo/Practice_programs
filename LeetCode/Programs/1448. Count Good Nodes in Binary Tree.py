# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        return self.goodNodesUtil(root, root.val)
    
    def goodNodesUtil(self, root, largest):
        if root.val < largest:
            return (0 if not root.left else self.goodNodesUtil(root.left, largest)) + (0 if not root.right else self.goodNodesUtil(root.right, largest))
        return 1 + (0 if not root.left else self.goodNodesUtil(root.left, root.val)) + (0 if not root.right else self.goodNodesUtil(root.right, root.val))