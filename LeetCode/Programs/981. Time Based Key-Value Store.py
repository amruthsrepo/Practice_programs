# Memory efficient
class TimeMap(object):

    def __init__(self):
        self.db = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.db:
            self.db[key][0].append(value)
            self.db[key][1].append(timestamp)
        else:
            self.db[key] = [[value],[timestamp]]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.db:
            return ""
        searchIn =  self.db[key]
        # if timestamp in searchIn:
        #         return searchIn[timestamp]
        sortedValues = searchIn[0]
        sortedTS = searchIn[1]
        if timestamp < sortedTS[0]:
            return ""
        if timestamp == sortedTS[0]:
            sortedValues[0]
        if timestamp == sortedTS[-1]:
            sortedValues[-1]
        l,r = 1,len(sortedTS)-1
        p = ((r-l) // 2) + l
        while r>l:
            if timestamp == sortedTS[p]:
                return sortedValues[p]
            elif timestamp > sortedTS[p]:
                l = p + 1
                p = ((r-l) // 2) + l
            else:
                r = p - 1
                p = ((r-l) // 2) + l
        while sortedTS[p] > timestamp:
            p -= 1
            if sortedTS[p] <= timestamp:
                return sortedValues[p]
        return sortedValues[p]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# time efficient

class TimeMap(object):

    def __init__(self):
        self.db = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.db[key] = self.db.get(key, {})
        self.db[key][timestamp] = value

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.db:
            return ""
        searchIn =  self.db[key]
        while timestamp > 0:
            if timestamp in searchIn:
                return searchIn[timestamp]
            timestamp -= 1
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)