# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         oneCheck = 2 ** 32
#         retNum = 0
#         for i in range(32, -1, -1):
#             if n & oneCheck > 1:
#                 retNum += i ** 2
#             oneCheck = oneCheck >> 1

# class Solution:
#     # @param n, an integer
#     # @return an integer
#     def reverseBits(self, n):
#         retNum = 0
#         for i in range(31, -1, -1):
#             if n & 1 > 0:
#                 retNum += 2 ** i
#             n = n>>1

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        retNum = 0
        for i in range(31, -1, -1):
            retNum += ((n & 1) * (2 ** i))
            n = n>>1
        return retNum