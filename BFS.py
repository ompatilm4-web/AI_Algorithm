from collections import deque

def bfs(graph, start):
    visited = set()  
    queue = deque([start])

    visited.add(start)


    while queue:
        node = queue.popleft()
        print(node,end=' ')


        #visit all the adjecent nodes
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print ("BFS starting from node A:")
bfs(graph, 'A')