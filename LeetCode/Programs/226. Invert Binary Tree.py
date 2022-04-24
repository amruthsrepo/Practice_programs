# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        lis = [root]
        if root == None:
            return root
        while lis:
            node = lis.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                lis.insert(0,node.left)
            if node.right:
                lis.insert(0,node.right)
        return root