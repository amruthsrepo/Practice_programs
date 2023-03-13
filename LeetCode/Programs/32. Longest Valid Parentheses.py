class Solution(object):
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """

    s = '[' + s
    stack = []
    maxValid = 0
    maxAti = [0] * (len(s)+1)

    for i,b in enumerate(s):
      if b == ')':
        if not stack: continue
        maxAti[i] = 2+maxAti[stack.pop()-1]+maxAti[i-1]
        maxValid = max(maxValid, maxAti[i])
      elif b == '(':
        stack.append(i)

    return maxValid