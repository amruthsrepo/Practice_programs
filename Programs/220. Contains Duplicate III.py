from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        num_len = len(nums)
        sortedIndices = sorted(range(len(nums)), key=lambda k: nums[k])
        if k > 0 and num_len > 1:
            for i in range(0, num_len-1):
                for j in range(i+1, num_len):
                    try:
                        if not abs(nums[sortedIndices[i]] - nums[sortedIndices[j]]) <= t:
                            break
                        elif abs(sortedIndices[i] - sortedIndices[j]) <= k:
                            return True
                    except IndexError:
                        break
            return False
        else:
            return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1, 3, 6, 2], 1, 2))
print(s.containsNearbyAlmostDuplicate([7, 1, 3], 15, 3))
print(s.containsNearbyAlmostDuplicate([4, 1, -1, 6, 5], 3, 1))
print(s.containsNearbyAlmostDuplicate([7, 1, 3], 3, 3))
print(s.containsNearbyAlmostDuplicate([7, 1, 3], 2, 3))
print(s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))
print(s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2))
print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
