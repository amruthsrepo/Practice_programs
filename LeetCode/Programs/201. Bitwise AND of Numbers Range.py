class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        leftCopy = left
        sqNum = 1
        while leftCopy > 0:
            sqNum = sqNum<<1
            leftCopy = leftCopy>>1
        if sqNum <= right:
            return 0
        andNum = left
        while andNum > 0 and left < right:
            left += 1
            andNum &= left
        return andNum