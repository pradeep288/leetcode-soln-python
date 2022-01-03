class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        if len(trust) == 0:
            return -1

        persons = []
        for i in range(n + 1):
            persons.append({"id": i, "trusted_by": 0, "trusts": 0})

        for i, v in enumerate(trust):
            persons[v[0]]["trusts"] += 1
            persons[v[1]]["trusted_by"] += 1

        for p in persons:
            if p["trusts"] == 0 and p["trusted_by"] == n - 1:
                return p["id"]

        return -1
