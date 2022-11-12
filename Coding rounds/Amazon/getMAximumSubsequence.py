def getMAximumSubsequence(text):
    aArr,mArr,zArr = [],[],[]
    for i in range(len(text)):
        if text[i] == 'A':
            aArr.append(i)
        elif text[i] == 'M':
            mArr.append(i)
        elif text[i] == 'Z':
            zArr.append(i)
    def removeOverlap(arr1, arr2):
        while arr1 and arr2 and arr1[-1] >= arr2[0]:
            if len(arr1) > len(arr2):
                arr1.pop()
            else:
                arr2.pop(0)
    removeOverlap(aArr,mArr)
    removeOverlap(mArr,zArr)
    letterCounts = [len(aArr), len(mArr), len(zArr)]
    # print(letterCounts)
    letterCounts.sort()
    if not letterCounts[0]:
        return letterCounts[1] * letterCounts[2]
    if letterCounts[0] == 1:
        return (letterCounts[0]+1) * letterCounts[1] * letterCounts[2]
    return letterCounts[0] * letterCounts[1] * (letterCounts[2] + 1)

# print(getMAximumSubsequence('AZ'))
# print(getMAximumSubsequence('AKMZ'))
print(getMAximumSubsequence('AKMMZ'))
print(getMAximumSubsequence('AMM'))