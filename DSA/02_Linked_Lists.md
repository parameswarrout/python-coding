# 02 - Linked Lists: Dynamic Data Structures

## Table of Contents
1. [Introduction](#introduction)
2. [What is a Linked List?](#what-is-a-linked-list)
3. [Types of Linked Lists](#types-of-linked-lists)
4. [Node Structure](#node-structure)
5. [Python Implementation](#python-implementation)
6. [Common Operations](#common-operations)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Advantages and Disadvantages](#advantages-and-disadvantages)
9. [Problem-Solving Patterns](#problem-solving-patterns)
10. [Advanced Concepts](#advanced-concepts)
11. [Practice Problems](#practice-problems)
12. [Summary](#summary)

## Introduction

Linked lists represent a fundamental shift from arrays in how we organize data. While arrays store elements in contiguous memory locations, linked lists connect elements through pointers. This difference leads to unique advantages and trade-offs that make linked lists suitable for specific scenarios.

Think of a treasure hunt where each clue points to the next location. Unlike arrays (where you know the address of every location beforehand), in linked lists, you must follow the clues sequentially to reach your destination.

## What is a Linked List?

A linked list is a linear data structure where elements (called nodes) are connected through pointers/references. Each node contains:
1. **Data**: The value stored in the node
2. **Pointer/Reference**: Points to the next node in the sequence

**Analogy**: Think of a train where each car is connected to the next. To get to the 5th car, you must pass through cars 1-4. Unlike arrays, you can't directly jump to the 5th car.

```
Head -> [Data|Next] -> [Data|Next] -> [Data|Next] -> NULL
```

## Types of Linked Lists

### 1. Singly Linked List
Each node points only to the next node.

### 2. Doubly Linked List
Each node points to both the next and previous nodes.

### 3. Circular Linked List
The last node points back to the first node, forming a circle.

## Node Structure

The basic building block of a linked list is the node:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

In a doubly linked list:
```python
class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

## Python Implementation

### Singly Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, val):
        """Add element to the end"""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1
    
    def prepend(self, val):
        """Add element to the beginning"""
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def display(self):
        """Display the linked list"""
        elements = []
        current = self.head
        while current:
            elements.append(current.val)
            current = current.next
        return elements
```

### Doubly Linked List

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, val):
        """Add element to the end"""
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
```

## Common Operations

### Basic Operations

| Operation | Description | Time Complexity |
|-----------|-------------|-----------------|
| Insert at head | Add element at beginning | O(1) |
| Insert at tail | Add element at end | O(1) for DLL, O(n) for SLL |
| Delete head | Remove first element | O(1) |
| Delete tail | Remove last element | O(1) for DLL, O(n) for SLL |
| Search | Find element | O(n) |
| Access | Get element at position | O(n) |

### Implementation Examples

```python
def insert_at_position(self, pos, val):
    """Insert at specific position"""
    if pos == 0:
        self.prepend(val)
        return
    
    new_node = ListNode(val)
    current = self.head
    
    # Traverse to position
    for i in range(pos - 1):
        if not current:
            raise IndexError("Position out of bounds")
        current = current.next
    
    # Insert new node
    new_node.next = current.next
    current.next = new_node
    self.size += 1

def delete_by_value(self, val):
    """Delete first occurrence of value"""
    if not self.head:
        return False
    
    # If head contains the value
    if self.head.val == val:
        self.head = self.head.next
        self.size -= 1
        return True
    
    current = self.head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            self.size -= 1
            return True
        current = current.next
    
    return False  # Value not found
```

## Time and Space Complexity

### Time Complexity Comparison

| Operation | Array | Singly LL | Doubly LL |
|-----------|-------|-----------|-----------|
| Access | O(1) | O(n) | O(n) |
| Insert at head | O(n) | O(1) | O(1) |
| Insert at tail | O(1)* | O(n) | O(1) |
| Delete at head | O(n) | O(1) | O(1) |
| Delete at tail | O(1)* | O(n) | O(1) |
| Search | O(n) | O(n) | O(n) |

*Amortized for dynamic arrays

### Space Complexity
- Singly Linked List: O(n) - each node stores data + one pointer
- Doubly Linked List: O(n) - each node stores data + two pointers

## Advantages and Disadvantages

### Advantages of Linked Lists
1. **Dynamic Size**: Can grow/shrink during runtime
2. **Efficient Insertions/Deletions**: O(1) at known positions
3. **No Memory Waste**: Allocate only needed memory
4. **Easy Implementation**: Of other data structures (stacks, queues)

### Disadvantages of Linked Lists
1. **No Random Access**: Must traverse from head
2. **Extra Memory**: For storing pointers
3. **Not Cache-Friendly**: Nodes scattered in memory
4. **Reverse Traversal**: Not possible in singly LL

## Problem-Solving Patterns

### 1. Two Pointers Technique
Often used for detecting cycles, finding middle, etc.

```python
def has_cycle(head):
    """Detect cycle using Floyd's Cycle Detection"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def find_middle(head):
    """Find middle element using slow-fast pointers"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val
```

### 2. Reverse a Linked List
```python
def reverse_list(head):
    """Iterative reversal"""
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current           # Move prev forward
        current = next_temp      # Move current forward
    
    return prev  # New head is prev
```

### 3. Merge Two Sorted Lists
```python
def merge_two_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = l1 or l2
    return dummy.next
```

## Advanced Concepts

### 1. Dummy Head Technique
Using a dummy node simplifies edge cases:

```python
def remove_elements(head, val):
    """Remove all nodes with specific value"""
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    current = head
    
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    
    return dummy.next
```

### 2. Recursion in Linked Lists
Many linked list problems can be solved elegantly with recursion:

```python
def reverse_recursive(head):
    """Recursive reversal"""
    # Base case
    if not head or not head.next:
        return head
    
    # Recursive call
    new_head = reverse_recursive(head.next)
    
    # Reverse the connection
    head.next.next = head
    head.next = None
    
    return new_head
```

### 3. Palindrome Check
```python
def is_palindrome(head):
    """Check if linked list is palindrome"""
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Compare first and second half
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True
```

## Practice Problems

### Beginner Level
1. **Reverse a linked list**: Change direction of all pointers
2. **Detect cycle**: Determine if there's a loop in the list
3. **Find middle element**: Use slow-fast pointer technique

### Intermediate Level
1. **Remove nth node from end**: Use two pointers with gap
2. **Add two numbers**: Represent numbers as linked lists
3. **Intersection of two lists**: Find where two lists meet

### Advanced Level
1. **Copy random pointer list**: Clone complex linked list structure
2. **LRU cache implementation**: Using doubly linked list
3. **Sort list**: Implement merge sort for linked list

## Summary

Linked lists offer a flexible alternative to arrays with dynamic sizing and efficient insertions/deletions. Key takeaways:

1. **Structure**: Nodes with data and pointers connecting them
2. **Trade-offs**: Sacrifice random access for dynamic operations
3. **Patterns**: Two pointers, dummy heads, recursion are common techniques
4. **Applications**: Building blocks for stacks, queues, and other structures

Understanding linked lists is crucial as they form the basis for more complex data structures and algorithms. The next topic will cover Stacks and Queues, which can be efficiently implemented using linked lists.