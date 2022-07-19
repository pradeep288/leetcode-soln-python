class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos = []
        self.cur_idx = 0
        cur_combo = []

        def backtrack(i):
            if i > combinationLength and len(cur_combo) == combinationLength:
                self.combos.append("".join(cur_combo.copy()))
                return
            elif i > combinationLength:
                return

            cur_combo.append(characters[i])
            backtrack(i + 1)

            cur_combo.pop()
            backtrack(i + 1)

        backtrack(0)

    def next(self) -> str:
        next_str = self.combos[self.cur_idx]
        self.cur_idx += 1
        return next_str

    def hasNext(self) -> bool:
        return self.cur_idx < len(self.combos)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
