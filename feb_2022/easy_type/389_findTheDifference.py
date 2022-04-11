class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = ''.join(sorted(s)), ''.join(sorted(t))

        for i in range(len(t) - 1):
            if s[i] != t[i]:
                return t[i]

        return t[-1]
