def calculateMax(network_nodes, network_from, network_to, frequency):

    edges = {}
    distances = {}

    for i in range(len(network_from)):
        start = network_from[i] - 1
        end = network_to[i] - 1
        edges[start] = edges.get(start, set())
        edges[start].add(end)
        edges[end] = edges.get(end, set())
        edges[end].add(start)

    maxDistance = 0

    def checkDistance(start, distance=0, visited=set()):
        visited.add(start)
        maxDist = distance
        for end in edges[start]:
            _dist = 0
            if (start, end) in distances:
                _dist = distances[(start, end)]
            elif (abs(frequency[start] - frequency[end]) < 2) and end not in visited:
                _dist = checkDistance(end, distance + 1, visited)
                distances[(start, end)] = _dist
            maxDist = max(maxDist, _dist)
        visited.remove(start)
        return maxDist

    for node in edges:
        maxDistance = max(maxDistance, checkDistance(node))

    return maxDistance


print(calculateMax(4, [1, 1, 1], [2, 3, 4], [1, 1, 1, 1]))
print(calculateMax(3, [2, 1], [1, 3], [1, 1, 1]))
print(calculateMax(3, [2, 1], [1, 3], [3, 1, 1]))
