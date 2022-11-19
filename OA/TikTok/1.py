
import collections


class Graph:

	# init function to declare class variables
	def __init__(self):
		self.V = set()
		self.adj = {}

	def DFSUtil(self, temp, v, visited):

		# Mark the current vertex as visited
		visited.add(v)

		# Store the vertex to list
		temp.append(v)

		# Repeat for all vertices adjacent
		# to this vertex v
		self.adj[v] = self.adj.get(v, list())
		for i in self.adj[v]:
			if i not in visited:

				# Update the list
				temp = self.DFSUtil(temp, i, visited)
		return temp

	# method to add an undirected edge
	def addEdge(self, v):
		v,w = v[0], v[1]
		self.adj[v] = self.adj.get(v, list())
		self.adj[v].append(w)
		self.adj[w] = self.adj.get(w, list())
		self.adj[w].append(v)
		self.V.add(v)
		self.V.add(w)

	# Method to retrieve connected components
	# in an undirected graph
	def connectedComponents(self):
		visited = set()
		longestNw = 0
		# for i in range(self.V):
		# 	visited.append(False)
		for v in self.V:
			if v not in visited:
				temp = []
				currNW = len(self.DFSUtil(temp, v, visited))
				longestNw = max(longestNw, currNW)
		return longestNw


# Driver Code
if __name__ == "__main__":

	# numSets = input()
	for T in range(int(input())):
		g = Graph()
		for m in range(int(input())):
			g.addEdge(input().split(' '))
		print(g.connectedComponents())
	# print("Following are connected components")
	# print(cc)



def numberOfPaths(m, n, numPaths = {}):
    if(m == 1 or n == 1):
        return 1
    # mOne, nOne = numberOfPaths(m-1, n), numberOfPaths(m, n-1)
    if (m-1, n) in numPaths:
        mOne = numPaths[(m-1, n)]
    else:
        mOne = numberOfPaths(m-1, n)
        numPaths[(m-1, n)] = mOne
    if (m, n-1) in numPaths:
        nOne = numPaths[(m, n-1)]
    else:
        nOne = numberOfPaths(m, n-1)
        numPaths[(m, n-1)] = nOne
    return mOne + nOne

# m = 200
# n = 200
# print(numberOfPaths(m, n))



def getMinimumUniqueSum(arr):
    numSet = set()
    numCounts = {}
    
    for n in arr:
        if n in numSet:
            numCounts[n] += 1
        else:
            numSet.add(n)
            numCounts[n] = 1
    
    sum = 0
    numIncr = 0
    numsList = list(numSet)
    numsList.sort()