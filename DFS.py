# DFS Function 
def DFS(graph, node, visited=None):
    if visited is None:
        visited = set()   # initialize visited set

    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in graph[node]:
            DFS(graph, neighbor, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS starting from node A:")
DFS(graph, 'A')