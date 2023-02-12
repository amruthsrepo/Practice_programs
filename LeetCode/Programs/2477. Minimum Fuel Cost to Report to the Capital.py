class Solution(object):
    def minimumFuelCost(self, roads, seats):
        """
        :type roads: List[List[int]]
        :type seats: int
        :rtype: int
        """
        if not roads:   return 0
        roadsMap = {}
        for f,t in roads:
            roadsMap[f] = roadsMap.get(f, set())
            roadsMap[t] = roadsMap.get(t, set())
            roadsMap[f].add(t)
            roadsMap[t].add(f)

        def findCost(node, fromNode):
            retCost, people = 0, 1
            roadsMap[node].remove(fromNode)
            for n in roadsMap[node]:
                rc, pp = findCost(n, node)
                # print(n, rc, pp)
                retCost += rc
                people += pp
            
            return -(-people // seats) + retCost, people
        
        totCost = 0
        for node in roadsMap[0]:
            rc, pp = findCost(node, 0)
            # print(node, rc, pp)
            totCost += rc
        
        return totCost