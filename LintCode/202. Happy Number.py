class Solution(object):
    def isHappy(self, n):
        listNums = []
        while n not in listNums:
            if n == 1:
                return True
            listNums.append(n)
            num = n
            n = 0
            while num > 0:
                mod10 = num % 10
                num = int(num / 10)
                n += mod10 ** 2
        return False