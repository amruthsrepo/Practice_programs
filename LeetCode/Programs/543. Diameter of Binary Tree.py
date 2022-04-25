# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root.left and not root.right:
            return 0
        res = (self.diameterOfBinaryTreeUtil(root))
        print(res)
        res[1] -= 1
        return max(res)

    def diameterOfBinaryTreeUtil(self, root):
        if not root.left and not root.right:
            return [0, 1]
        leftH = rightH = leftDia = rightDia = 0
        if root.left:
            leftDia, leftH = self.diameterOfBinaryTreeUtil(root.left)
        if root.right:
            rightDia, rightH = self.diameterOfBinaryTreeUtil(root.right)
        return [max((leftH + rightH), leftDia, rightDia), 1 + max(leftH, rightH)]



[4,1,null,2,null,3]
[1,null,3,6]
[2,3,null,1]
[1,2,3,4,5]
[1,2]
[1]
[1,2,3]