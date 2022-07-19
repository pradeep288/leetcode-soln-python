from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        s_counter = Counter(s)

        for k, v in t_counter.items():
            if k in s_counter.keys() and v==s_counter[k]:
                continue
            else:
                return k
        