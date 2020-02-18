# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.found = None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root.val == val:
            self.found = root
            return root
        if root.left != None:
            self.searchBST(root.left, val)
            if self.found != None:
                return self.found
        if root.right != None:
            self.searchBST(root.right, val)
            return self.found