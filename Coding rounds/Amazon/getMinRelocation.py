def getMinRelocation(regionStart, regionEnd):
    regionRange = list(zip(regionStart, regionEnd))
    regionRange.sort(key= lambda x: x[0])
    numRelocations = 0
    prevMax = regionRange[0][1]
    for start, end in regionRange[1:]:
        if start <= prevMax:
            prevMax = max(prevMax, end)
        else:
            numRelocations += 1
            prevMax = end
    return numRelocations

print(getMinRelocation([1,3,4,6,9], [2,8,5,7,10]))