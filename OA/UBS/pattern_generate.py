# So Mr. George recently joined college and he is too much fascinated by patterns. He was able to implement the following star pattern-
# *
# **
# ***
# ****
# in which the no. of asterisk at a level N is N.
# Now instead of just Asterisk, Mr. George also decided to use small alphabet o
# So Patterns may look like these -
# *
# 00
# ***
# ****
# 00000
# But he won't mix a row with both 'o' and'*'.
# Now given He has A no. of 'd' and B no. of '*', Tell the total ways he can implement a star pattern.
# Since this no. can be very large, return it modulo 998244353.


class Solution(object):
    def pattern_generate(self, d, s):
        """
        :type d: int
        :type s: int
        :rtype: int
        """
        if d == 0 and s == 0:
            return 1
        if d == 0 and s == 1:
            return 1
        if d == 1 and s == 0:
            return 1
        if d == 1 and s == 1:
            return 2
        if d == 0 and s > 1:
            return 0
        if d > 1 and s == 0:
            return 0
        if d == 1 and s > 1:
            return 1
        if d > 1 and s == 1:
            return 1
        return self.pattern_generate(d - 1, s) + self.pattern_generate(d, s - 1)


s = Solution()

print(s.pattern_generate(2, 2))  # Output: 4
print(s.pattern_generate(7, 8))  # Output: 1716
print(s.pattern_generate(1, 1))  # Output: 2
print(s.pattern_generate(3, 2))  # Output: 6
print(s.pattern_generate(4, 4))  # Output: 35
