class Solution(object):
  def shortestAlternatingPaths(self, n, redEdges, blueEdges):
    """
    :type n: int
    :type redEdges: List[List[int]]
    :type blueEdges: List[List[int]]
    :rtype: List[int]
    """
    rEdges, bEdges = {}, {}
    while redEdges and blueEdges:
      f,t = redEdges.pop()
      rEdges[f] = rEdges.get(f, [])
      rEdges[f].append(t)
      f,t = blueEdges.pop()
      bEdges[f] = bEdges.get(f, [])
      bEdges[f].append(t)
    
    while redEdges:
      f,t = redEdges.pop()
      rEdges[f] = rEdges.get(f, [])
      rEdges[f].append(t)
    while blueEdges:
      f,t = blueEdges.pop()
      bEdges[f] = bEdges.get(f, [])
      bEdges[f].append(t)
    
    numHops = 1
    pathLens = [1000] * n
    rq, bq, rqn, bqn = [0], [0], [], []
    rVisited, bVisited = set(), set()
    rVisited.add(0)
    bVisited.add(0)
    while bq or rq:
      while rq:
        node = rq.pop()
        for e in rEdges.get(node, []):
          if e not in bVisited:
            bVisited.add(e)
            bqn.append(e)
            pathLens[e] = min(pathLens[e], numHops)
      while bq:
        node = bq.pop()
        for e in bEdges.get(node, []):
          if e not in rVisited:
            rVisited.add(e)
            rqn.append(e)
            pathLens[e] = min(pathLens[e], numHops)
      numHops += 1
      bq,rq,bqn,rqn = bqn,rqn,[],[]
    
    pathLens[0] = 0
    for i in range(n):
      pathLens[i] = pathLens[i] if pathLens[i] < 1000 else -1
    return pathLens