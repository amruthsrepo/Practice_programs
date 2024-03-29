def maxLength(a, k):
    l, r = 0, 0
    currSum = 0
    maxSub = 0

    while r < len(a):
        if currSum <= k:
            maxSub = (maxSub, r - l)[maxSub < r - l]
            currSum += a[r]
            r += 1
        else:
            currSum -= a[l]
            l += 1

    if currSum <= k:
        maxSub = (maxSub, r - l)[maxSub < r - l]

    return maxSub


print(maxLength([1, 1, 3, 4, 5, 1, 1, 1, 1], 3))
print(maxLength([3, 1, 2, 1], 4))
