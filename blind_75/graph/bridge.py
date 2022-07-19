def dfs(node, parent, visited, time_insertion, lowest_insertion_time_of_adj_node, adj, timer):
    visited.add(node)
    time_insertion[node] = lowest_insertion_time_of_adj_node[node] = timer
    timer += 1

    for n in adj[node]:
        if n == parent:
            continue
        if n not in visited:
            dfs(n, node, visited, time_insertion, lowest_insertion_time_of_adj_node, adj, timer)
            lowest_insertion_time_of_adj_node[node] = min(lowest_insertion_time_of_adj_node[n],
                                                          lowest_insertion_time_of_adj_node[node])

            if lowest_insertion_time_of_adj_node[n] > time_insertion[node]:
                print("bridge")
        else:
            lowest_insertion_time_of_adj_node[node] = min(lowest_insertion_time_of_adj_node[n],
                                                          lowest_insertion_time_of_adj_node[node])


def print_bridges(adj, n):
    visited = set()
    time_insertion = [float('inf')] * n
    low_time = [float('inf')] * n

    timer = 0

    for i in range(n):
        if n not in visited:
            dfs(i, -1, visited, time_insertion, low_time, adj, timer)
