# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
  def reverseOddLevels(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: Optional[TreeNode]
    """
    # if not root.left: return root
    oddLevel = False
    q1,q2,q3 = [root],[],[]
    # Get L1, L2 and L3 then reverse L2
    # Set L1=L3 then get L2 and L3
    while q1:
      if not q1[0].left:  break
      for node in q1:
        leftNode, rightNode = node.left, node.right
        q2.extend([leftNode, rightNode])
        q3.extend([leftNode.left, leftNode.right, rightNode.left, rightNode.right])
      for i,node in enumerate(q1):
        node.left, node.right = q2.pop(), q2.pop()
        node.left.left,node.left.right,node.right.left,node.right.right = q3[(i*4):((i+1)*4)]
      q1,q2,q3 = q3 if q3[0] else [],[],[]
    return root