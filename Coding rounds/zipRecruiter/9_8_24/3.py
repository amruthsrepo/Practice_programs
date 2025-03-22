def calcCross(matrix):

    totalCross = 0

    l, w = len(matrix), len(matrix[0])
    validCols = {}
    validColsCount = 0

    for j in range(w):
        colSet = set()
        for i in range(l):
            colSet.add(matrix[i][j])
            if len(colSet) > 2:
                break
        if len(colSet) < 2:
            validCols[j] = range(l)
            validColsCount += l
        else:
            counts = {}
            for t in range(l):
                k = matrix[t][j]
                counts[k] = counts.get(k, 0) + 1
                if counts[k] > 1:
                    del counts[k]
                    for num in counts:
                        validCols[j] = [num]
                        validColsCount += 1

    print(validCols)

    for i in range(l):
        lineSet = set()
        for j in range(w):
            lineSet.add(matrix[i][j])
            if len(set) > 2:
                break
        if len(lineSet) > 1:
            pass
        else:
            totalCross += validColsCount
