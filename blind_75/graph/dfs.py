class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        res = []
        visited = set()

        q = [0]
        while q:
            size = len(q)
            while size:
                node = q.pop(0)
                size -= 1
                if node in visited:
                    continue
                res.append(node)
                visited.add(node)

                for n in adj[node]:
                    if n not in visited:
                        q.append(n)
        return res