class Solution(object):
    def twoSum(self, numbers, target):
        i,j = 0, len(numbers)-1
        numSum = numbers[i] + numbers[j]
        while numSum != target:
            if numSum > target:
                j -= 1
            elif numSum < target:
                i += 1
            numSum = numbers[i] + numbers[j]
        return [i+1, j+1]