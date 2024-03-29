# Given an array of n integers, arr, distribute its elements into the minimum possible buckets. Buckets can hold any number of elements, but a bucket of x elements must have more than floor(x/2) elements of the same value. Determine the minimum number of buckets required.


def minimumBuckets(arr):

    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    countInv = {}

    for num in counts:
        count = counts[num]
        countInv[count] = countInv.get(count, 0) + 1
