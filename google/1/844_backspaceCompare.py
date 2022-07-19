class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_string(inp):
            stack = []
            for i in range(len(inp)):
                if stack and inp[i] == "#":
                    stack.pop()
                elif inp[i] == "#":
                    continue
                else:
                    stack.append(inp[i])
            return "".join(stack)

        print(get_string(s))
        print(get_string(t))
        return get_string(s) == get_string(t)
