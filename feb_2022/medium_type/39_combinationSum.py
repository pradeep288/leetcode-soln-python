class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[
        List[int]]:
        res = []

        def backtracking(path, i, total):
            if total == target:
                res.append(path.copy())
                return

            if i >= len(candidates) or total > target:
                return

            path.append(candidates[i])
            backtracking(path, i, total + candidates[i])
            path.pop()
            backtracking(path, i + 1, total)

        backtracking([], 0, 0)

        return res
