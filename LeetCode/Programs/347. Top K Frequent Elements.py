class Solution(object):
    def topKFrequent(self, nums, k):
        topKcounts = {}
        for n in nums:
            try:
                topKcounts[n] += 1
            except:
                topKcounts[n] = 1
        vals, counts = topKcounts.keys(), topKcounts.values()
        print(counts, vals)
        counts = sorted(range(len(counts)), key=lambda k: counts[k])
        kTop = []
        print(counts, vals)
        for i in range(k):
            kTop.append(vals[counts[i]])
        return kTop