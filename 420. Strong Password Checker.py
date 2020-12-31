class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        inputLen = len(password)
        if inputLen < 2:
            return 6 - inputLen
        noCapital, noSmall, noNumber, continousReplaced, steps = True, True, True, False, 0
        prev2, prev1, latestIncr, latestIncrI, steps, replacement = '', '', '', 0, 0, 0
        alphaSet, repeatedMax, repeatedNum = set(), 0, 0
        for i in range(inputLen):
            alphaSet.add(password[i])
            if prev1 == prev2 == password[i] and (i - latestIncrI) > 1:
                replacement += 1
                continousReplaced = continousReplaced or latestIncr == password[i]
                latestIncrI, latestIncr = i+1, password[i]
            repeatedNum += 1 if prev1 == password[i] else -repeatedNum
            repeatedMax = max(repeatedMax, repeatedNum)
            prev2, prev1 = prev1, password[i]
            charCode = ord(password[i])
            if 64 < charCode < 97:
                noCapital = False
            elif 96 < charCode < 123:
                noSmall = False
            elif 47 < charCode < 58:
                noNumber = False
        steps += int(noCapital) + int(noSmall) + int(noNumber)
        if inputLen < 6:
            t = abs(replacement - steps)
            return max(t, steps) if t != 0 else t + (6 - inputLen)
        if inputLen > 20:
            t = (inputLen - 20)
            if replacement == t:
                return max(replacement, steps) + 1
            if continousReplaced and t > replacement:
                return t+replacement-int(t/3)-(t % 3)-steps-int(repeatedMax % 3 == 0)
            if t > replacement:
                return t+steps+int(repeatedMax > 3)
            if steps == 0:
                return replacement
            if len(alphaSet) > 1 and steps < 3:
                return replacement-steps+t
            t1 = [replacement, steps, t]
            t1.sort()
            return replacement+steps+t-t1[0]-t1[1]
        if steps == replacement == 0:
            return 0
        return (steps, replacement)[replacement > steps]


s = Solution()
print(f'13 : {s.strongPasswordChecker("aaaaaaaAAAAAA6666bbbbaaaaaaABBC")}')
print(f'4 : {s.strongPasswordChecker("aaaaaa1234567890123Ubefg")}')
print(f'7 : {s.strongPasswordChecker("..................!!!")}')
print(f'3 : {s.strongPasswordChecker("1234567890123456Baaaaa")}')
print(f'3 : {s.strongPasswordChecker("...")}')
print(f'3 : {s.strongPasswordChecker("abababababababababaaa")}')
print(f'7 : {s.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa")}')
print(f'8 : {s.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc")}')
print(f'8 : {s.strongPasswordChecker("aaaabbbbccccddeeddeeddeedd")}')
print(f'4 : {s.strongPasswordChecker("A1234567890aaabbbbccccc")}')
print(f'23 : {s.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA")}')
print(f'5 : {s.strongPasswordChecker("aaaaAAAAAA000000123456")}')
print(f'1 : {s.strongPasswordChecker("aa123")}')
print(f'0 : {s.strongPasswordChecker("1337C0d3")}')
print(f'3 : {s.strongPasswordChecker("1111111111")}')
print(f'2 : {s.strongPasswordChecker("aaa111")}')
print(f'3 : {s.strongPasswordChecker("aA1")}')
