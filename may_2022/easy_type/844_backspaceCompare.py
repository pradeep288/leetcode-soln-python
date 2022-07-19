class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_stack(st):
            temp = []
            for c in st:
                if c != "#":
                    temp.append(c)
                else:
                    if len(temp) == 0:
                        continue
                    else:
                        temp.pop()
            return temp

        return build_stack(s) == build_stack(t)
