class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = []
        self.data = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.data[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.data:
            self.data[key] = value
            self.keys.remove(key)
            self.keys.insert(0, key)
        else:
            data, keys, size, capacity = self.data, self.keys, self.size, self.capacity
            data[key] = value
            keys.insert(0, key)
            if size == capacity:
                del data[keys.pop()]
            else:
                self.size += 1
            
        # print('p', key, value, self.keys, self.values)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)