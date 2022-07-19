class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            l, r = 0, len(potions)
            while l < r:
                m = l + (r - l) // 2
                if spell * potions[m] >= success:
                    res.append(len(potions) - m)
                    break
                if spell * potions[m] < success:
                    l = m + 1

        return res
