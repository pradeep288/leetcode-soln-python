class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, key):
        cur_node = self.cache[key]
        cur_node.prev.next, cur_node.next = cur_node.next, cur_node.prev

    def insert(self, key):
        cur_node = self.cache[key]
        k, v = cur_node.key, cur_node.val
        new_node = Node(key=k, val=v)
        new_node.prev = self.right.prev
        new_node.next = self.right
        new_node.prev.next = new_node
        self.right.prev = new_node

    def get(self, key: int) -> int:
        if not key in self.cache.keys():
            return -1
        self.remove(key)
        self.insert(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        self.cache[key] = Node(key, value)
        self.insert(key)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru.key)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
