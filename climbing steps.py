class Solution:
    def climbStairs(self, n: int) -> int:
        if n<5:
            return n
        def sumN(num) -> int:
            return ((num * (num + 1)) / 2)
        totalCombs, num1s, num2s = n, n, 0
        def combsGen() -> int:

        print(tot


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(int(input('Enter staeps'))))