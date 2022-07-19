import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        N = len(s)
        parent = list(range(N))

        def find(a):
            if parent[a] != a:
                find(parent[a])
            return parent[a]

        def union(a1, b1):
            parent[find(b1)] = find(a1)

        for a, b in pairs:
            union(a, b)

        group_i = collections.defaultdict(list)
        group_c = collections.defaultdict(list)
        res = [""]*N
        for i in range(N):
            group = find(i)
            group_i[group].append(i)
            group_c[group].append(s[i])

        for g in group_i.keys():
            idx = sorted(group_i[g])
            chrs = sorted(group_c[g])

            for i, c in zip(idx, chrs):
                res[i]=c

        return "".join(res)


