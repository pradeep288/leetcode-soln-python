from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        if k == 0:
            for key, val in c.items():
                if val > 1:
                    count += 1
        else:
            for key, _ in c.items():
                if key + k in c:
                    count += 1

        return count
