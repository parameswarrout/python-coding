# 07 - Sorting Algorithms: Organizing Data Efficiently

## Table of Contents
1. [Introduction](#introduction)
2. [Sorting Fundamentals](#sorting-fundamentals)
3. [Comparison-Based Sorting](#comparison-based-sorting)
4. [Non-Comparison Sorting](#non-comparison-sorting)
5. [Python Implementation](#python-implementation)
6. [Time and Space Complexity](#time-and-space-complexity)
7. [Stability in Sorting](#stability-in-sorting)
8. [Applications and Use Cases](#applications-and-use-cases)
9. [Problem-Solving Patterns](#problem-solving-patterns)
10. [Advanced Sorting Concepts](#advanced-sorting-concepts)
11. [Practice Problems](#practice-problems)
12. [Summary](#summary)

## Introduction

Sorting algorithms are fundamental to computer science and are used to arrange elements in a specific order (typically ascending or descending). Understanding different sorting algorithms is crucial because they vary in efficiency, stability, and use cases.

Think of sorting like organizing your bookshelf - you could use different strategies depending on the number of books, how disorganized they are, and how much time you have.

## Sorting Fundamentals

### What is Sorting?
Sorting is the process of arranging elements in a particular order (numerical, alphabetical, etc.) based on a comparison operator.

### Why Sort?
- Enables faster searching (binary search requires sorted data)
- Helps in data analysis and visualization
- Prerequisite for many algorithms
- Improves data presentation

### Classification of Sorting Algorithms:
1. **Based on Time Complexity**: O(n²), O(n log n), O(n)
2. **Based on Space Complexity**: In-place vs. out-of-place
3. **Based on Stability**: Stable vs. unstable
4. **Based on Adaptability**: Adaptive vs. non-adaptive

## Comparison-Based Sorting

### 1. Bubble Sort
Repeatedly swaps adjacent elements if they're in the wrong order.

```python
def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Optimization: if no swap occurred, array is sorted
            break
    return arr
```

### 2. Selection Sort
Finds the minimum element and places it at the beginning.

```python
def selection_sort(arr):
    """Selection sort implementation"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 3. Insertion Sort
Builds the sorted array one element at a time.

```python
def insertion_sort(arr):
    """Insertion sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### 4. Merge Sort
Divide and conquer algorithm that divides the array and merges sorted halves.

```python
def merge_sort(arr):
    """Merge sort implementation"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Helper function to merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
```

### 5. Quick Sort
Divide and conquer algorithm that picks a pivot and partitions around it.

```python
def quick_sort(arr):
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# In-place version
def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort implementation"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    """Partition function for quick sort"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

### 6. Heap Sort
Uses a binary heap data structure to sort elements.

```python
def heap_sort(arr):
    """Heap sort implementation"""
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)  # Call heapify on reduced heap
    
    return arr

def heapify(arr, n, i):
    """Helper function to maintain heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

## Non-Comparison Sorting

### 1. Counting Sort
Counts occurrences of each element and reconstructs the sorted array.

```python
def counting_sort(arr):
    """Counting sort implementation"""
    if not arr:
        return arr
    
    # Find range of input
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Create count array
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Store count of each element
    for num in arr:
        count[num - min_val] += 1
    
    # Change count[i] to actual position
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    # Copy output array to arr
    for i in range(len(arr)):
        arr[i] = output[i]
    
    return arr
```

### 2. Radix Sort
Sorts numbers digit by digit from least to most significant.

```python
def radix_sort(arr):
    """Radix sort implementation"""
    if not arr:
        return arr
    
    # Find maximum number to know number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr

def counting_sort_by_digit(arr, exp):
    """Counting sort for specific digit"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] to actual position
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy output array to arr
    for i in range(n):
        arr[i] = output[i]
```

### 3. Bucket Sort
Distributes elements into buckets and sorts individual buckets.

```python
def bucket_sort(arr):
    """Bucket sort implementation"""
    if len(arr) <= 1:
        return arr
    
    # Find maximum and minimum values
    max_val, min_val = max(arr), min(arr)
    bucket_range = (max_val - min_val) / len(arr)
    
    # Create buckets
    buckets = [[] for _ in range(len(arr))]
    
    # Distribute input array values into buckets
    for num in arr:
        if num == max_val:
            # Put maximum value in last bucket
            bucket_idx = len(buckets) - 1
        else:
            bucket_idx = int((num - min_val) / bucket_range)
        buckets[bucket_idx].append(num)
    
    # Sort individual buckets and concatenate
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(insertion_sort(bucket))
    
    return sorted_arr
```

## Time and Space Complexity

### Comparison of Sorting Algorithms

| Algorithm | Best Case | Average Case | Worst Case | Space | Stable | Adaptive |
|-----------|-----------|--------------|------------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes | No |
| Radix Sort | O(d*(n+k)) | O(d*(n+k)) | O(d*(n+k)) | O(n+k) | Yes | No |
| Bucket Sort | O(n+k) | O(n+k) | O(n²) | O(n) | Yes | No |

Where:
- n = number of elements
- k = range of input
- d = number of digits

## Stability in Sorting

A sorting algorithm is stable if it preserves the relative order of equal elements.

### Stable Algorithms:
- Merge Sort
- Bubble Sort
- Insertion Sort
- Counting Sort
- Radix Sort
- Bucket Sort

### Unstable Algorithms:
- Quick Sort
- Heap Sort
- Selection Sort

```python
def stable_selection_sort(arr):
    """A stable version of selection sort"""
    n = len(arr)
    
    # Note: This is not truly selection sort anymore, but maintains stability
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Instead of swapping, shift elements
        key = arr[min_idx]
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        arr[i] = key
    
    return arr
```

## Applications and Use Cases

### 1. When to Use Each Algorithm

- **Small datasets (< 50 elements)**: Insertion Sort
- **Nearly sorted data**: Insertion Sort or Bubble Sort
- **Guaranteed O(n log n)**: Merge Sort
- **Memory constrained**: Heap Sort
- **Average case performance**: Quick Sort
- **Integers with limited range**: Counting Sort
- **Floating point numbers**: Bucket Sort
- **Multi-key sorting**: Radix Sort

### 2. Real-World Applications

```python
def sort_students_by_grade(students):
    """Sort students by grade, maintaining original order for ties"""
    # Use stable sort to maintain original order for same grades
    return sorted(students, key=lambda x: x['grade'])

def sort_products_by_price(products):
    """Sort products by price using efficient algorithm"""
    # For large datasets, use built-in sort (Timsort)
    return sorted(products, key=lambda x: x['price'])

def sort_large_dataset_integers(numbers):
    """For large dataset of integers with known range"""
    # Use counting sort if range is not too large
    if max(numbers) - min(numbers) < len(numbers):
        return counting_sort(numbers.copy())
    else:
        # Use merge sort for guaranteed O(n log n)
        return merge_sort(numbers)
```

## Problem-Solving Patterns

### 1. Sorting for Optimization

```python
def two_sum_sorted(arr, target):
    """Find two numbers that sum to target in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def merge_intervals(intervals):
    """Merge overlapping intervals"""
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged
```

### 2. Custom Sorting

```python
from functools import cmp_to_key

def custom_sort_strings(strings):
    """Sort strings by length, then alphabetically"""
    def compare(a, b):
        if len(a) != len(b):
            return len(a) - len(b)
        else:
            return -1 if a < b else (1 if a > b else 0)
    
    return sorted(strings, key=cmp_to_key(compare))

def sort_colors(nums):
    """Sort array with only 0, 1, 2 (Dutch National Flag)"""
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    
    return nums
```

### 3. Kth Largest/Smallest

```python
import heapq

def find_kth_largest(arr, k):
    """Find kth largest element using heap"""
    # Use min heap of size k
    heap = []
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

def find_kth_largest_quickselect(arr, k):
    """Find kth largest element using quickselect"""
    def quickselect(left, right, k_smallest):
        if left == right:
            return arr[left]
        
        # Choose random pivot
        import random
        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return arr[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    def partition(arr, left, right, pivot_index):
        pivot = arr[pivot_index]
        # Move pivot to end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        store_index = left
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1
        
        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index
    
    return quickselect(0, len(arr) - 1, len(arr) - k)
```

## Advanced Sorting Concepts

### 1. External Sorting
For data that doesn't fit in memory:

```python
def external_merge_sort(input_file, output_file, chunk_size):
    """External merge sort for large files"""
    # Step 1: Split input into sorted chunks
    chunk_files = []
    with open(input_file, 'r') as f:
        chunk_num = 0
        while True:
            chunk = []
            for _ in range(chunk_size):
                line = f.readline()
                if not line:
                    break
                chunk.append(int(line.strip()))
            
            if not chunk:
                break
            
            # Sort chunk in memory
            chunk.sort()
            
            # Write sorted chunk to temporary file
            chunk_file = f'chunk_{chunk_num}.txt'
            with open(chunk_file, 'w') as cf:
                for num in chunk:
                    cf.write(f'{num}\n')
            chunk_files.append(chunk_file)
            chunk_num += 1
    
    # Step 2: Merge sorted chunks
    merge_sorted_files(chunk_files, output_file)
    
    # Clean up temporary files
    import os
    for chunk_file in chunk_files:
        os.remove(chunk_file)

def merge_sorted_files(file_list, output_file):
    """Merge multiple sorted files"""
    import heapq
    
    # Open all files and create iterators
    file_handles = [open(f, 'r') for f in file_list]
    heap = []
    
    # Initialize heap with first element from each file
    for i, fh in enumerate(file_handles):
        line = fh.readline()
        if line:
            heapq.heappush(heap, (int(line.strip()), i))
    
    with open(output_file, 'w') as out:
        while heap:
            value, file_idx = heapq.heappop(heap)
            out.write(f'{value}\n')
            
            # Read next line from the same file
            next_line = file_handles[file_idx].readline()
            if next_line:
                heapq.heappush(heap, (int(next_line.strip()), file_idx))
    
    # Close all file handles
    for fh in file_handles:
        fh.close()
```

### 2. Timsort (Python's Built-in Sort)
Hybrid stable sorting algorithm derived from merge sort and insertion sort:

```python
def timsort_concept(arr):
    """Conceptual implementation of Timsort principles"""
    MIN_MERGE = 32
    
    def calc_min_run(n):
        """Calculate minimum run length"""
        r = 0
        while n >= MIN_MERGE:
            r |= n & 1
            n >>= 1
        return n + r
    
    def insertion_sort_range(arr, left, right):
        """Insertion sort for small ranges"""
        for i in range(left + 1, right + 1):
            j = i
            while j > left and arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1
    
    def merge(arr, l, m, r):
        """Merge function for tim sort"""
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        
        for i in range(0, len1):
            left.append(arr[l + i])
        for i in range(0, len2):
            right.append(arr[m + 1 + i])
        
        i, j, k = 0, 0, l
        
        while i < len1 and j < len2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len1:
            arr[k] = left[i]
            k += 1
            i += 1
        
        while j < len2:
            arr[k] = right[j]
            k += 1
            j += 1
    
    n = len(arr)
    min_run = calc_min_run(n)
    
    # Sort individual subarrays of size RUN
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)
    
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = min_run
    while size < n:
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+size*2-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)
        
        size = 2 * size
    
    return arr
```

## Practice Problems

### Beginner Level
1. **Sort Array**: Implement basic sorting algorithms
2. **Sort Colors**: Sort array with only 3 distinct values
3. **Kth Largest Element**: Find kth largest without full sorting

### Intermediate Level
1. **Merge Intervals**: Merge overlapping intervals
2. **Sort List**: Sort linked list in O(n log n)
3. **Wiggle Sort**: Arrange array in wiggle pattern

### Advanced Level
1. **Skyline Problem**: Use sorting for geometric problem
2. **Count of Smaller Numbers**: Use merge sort for counting
3. **Reverse Pairs**: Count pairs with specific condition

## Summary

Sorting algorithms are essential tools with different trade-offs:

1. **Selection Criteria**: Dataset size, stability needs, memory constraints
2. **Time Complexity**: Trade-off between best/average/worst cases
3. **Space Complexity**: In-place vs. extra space requirements
4. **Stability**: Preserving relative order of equal elements
5. **Practical Use**: Python's Timsort combines multiple approaches

Understanding sorting algorithms provides insight into algorithm design principles and serves as a foundation for solving many computational problems. The next topic will cover Searching Algorithms, which often work in conjunction with sorted data.