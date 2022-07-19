class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        col = [-1] * N

        for i in range(N):
            if col[i] != -1:
                continue
            q = [(i, 0)]
            while len(q) > 0:
                size = len(q)
                while size > 0:
                    cur_node, color = q.pop(0)
                    size -= 1
                    if col[cur_node] == -1:
                        for n in graph[cur_node]:
                            q.append((n, color ^ 1))
                        col[cur_node]=color
                    if col[cur_node] != color:
                        return False
        return True
