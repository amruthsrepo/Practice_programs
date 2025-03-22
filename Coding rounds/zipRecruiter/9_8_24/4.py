def solution(a, b, queries):

    result = []
    sortedA = sorted(a)
    currQuery = 0
    lastPairQuery = -1

    for query in queries:

        x = query[-1]
        currQuery += 1

        if len(query) == 2:
            i, j = 0, 0
            totalPAirs = 0
            if lastPairQuery < currQuery - 1:
                sortedB = sorted(b, reverse=True)
            lasti = sortedA[0] - 1
            lastiCount = 0
            while i < len(a) and j < len(b):
                if sortedA[i] + sortedB[j] == x:
                    totalPAirs += 1
                    lastiCount += 1
                if (sortedA[i] + sortedB[j] < x) or (len(sortedA) - i > len(sortedB) - j):
                    lasti = sortedA[i]
                    i += 1
                    while i < len(a) and sortedA[i] == lasti:
                        totalPAirs += lastiCount
                        i += 1
                    lastiCount = 0
                else:
                    j += 1
            result += [totalPAirs]
            lastPairQuery = currQuery

        else:
            i = query[1]
            b[i] += x

    return result


print(solution([1, 2, 3], [1, 4], [[1, 5], [0, 0, 2], [1, 5]]))

print(solution([1, 2, 2], [2, 3], [[1, 4], [0, 0, 1], [1, 5]]))
