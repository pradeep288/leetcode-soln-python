class MyHashSet:
    def __init__(self):
        self.hash_set = [[None] for _ in range(1000)]

    def add(self, key: int) -> None:
        group = key % 1000
        self.hash_set[group].append(key)

    def remove(self, key: int) -> None:
        group = key % 1000
        if self.contains(key):
            self.hash_set[group].remove(key)

    def contains(self, key: int) -> bool:
        group = key % 1000
        return key in self.hash_set[group]
