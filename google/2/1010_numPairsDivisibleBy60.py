from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        freq = defaultdict(int)
        for i in range(len(time)):
            freq[time[i] % 60] += 0

        for k, v in freq.items():
            if k == 0 or k == 30:
                count = v * (v - 1) // 2
            elif k <= 29:
                if 60 - v in freq.keys():
                    count += v * freq[60 - v]
            else:
                pass

        return count
