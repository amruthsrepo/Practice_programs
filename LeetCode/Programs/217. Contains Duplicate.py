class Solution(object):
    def containsDuplicate(self, nums):
        hs = set()
        for i in nums:
            if i in hs:
                return True
            hs.add(i)
        return False