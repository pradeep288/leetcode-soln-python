class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] != 0:
                continue
            q = [i]
            color[i] = 1
            while q:
                node = q.pop()
                for n in graph[node]:
                    if color[n] == color[node]:
                        return False
                    elif color[n] == 0:
                        color[n] = -color[node]
                        q.append(n)

        return True
