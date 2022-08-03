class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            if nums[0] == target:
                return 0
            elif len(nums) == 2 and nums[1] == target:
                return 1
            else:
                return -1
        l,r = 0,len(nums)-1
        p = (-1 * ((-(r-l)) // 2)) + l
        lowest = r
        while r >= l:
            # print(l,p,r)
            if nums[p] > nums[lowest]:
                l = p+1
                p = (-1 * ((-(r-l)) // 2)) + l
            else:
                lowest = p
                r = p-1
                p = (-1 * ((-(r-l)) // 2)) + l
            if l == r == 0:
                p = 0
                if nums[p] < nums[lowest]:
                    lowest = p
                break
        # print('low:',lowest)
        if target > nums[-1]:
            l,r = 0,lowest-1
        elif target < nums[-1]:
            l,r = lowest,len(nums)-1
        else:
            return len(nums)-1
        p = (-1 * ((-(r-l)) // 2)) + l
        # print('u',l,p,r)
        while l <= r:
            # print(l,p,r)
            if target > nums[p]:
                l = p+1
                p = (-1 * ((-(r-l)) // 2)) + l
            elif target < nums[p]:
                r = p-1
                p = (-1 * ((-(r-l)) // 2)) + l
            else:
                return p
            if l == r == 0:
                # print('in')
                p = 0
                if nums[p] == target:
                    return p
        return -1