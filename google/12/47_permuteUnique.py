import collections


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = collections.Counter(nums)
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            for c in count:
                if count[c] > 0:
                    perm.append(c)
                    count[c] -= 1

                    dfs()

                    perm.pop()
                    count[c] += 1
        dfs()

        return res
