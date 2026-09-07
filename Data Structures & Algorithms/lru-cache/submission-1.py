class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache.pop(key)
        self.cache[key]=val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            val = self.cache.pop(key)
            self.cache[key] = val
        self.cache[key] = value
        if len(self.cache)>self.cap:
            lru = next(iter(self.cache))
            self.cache.pop(lru)
        
