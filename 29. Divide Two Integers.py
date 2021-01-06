LIMIT = 2 ** 31


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        isMinus = True if (dividend < 0 and divisor > 0) or (
            dividend > 0 and divisor < 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        res, pivot = 0, 1
        def limitCheck(count, isMinus):
            if not isMinus and count >= LIMIT:
                count = LIMIT - 1
            return count if not isMinus else -count
        while dividend > divisor:
            divisor <<= 1
            pivot <<= 1
        if dividend == divisor:
            return limitCheck(pivot, isMinus)
        while pivot > 0:
            while dividend < divisor:
                pivot >>= 1
                divisor >>= 1
            dividend -= divisor
            res += pivot
        return limitCheck(res, isMinus)


s = Solution()
print(s.divide(29, 3))
print(s.divide(1, 1))
print(s.divide(-2147483648, 1))
print(s.divide(-2147483648, -1))
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(0, 1))
