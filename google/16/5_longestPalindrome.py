class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0

        def expand_boundary(left, right):
            if left > right:
                return 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return right-left-1

        if s == "":
            return 0

        if len(s) == 1:
            return 1
        start, end = 0, 0
        for i in range(len(s)):
            left = expand_boundary(i, i)
            right = expand_boundary(i, i + 1)
            max_len = max(left, right)
            if max_len > end - start:
                start = i - ((max_len-1) // 2)
                end = i + (max_len // 2)

        return s[start:end+1]
