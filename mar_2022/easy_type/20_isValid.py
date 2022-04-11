class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        hash_map = {"}": "{",
                    ")": "(",
                    "]": "["}
        stack = []
        for c in s:
            if c in ["{", "(", "["]:
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == hash_map[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0
