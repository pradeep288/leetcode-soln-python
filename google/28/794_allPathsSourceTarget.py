class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        q = [[0]]
        target = len(graph) - 1

        while q:
            temp = q.pop(0)
            if temp[-1] == target:
                result.append(temp)

            for neighbour in graph[temp[-1]]:
                q.append(temp+[neighbour])

        return result
