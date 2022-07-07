# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def __init__(self):
        self.kNum = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # print('c', root.val, root.left, root.right)
        if root.left:
            lVal = self.kthSmallest(root.left, k)
            if lVal > -1:
                return lVal
        self.kNum += 1
        if self.kNum == k:
            return root.val
        if root.right:
            rVal = self.kthSmallest(root.right, k)
            if rVal > -1:
                return rVal
        # print(kNum, root.val, k)
        return -1