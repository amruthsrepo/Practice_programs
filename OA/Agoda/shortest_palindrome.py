class Solution:
    def solution(self, s):
        stArr = [_ for _ in s]
        l, r = 0, len(stArr) - 1

        while r > l:
            if stArr[r] != stArr[l]:
                stArr.insert(r + 1, stArr[l])
            else:
                r -= 1
            l += 1

        return "".join(stArr)


se = "abcdc"
s = Solution()
print(s.solution(se))
