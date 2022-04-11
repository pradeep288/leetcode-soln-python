class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        def create_hashmap(arr):
            d = {}
            for val in arr:
                if val in d.keys():
                    d[val] += 1
                else:
                    d[val] = 1
            return d

        cur, expected = create_hashmap(s[:len(p)]), create_hashmap(p)
        res = []

        prev = ""
        for i in range(len(s)-len(p)+1):
            if i == 0:
                pass
            else:
                if cur[prev] >= 2:
                    cur[prev] -= 1
                else:
                    del cur[prev]

                if s[i + len(p)] in cur.keys():
                    cur[s[i + len(p)]] = 1
                else:
                    cur[s[i + len(p)]] += 1
            prev = s[i]
            if cur == expected:
                res.append(i)


        return res
