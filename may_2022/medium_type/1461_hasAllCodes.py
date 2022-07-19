class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binary_codes = set()
        for i in range(len(s) - k + 1):
            binary_codes.add(s[i:i + k])

        return len(binary_codes) == 2 ** k
