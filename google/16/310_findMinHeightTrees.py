class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        neighbours = [set() for i in range(n)]
        for start, end in edges:
            neighbours[start].add(end)
            neighbours[end].add(start)

        leaves = []
        for i in range(n):
            if len(neighbours[i]) == 1:
                leaves.append(i)

        reamining_nodes = n
        while reamining_nodes > 2:
            reamining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = neighbours[leaf].pop()
                neighbours[neighbor].remove(leaf)
                if len(neighbours[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves
