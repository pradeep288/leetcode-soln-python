class MyHashSet:

    def __init__(self):
        self.hash_set = [[] for _ in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            subkey = key % 1000
            self.hash_set[subkey].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            subkey = key % 1000
            self.hash_set[subkey].remove(key)

    def contains(self, key: int) -> bool:
        subkey = key % 1000
        return key in self.hash_set[subkey]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
