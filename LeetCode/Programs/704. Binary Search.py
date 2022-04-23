class Solution(object):
    def search(self, nums, target):
        r = len(nums)-1
        l = 0
        p = (r-l)/2
        i = 0
        while l <= r and i <10:
            i += 1
            if nums[p] == target:
                return p
            elif target < nums[p]:
                r = p - 1
            else:
                l = p + 1
            p = l + (r-l)/2
        return -1


sl = Solution()
print(sl.search([-1,0,3,5,9,12], 12))
print(sl.search([-1,0,3,5,9,12], 2))
print(sl.search([-1,0,3,5,9,12], -1))
print(sl.search([-1,0,3,5,9,12], 0))
print(sl.search([-1,0,3,5,9,12], 3))
print(sl.search([-1,0,3,5,9,12], 5))
print(sl.search([-1,0,3,5,9,12], 9))
print(sl.search([-1,0,3,5,9,12], 13))