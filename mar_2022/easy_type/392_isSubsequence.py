class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = len(s)
        for i in s:
            for j in t:
                if i == j:
                    count -= 1
                    break

        return count == 0