# 03 - Stacks and Queues: Abstract Data Types

## Table of Contents
1. [Introduction](#introduction)
2. [Stacks Explained](#stacks-explained)
3. [Queues Explained](#queues-explained)
4. [Python Implementation](#python-implementation)
5. [Common Operations](#common-operations)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Applications and Use Cases](#applications-and-use-cases)
8. [Problem-Solving Patterns](#problem-solving-patterns)
9. [Advanced Variants](#advanced-variants)
10. [Practice Problems](#practice-problems)
11. [Summary](#summary)

## Introduction

Stacks and queues are fundamental abstract data types that define specific ways to add and remove elements. They are called "abstract" because they specify what operations can be performed but not how they're implemented.

Think of these as rules for organizing everyday activities:
- **Stack**: Like stacking plates in a restaurant kitchen - you add and remove from the top
- **Queue**: Like waiting in line at a bank - first come, first served

## Stacks Explained

### What is a Stack?

A stack is a linear data structure that follows the **LIFO (Last In, First Out)** principle. The last element added is the first one removed.

**Analogy**: A pile of books. You can only take the top book, and you can only add books to the top.

### Stack Operations:
- **Push**: Add element to top
- **Pop**: Remove element from top
- **Peek/Top**: View top element without removing
- **isEmpty**: Check if stack is empty
- **Size**: Get number of elements

```
Top -> [Element 3]
       [Element 2]
       [Element 1]
Bottom -> [Element 0]
```

## Queues Explained

### What is a Queue?

A queue is a linear data structure that follows the **FIFO (First In, First Out)** principle. The first element added is the first one removed.

**Analogy**: People waiting in a line. The person who arrived first is served first.

### Queue Operations:
- **Enqueue**: Add element to rear
- **Dequeue**: Remove element from front
- **Front**: View front element without removing
- **Rear**: View rear element without removing
- **isEmpty**: Check if queue is empty
- **Size**: Get number of elements

```
Front -> [Element 0] [Element 1] [Element 2] <- Rear
```

## Python Implementation

### Stack Implementation

```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get number of items in stack"""
        return len(self.items)

# Alternative implementation using collections.deque
from collections import deque

class StackDeque:
    def __init__(self):
        self.items = deque()
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
```

### Queue Implementation

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()
    
    def front(self):
        """Return front item without removing"""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def rear(self):
        """Return rear item without removing"""
        if self.is_empty():
            raise IndexError("rear from empty queue")
        return self.items[-1]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get number of items in queue"""
        return len(self.items)

# Alternative using list (less efficient for dequeue)
class QueueList:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)  # O(1)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)  # O(n) - inefficient!
    
    def is_empty(self):
        return len(self.items) == 0
```

## Common Operations

### Stack Operations Complexity

| Operation | Array/List | Linked List |
|-----------|------------|-------------|
| Push | O(1) amortized | O(1) |
| Pop | O(1) | O(1) |
| Peek | O(1) | O(1) |
| Space | O(n) | O(n) |

### Queue Operations Complexity

| Operation | Deque | Linked List |
|-----------|-------|-------------|
| Enqueue | O(1) | O(1) |
| Dequeue | O(1) | O(1) |
| Front/Rear | O(1) | O(1) |
| Space | O(n) | O(n) |

## Applications and Use Cases

### Stack Applications

1. **Function Call Management**: System stack manages function calls
2. **Expression Evaluation**: Converting infix to postfix notation
3. **Undo Mechanisms**: Browser back button, text editor undo
4. **Balanced Parentheses**: Checking matching brackets
5. **Depth-First Search**: Tree/graph traversal

### Queue Applications

1. **Breadth-First Search**: Level-order tree traversal
2. **CPU Scheduling**: Process scheduling in operating systems
3. **Buffer Management**: Keyboard buffer, printer queue
4. **Breadth-First Search**: Graph algorithms
5. **Level-order Traversal**: Tree algorithms

## Problem-Solving Patterns

### 1. Balanced Parentheses (Stack)

```python
def is_balanced(s):
    """Check if parentheses are balanced"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    
    return not stack
```

### 2. Valid Parentheses with Multiple Types

```python
def min_add_to_make_valid(s):
    """Minimum additions to make parentheses valid"""
    stack = 0
    additions = 0
    
    for char in s:
        if char == '(':
            stack += 1
        elif char == ')':
            if stack > 0:
                stack -= 1
            else:
                additions += 1
    
    return stack + additions
```

### 3. Queue-based Level Order Traversal

```python
from collections import deque

def level_order_traversal(root):
    """BFS traversal of binary tree"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level_nodes)
    
    return result
```

### 4. Monotonic Stack Pattern

```python
def next_greater_element(nums):
    """Find next greater element for each element"""
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

## Advanced Variants

### 1. Double-Ended Queue (Deque)

```python
from collections import deque

# Deque supports operations at both ends
dq = deque()

# Add/remove from both ends
dq.appendleft(1)  # Add to front
dq.append(2)      # Add to rear
dq.popleft()      # Remove from front
dq.pop()          # Remove from rear
```

### 2. Priority Queue (Min/Max Heap)

```python
import heapq

class PriorityQueue:
    def __init__(self, is_min_heap=True):
        self.heap = []
        self.is_min_heap = is_min_heap
    
    def push(self, item):
        if not self.is_min_heap:
            item = -item  # Negate for max heap
        heapq.heappush(self.heap, item)
    
    def pop(self):
        item = heapq.heappop(self.heap)
        if not self.is_min_heap:
            item = -item
        return item
    
    def peek(self):
        if self.heap:
            item = self.heap[0]
            if not self.is_min_heap:
                item = -item
            return item
        return None
```

### 3. Circular Queue

```python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0
    
    def enqueue(self, item):
        if self.size == self.capacity:
            raise Exception("Queue is full")
        
        if self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        
        self.queue[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        return item
```

### 4. Stack with Min/Max in O(1)

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Auxiliary stack to track minimums
    
    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self):
        if not self.stack:
            return None
        
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        return val
    
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]
    
    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
```

## Practice Problems

### Beginner Level
1. **Valid Parentheses**: Check if brackets are properly closed
2. **Implement Stack using Queues**: Use two queues to simulate stack
3. **Implement Queue using Stacks**: Use two stacks to simulate queue

### Intermediate Level
1. **Evaluate Reverse Polish Notation**: Use stack for expression evaluation
2. **Sliding Window Maximum**: Use deque for efficient solution
3. **Design Circular Queue**: Implement queue with fixed capacity

### Advanced Level
1. **LRU Cache**: Combine hash map and doubly linked list
2. **Trapping Rain Water**: Use stack-based approach
3. **Largest Rectangle in Histogram**: Stack-based solution

## Summary

Stacks and queues are essential abstract data types with specific ordering principles:

1. **Stacks**: LIFO principle, excellent for managing nested operations
2. **Queues**: FIFO principle, ideal for processing items in order
3. **Implementation**: Can use arrays/lists or linked lists
4. **Applications**: Numerous real-world scenarios and algorithmic problems
5. **Variants**: Several specialized versions for specific use cases

These data structures form the foundation for many algorithms and are frequently used in system design and problem-solving. The next topic will cover Hashing and Hash Tables, which provide efficient key-value storage and retrieval.