from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        for i in range(l):
            end = i + k + 1
            print('e',end,l,(end,l)[end>l],end>l)
            for j in range(i+1, (end,l)[end>l]):
                print(i,j)
                if nums[i] == nums[j]:
                    return True
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(s.containsNearbyDuplicate([1,2,3,1], 3))