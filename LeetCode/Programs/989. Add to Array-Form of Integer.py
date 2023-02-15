class Solution(object):
    def addToArrayForm(self, num, k):
        carry = 0
        numLen = len(num)-1
        while numLen > -1:
            toAdd = (k%10) + carry + num[numLen]
            toAdd,carry = (toAdd,0) if toAdd<10 else ((toAdd%10),(toAdd//10))
            num[numLen] = toAdd
            k = k//10
            numLen -= 1
        while k:
            toAdd = (k%10) + carry
            toAdd,carry = (toAdd,0) if toAdd<10 else ((toAdd%10),(toAdd//10))
            num.insert(0,toAdd)
            k = k//10
        return [carry]+num if carry else num