class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        inputLen = len(password)
        if inputLen < 2:
            return 6 - inputLen
        noCapital, noSmall, noNumber, continousReplaced, steps = True, True, True, False, 0
        prev2, prev1, latestIncr, latestIncrI, steps, replacement = '', '', '', 0, 0, 0
        for i in range(inputLen):
            if prev1 == prev2 == password[i] and (i - latestIncrI) > 1:
                replacement += 1
                continousReplaced = continousReplaced or latestIncr == password[i]
                latestIncrI, latestIncr = i+1, password[i]
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
            return t if t != 0 else t + (6 - inputLen)
        elif inputLen > 20:
            t = (inputLen - 20)
            if continousReplaced and t > replacement:
                return t+replacement-int(t/3)-steps
            return t+steps if t > replacement else replacement if steps == 0 else replacement-steps+t
        elif steps == replacement == 0:
            return 0
        return (steps, replacement)[replacement > steps]


s = Solution()
print(f'4 : {s.strongPasswordChecker("A1234567890aaabbbbccccc")}')
print(f'23 : {s.strongPasswordChecker("FFFFFFFFFFFFFFF11111111111111111111AAA")}')
print(f'8 : {s.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc")}')
print(f'8 : {s.strongPasswordChecker("aaaabbbbccccddeeddeeddeedd")}')
print(f'5 : {s.strongPasswordChecker("aaaaAAAAAA000000123456")}')
print(f'1 : {s.strongPasswordChecker("aa123")}')
print(f'0 : {s.strongPasswordChecker("1337C0d3")}')
print(f'3 : {s.strongPasswordChecker("1111111111")}')
print(f'2 : {s.strongPasswordChecker("aaa111")}')
print(f'3 : {s.strongPasswordChecker("aA1")}')
