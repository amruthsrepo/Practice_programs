def strokesRequired(picture):
    picture = [[_ for _ in r] for r in picture]

    def getAdjacent(i, j):
        adj = []
        if i < len(picture) - 1:
            adj.append((i + 1, j))
        if i > 0:
            adj.append((i - 1, j))
        if j < len(picture[0]) - 1:
            adj.append((i, j + 1))
        if j > 0:
            adj.append((i, j - 1))
        return adj

    def traverse(letter, i, j):
        bfsQueue = [(i, j)]
        picture[i][j] = "v"
        while bfsQueue:
            i, j = bfsQueue.pop()
            adj = getAdjacent(i, j)
            for pair in adj:
                a, b = pair
                if picture[a][b] == letter:
                    bfsQueue.append((a, b))
                    picture[a][b] = "v"

    numIslands = 0
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] != "v":
                traverse(picture[i][j], i, j)
                numIslands += 1

    return numIslands


print(strokesRequired(["aaaba", "ababa", "aaaca"]))
