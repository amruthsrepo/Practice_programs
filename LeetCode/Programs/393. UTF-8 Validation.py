class Solution(object):
  def validUtf8(self, data):
    """
    :type data: List[int]
    :rtype: bool
    """
    # valid- [1B][2B,F][3B,F,F][4B,F,F,F]
    # invalid- [F][2B,NF][3B,NF,NF][4B,NF,NF,NF]
    oneB = (1<<7)
    twoBmax,threeBmax,fourBmax,followerBmax = int('11011111',2),int('11101111',2),int('11110111',2),int('10111111',2)
    twoBmin,threeBmin,fourBmin,followerBmin = int('11000000',2),int('11100000',2),int('11110000',2),int('10000000',2)

    # mask required digits
    # not xor to see if it is equal
    # based on that decide how many to pop
    data = data[::-1]

    while data:
      decider = data.pop()
      if not oneB&decider:  continue
      if decider>fourBmax or (followerBmin<=decider<=followerBmax):  return False
      toPop = ((twoBmin<=decider<=twoBmax)*1) + ((threeBmin<=decider<=threeBmax)*2) + ((fourBmin<=decider<=fourBmax)*3)
      for _ in range(toPop):
        try:
          fData = data.pop()
          if not (followerBmin<=fData<=followerBmax):
            return False
        except Exception as e:  return False
    
    return True