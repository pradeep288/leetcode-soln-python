class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q, res = [], []
        for i in range(1, 10):
            q.append(i)

        while len(q):
            cur_val = q.pop()
            if low <= cur_val <= high:
                res.append(cur_val)
            new_val = cur_val * 10 + cur_val % 10 + 1
            if new_val <= high and cur_val % 10 != 9:
                q.append(new_val)

        return sorted(res)
