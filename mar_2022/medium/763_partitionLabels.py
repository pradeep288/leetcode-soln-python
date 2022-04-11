class Solution(object):
    def partitionLabels(self, S):
        last_idx = {}
        for i, c in enumerate(S):
            last_idx[c] = i

        size, end = 0, 0
        res = []
        for i, c in enumerate(S):
            size += 1
            end = max(end, last_idx[c])
            if end == i:
                res.append(size)
                size = 0

        return res
