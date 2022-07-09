class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dists = []
        for p in points:
            dists.append((p[0]**2) + (p[1]**2))
        dists = sorted(range(len(dists)), key=lambda j: dists[j])
        kClosest = [points[i] for i in dists[:k]]
        return kClosest

# Non hack time limit exceeded
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        kClosest = [[0,0]] * k
        dists = [float('inf')] * k
        for p in points:
            dist = (p[0]**2) + (p[1]**2)
            # print(p)
            if len(kClosest) < k or dist < dists[0]:
                # print(p, dist)
                l,r = 0,k
                piv = (r-l)//2
                while r-l > 2 and dists[piv] != dist:
                    # print(l, piv, r, i)
                    if dists[piv] > dist:
                        l = piv
                    elif dists[piv] < dist:
                        r = piv
                    piv = (r-l)//2
                piv += 1
                if dists[piv] < dist:
                    piv -= 1
                print(p, piv, dist, dists)
                kClosest.insert(piv, p)
                kClosest.pop(0)
                dists.insert(piv, dist)
                dists.pop(0)
        return kClosest