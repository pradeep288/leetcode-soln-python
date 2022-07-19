from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)

        print(count.keys())
        res = 0
        if k == 0:
            for key, val in count.items():
                if val > 1:
                    res += 1
        else:
            for key, val in count.items():
                if k + key in count:
                    res += 1

        return res
