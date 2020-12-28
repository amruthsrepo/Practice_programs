def twoSum():
    nums = [2, 7, 11, 15]
    target = 9
    numlen = len(nums)
    for i in range(0, numlen):
        for j in range(i+1, numlen):
            if (nums[i]+nums[j] == target):
                return [i, j]


twoSum()
