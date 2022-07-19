import collections


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build Graph
        graph = {}

        def build_graph(equations, values):
            def add_edge(f, t, v):
                if f in graph:
                    graph[f].append((t, v))
                else:
                    graph[f] = [(t, v)]

            for vertices, value in zip(equations, values):
                f, t = vertices
                add_edge(f, t, value)
                add_edge(t, f, 1 / value)

        # Run BFS
        def find_path(query):
            b, e = query

            if b not in graph or e not in graph:
                return -1.0

            q = collections.deque([(b, 1.0)])
            visited = set()

            while q:
                front, cur_product = q.popleft()
                if front == e:
                    return cur_product
                visited.add(front)
                for neigh, v in graph[front]:
                    if neigh not in visited:
                        q.append((neigh, cur_product * v))

            return -1.0

        build_graph(equations, values)
        return [find_path(q) for q in queries]
