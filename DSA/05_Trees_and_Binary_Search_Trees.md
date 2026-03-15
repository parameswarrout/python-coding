# 05 - Trees and Binary Search Trees: Hierarchical Data Structures

## Table of Contents
1. [Introduction](#introduction)
2. [Tree Terminology](#tree-terminology)
3. [Binary Trees Explained](#binary-trees-explained)
4. [Binary Search Trees Explained](#binary-search-trees-explained)
5. [Tree Traversals](#tree-traversals)
6. [Python Implementation](#python-implementation)
7. [Common Operations](#common-operations)
8. [Time and Space Complexity](#time-and-space-complexity)
9. [Applications and Use Cases](#applications-and-use-cases)
10. [Problem-Solving Patterns](#problem-solving-patterns)
11. [Advanced Tree Concepts](#advanced-tree-concepts)
12. [Practice Problems](#practice-problems)
13. [Summary](#summary)

## Introduction

Trees represent hierarchical relationships between elements, similar to family trees or organizational charts. Unlike linear data structures (arrays, linked lists), trees allow for branching, making them ideal for representing hierarchical data and enabling efficient searching, insertion, and deletion operations.

Think of a tree as a company hierarchy where the CEO is at the top, followed by department heads, managers, and employees. Each person reports to one supervisor but can supervise multiple subordinates.

## Tree Terminology

### Basic Terms:
- **Root**: Topmost node with no parent
- **Leaf**: Node with no children
- **Internal Node**: Node with at least one child
- **Parent**: Node that has children
- **Child**: Node that has a parent
- **Sibling**: Nodes with the same parent
- **Ancestor**: Parent, grandparent, etc. of a node
- **Descendant**: Child, grandchild, etc. of a node
- **Subtree**: Tree formed by a node and its descendants
- **Height**: Longest path from node to leaf
- **Depth**: Distance from root to node

## Binary Trees Explained

### What is a Binary Tree?

A binary tree is a tree data structure where each node has at most two children, referred to as the left child and right child.

**Analogy**: Think of a decision tree where each decision leads to at most two options.

```
        Root
       /    \
    Left   Right
   /   \   /    \
  L-L  L-R R-L  R-R
```

### Properties of Binary Trees:
- Maximum nodes at level i: 2^i
- Maximum nodes in tree of height h: 2^(h+1) - 1
- Minimum height for n nodes: ⌈log₂(n+1)⌉ - 1

## Binary Search Trees Explained

### What is a Binary Search Tree (BST)?

A BST is a binary tree with the following properties:
1. Left subtree contains only nodes with keys less than the node's key
2. Right subtree contains only nodes with keys greater than the node's key
3. Both left and right subtrees are also BSTs

**Analogy**: Like a sorted array but with the flexibility of a tree structure, allowing for efficient insertions and deletions.

```
       50
      /  \
    30    70
   /  \   /  \
  20  40 60  80
```

## Tree Traversals

### 1. Depth-First Search (DFS)
- **Inorder**: Left → Root → Right (gives sorted order in BST)
- **Preorder**: Root → Left → Right (used for copying tree)
- **Postorder**: Left → Right → Root (used for deleting tree)

### 2. Breadth-First Search (BFS)
- Level-order traversal using a queue

## Python Implementation

### TreeNode Class

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Binary Search Tree Implementation

```python
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        """Insert value into BST"""
        self.root = self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self._insert_recursive(node.left, val)
        elif val > node.val:
            node.right = self._insert_recursive(node.right, val)
        # If val == node.val, we don't insert (no duplicates)
        
        return node
    
    def search(self, val):
        """Search for value in BST"""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node, val):
        if not node or node.val == val:
            return node
        
        if val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def delete(self, val):
        """Delete value from BST"""
        self.root = self._delete_recursive(self.root, val)
    
    def _delete_recursive(self, node, val):
        if not node:
            return node
        
        if val < node.val:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.val:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Node to be deleted found
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node has two children
            # Find inorder successor (smallest in right subtree)
            min_val_node = self._find_min(node.right)
            node.val = min_val_node.val
            node.right = self._delete_recursive(node.right, min_val_node.val)
        
        return node
    
    def _find_min(self, node):
        """Find minimum value node in subtree"""
        while node.left:
            node = node.left
        return node
```

## Common Operations

### Tree Traversals Implementation

```python
def inorder_traversal(root):
    """Inorder: Left -> Root -> Right"""
    result = []
    
    def inorder_helper(node):
        if node:
            inorder_helper(node.left)
            result.append(node.val)
            inorder_helper(node.right)
    
    inorder_helper(root)
    return result

def preorder_traversal(root):
    """Preorder: Root -> Left -> Right"""
    result = []
    
    def preorder_helper(node):
        if node:
            result.append(node.val)
            preorder_helper(node.left)
            preorder_helper(node.right)
    
    preorder_helper(root)
    return result

def postorder_traversal(root):
    """Postorder: Left -> Right -> Root"""
    result = []
    
    def postorder_helper(node):
        if node:
            postorder_helper(node.left)
            postorder_helper(node.right)
            result.append(node.val)
    
    postorder_helper(root)
    return result

def level_order_traversal(root):
    """Level-order (BFS) traversal"""
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result
```

### Iterative Traversals

```python
def inorder_iterative(root):
    """Iterative inorder traversal using stack"""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None here
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

def preorder_iterative(root):
    """Iterative preorder traversal using stack"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Add right first, then left (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result
```

## Time and Space Complexity

### Binary Search Tree Operations

| Operation | Best/Average Case | Worst Case | Space |
|-----------|-------------------|------------|-------|
| Search | O(log n) | O(n) | O(log n)/O(n) |
| Insert | O(log n) | O(n) | O(log n)/O(n) |
| Delete | O(log n) | O(n) | O(log n)/O(n) |
| Traversal | O(n) | O(n) | O(h) where h=height |

### Tree Traversal Complexity
- **Time**: O(n) for all traversals (visit each node once)
- **Space**: O(h) for recursive, O(w) for iterative BFS (w=max width)

## Applications and Use Cases

### 1. Expression Trees
Represent mathematical expressions:
```
    +
   / \
  *   5
 / \
3   4
```
Represents: (3 * 4) + 5

### 2. Huffman Coding
Used in compression algorithms

### 3. Database Indexing
B-trees and variants used in databases

### 4. File Systems
Directory structures

## Problem-Solving Patterns

### 1. Validate BST
```python
def is_valid_bst(root):
    """Check if tree is valid BST"""
    def validate(node, min_val, max_val):
        if not node:
            return True
        
        if node.val <= min_val or node.val >= max_val:
            return False
        
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

### 2. Lowest Common Ancestor
```python
def lowest_common_ancestor(root, p, q):
    """Find LCA in BST"""
    if not root:
        return None
    
    # If both p and q are smaller than root, LCA is in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both p and q are greater than root, LCA is in right subtree
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # We found the split point where p and q are on different sides
    else:
        return root
```

### 3. Kth Smallest Element
```python
def kth_smallest(root, k):
    """Find kth smallest element in BST"""
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    return inorder(root)[k-1]

# More efficient approach using iterative inorder
def kth_smallest_efficient(root, k):
    stack = []
    current = root
    count = 0
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process current node
        current = stack.pop()
        count += 1
        
        if count == k:
            return current.val
        
        # Move to right subtree
        current = current.right
    
    return None
```

### 4. Serialize and Deserialize
```python
def serialize(root):
    """Serialize BST to string"""
    def preorder(node):
        if not node:
            return "null"
        return str(node.val) + "," + preorder(node.left) + "," + preorder(node.right)
    
    return preorder(root)

def deserialize(data):
    """Deserialize string back to BST"""
    def build_tree(nodes):
        val = next(nodes)
        if val == "null":
            return None
        
        node = TreeNode(int(val))
        node.left = build_tree(nodes)
        node.right = build_tree(nodes)
        return node
    
    nodes = iter(data.split(","))
    return build_tree(nodes)
```

## Advanced Tree Concepts

### 1. Balanced Trees
AVL trees, Red-Black trees maintain balance to ensure O(log n) operations.

### 2. Self-Balancing BST Operations
```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
```

### 3. Morris Traversal (Threaded Trees)
Space-efficient traversal without recursion or stack:

```python
def morris_inorder(root):
    """Morris inorder traversal - O(1) space"""
    result = []
    current = root
    
    while current:
        if not current.left:
            # No left subtree, process current and go right
            result.append(current.val)
            current = current.right
        else:
            # Find inorder predecessor
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            if not predecessor.right:
                # Make threading
                predecessor.right = current
                current = current.left
            else:
                # Revert threading and process current
                predecessor.right = None
                result.append(current.val)
                current = current.right
    
    return result
```

### 4. Segment Trees (Range Queries)
```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query(2 * node + 1, start, mid, l, r)
        right_sum = self.query(2 * node + 2, mid + 1, end, l, r)
        return left_sum + right_sum
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]
```

## Practice Problems

### Beginner Level
1. **Maximum Depth**: Find height of binary tree
2. **Symmetric Tree**: Check if tree is mirror of itself
3. **Same Tree**: Check if two trees are identical

### Intermediate Level
1. **Validate BST**: Check if binary tree is valid BST
2. **Kth Smallest Element**: Find kth smallest in BST
3. **Lowest Common Ancestor**: Find LCA of two nodes

### Advanced Level
1. **Serialize and Deserialize**: Convert tree to string and back
2. **BST Iterator**: Implement iterator for BST
3. **Count of Range Sum**: Use BST for range queries

## Summary

Trees provide hierarchical data organization with efficient operations:

1. **Structure**: Nodes connected in parent-child relationships
2. **BST Property**: Left < Root < Right enables efficient searching
3. **Traversals**: DFS and BFS for different use cases
4. **Operations**: Insert, search, delete with O(log n) average complexity
5. **Applications**: Expression evaluation, database indexing, file systems

Trees bridge the gap between linear and complex graph structures, making them essential for understanding more advanced data structures. The next topic will cover Graphs, which generalize trees to allow more complex relationships.