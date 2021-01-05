class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        r, s = 0, (dividend < 0 and divisor < 0) or \
            (dividend > 0 and divisor > 0)
        if divisor == 1 or divisor == -1:
            dividend = dividend if divisor > 0 else 0-dividend
            dividend = (dividend, 2**31 - 1)[dividend > 2**31-1]
            dividend = (dividend, -2**31)[dividend < -2**31]
            return dividend
        divisor, dividend = abs(divisor), abs(dividend)
        if divisor > dividend:
            return 0
        while(dividend >= divisor):
            dividend -= divisor
            r += 1
        r = (r, (2**31)-1)[r > (2**31)-1]
        r = (r, -2**31)[r < -2**31]
        return r if s else 0-r


s = Solution()
print(s.divide(1, 1))
print(s.divide(-2147483648, 1))
print(s.divide(-2147483648, -1))
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(0, 1))
