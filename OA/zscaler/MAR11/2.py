def countSignals(frequencies, filtersRanges):
    maxStart, minEnd = filtersRanges[0]

    for filtersRange in filtersRanges:
        start, end = filtersRange
        maxStart = (start, maxStart)[start < maxStart]
        minEnd = (end, minEnd)[end > minEnd]

    allowCount = 0

    for frequency in frequencies:
        if maxStart <= frequency <= minEnd:
            allowCount += 1

    return allowCount


print(countSignals([8, 15, 14, 16, 21], [[10, 17], [13, 15], [13, 17]]))
print(countSignals([20, 5, 6, 7, 12], [[10, 20], [5, 15], [5, 30]]))
print(countSignals([20, 5, 6, 7, 12], [[5, 20], [6, 15], [1, 20]]))
