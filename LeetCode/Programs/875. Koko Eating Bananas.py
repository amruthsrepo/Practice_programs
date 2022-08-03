class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def ceil(a, b):
            return -1 * (-a // b)
        l,r = 1,ceil(max(piles+[h]),(h / len(piles)))
        p = ((r-l) / 2) + l
        soln = r
        while r >= l:
            # print(l,p,r,h)
            totalHours = 0
            for nBan in piles:
                totalHours += ceil(nBan, p)
                if totalHours > h:
                    break
            if totalHours > h:
                l = p + 1
                p = ceil((r-l), 2) + l
                # print('thl',totalHours)
            else:
                soln = p
                r = p - 1
                p = ceil((r-l), 2) + l
                # print('thr',totalHours)
        return soln