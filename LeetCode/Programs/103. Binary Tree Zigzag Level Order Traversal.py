# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        retList = []
        currentLevel = [root] if root else []
        r2l = True
        while currentLevel:
            nextLevel = []
            valuesInCurrentLevel = []
            for node in currentLevel:
                if r2l:
                    valuesInCurrentLevel.append(node.val)
                else:
                    valuesInCurrentLevel.insert(0, node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            r2l = not r2l
            retList.append(valuesInCurrentLevel)
            currentLevel = nextLevel
        return retList