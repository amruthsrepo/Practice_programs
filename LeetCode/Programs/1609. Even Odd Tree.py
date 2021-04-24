# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        parentList = [root]
        shouldBeEven = False
        childList = []
        parentListLen = len(parentList)
        while parentListLen > 0:
            for i in range(parentListLen):
                if (shouldBeEven and not parentList[i].val % 2 == 0) or (not shouldBeEven and parentList[i].val % 2 == 0):
                    return False
                childList += [] if not parentList[i].left else [parentList[i].left]
                childList += [] if not parentList[i].right else [parentList[i].right]
            shouldBeEven = not shouldBeEven
            childListLen = len(childList)
            if shouldBeEven and childListLen > 1:
                for i in range(childListLen - 1):
                    if not childList[i].val > childList[i + 1].val:
                        return False
            elif childListLen > 1:
                for i in range(childListLen - 1):
                    if not childList[i].val < childList[i + 1].val:
                        return False
            parentList, childList = childList, []
            parentListLen = childListLen
        return True

# [5,4,2,3,3,7]
# [1,10,4,3,null,7,9,12,8,6,null,null,2]
