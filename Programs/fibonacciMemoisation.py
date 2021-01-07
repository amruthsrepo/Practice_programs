class Solution:
    def fib(self, N: int) -> int:
        cache = {'lar':-1}
        def recur(N):
            if N < 2:
                return N
            elif N < cache['lar']:
                return cache[N]
            else:
                r = (recur(N-1) + recur(N-2))
                cache[N] = r
                cache['lar'] = N
                return r
        return recur(N)

if __name__ == "__main__":
    s = Solution()
    # out = s.fib(int(input()))
    out = s.fib(7)
    print(out)