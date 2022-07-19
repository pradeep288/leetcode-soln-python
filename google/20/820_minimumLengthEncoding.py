class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words.sort(key=len, reverse=True)
        res = ""

        for w in words:
            if w + "#" not in res:
                res += w + "#"

        return len(res)
