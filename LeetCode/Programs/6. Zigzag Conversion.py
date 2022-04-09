class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lenStr = len(s)
        rowData = [''] * numRows
        rowNum = 0
        toggle = 1
        lastInd = numRows-1
        for i in range(len(s)):
            rowData[rowNum] += s[i]
            if rowNum == lastInd:
                toggle = -1
            elif rowNum == 0:
                toggle = 1
            rowNum += toggle
        resStr = ''
        for r in rowData:
            resStr += r
        return resStr