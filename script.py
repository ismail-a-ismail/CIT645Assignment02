import heapq
from collections import deque



# Adjacency List Representation
graph = {
    'A': ['B'],
    'B': ['C', 'D'],
    'C': ['E', 'F'],
    'D': ['E', 'F'],
    'E': [],
    'F': ['D','E']
}


# BFS Traversal
def bfs(graph, start):
    
    visited = {start}
    queue = deque([start])
    order = [start]
    tree_edges = []
    
    while queue:
        vertex = queue.popleft()
        
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                order.append(neighbor)
                tree_edges.append((vertex, neighbor))
    
    return order, tree_edges

bfs_order, bfs_tree = bfs(graph, 'A')
# print("BFS Order:", bfs_order)
# print("BFS Tree Edges:", bfs_tree)



# DFS Traversal
def dfs(graph, start):
    visited = set()
    order = []
    tree_edges = []
    
    def _dfs(vertex):
        nonlocal order
        visited.add(vertex)
        order.append(vertex)
        
        for neighbor in sorted(graph[vertex]):
            if neighbor not in visited:
                tree_edges.append((vertex, neighbor))
                _dfs(neighbor)
    
    _dfs(start)
    return order, tree_edges

dfs_order, dfs_tree = dfs(graph, 'A')
# print("DFS Order:", dfs_order)
# print("DFS Tree Edges:", dfs_tree)



def prim(graph, start):
    
    mst = []
    visited = {start}
    
    edges = [
        (1, start, neighbor) 
        for neighbor in graph[start]
    ]
    
    heapq.heapify(edges)
    total_weight = 0
    
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v))
            total_weight += weight
            for neighbor in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (1, v, neighbor))
    
    return mst, total_weight

mst_edges, mst_weight = prim(graph, 'A')
# print("MST Edges:", mst_edges)
# print("Total Weight:", mst_weight)



def dijkstra(graph, start):
    
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    heap = [(0, start)]
    path_tree = {start: None}
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if current_dist > distances[u]:
            continue
            
        for v in graph[u]:
            distance = current_dist + 1  # all edges have weight 1
            if distance < distances[v]:
                distances[v] = distance
                path_tree[v] = u
                heapq.heappush(heap, (distance, v))
    
    return distances, path_tree

distances, path_tree = dijkstra(graph, 'A')
# print("Shortest Distances:", distances)
# print("Shortest Path Tree:", path_tree)





