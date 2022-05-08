class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, 0, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        if digits[0] == 9:
            digits[0] = 0
            digits.insert(0, 1)
            return digits
        digits[0] += 1
        return digits