class Solution(object):
  def removeStars(self, s):
    """
    :type s: str
    :rtype: str
    """

    retS = ""
    for c in s:
      if c != '*':
        retS += c
      else:
        retS = retS[:-1]
    
    return retS