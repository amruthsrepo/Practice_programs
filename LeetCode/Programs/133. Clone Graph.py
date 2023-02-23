"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
  def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:  return node

    retNode = Node(node.val, [])
    level1og = [node]
    level1copy = [retNode]
    copyList = {node:retNode}

    while level1og:
      og,copy = level1og.pop(),level1copy.pop()
      for n in og.neighbors:
        nCopy = copyList.get(n, Node(n.val,[]))
        copy.neighbors.append(nCopy)
        if n not in copyList:
          copyList[n] = nCopy
          level1og = level1og + [n]
          level1copy = level1copy + [copyList[n]]
    
    return retNode