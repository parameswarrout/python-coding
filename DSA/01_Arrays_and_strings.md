# 01 - Arrays and Strings: Foundation of Data Structures

## Table of Contents
1. [Introduction](#introduction)
2. [Arrays Explained](#arrays-explained)
3. [Strings Explained](#strings-explained)
4. [Python Implementation](#python-implementation)
5. [Common Operations](#common-operations)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Problem-Solving Patterns](#problem-solving-patterns)
8. [Advanced Concepts](#advanced-concepts)
9. [Practice Problems](#practice-problems)
10. [Summary](#summary)

## Introduction

Arrays and strings form the backbone of data structures and algorithms. Think of an array as a row of mailboxes in an apartment building - each mailbox has a unique number (index) and can hold one item. Similarly, a string is like a sequence of letters in a word, where each letter has a position.

Understanding these fundamental concepts is crucial because:
- They appear in almost every algorithm problem
- Many complex data structures are built upon arrays
- String manipulation is essential for text processing
- They provide the foundation for more advanced topics

## Arrays Explained

### What is an Array?

An array is a collection of elements stored in contiguous memory locations. Each element can be accessed using an index.

**Analogy**: Imagine a parking lot with numbered spots. Each spot (index) holds one car (element). You can instantly access any car by knowing its spot number.

```
Index:    0   1   2   3   4
Array:   [10, 25, 30, 45, 50]
```

### Key Characteristics:
- **Fixed Size**: Traditional arrays have a predetermined size
- **Random Access**: Elements can be accessed directly using indices
- **Homogeneous**: All elements are typically of the same data type
- **Contiguous Memory**: Elements are stored next to each other in memory

### Types of Arrays:
1. **One-dimensional**: Single row of elements
2. **Multi-dimensional**: Arrays of arrays (matrices, grids)

## Strings Explained

### What is a String?

A string is essentially an array of characters. In many programming languages, strings are immutable, meaning once created, they cannot be changed.

**Analogy**: Think of a string as a necklace with different beads. Each bead represents a character, and the order matters. If you want to change a bead, you need to create a new necklace.

### Key Characteristics:
- **Immutable** in Python (technically, str objects are immutable)
- **Indexed** like arrays (0-indexed)
- **Ordered** - character positions matter
- **Iterable** - can be looped through

## Python Implementation

### Arrays in Python

Python doesn't have a native array data type like other languages. Instead, it uses:
- **Lists**: Dynamic arrays that can store mixed data types
- **array module**: For homogeneous data (more memory efficient)
- **NumPy arrays**: For numerical computations

```python
# Using Lists (most common)
arr = [1, 2, 3, 4, 5]
print(arr[0])  # Output: 1

# Using array module (for numeric data)
import array
numeric_arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' for integers

# Using NumPy (for mathematical operations)
import numpy as np
np_arr = np.array([1, 2, 3, 4, 5])
```

### Strings in Python

```python
# Creating strings
str1 = "Hello"
str2 = 'World'
str3 = """Multi-line
string"""

# String operations
text = "Hello World"
print(text[0])        # Output: 'H'
print(text[0:5])      # Output: 'Hello'
print(len(text))      # Output: 11
```

## Common Operations

### Array Operations

| Operation | Description | Python Example |
|-----------|-------------|----------------|
| Access | Retrieve element at index | `arr[2]` |
| Insert | Add element at position | `arr.insert(1, value)` |
| Delete | Remove element | `arr.remove(value)` or `del arr[index]` |
| Search | Find element | `value in arr` or `arr.index(value)` |
| Update | Modify element | `arr[2] = new_value` |

### String Operations

| Operation | Description | Python Example |
|-----------|-------------|----------------|
| Access | Get character at index | `s[2]` |
| Slice | Extract substring | `s[1:4]` |
| Concatenate | Join strings | `s1 + s2` |
| Find | Locate substring | `s.find(substring)` |
| Replace | Substitute characters | `s.replace(old, new)` |
| Split | Divide into list | `s.split(delimiter)` |

## Time and Space Complexity

### Array Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(1) | O(1) |
| Search (unsorted) | O(n) | O(1) |
| Insertion (at end) | O(1) amortized | O(1) |
| Insertion (middle) | O(n) | O(1) |
| Deletion (middle) | O(n) | O(1) |
| Space | - | O(n) |

### String Operations Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access | O(1) | O(1) |
| Substring | O(k) where k is length | O(k) |
| Concatenation | O(n + m) | O(n + m) |
| Search | O(n*m) worst case | O(1) |
| Space | - | O(n) |

## Problem-Solving Patterns

### Two Pointers Technique
Useful for problems involving sorted arrays or palindromes.

```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

### Sliding Window
Effective for subarray/substring problems.

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Dutch National Flag Algorithm
For sorting arrays with 3 distinct values.

```python
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums
```

## Advanced Concepts

### Dynamic Arrays
Python lists are dynamic arrays that automatically resize.

```python
# Python list automatically resizes
my_list = []
for i in range(1000):  # No need to predefine size
    my_list.append(i)
```

### String Interning
Python optimizes memory by reusing string objects for commonly used strings.

```python
a = "hello"
b = "hello"
print(a is b)  # True - same object in memory
```

### Memory Layout
Understanding how arrays are stored helps optimize performance:

```python
import sys
arr = [1, 2, 3, 4, 5]
print(sys.getsizeof(arr))  # Size of the list object
```

## Practice Problems

### Beginner Level
1. **Reverse an array**: Given `[1,2,3,4,5]`, return `[5,4,3,2,1]`
2. **Find maximum element**: Return the largest number in an array
3. **Check palindrome**: Determine if a string reads the same forwards and backwards

### Intermediate Level
1. **Two Sum**: Find two numbers that add up to a target
2. **Longest substring without repeating characters**
3. **Rotate array**: Shift elements by k positions

### Advanced Level
1. **Median of two sorted arrays**: Find median without merging
2. **Wildcard matching**: Implement pattern matching with wildcards
3. **Minimum window substring**: Find smallest substring containing all characters

## Summary

Arrays and strings are fundamental building blocks in computer science. Mastering them involves understanding:

1. **Basic operations**: Access, insertion, deletion, searching
2. **Memory implications**: How data is stored and accessed
3. **Common patterns**: Two pointers, sliding window, etc.
4. **Complexity analysis**: Time and space trade-offs
5. **Problem-solving techniques**: Breaking down complex problems

These concepts serve as the foundation for more advanced data structures like linked lists, trees, and graphs. A solid understanding of arrays and strings is essential for success in algorithm interviews and competitive programming.

Next, we'll explore Linked Lists, which solve some limitations of arrays while introducing new trade-offs.