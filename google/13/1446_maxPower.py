class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        temp = 1
        for i in range(1, len(s)+1):
            if s[i - 1] == s[i]:
                temp += 1
            else:
                max_len = max(max_len, temp)
                temp =1

        return max_len
