# 04 - Hashing and Hash Tables: Efficient Key-Value Storage

## Table of Contents
1. [Introduction](#introduction)
2. [Hash Functions Explained](#hash-functions-explained)
3. [Hash Table Structure](#hash-table-structure)
4. [Collision Resolution](#collision-resolution)
5. [Python Implementation](#python-implementation)
6. [Common Operations](#common-operations)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Applications and Use Cases](#applications-and-use-cases)
9. [Problem-Solving Patterns](#problem-solving-patterns)
10. [Advanced Concepts](#advanced-concepts)
11. [Practice Problems](#practice-problems)
12. [Summary](#summary)

## Introduction

Hash tables (also called hash maps or dictionaries) are among the most important data structures in computer science. They provide average O(1) time complexity for insertion, deletion, and lookup operations, making them incredibly efficient for many applications.

Think of a hash table as a sophisticated filing cabinet where each document (value) has a unique identifier (key) that determines exactly which drawer (bucket) it goes in. The hash function acts as the filing clerk who knows exactly where each document belongs.

## Hash Functions Explained

### What is a Hash Function?

A hash function takes an input (key) and returns an integer (hash code) that determines where the corresponding value is stored in the hash table.

**Analogy**: A hash function is like a GPS system that converts an address (key) into coordinates (hash code) that pinpoint the exact location (index) where something is stored.

### Properties of Good Hash Functions:
1. **Deterministic**: Same input always produces same output
2. **Uniform Distribution**: Distributes keys evenly across buckets
3. **Efficient**: Computes quickly
4. **Minimizes Collisions**: Different inputs should rarely produce same output

### Simple Hash Function Example:

```python
def simple_hash(key, table_size):
    """Simple hash function for demonstration"""
    hash_code = 0
    for char in str(key):
        hash_code = (hash_code * 31 + ord(char)) % table_size
    return hash_code
```

## Hash Table Structure

### Basic Structure

A hash table consists of:
1. **Array of Buckets**: Fixed-size array where values are stored
2. **Hash Function**: Maps keys to array indices
3. **Collision Resolution Strategy**: Handles when multiple keys map to same index

```
Index:    0     1     2     3     4     5
Table: [____] [____] [____] [____] [____] [____]
        Key:  Key:  Key:  Key:  Key:  Key:
        Val:  Val:  Val:  Val:  Val:  Val:
```

## Collision Resolution

### 1. Chaining (Separate Chaining)
When multiple keys hash to the same index, store them in a linked list at that index.

```
Index 0: [key1->val1] -> [key4->val4] -> [key7->val7] -> NULL
Index 1: [key2->val2] -> NULL
Index 2: [key3->val3] -> [key5->val5] -> NULL
```

### 2. Open Addressing
When collision occurs, find another available slot using probing techniques:
- **Linear Probing**: Check next slot (i+1, i+2, ...)
- **Quadratic Probing**: Check slots (i+1², i+2², ...)
- **Double Hashing**: Use second hash function

## Python Implementation

### Basic Hash Table with Chaining

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # List of lists for chaining
    
    def _hash(self, key):
        """Simple hash function"""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            return hash(key) % self.size
    
    def put(self, key, value):
        """Insert key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        # Check if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Add new key-value pair
        bucket.append((key, value))
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove key-value pair"""
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def display(self):
        """Display hash table contents"""
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
```

### Hash Table with Linear Probing (Open Addressing)

```python
class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.deleted = [False] * size  # Track deleted slots
    
    def _hash(self, key):
        """Hash function"""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        elif isinstance(key, int):
            return key % self.size
        else:
            return hash(key) % self.size
    
    def _probe(self, key):
        """Linear probing to find key or empty slot"""
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                return index
            index = (index + 1) % self.size
            
            # If we've gone full circle
            if index == self._hash(key):
                break
        
        return index
    
    def put(self, key, value):
        """Insert key-value pair"""
        index = self._probe(key)
        
        if self.keys[index] is None or self.deleted[index]:
            # Found empty or previously deleted slot
            self.keys[index] = key
            self.values[index] = value
            self.deleted[index] = False
        else:
            # Key already exists, update value
            self.values[index] = value
    
    def get(self, key):
        """Retrieve value by key"""
        index = self._probe(key)
        
        if self.keys[index] == key and not self.deleted[index]:
            return self.values[index]
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        """Remove key-value pair"""
        index = self._probe(key)
        
        if self.keys[index] == key and not self.deleted[index]:
            self.deleted[index] = True
            return self.values[index]
        
        raise KeyError(f"Key '{key}' not found")
```

## Common Operations

### Dictionary Operations in Python

Python's built-in dictionary is implemented as a hash table:

```python
# Creating a dictionary
d = {}
d = dict()
d = {'a': 1, 'b': 2, 'c': 3}

# Common operations
d['key'] = 'value'        # Insert/update - O(1) average
value = d['key']          # Access - O(1) average
value = d.get('key', 'default')  # Safe access with default
del d['key']              # Delete - O(1) average
'key' in d               # Membership test - O(1) average
len(d)                   # Size - O(1)
```

## Time and Space Complexity

### Average Case Complexity

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert | O(1) | O(1) |
| Lookup | O(1) | O(1) |
| Delete | O(1) | O(1) |
| Space | - | O(n) |

### Worst Case Complexity
- When all keys collide: O(n) for all operations
- This happens with poor hash functions or when load factor is too high

### Load Factor
Load factor = (number of elements) / (size of hash table)
- Ideal load factor: < 0.7 for good performance
- Higher load factor → more collisions → worse performance

## Applications and Use Cases

### 1. Counting Frequencies
```python
def count_frequencies(arr):
    freq_map = {}
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    return freq_map
```

### 2. Caching/Memoization
```python
cache = {}

def fibonacci_memo(n):
    if n in cache:
        return cache[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
    cache[n] = result
    return result
```

### 3. Two Sum Problem
```python
def two_sum(nums, target):
    seen = {}  # value -> index mapping
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

## Problem-Solving Patterns

### 1. Frequency Counting
```python
def is_anagram(s, t):
    """Check if two strings are anagrams"""
    if len(s) != len(t):
        return False
    
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] == 0:
            del count[char]
    
    return len(count) == 0
```

### 2. Two Pointer with Hash Map
```python
def longest_substring_without_repeating(s):
    """Longest substring without repeating characters"""
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

### 3. Grouping with Hash Map
```python
def group_anagrams(strs):
    """Group anagrams together"""
    groups = {}
    for s in strs:
        # Sort characters to create a canonical form
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    
    return list(groups.values())
```

## Advanced Concepts

### 1. Perfect Hashing
For static sets of keys, create a hash function with no collisions.

### 2. Bloom Filters
Probabilistic data structure that can test membership with small memory footprint (may have false positives but never false negatives).

```python
import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size
    
    def _hash(self, item, seed):
        """Generate hash with different seeds"""
        h = hashlib.md5((str(item) + str(seed)).encode())
        return int(h.hexdigest(), 16) % self.size
    
    def add(self, item):
        """Add item to bloom filter"""
        for i in range(self.hash_count):
            index = self._hash(item, i)
            self.bit_array[index] = 1
    
    def check(self, item):
        """Check if item might be in set"""
        for i in range(self.hash_count):
            index = self._hash(item, i)
            if self.bit_array[index] == 0:
                return False
        return True  # May be present (false positive possible)
```

### 3. Open Addressing with Quadratic Probing
```python
class QuadraticProbingHashTable:
    def __init__(self, size=11):  # Prime number for better distribution
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def _quadratic_probe(self, key):
        index = self._hash(key)
        i = 0
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return index
            i += 1
            index = (self._hash(key) + i*i) % self.size
            
            # Prevent infinite loop
            if i >= self.size:
                break
        
        return index
```

### 4. Resizable Hash Table
```python
class ResizableHashTable:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        self.load_factor_threshold = 0.75
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def _resize(self):
        """Resize table when load factor exceeds threshold"""
        old_table = self.table
        self.size *= 2
        self.count = 0
        self.table = [[] for _ in range(self.size)]
        
        # Rehash all elements
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)
    
    def put(self, key, value):
        # Resize if needed
        if self.count >= self.size * self.load_factor_threshold:
            self._resize()
        
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
```

## Practice Problems

### Beginner Level
1. **Two Sum**: Find two numbers that add up to target
2. **Contains Duplicate**: Check if array has duplicates
3. **Valid Anagram**: Determine if two strings are anagrams

### Intermediate Level
1. **Group Anagrams**: Group words that are anagrams
2. **Longest Consecutive Sequence**: Find longest consecutive sequence
3. **LRU Cache**: Design least recently used cache

### Advanced Level
1. **Design In-Memory File System**: Implement file system with hash tables
2. **Snapshot Array**: Implement array with snapshot functionality
3. **Random Pick with Blacklist**: Efficient random selection with exclusions

## Summary

Hash tables provide exceptional performance for key-value operations:

1. **Efficiency**: Average O(1) time for insert, lookup, and delete
2. **Flexibility**: Handle various data types as keys
3. **Implementation**: Chaining vs. open addressing approaches
4. **Applications**: Caching, frequency counting, indexing
5. **Considerations**: Hash function quality affects performance

Hash tables are fundamental to many algorithms and data structures, making them essential knowledge for any programmer. The next topic will cover Trees and Binary Search Trees, which provide hierarchical data organization.