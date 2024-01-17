# Given two arrays team_a and team_b of n integers each, choose two indices i and j such that the subarrays [team_a[i], team_a[i+1]... team_a[j]] and [team_b[i], team_b[i+1]... team_b[j]] can form a non decreasing sequence. Find the maximum possible value of (j-1+1) i.e. the length of the chosen subarray.
# print(get_max_team([3,2,5,3], [10,2,8,4])) # Output: 2
# print(get_max_team([2,7,3], [4,2,6])) # Output: 3
# print(get_max_team([5,2,4,1], [2,6,2,2])) # Output: 3


class Solution(object):
    def get_max_team(self, team1, team2):
        """
        :type team1: List[int]
        :type team2: List[int]
        :rtype: int
        """
        if not team1 or not team2:
            return 0
        if len(team1) != len(team2):
            return 0
        if len(team1) == 1:
            return 1
        max_len = 0
        for i in range(len(team1)):
            for j in range(i, len(team1)):
                if self.is_non_decreasing(team1[i : j + 1]) and self.is_non_decreasing(
                    team2[i : j + 1]
                ):
                    max_len = max(max_len, j - i + 1)
        return max_len

    def is_non_decreasing(self, arr):
        if not arr:
            return False
        if len(arr) == 1:
            return True
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True


s = Solution()
print(s.get_max_team([3, 2, 5, 3], [10, 2, 8, 4]))  # Output: 2
print(s.get_max_team([2, 7, 3], [4, 2, 6]))  # Output: 3
print(s.get_max_team([5, 2, 4, 1], [2, 6, 2, 2]))  # Output: 3
