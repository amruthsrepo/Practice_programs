def getMaximumRewardPoints(reward):
    reward = sorted(reward, reverse=True)
    maxPoints = 0
    for i in range(len(reward)):
        if reward[i] > i:
            maxPoints += reward[i] - i
        else:
            return maxPoints
    return maxPoints


print(getMaximumRewardPoints([5, 2, 2, 3, 1]))
print(getMaximumRewardPoints([1, 2, 3, 4, 5]))
print(getMaximumRewardPoints([5, 5, 5]))
