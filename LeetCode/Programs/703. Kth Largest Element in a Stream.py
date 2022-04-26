class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        nums.sort(reverse = True)
        self.largestArr = nums[:k]

    def add(self, val):
        k = self.k
        largestArr = self.largestArr
        lenArr = len(largestArr)
        if lenArr < k or val > largestArr[k-1]:
            largestArr.append(val)
            lenArr += 1
            for i in range(lenArr):
                if val >= largestArr[i]:
                    break
            largestArr.insert(i, val)
        del largestArr[k:]
        return largestArr[-1]