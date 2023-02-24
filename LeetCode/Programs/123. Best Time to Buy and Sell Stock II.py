class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # 1 2 3 4 3 2 4 6 3 2 5
    # 1     4   2   6   2 5
    # peak: 2trans=1Trans+low-curr,1trans=prevLow-curr
    # Valley: update low
    # [91,53,95,62,38,30,4,27,81,71,94,17,40,96,100,91,30,37]
    # valley: update valley,lowest
    # peak: 2trans = max(2trans,1trans+peak-valley), 1tras = max(1trans,peak-min(valley,lowest))
    # return max(1trans,2trans)

    if len(prices)<2: return 0

    oneT,twoT = 0,0
    prices = [prices[0]] + prices + [prices[-1]]
    valley,lowest,lowestInter = 0,0,0
    highestLookAhead = list(prices)

    for i in range(len(prices)-2,-1,-1):
      highestLookAhead[i] = max(highestLookAhead[i:i+2])
    highestLookAhead = [0] + highestLookAhead + [0]

    i = 1
    while i<len(prices)-1:
      p,c,n = prices[i-1:i+2]
      i+=1
      if p>=c<=n:
        # print('1v',c)
        valley,lowest,lowestInter = c,c,c
        break

    # [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]
    while i<len(prices)-1:
      p,c,n = prices[i-1:i+2]
      # print('v',p,c,n)
      i+= 2 if n==c else 1
      if p>=c<=n:
        # print('2v',c,oneT,twoT)
        lowest,lowestInter = min(lowest,c),min(lowestInter,c)
        twoT = max(twoT,oneT+highestLookAhead[i]-c)
      elif p<=c>=n:
        # print('p',c,oneT,twoT)
        twoT = max(oneT,oneT+c-lowestInter,twoT)
        if c-lowest > oneT:
          oneT = c-lowest
          lowestInter = 100001
        # print('p',c,oneT,twoT)
    # print(oneT,twoT)
    return twoT