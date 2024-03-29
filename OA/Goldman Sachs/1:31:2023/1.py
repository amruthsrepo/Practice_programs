def isPossible(a, b, c, d):
    bfsQueue = [(a, b)]

    while bfsQueue:
        a, b = bfsQueue.pop()

        if a == c and b == d:
            return "Yes"

        ab = a + b
        if ab <= c:
            bfsQueue.insert(0, (ab, b))
        if ab <= d:
            bfsQueue.insert(0, (a, ab))

    return "No"


print(isPossible(1, 4, 5, 9))
print(isPossible(1, 2, 3, 6))
