class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(idx, cur_combination, target):
            if len(cur_combination) == k and target == 0:
                res.append(cur_combination.copy())

            if target < 0 or idx > 9:
                return

            for i in range(idx + 1, 10):
                backtrack(i, cur_combination + [i], target - i)
                backtrack(i, cur_combination, target)

        backtrack(0, [], n)
        
        return res
