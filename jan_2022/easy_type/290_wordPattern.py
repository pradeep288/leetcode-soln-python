class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_w, w_to_p = {}, {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        for k, v in enumerate(pattern):
            if v not in p_to_w.keys():
                p_to_w[v] = words[k]
            elif p_to_w[v] != words[k]:
                return False

            if words[k] not in w_to_p.keys():
                w_to_p[words[k]] = v
            elif w_to_p[words[k]] != v:
                return False

        return True
