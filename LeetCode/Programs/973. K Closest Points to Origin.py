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