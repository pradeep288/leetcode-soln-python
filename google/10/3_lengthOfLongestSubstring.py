class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = float('-inf')
        for idx, _ in enumerate(s):
            visited = set()
            cur_idx = idx
            cur_len = 0
            while cur_idx < len(s) and s[cur_idx] not in visited:
                visited.add(s[cur_idx])
                cur_idx += 1
                cur_len += 1
            max_len = max(max_len, cur_len)

        return max_len
