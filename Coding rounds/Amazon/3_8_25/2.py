from typing import List


def calculateMaxQualityScore(impactFactor: int, ratings: List[int]) -> int:
    n = len(ratings)

    # Helper function to calculate the maximum subarray sum
    def maxSubarraySum(arr):
        max_sum = float("-inf")
        current_sum = 0
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    # Calculate the initial maximum subarray sum
    initial_max = maxSubarraySum(ratings)

    # Strategy 1: Amplify Ratings
    amplified = [rating * impactFactor for rating in ratings]
    max_amplified = float("-inf")

    for i in range(n):
        for j in range(i, n):
            temp = []
            temp.extend(ratings[:i])
            j += 1
            temp.extend(amplified[i:j])
            temp.extend(ratings[j:])
            max_amplified = max(max_amplified, maxSubarraySum(temp))

    # Strategy 2: Adjust Ratings
    adjusted = [
        (rating // impactFactor if rating > 0 else -(-rating // impactFactor)) for rating in ratings
    ]
    max_adjusted = float("-inf")

    for i in range(n):
        for j in range(i, n):
            temp = ratings[:i] + adjusted[i : j + 1] + ratings[j + 1 :]
            max_adjusted = max(max_adjusted, maxSubarraySum(temp))

    # Return the maximum of the three scores
    return max(initial_max, max_amplified, max_adjusted)


print(calculateMaxQualityScore(3, [5, -3, -3, 2, 4]))

print(calculateMaxQualityScore(1, [-2, 3, -3, -1]))

print(calculateMaxQualityScore(3, [-4]))
