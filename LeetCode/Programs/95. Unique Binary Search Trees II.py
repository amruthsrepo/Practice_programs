# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def permuteTree(nodesList):
            if not nodesList:   return []
            if len(nodesList) < 2:
                leaf = TreeNode(nodesList[0])
                return [leaf]
            retTrees = []
            for root in range(1,len(nodesList)+1):
                # print('call', nodesList, nodesList[root-1], nodesList[:root-1], nodesList[root:])
                leftTrees = permuteTree(nodesList[:root-1])
                rightTrees = permuteTree(nodesList[root:])
                if leftTrees and rightTrees:
                    for lTree in leftTrees:
                        for rTree in rightTrees:
                            rootNode = TreeNode(nodesList[root-1])
                            rootNode.left = lTree
                            rootNode.right = rTree
                            retTrees.append(rootNode)
                    continue
                if leftTrees:
                    for tree in leftTrees:
                        rootNode = TreeNode(nodesList[root-1])
                        rootNode.left = tree
                        retTrees.append(rootNode)
                if rightTrees:
                    for tree in rightTrees:
                        rootNode = TreeNode(nodesList[root-1])
                        rootNode.right = tree
                        retTrees.append(rootNode)
            # print('r',nodesList, retTrees)
            return retTrees
        
        nodesList = [i for i in range(1,n+1)]
        
        return permuteTree(nodesList)
