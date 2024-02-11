# You will be given an integer array and a threshold value. The threshold represents the maximum length of subarrays that may be created for the challenge. Each subarray created has a cost equal to the maximum integer within the subarray. Partition the entire array into subarrays with lengths less than or equal to the threshold, and do it at a minimum cost. The subarrays are to be chosen from contiguous elements, and the given array must remain in its original order.

# Example
# arr = [1, 3, 4, 5, 2, 6]
# threshold = 3
# Here are some ways to partition the arrays as an example. The lengths of partitions can differ as long as none are longer than threshold.
# • Partition into 6 subarrays of length 1 as [1], [3], [4], [5], [2], [6]. The total cost is 1 + 3+4+5+2+6 = 21.
# • Partition into 4 subarrays of various lengths: [1, 3], [4], [5], [2, 6]. The total cost is 3 + 4 + 5 + 6 = 18.
# • Partition into 3 subarrays of length 2 as : [1, 3] [4, 5], [2, 6]. The total cost is 3 + 5+ 6 = 14
# • Partition into 2 subarrays of length 3 as : [1, 3, 4], [5, 2, 6]. The total cost is 4 + 6 = 10.
# The optimal cost is 10.


from heapq import heappush, heappop


def calculateCost(arr, threshold):

    n = len(arr)
    cost = 0
    heap = []
    taken = [0] * n

    for i in range(n):
        heappush(heap, (-arr[i], i))

    while heap:
        num, i = heappop(heap)
        if taken[i]:
            continue

        num = -num
        maxNum = num

        p = i
        while p > 0 and p > (i - threshold + 1) and not taken[p - 1]:
            p -= 1
            maxNum = (maxNum, arr[p])[maxNum < arr[p]]
        q = i
        while q < (len(arr) - 1) and q < (i + threshold - 1) and not taken[q + 1]:
            q += 1
            maxNum = (maxNum, arr[q])[maxNum < arr[q]]

        if (q - p) <= (threshold - 1):
            for k in range(p, q + 1):
                taken[k] = 1
            cost += maxNum
        else:
            tempSum = 0
            k = p
            maxHeap = []
            for k in range(p, p + threshold):
                tempSum += arr[k]
                heappush(maxHeap, (-arr[k], k))
            maxSumHeap = maxHeap.copy()
            maxSum = tempSum
            maxSumInd = (p, k)
            while k < q:
                k += 1
                tempSum += arr[q]
                tempSum -= arr[p]
                p += 1

                heappush(maxHeap, (-arr[k], k))

                t = len(maxHeap) - 1
                while t > -1:
                    if maxHeap[t][1] < p:
                        maxHeap = maxHeap[:t] + maxHeap[t + 1 :]
                    t -= 1

                if tempSum > maxSum:
                    maxSumHeap = maxHeap.copy()
                    maxSumInd = (p, k)
                    maxSum = tempSum
                elif tempSum == maxSum:
                    b = 0
                    for b in range(len(maxSumHeap)):
                        if not (maxSumHeap[b][0] == maxHeap[b][0]):
                            break

                    if maxSumHeap[b][0] < maxHeap[b][0]:
                        maxSumHeap = maxHeap.copy()
                        maxSumInd = (p, k)
                        maxSum = tempSum

            cost += -maxSumHeap[0][0]
            p, k = maxSumInd
            for k in range(p, k + 1):
                taken[k] = 1
    return cost


print(calculateCost([1, 3, 4, 5, 2, 6], 3))
print(calculateCost([1, 2], 1))
print(calculateCost([1, 5, 2], 2))
