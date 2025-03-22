def MEXarray(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] > i:
            return i
    return i + 1

print(MEXarray([3,0,1,2]))