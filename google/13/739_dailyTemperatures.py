class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # idx, t
        for i, t in enumerate(temperatures):
            if stack and t > stack[-1][1]:
                idx, temp = stack.pop()
                res[idx] = i - idx
            stack.append([i, t])

        return res