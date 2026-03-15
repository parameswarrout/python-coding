# 08 - Searching Algorithms: Finding Elements Efficiently

## Table of Contents
1. [Introduction](#introduction)
2. [Linear Search](#linear-search)
3. [Binary Search](#binary-search)
4. [Interpolation Search](#interpolation-search)
5. [Jump Search](#jump-search)
6. [Exponential Search](#exponential-search)
7. [Python Implementation](#python-implementation)
8. [Time and Space Complexity](#time-and-space-complexity)
9. [Applications and Use Cases](#applications-and-use-cases)
10. [Problem-Solving Patterns](#problem-solving-patterns)
11. [Advanced Searching Concepts](#advanced-searching-concepts)
12. [Practice Problems](#practice-problems)
13. [Summary](#summary)

## Introduction

Searching algorithms are fundamental methods for finding specific elements within data structures. The efficiency of searching depends heavily on the organization of the data and the algorithm chosen. Understanding when and how to use different searching techniques is crucial for optimal performance.

Think of searching like looking for a book in a library - if books are randomly placed, you might need to check every shelf (linear search). But if they're organized alphabetically, you can use more efficient methods (binary search).

## Linear Search

### What is Linear Search?

Linear search (sequential search) examines each element in a list until the target is found or the end is reached.

**Analogy**: Looking for your friend in a crowd by checking each person one by one.

### Implementation

```python
def linear_search(arr, target):
    """Linear search implementation"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index of target
    return -1  # Target not found

# Alternative implementation with enumerate
def linear_search_enumerate(arr, target):
    """Linear search using enumerate"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1
```

### Characteristics:
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Works on**: Any data structure (sorted or unsorted)
- **Best Case**: O(1) - target is first element
- **Worst Case**: O(n) - target is last element or not present

## Binary Search

### What is Binary Search?

Binary search efficiently finds an element in a sorted array by repeatedly dividing the search space in half.

**Analogy**: Playing "guess the number" game where you're told if your guess is too high or too low.

### Implementation

```python
def binary_search(arr, target):
    """Binary search implementation"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Prevent overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Recursive implementation
def binary_search_recursive(arr, target, left=0, right=None):
    """Recursive binary search"""
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

### Variants of Binary Search

#### 1. Find First Occurrence
```python
def find_first_occurrence(arr, target):
    """Find first occurrence of target in sorted array with duplicates"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

#### 2. Find Last Occurrence
```python
def find_last_occurrence(arr, target):
    """Find last occurrence of target in sorted array with duplicates"""
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

#### 3. Count Occurrences
```python
def count_occurrences(arr, target):
    """Count occurrences of target in sorted array"""
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    
    last = find_last_occurrence(arr, target)
    return last - first + 1
```

## Interpolation Search

### What is Interpolation Search?

Interpolation search estimates the position of the target value using the formula for linear interpolation. Works well on uniformly distributed sorted arrays.

### Implementation

```python
def interpolation_search(arr, target):
    """Interpolation search implementation"""
    low, high = 0, len(arr) - 1
    
    while low <= high and target >= arr[low] and target <= arr[high]:
        # If array has only one element
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # Probing position with interpolation formula
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1
```

### Characteristics:
- **Time Complexity**: O(log log n) average case, O(n) worst case
- **Space Complexity**: O(1)
- **Best for**: Uniformly distributed sorted arrays
- **Requirement**: Array must be sorted

## Jump Search

### What is Jump Search?

Jump search finds the target by jumping ahead by fixed steps and then performing linear search in the identified block.

### Implementation

```python
import math

def jump_search(arr, target):
    """Jump search implementation"""
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump size
    prev = 0
    
    # Jump in blocks until element is found or exceeded
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the identified block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1
```

### Characteristics:
- **Time Complexity**: O(√n)
- **Space Complexity**: O(1)
- **Best for**: Sorted arrays where binary search is not preferred
- **Requirement**: Array must be sorted

## Exponential Search

### What is Exponential Search?

Exponential search finds the range where the target lies and then performs binary search in that range. Useful for unbounded or infinite arrays.

### Implementation

```python
def exponential_search(arr, target):
    """Exponential search implementation"""
    if not arr:
        return -1
    
    if arr[0] == target:
        return 0
    
    # Find range for binary search by repeated doubling
    i = 1
    while i < len(arr) and arr[i] <= target:
        i *= 2
    
    # Call binary search for the found range
    return binary_search_range(arr, target, i // 2, min(i, len(arr) - 1))

def binary_search_range(arr, target, left, right):
    """Binary search in a specific range"""
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
```

### Characteristics:
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)
- **Best for**: Unbounded or infinite sorted arrays
- **Requirement**: Array must be sorted

## Python Implementation

### Standard Library Functions

Python provides built-in searching capabilities:

```python
# Using built-in methods
arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Linear search using built-in methods
index = arr.index(7) if 7 in arr else -1  # Raises ValueError if not found
index = next((i for i, x in enumerate(arr) if x == 7), -1)  # Safer approach

# Using bisect module for binary search
import bisect

# Find insertion point
pos = bisect.bisect_left(arr, 7)  # Leftmost insertion point
if pos < len(arr) and arr[pos] == 7:
    index = pos  # Found
else:
    index = -1  # Not found

# Other bisect functions
bisect.bisect_right(arr, 7)  # Rightmost insertion point
bisect.insort(arr, 6)  # Insert in sorted order
```

### Advanced Searching Implementations

```python
def ternary_search(arr, target):
    """Ternary search implementation (divides array into 3 parts)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2
        
        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    
    return -1

def fibonacci_search(arr, target):
    """Fibonacci search implementation"""
    n = len(arr)
    
    # Generate fibonacci numbers until fibM >= n
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number
    
    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1
    
    offset = -1  # Marks eliminated range from front
    
    while fib_m > 1:
        # Check if fib_m2 is valid location
        i = min(offset + fib_m2, n - 1)
        
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i
    
    # Comparing last element with target
    if fib_m1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1
    
    return -1
```

## Time and Space Complexity

### Comparison of Searching Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Requirement |
|-----------|-----------|--------------|------------|-------|-------------|
| Linear Search | O(1) | O(n) | O(n) | O(1) | None |
| Binary Search | O(1) | O(log n) | O(log n) | O(1) | Sorted |
| Jump Search | O(1) | O(√n) | O(√n) | O(1) | Sorted |
| Interpolation Search | O(1) | O(log log n) | O(n) | O(1) | Sorted, Uniform |
| Exponential Search | O(1) | O(log n) | O(log n) | O(1) | Sorted |
| Ternary Search | O(1) | O(log₃ n) | O(log₃ n) | O(1) | Sorted |

## Applications and Use Cases

### 1. When to Use Each Algorithm

- **Linear Search**: Small datasets, unsorted data, or when simplicity is preferred
- **Binary Search**: Sorted arrays, frequent searches, optimal performance
- **Jump Search**: When jumping back is costly (e.g., linked lists)
- **Interpolation Search**: Uniformly distributed sorted data
- **Exponential Search**: Unbounded arrays or when target is closer to beginning

### 2. Real-World Applications

```python
def search_in_rotated_array(nums, target):
    """Search in rotated sorted array using modified binary search"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left side is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right side is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

def search_2d_matrix(matrix, target):
    """Search in sorted 2D matrix"""
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_val = matrix[mid // cols][mid % cols]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

def find_peak_element(nums):
    """Find peak element using binary search"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left
```

## Problem-Solving Patterns

### 1. Binary Search on Answer

```python
def find_sqrt(x):
    """Find integer square root using binary search"""
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
            result = mid  # Potential answer
        else:
            right = mid - 1
    
    return result

def search_insert_position(nums, target):
    """Find insert position in sorted array"""
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left
```

### 2. Finding Rotation Point

```python
def find_rotation_point(words):
    """Find rotation point in rotated sorted array"""
    first_word = words[0]
    floor_index = 0
    ceiling_index = len(words) - 1
    
    while floor_index < ceiling_index:
        # Guess a point halfway between floor and ceiling
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)
        
        # If guess comes after first word or is the first word
        if words[guess_index] >= first_word:
            # Go right
            floor_index = guess_index
        else:
            # Go left
            ceiling_index = guess_index
        
        # If floor and ceiling have converged
        if floor_index + 1 == ceiling_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is the first word
            return ceiling_index
    
    return 0
```

### 3. Search in Matrix

```python
def search_matrix_optimized(matrix, target):
    """Search in sorted matrix - start from top-right corner"""
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start from top-right
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down
    
    return False
```

## Advanced Searching Concepts

### 1. Search in Rotated Arrays

```python
def search_rotated_with_duplicates(nums, target):
    """Search in rotated sorted array with duplicates"""
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return True
        
        # Handle duplicates: skip equal elements
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False
```

### 2. Peak Finding

```python
def find_peak_element_2d(matrix):
    """Find peak element in 2D matrix"""
    rows, cols = len(matrix), len(matrix[0])
    
    def find_max_in_column(col):
        """Find row index of maximum element in column"""
        max_row = 0
        for i in range(rows):
            if matrix[i][col] > matrix[max_row][col]:
                max_row = i
        return max_row
    
    left, right = 0, cols - 1
    
    while left <= right:
        mid_col = (left + right) // 2
        max_row = find_max_in_column(mid_col)
        
        # Check if this element is a peak
        left_val = matrix[max_row][mid_col - 1] if mid_col > 0 else float('-inf')
        right_val = matrix[max_row][mid_col + 1] if mid_col < cols - 1 else float('-inf')
        
        if matrix[max_row][mid_col] >= left_val and matrix[max_row][mid_col] >= right_val:
            return (max_row, mid_col)
        elif left_val > matrix[max_row][mid_col]:
            right = mid_col - 1
        else:
            left = mid_col + 1
    
    return (-1, -1)
```

### 3. Search in Infinite Array

```python
def search_infinite_array(reader, target):
    """
    Search in infinite sorted array using ArrayReader interface
    ArrayReader.get(i) returns value at index i or 2^31 - 1 if i is out of bounds
    """
    # First, find bounds
    if reader.get(0) == target:
        return 0
    
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right *= 2
    
    # Binary search in the found bounds
    while left <= right:
        mid = (left + right) // 2
        mid_val = reader.get(mid)
        
        if mid_val == target:
            return mid
        elif mid_val > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1
```

## Practice Problems

### Beginner Level
1. **Binary Search**: Implement basic binary search
2. **First Bad Version**: Use binary search to find first occurrence
3. **Guess Number Higher or Lower**: Interactive binary search

### Intermediate Level
1. **Search in Rotated Array**: Modified binary search
2. **Find Peak Element**: Binary search on conditions
3. **Search a 2D Matrix**: Apply binary search concepts in 2D

### Advanced Level
1. **Median of Two Sorted Arrays**: Advanced binary search
2. **Find Minimum in Rotated Array**: Modified binary search
3. **Search in Sorted Matrix II**: Optimized search patterns

## Summary

Searching algorithms are essential for efficient data retrieval:

1. **Linear Search**: Simple but O(n) time complexity
2. **Binary Search**: Efficient O(log n) for sorted data
3. **Specialized Variants**: Adapted for specific use cases
4. **Applications**: Beyond basic search - optimization problems
5. **Trade-offs**: Time vs. space complexity considerations

Mastering searching algorithms provides the foundation for solving many computational problems efficiently. The next topic will cover Dynamic Programming, which builds solutions incrementally from smaller subproblems.