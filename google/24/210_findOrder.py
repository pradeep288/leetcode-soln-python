import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        in_degree = [0] * numCourses

        for nodes in adj:
            for n in adj[nodes]:
                in_degree[n] += 1

        q = []
        for i in in_degree:
            if in_degree[i] == 0:
                q.append(i)

        topo_sort = []

        while len(q) > 0:
            size = len(q)
            while size > 0:
                node = q.pop(0)
                size -= 1
                topo_sort.append(node)
                for n in adj[node]:
                    in_degree[n] -= 1
                    if in_degree[n] == 0:
                        q.append(n)

        return topo_sort
