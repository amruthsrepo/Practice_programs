# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sumCounts = {}
        self.highestFreq = 0
        self.highestSum = []

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.findFrequentTreeSumUtil(root)
        return self.highestSum
    
    def findFrequentTreeSumUtil(self, root):
        nodeSum = 0
        if root.left:
            nodeSum += self.findFrequentTreeSumUtil(root.left)
        if root.right:
            nodeSum += self.findFrequentTreeSumUtil(root.right)
        nodeSum += root.val
        self.sumCounts[nodeSum] = self.sumCounts.get(nodeSum, 0) + 1
        if self.sumCounts[nodeSum] > self.highestFreq:
            self.highestFreq = self.sumCounts[nodeSum]
            self.highestSum = [nodeSum]
        elif self.sumCounts[nodeSum] == self.highestFreq:
            self.highestSum.append(nodeSum)
        return nodeSum