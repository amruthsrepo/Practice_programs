from heapq import heappush, heappop


def itemSort(items):
    itemCount = {}

    for item in items:
        itemCount[item] = itemCount.get(item, 0) + 1

    heap = []
    for item in itemCount:
        heappush(heap, (itemCount[item], item))

    items = []
    while heap:
        f, v = heappop(heap)
        items += [v] * f

    return items


print(itemSort([4, 5, 6, 5, 4, 3]))
