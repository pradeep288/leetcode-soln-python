class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(val, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
                else:
                    return

            for x in range(val + 1, 10):
                if x <= target:
                    backtrack(x, stack + [x], target - x)
                else:
                    return

        backtrack(0, [], n)

        return res
