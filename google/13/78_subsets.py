class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx, perm):
            if len(perm) == len(nums):
                return
            res.append(perm.copy())
            for i in range(idx+1, len(nums)):
                perm.append(nums[i])
                dfs(i, perm)
                perm.pop()
                dfs(i, perm)

        dfs(0, [])

        return res

