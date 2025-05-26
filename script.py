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
# Iterative Implementation (Using Queue)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()  # FIFO
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

# print("\nBFS Iterative:")
# bfs(graph, 'A')
# --------------------------------------------------------------- #



# DFS Traversal
# Iterative Implementation (Using Stack)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()  # LIFO
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # add neighbors in reversed order
            stack.extend(reversed(graph[node]))  

# print("\nDFS Iterative:")
# dfs_iterative(graph, 'A')
# --------------------------------------------------------------- #


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





