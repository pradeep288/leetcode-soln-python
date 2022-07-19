class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        i = 0
        tmp = sorted(p)
        res = []
        while i < len(s) - len(p):
            if sorted(s[i:len(p)]) == tmp:
                res.append(i)
            i += 1
        return res
