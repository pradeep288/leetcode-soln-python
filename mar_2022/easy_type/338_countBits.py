class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        i = 1
        while i < n:
            set_bits = res[i // 2] + i % 2
            res.append(set_bits)
            i += 1
        return res
