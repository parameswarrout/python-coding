# 06 - Graphs: Modeling Relationships

## Table of Contents
1. [Introduction](#introduction)
2. [Graph Terminology](#graph-terminology)
3. [Types of Graphs](#types-of-graphs)
4. [Graph Representations](#graph-representations)
5. [Python Implementation](#python-implementation)
6. [Graph Traversals](#graph-traversals)
7. [Common Algorithms](#common-algorithms)
8. [Time and Space Complexity](#time-and-space-complexity)
9. [Applications and Use Cases](#applications-and-use-cases)
10. [Problem-Solving Patterns](#problem-solving-patterns)
11. [Advanced Graph Concepts](#advanced-graph-concepts)
12. [Practice Problems](#practice-problems)
13. [Summary](#summary)

## Introduction

Graphs are mathematical structures used to model pairwise relationships between objects. They consist of vertices (nodes) connected by edges (relationships). Graphs are incredibly versatile and can represent social networks, road networks, computer networks, and many other real-world systems.

Think of a graph as a social network where people are represented as nodes and friendships as connections between them. Unlike trees, graphs can have cycles and don't necessarily have a hierarchical structure.

## Graph Terminology

### Basic Terms:
- **Vertex/Node**: Individual element in the graph
- **Edge**: Connection between two vertices
- **Adjacent Vertices**: Vertices connected by an edge
- **Degree**: Number of edges incident to a vertex
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at the same vertex
- **Connected Graph**: Every vertex reachable from every other vertex
- **Complete Graph**: Every vertex connected to every other vertex
- **Weighted Graph**: Edges have associated weights/costs
- **Directed Graph (Digraph)**: Edges have direction
- **Undirected Graph**: Edges have no direction

## Types of Graphs

### 1. Directed vs Undirected
- **Undirected**: Edges have no direction (friendship)
- **Directed**: Edges have direction (following someone)

### 2. Weighted vs Unweighted
- **Unweighted**: All edges have equal importance
- **Weighted**: Edges have associated costs/values

### 3. Cyclic vs Acyclic
- **Cyclic**: Contains at least one cycle
- **Acyclic**: Contains no cycles (DAG - Directed Acyclic Graph)

## Graph Representations

### 1. Adjacency Matrix
2D array where matrix[i][j] represents edge between vertex i and j.

**Pros**: O(1) edge lookup, easy to implement
**Cons**: O(V²) space, slow for sparse graphs

### 2. Adjacency List
Array of lists where each list contains adjacent vertices.

**Pros**: Space efficient for sparse graphs, O(degree) neighbor access
**Cons**: O(V) worst-case edge lookup

### 3. Edge List
List of all edges in the graph.

**Pros**: Simple representation, good for certain algorithms
**Cons**: Slow neighbor and edge queries

## Python Implementation

### Graph Class with Adjacency List

```python
from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight=None):
        """Add edge between vertices u and v"""
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)
    
    def add_vertex(self, v):
        """Add vertex to graph"""
        if v not in self.graph:
            self.graph[v] = []
    
    def remove_edge(self, u, v):
        """Remove edge between u and v"""
        if v in self.graph[u]:
            self.graph[u].remove(v)
        if not self.directed and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def get_neighbors(self, v):
        """Get neighbors of vertex v"""
        return self.graph[v]
    
    def vertices(self):
        """Get all vertices"""
        return list(self.graph.keys())
    
    def edges(self):
        """Get all edges"""
        edges = []
        for u in self.graph:
            for v in self.graph[u]:
                edges.append((u, v))
        return edges
    
    def display(self):
        """Display graph"""
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
```

### Weighted Graph Implementation

```python
class WeightedGraph:
    def __init__(self, directed=False):
        self.graph = defaultdict(list)
        self.directed = directed
    
    def add_edge(self, u, v, weight):
        """Add weighted edge between u and v"""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))
    
    def get_neighbors_with_weights(self, v):
        """Get neighbors with their weights"""
        return self.graph[v]
    
    def get_weight(self, u, v):
        """Get weight of edge u-v"""
        for neighbor, weight in self.graph[u]:
            if neighbor == v:
                return weight
        return None
```

## Graph Traversals

### 1. Breadth-First Search (BFS)

```python
def bfs(graph, start):
    """BFS traversal starting from start vertex"""
    visited = set()
    queue = deque([start])
    result = []
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add unvisited neighbors to queue
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

def bfs_shortest_path(graph, start, end):
    """Find shortest path using BFS"""
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])  # (vertex, path to vertex)
    
    while queue:
        vertex, path = queue.popleft()
        if vertex in visited:
            continue
        
        visited.add(vertex)
        
        for neighbor in graph.get_neighbors(vertex):
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return []  # No path found
```

### 2. Depth-First Search (DFS)

```python
def dfs_recursive(graph, start, visited=None, result=None):
    """Recursive DFS traversal"""
    if visited is None:
        visited = set()
    if result is None:
        result = []
    
    visited.add(start)
    result.append(start)
    
    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited, result)
    
    return result

def dfs_iterative(graph, start):
    """Iterative DFS using stack"""
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors in reverse order to maintain left-to-right traversal
            for neighbor in reversed(graph.get_neighbors(vertex)):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result
```

## Common Algorithms

### 1. Detect Cycle in Undirected Graph

```python
def has_cycle_undirected(graph):
    """Detect cycle in undirected graph using DFS"""
    visited = set()
    
    for vertex in graph.vertices():
        if vertex not in visited:
            if _has_cycle_dfs(graph, vertex, visited, -1):
                return True
    return False

def _has_cycle_dfs(graph, vertex, visited, parent):
    visited.add(vertex)
    
    for neighbor in graph.get_neighbors(vertex):
        if neighbor not in visited:
            if _has_cycle_dfs(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            # Back edge found - cycle detected
            return True
    
    return False
```

### 2. Detect Cycle in Directed Graph

```python
def has_cycle_directed(graph):
    """Detect cycle in directed graph using DFS"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {vertex: WHITE for vertex in graph.vertices()}
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Back edge found
        if color[node] == BLACK:
            return False
        
        color[node] = GRAY
        for neighbor in graph.get_neighbors(node):
            if dfs(neighbor):
                return True
        
        color[node] = BLACK
        return False
    
    for vertex in graph.vertices():
        if color[vertex] == WHITE:
            if dfs(vertex):
                return True
    
    return False
```

### 3. Topological Sort (for DAGs)

```python
def topological_sort(graph):
    """Topological sort using DFS"""
    visited = set()
    stack = []
    
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(vertex)
    
    for vertex in graph.vertices():
        if vertex not in visited:
            dfs(vertex)
    
    return stack[::-1]  # Reverse the stack

def topological_sort_kahn(graph):
    """Topological sort using Kahn's algorithm"""
    # Calculate in-degrees
    in_degree = {v: 0 for v in graph.vertices()}
    for u in graph.vertices():
        for v in graph.get_neighbors(u):
            in_degree[v] += 1
    
    # Find vertices with in-degree 0
    queue = deque([v for v in graph.vertices() if in_degree[v] == 0])
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Decrease in-degree of neighbors
        for neighbor in graph.get_neighbors(vertex):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all vertices were processed (no cycle)
    if len(result) != len(graph.vertices()):
        return []  # Graph has a cycle
    
    return result
```

## Time and Space Complexity

### Graph Representation Complexity

| Representation | Space | Add Edge | Remove Edge | Query Edge | Neighbors |
|----------------|-------|----------|-------------|------------|-----------|
| Adjacency Matrix | O(V²) | O(1) | O(1) | O(1) | O(V) |
| Adjacency List | O(V+E) | O(1) | O(E) | O(degree) | O(degree) |

### Traversal Complexity
- **BFS/DFS**: O(V + E) time, O(V) space
- **Shortest Path (BFS)**: O(V + E) time, O(V) space
- **Topological Sort**: O(V + E) time, O(V) space

## Applications and Use Cases

### 1. Social Networks
Modeling relationships between people

### 2. Computer Networks
Routing protocols, network topology

### 3. Transportation Networks
Flight routes, road networks

### 4. Web Crawling
Modeling web pages and links

### 5. Dependency Management
Package managers, course prerequisites

## Problem-Solving Patterns

### 1. Islands Count (Connected Components)

```python
def count_islands(grid):
    """Count number of islands in 2D grid"""
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    count = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            visited[r][c] or grid[r][c] == '0'):
            return
        
        visited[r][c] = True
        for dr, dc in directions:
            dfs(r + dr, c + dc)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1
    
    return count
```

### 2. Course Schedule (Topological Sort)

```python
def can_finish_courses(num_courses, prerequisites):
    """Can finish all courses given prerequisites?"""
    # Build graph
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Kahn's algorithm
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses
```

### 3. Shortest Path in Binary Matrix

```python
def shortest_path_binary_matrix(grid):
    """Find shortest path in binary matrix"""
    if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    
    n = len(grid)
    if n == 1:
        return 1
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = set()
    visited.add((0, 0))
    
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    while queue:
        row, col, dist = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (new_row < 0 or new_row >= n or 
                new_col < 0 or new_col >= n or 
                grid[new_row][new_col] == 1 or 
                (new_row, new_col) in visited):
                continue
            
            if new_row == n - 1 and new_col == n - 1:
                return dist + 1
            
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, dist + 1))
    
    return -1
```

## Advanced Graph Concepts

### 1. Dijkstra's Algorithm (Single Source Shortest Path)

```python
import heapq

def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest paths"""
    distances = {vertex: float('infinity') for vertex in graph.vertices()}
    distances[start] = 0
    pq = [(0, start)]  # (distance, vertex)
    visited = set()
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph.get_neighbors_with_weights(current_vertex):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
```

### 2. Union-Find (Disjoint Set Union)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        """Find root with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union with union by rank"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    
    def connected(self, x, y):
        """Check if x and y are connected"""
        return self.find(x) == self.find(y)
```

### 3. Minimum Spanning Tree (Kruskal's Algorithm)

```python
def kruskal(vertices, edges):
    """Kruskal's algorithm for MST"""
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(vertices)
    mst = []
    
    for u, v, weight in edges:
        if not uf.connected(u, v):
            uf.union(u, v)
            mst.append((u, v, weight))
            if len(mst) == vertices - 1:
                break
    
    return mst
```

## Practice Problems

### Beginner Level
1. **Number of Islands**: Count connected components in 2D grid
2. **Valid Path**: Check if path exists between two nodes
3. **Graph Valid Tree**: Check if graph is a valid tree

### Intermediate Level
1. **Course Schedule**: Topological sort with cycle detection
2. **Clone Graph**: Deep copy of graph
3. **Pacific Atlantic Water Flow**: Multi-source BFS

### Advanced Level
1. **Network Delay Time**: Dijkstra's algorithm
2. **Redundant Connection**: Union-Find
3. **Critical Connections**: Tarjan's algorithm for bridges

## Summary

Graphs are powerful structures for modeling relationships:

1. **Representation**: Adjacency list/matrix based on graph density
2. **Traversal**: BFS for shortest path, DFS for exploration
3. **Algorithms**: Topological sort, cycle detection, shortest paths
4. **Applications**: Networks, dependencies, routing
5. **Advanced**: Minimum spanning trees, strongly connected components

Graphs provide the foundation for solving complex real-world problems involving relationships and connections. The next topic will cover Sorting Algorithms, which are essential for organizing data efficiently.