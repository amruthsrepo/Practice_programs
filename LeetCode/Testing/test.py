class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longestTime = releaseTimes[0]
        longestKey = keysPressed[0]
        for i in range(1, (len(releaseTimes) - 1)):
            iTime = releaseTimes[i+1] - releaseTimes[i]
            print(repr(iTime) + ' ' + repr(ord(keysPressed[i]))
            if((iTime > longestTime) or (iTime is longestTime and ord(keysPressed[i]) > ord(longestKey))):
                longestTime=iTime
                longestKey=keysPressed[i]
        return longestKey
