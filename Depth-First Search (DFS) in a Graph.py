def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example usage
graph = {'A': ['B', 'C'],
         'B': ['A', 'D'],
         'C': ['A', 'E'],
         'D': ['B'],
         'E': ['C']}
visited_nodes = set()
dfs(graph, 'A', visited_nodes)
