class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c not in stack:
                while stack and c < stack[-1] and d[stack[-1]] > i:
                    stack.pop()
                stack.append(c)

        return "".join(stack)