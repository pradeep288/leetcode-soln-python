"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = ''.join(sorted(s1))
        i = 0
        while i <= len(s2) - len(s1):
            cur_sub_str = ''.join(sorted(s2[i:i + len(s1)]))
            if cur_sub_str == s1:
                return True
            i += 1

        return False
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1 = Counter(s1)
        i = 0
        while i <= len(s2) - len(s1):
            c2 = Counter(s2[i:i + len(s1)])
            if c1 == c2:
                return True
            i += 1

        return False
