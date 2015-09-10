"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key
exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.


TLE
"""


class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.times = {}
        self.cache = {}
        self.timestamp = 0

    # @return an integer
    def get(self, key):
        self.timestamp += 1
        if key in self.cache:
            self.times[key] = self.timestamp
            return self.cache[key]
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        self.timestamp += 1
        if key in self.cache:
            self.times[key] = self.timestamp
        else:
            if len(self.cache) >= self.capacity:
                lru_key = self.get_lru_key()
                del self.cache[lru_key]
                del self.times[lru_key]
            self.cache[key] = value
            self.times[key] = self.timestamp

    def get_lru_key(self):
        min_time = self.timestamp
        res = None
        for key in self.times:
            if self.times[key] <= min_time:
                res = key
                min_time = self.times[key]
        return res
