import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import heapq
from collections import deque, defaultdict

"""
=============================================================================
🕸️ DSA TOPIC 06: GRAPHS (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 06_Graphs_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 06_Graphs_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Graph Representation & Breadth-First Search (BFS Shortest Path)
# Graphs represented via Adjacency Lists. BFS finds the shortest path in unweighted graphs in $O(V + E)$ time.

# %% [code]
def cell_1():
    """Cell 1: Adjacency List & BFS Shortest Path"""
    print("=" * 60)
    print("▶ CELL 1: Adjacency List Graph & BFS Shortest Path")
    print("=" * 60)

    class Graph:
        def __init__(self):
            self.adj = defaultdict(list)

        def add_edge(self, u, v, directed=False):
            self.adj[u].append(v)
            if not directed:
                self.adj[v].append(u)

        def bfs_shortest_path(self, start, target):
            queue = deque([(start, [start])])
            visited = {start}

            while queue:
                node, path = queue.popleft()
                if node == target:
                    return path

                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, path + [neighbor]))
            return None

    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "F")
    g.add_edge("E", "F")

    path = g.bfs_shortest_path("A", "F")
    print("Adjacency List:")
    for k, v in g.adj.items():
        print(f"  {k} -> {v}")
    print(f"\nShortest Path from A to F: {' -> '.join(path)}")


# %% [markdown]
# ### 📌 Cell 2: Depth-First Search (DFS) & Cycle Detection
# Using 3-color node states (0 = Unvisited, 1 = Visiting in current path, 2 = Completely Visited) to detect cycles in directed graphs.

# %% [code]
def cell_2():
    """Cell 2: DFS Cycle Detection in Directed Graph"""
    print("=" * 60)
    print("▶ CELL 2: DFS Cycle Detection (3-Color State Machine)")
    print("=" * 60)

    def has_cycle_directed(num_nodes: int, edges: list) -> bool:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        # 0: unvisited, 1: visiting (in current recursion stack), 2: visited
        state = [0] * num_nodes

        def dfs(node):
            state[node] = 1  # Mark as currently visiting
            for neighbor in adj[node]:
                if state[neighbor] == 1:
                    return True  # Found back-edge -> Cycle detected!
                if state[neighbor] == 0:
                    if dfs(neighbor):
                        return True
            state[node] = 2  # Mark as fully explored
            return False

        for i in range(num_nodes):
            if state[i] == 0:
                if dfs(i):
                    return True
        return False

    # Graph 1: 0 -> 1 -> 2 -> 0 (Cycle)
    edges1 = [[0, 1], [1, 2], [2, 0]]
    # Graph 2: 0 -> 1 -> 2 (DAG, No Cycle)
    edges2 = [[0, 1], [1, 2]]

    print(f"Graph 1 (0->1->2->0) has cycle? -> {has_cycle_directed(3, edges1)}")
    print(f"Graph 2 (0->1->2) has cycle?    -> {has_cycle_directed(3, edges2)}")


# %% [markdown]
# ### 📌 Cell 3: Dijkstra's Shortest Path Algorithm (Min-Heap Priority Queue)
# Finding single-source shortest paths on non-negative weighted graphs in $O((V + E) \log V)$ time.

# %% [code]
def cell_3():
    """Cell 3: Dijkstra's Algorithm"""
    print("=" * 60)
    print("▶ CELL 3: Dijkstra's Shortest Path with Min-Heap")
    print("=" * 60)

    def dijkstra(num_nodes: int, edges: list, start_node: int) -> dict:
        adj = defaultdict(list)
        for u, v, weight in edges:
            adj[u].append((v, weight))
            adj[v].append((u, weight))

        distances = {i: float('inf') for i in range(num_nodes)}
        distances[start_node] = 0
        min_heap = [(0, start_node)]  # (cost, node)

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)
            if current_dist > distances[u]:
                continue

            for v, weight in adj[u]:
                dist = current_dist + weight
                if dist < distances[v]:
                    distances[v] = dist
                    heapq.heappush(min_heap, (dist, v))

        return distances

    # Weighted edges: [u, v, weight]
    weighted_edges = [
        (0, 1, 4), (0, 2, 2),
        (1, 2, 1), (1, 3, 5),
        (2, 3, 8), (2, 4, 10),
        (3, 4, 2)
    ]
    num_nodes = 5
    start = 0
    shortest_paths = dijkstra(num_nodes, weighted_edges, start)
    print(f"Shortest Distances from Node {start}:")
    for node, dist in shortest_paths.items():
        print(f"  To Node {node}: Distance = {dist}")


# %% [markdown]
# ### 📌 Cell 4: Topological Sort (Kahn's In-Degree BFS Algorithm)
# Linearly ordering Directed Acyclic Graphs (DAG) vertices according to dependencies (e.g. Course Schedule).

# %% [code]
def cell_4():
    """Cell 4: Topological Sort (Kahn's Algorithm)"""
    print("=" * 60)
    print("▶ CELL 4: Topological Sort (Kahn's In-Degree Algorithm)")
    print("=" * 60)

    def topological_sort(num_courses: int, prerequisites: list) -> list:
        adj = defaultdict(list)
        in_degree = [0] * num_courses

        for dest, src in prerequisites:
            adj[src].append(dest)
            in_degree[dest] += 1

        # Queue nodes with 0 incoming dependencies
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == num_courses else []

    # Course dependencies: [Course, Prerequisite]
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    num_courses = 4
    course_order = topological_sort(num_courses, prereqs)
    print(f"Course Prerequisites: {prereqs}")
    print(f"Valid Learning Order: {course_order}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Adjacency List & BFS Shortest Path", cell_1),
    2: ("DFS Cycle Detection in Directed Graphs", cell_2),
    3: ("Dijkstra's Algorithm (Min-Heap Shortest Path)", cell_3),
    4: ("Topological Sort (Kahn's In-Degree Algorithm)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 06_GRAPHS_INTERACTIVE.PY")
    print("#" * 70 + "\n")
    for num in sorted(CELLS.keys()):
        CELLS[num][1]()
        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip()
        if arg in ["--all", "all", "0"]:
            run_all()
        else:
            try:
                cell_no = int(arg)
                if cell_no in CELLS:
                    CELLS[cell_no][1]()
                else:
                    print(f"❌ Invalid Cell {cell_no}. Choose from: {list(CELLS.keys())}")
            except ValueError:
                print("Usage: python 06_Graphs_interactive.py [cell_number | --all]")
    else:
        run_all()
