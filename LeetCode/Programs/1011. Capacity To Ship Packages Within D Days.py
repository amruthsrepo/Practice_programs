class Solution(object):
  def shipWithinDays(self, weights, days):
    """
    :type weights: List[int]
    :type days: int
    :rtype: int
    """
    l,r = weights[0],weights[0]
    for w in weights:
      l,r = min(l,w),max(r,w)

    l,r = (l*len(weights))//days,r*len(weights)
    # print(l,r)

    lastValid = 0
    while l<=r:
      p = (r+l)//2

      isGreater = 0
      totDays = 1
      weightInShip = 0
      for w in weights:
        weightInShip += w
        if weightInShip > p:
          weightInShip = w
          totDays += 1
        if totDays > days or w>p:  
          isGreater = 1
          break
      
      lastValid = ((not isGreater) * p) + (isGreater * lastValid)
      # print('a',l,p,r,isGreater)
      l = ((not isGreater) * l) + (isGreater * (p+1))
      r = ((not isGreater) * (p-1)) + (isGreater * r)
      # print('b',l,p,r)
    
    return lastValid