# 10 - Greedy Algorithms: Making Locally Optimal Choices

## Table of Contents
1. [Introduction](#introduction)
2. [Greedy Algorithm Fundamentals](#greedy-algorithm-fundamentals)
3. [When to Use Greedy](#when-to-use-greedy)
4. [Python Implementation](#python-implementation)
5. [Classic Greedy Problems](#classic-greedy-problems)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Applications and Use Cases](#applications-and-use-cases)
8. [Greedy vs Dynamic Programming](#greedy-vs-dynamic-programming)
9. [Problem-Solving Patterns](#problem-solving-patterns)
10. [Advanced Greedy Concepts](#advanced-greedy-concepts)
11. [Practice Problems](#practice-problems)
12. [Summary](#summary)

## Introduction

Greedy algorithms make the locally optimal choice at each stage with the hope of finding a global optimum. Unlike Dynamic Programming, which explores all possibilities, greedy algorithms make decisions that seem best at the moment without reconsidering previous choices.

Think of a greedy algorithm like a hiker always moving toward the highest visible peak, hoping it leads to the tallest mountain. Sometimes this works perfectly, but other times it leads to a local maximum rather than the global maximum.

## Greedy Algorithm Fundamentals

### What is a Greedy Algorithm?

A greedy algorithm follows the problem-solving heuristic of making the locally optimal choice at each stage. For some problems, this approach leads to the global optimum, while for others, it provides a good approximation.

### Key Characteristics:
1. **Greedy Choice Property**: Local optimal choices lead to global optimal solution
2. **Optimal Substructure**: Optimal solution contains optimal solutions to subproblems
3. **Irrevocable Decisions**: Once a choice is made, it's never reconsidered

### General Structure:
```
1. Initialize solution set
2. While not complete:
   a. Make greedy choice
   b. Add to solution set
   c. Update constraints
3. Return solution
```

## When to Use Greedy

### Suitable Problems:
- **Activity Selection**: Select maximum number of non-overlapping activities
- **Fractional Knapsack**: Items can be divided
- **Huffman Coding**: Optimal prefix-free codes
- **Minimum Spanning Tree**: Kruskal's and Prim's algorithms
- **Shortest Path**: Dijkstra's algorithm (non-negative weights)

### When NOT to Use:
- **0/1 Knapsack**: Greedy doesn't guarantee optimal
- **Longest Path**: Greedy fails
- **Most DP problems**: Require exploring all possibilities

## Python Implementation

### 1. Activity Selection Problem

```python
def activity_selection(start_times, end_times):
    """Select maximum number of non-overlapping activities"""
    # Create list of (start, end, index) tuples
    activities = [(start_times[i], end_times[i], i) for i in range(len(start_times))]
    
    # Sort by end time (greedy choice: finish earliest)
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_end_time = float('-inf')
    
    for start, end, index in activities:
        if start >= last_end_time:  # No overlap
            selected.append(index)
            last_end_time = end
    
    return selected

# Example usage
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
result = activity_selection(start, end)
print(f"Selected activities: {result}")  # [0, 1, 3, 4]
```

### 2. Fractional Knapsack Problem

```python
def fractional_knapsack(weights, values, capacity):
    """Fractional knapsack - items can be divided"""
    # Calculate value-to-weight ratio
    items = [(values[i]/weights[i], weights[i], values[i], i) 
             for i in range(len(weights))]
    
    # Sort by value-to-weight ratio in descending order
    items.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for ratio, weight, value, index in items:
        if remaining_capacity >= weight:
            # Take whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break  # Knapsack is full
    
    return total_value

# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
result = fractional_knapsack(weights, values, capacity)
print(f"Maximum value: {result}")  # 240.0
```

### 3. Job Sequencing Problem

```python
def job_sequencing_deadlines(profits, deadlines):
    """Schedule jobs to maximize profit with deadlines"""
    n = len(profits)
    
    # Create list of (profit, deadline, job_id) tuples
    jobs = [(profits[i], deadlines[i], i) for i in range(n)]
    
    # Sort by profit in descending order (greedy: take most profitable first)
    jobs.sort(reverse=True)
    
    # Find maximum deadline to create time slots
    max_deadline = max(deadlines)
    
    # Initialize time slots (False means free)
    time_slots = [False] * (max_deadline + 1)
    scheduled_jobs = []
    total_profit = 0
    
    for profit, deadline, job_id in jobs:
        # Find a free slot before deadline (starting from deadline)
        for slot in range(min(deadline, max_deadline), 0, -1):
            if not time_slots[slot]:
                time_slots[slot] = True
                scheduled_jobs.append(job_id)
                total_profit += profit
                break
    
    return scheduled_jobs, total_profit

# Example usage
profits = [35, 30, 25, 20, 15, 12, 5]
deadlines = [3, 4, 4, 2, 3, 1, 2]
jobs, profit = job_sequencing_deadlines(profits, deadlines)
print(f"Scheduled jobs: {jobs}, Total profit: {profit}")
```

## Classic Greedy Problems

### 1. Huffman Coding

```python
import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(text):
    """Generate Huffman codes for text"""
    # Count frequency of each character
    freq = Counter(text)
    
    # Create priority queue with leaf nodes
    heap = [Node(char, frequency) for char, frequency in freq.items()]
    heapq.heapify(heap)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)
    
    # Root of the tree
    root = heap[0] if heap else None
    
    # Generate codes
    codes = {}
    def generate_codes(node, code=""):
        if node:
            if node.char is not None:  # Leaf node
                codes[node.char] = code or "0"  # Handle single character case
            else:
                generate_codes(node.left, code + "0")
                generate_codes(node.right, code + "1")
    
    generate_codes(root)
    return codes

# Example usage
text = "hello world"
codes = huffman_coding(text)
print("Huffman Codes:", codes)
```

### 2. Minimum Platforms Required

```python
def min_platforms(arrivals, departures):
    """Minimum platforms required for train schedule"""
    # Sort arrival and departure times
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 1
    max_platforms = 1
    i = 1  # Arrival index
    j = 0  # Departure index
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            # New train arrives before previous departs
            platforms_needed += 1
            i += 1
        else:
            # Train departs, free up platform
            platforms_needed -= 1
            j += 1
        
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms

# Example usage
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
result = min_platforms(arrivals, departures)
print(f"Minimum platforms required: {result}")
```

### 3. Gas Station Problem

```python
def can_complete_circuit(gas, cost):
    """Find starting gas station to complete circuit"""
    n = len(gas)
    
    # Check if total gas is sufficient
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    tank = 0
    
    for i in range(n):
        tank += gas[i] - cost[i]
        
        # If we can't reach next station, start from next station
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
result = can_complete_circuit(gas, cost)
print(f"Starting station: {result}")
```

## Time and Space Complexity

### Common Greedy Complexities

| Problem | Time Complexity | Space Complexity | Notes |
|---------|----------------|------------------|-------|
| Activity Selection | O(n log n) | O(1) | Due to sorting |
| Fractional Knapsack | O(n log n) | O(1) | Due to sorting |
| Job Sequencing | O(n²) | O(n) | Due to time slot checking |
| Huffman Coding | O(n log n) | O(n) | n = unique characters |
| Minimum Platforms | O(n log n) | O(1) | Due to sorting |
| Dijkstra's Algorithm | O((V+E) log V) | O(V) | V = vertices, E = edges |

## Applications and Use Cases

### 1. Network Design
```python
def minimum_spanning_tree_kruskal(n, edges):
    """Kruskal's algorithm for MST using Union-Find"""
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            return True
    
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break
    
    return mst_weight, mst_edges
```

### 2. Scheduling
```python
def minimize_maximum_lateness(jobs):
    """Minimize maximum lateness - schedule jobs by deadline"""
    # jobs = [(duration, deadline), ...]
    jobs.sort(key=lambda x: x[1])  # Sort by deadline
    
    current_time = 0
    max_lateness = 0
    
    for duration, deadline in jobs:
        current_time += duration
        lateness = max(0, current_time - deadline)
        max_lateness = max(max_lateness, lateness)
    
    return max_lateness
```

### 3. Load Balancing
```python
def minimize_load(tasks, machines):
    """Minimize maximum load on machines"""
    # Sort tasks in descending order (largest first)
    tasks.sort(reverse=True)
    
    # Initialize machine loads
    machine_loads = [0] * machines
    
    for task in tasks:
        # Assign to machine with minimum load
        min_load_idx = machine_loads.index(min(machine_loads))
        machine_loads[min_load_idx] += task
    
    return max(machine_loads)
```

## Greedy vs Dynamic Programming

### Key Differences:

| Aspect | Greedy | Dynamic Programming |
|--------|--------|-------------------|
| **Approach** | Local optimization | Global optimization |
| **Decision** | Irrevocable | Reconsidered |
| **Efficiency** | Generally faster | More computationally intensive |
| **Proof** | Requires proof of correctness | Mathematical induction |
| **Memory** | Usually less | Often more |
| **Scope** | Limited to specific problems | Broader applicability |

### When to Choose Which:
- **Greedy**: When greedy choice property and optimal substructure are proven
- **DP**: When greedy fails or problem has overlapping subproblems

## Problem-Solving Patterns

### 1. Interval Problems
```python
def erase_overlap_intervals(intervals):
    """Minimum intervals to remove to make rest non-overlapping"""
    if not intervals:
        return 0
    
    # Sort by end time (greedy: keep intervals that end early)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    end = float('-inf')
    
    for start, interval_end in intervals:
        if start >= end:
            # No overlap, keep this interval
            end = interval_end
        else:
            # Overlap, remove this interval
            count += 1
    
    return count
```

### 2. Greedy with Sorting
```python
def assign_cookies(children, cookies):
    """Assign cookies to children with greed factors"""
    # Sort both arrays
    children.sort()
    cookies.sort()
    
    child_idx = 0
    cookie_idx = 0
    
    while child_idx < len(children) and cookie_idx < len(cookies):
        # If cookie is big enough for current child
        if cookies[cookie_idx] >= children[child_idx]:
            child_idx += 1  # Satisfy this child
        cookie_idx += 1  # Move to next cookie
    
    return child_idx
```

### 3. Greedy with Data Structures
```python
def reconstruct_queue(people):
    """Reconstruct queue based on height and count"""
    # Sort by height (descending), then by count (ascending)
    people.sort(key=lambda x: (-x[0], x[1]))
    
    result = []
    for height, count in people:
        # Insert at position 'count' - this ensures correct positioning
        result.insert(count, [height, count])
    
    return result
```

## Advanced Greedy Concepts

### 1. Matroid Theory Application
```python
def maximum_spanning_tree(edges, n):
    """Maximum spanning tree using greedy approach"""
    # Sort edges in descending order of weight
    edges.sort(key=lambda x: x[2], reverse=True)
    
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            return True
    
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    
    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break
    
    return mst_weight, mst_edges
```

### 2. Greedy Approximation
```python
def set_cover(universe, sets):
    """Set cover approximation using greedy approach"""
    covered = set()
    chosen_sets = []
    
    while len(covered) < len(universe):
        # Find set that covers most uncovered elements
        best_set = None
        max_new_coverage = 0
        
        for s in sets:
            new_coverage = len(set(s) - covered)
            if new_coverage > max_new_coverage:
                max_new_coverage = new_coverage
                best_set = s
        
        if best_set is None:
            break  # No more coverage possible
        
        covered.update(best_set)
        chosen_sets.append(best_set)
        sets.remove(best_set)
    
    return chosen_sets
```

### 3. Online Algorithms
```python
def online_fractional_knapsack(items, capacity):
    """Online fractional knapsack with streaming data"""
    total_value = 0
    remaining_capacity = capacity
    
    # Process items as they arrive (online fashion)
    for weight, value in items:
        if remaining_capacity <= 0:
            break
        
        ratio = value / weight
        
        if weight <= remaining_capacity:
            # Take whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break
    
    return total_value
```

## Practice Problems

### Beginner Level
1. **Activity Selection**: Maximize non-overlapping activities
2. **Job Sequencing**: Maximize profit with deadlines
3. **Fractional Knapsack**: Optimize with divisible items

### Intermediate Level
1. **Minimum Platforms**: Railway station scheduling
2. **Huffman Coding**: Compression algorithm
3. **Gas Station**: Circular route problem

### Advanced Level
1. **Maximum Product Subarray**: Greedy with tracking
2. **Jump Game**: Reach end with minimum jumps
3. **Meeting Rooms II**: Interval scheduling optimization

## Summary

Greedy algorithms are powerful for specific problem types:

1. **Core Principle**: Make locally optimal choices hoping for global optimum
2. **Requirements**: Greedy choice property and optimal substructure
3. **Efficiency**: Generally faster than DP approaches
4. **Limitations**: Not universally applicable
5. **Applications**: Scheduling, optimization, network design

Greedy algorithms provide elegant solutions when applicable, but require careful analysis to ensure correctness. Combined with the previous topics, you now have a comprehensive foundation in Data Structures and Algorithms.