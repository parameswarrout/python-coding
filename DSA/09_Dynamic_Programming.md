# 09 - Dynamic Programming: Solving Optimization Problems

## Table of Contents
1. [Introduction](#introduction)
2. [Dynamic Programming Fundamentals](#dynamic-programming-fundamentals)
3. [Memoization vs Tabulation](#memoization-vs-tabulation)
4. [Identifying DP Problems](#identifying-dp-problems)
5. [Python Implementation](#python-implementation)
6. [Classic DP Problems](#classic-dp-problems)
7. [Time and Space Complexity](#time-and-space-complexity)
8. [Applications and Use Cases](#applications-and-use-cases)
9. [Problem-Solving Patterns](#problem-solving-patterns)
10. [Advanced DP Concepts](#advanced-dp-concepts)
11. [Practice Problems](#practice-problems)
12. [Summary](#summary)

## Introduction

Dynamic Programming (DP) is a powerful algorithmic technique for solving complex problems by breaking them down into simpler subproblems. It's particularly effective for optimization problems where the solution can be constructed from optimal solutions to subproblems.

Think of DP like climbing stairs where you remember how many ways you reached each step, so you don't recalculate when you need that information again. It's about trading space for time by storing computed results.

## Dynamic Programming Fundamentals

### What is Dynamic Programming?

Dynamic Programming is a method for solving problems with:
1. **Overlapping Subproblems**: The problem can be broken down into subproblems that are solved multiple times
2. **Optimal Substructure**: The optimal solution contains optimal solutions to subproblems

### Key Principles:
- **Memoization**: Store results of expensive function calls
- **Tabulation**: Build solution bottom-up using iteration
- **State Definition**: Define what each state represents
- **Transition**: Define how to move from one state to another

## Memoization vs Tabulation

### Memoization (Top-Down)
Solve the problem recursively, storing results to avoid recomputation.

```python
def fibonacci_memo(n, memo={}):
    """Fibonacci using memoization"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Better practice: avoid mutable defaults
def fibonacci_memo_correct(n, memo=None):
    """Corrected fibonacci with memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memo_correct(n-1, memo) + fibonacci_memo_correct(n-2, memo)
    return memo[n]
```

### Tabulation (Bottom-Up)
Solve subproblems iteratively, building up to the final solution.

```python
def fibonacci_tab(n):
    """Fibonacci using tabulation"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

# Space-optimized version
def fibonacci_optimized(n):
    """Space-optimized fibonacci"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

## Identifying DP Problems

### Common Indicators:
1. **Optimization**: Finding maximum/minimum
2. **Counting**: Counting number of ways
3. **Decision**: Whether something is possible
4. **Recursion**: Natural recursive structure
5. **Overlapping**: Same subproblems solved multiple times

### Classic Patterns:
- **Fibonacci-like sequences**
- **Grid/path problems**
- **Knapsack variations**
- **Longest common subsequence**
- **Matrix chain multiplication**

## Python Implementation

### 1. Climbing Stairs Problem

```python
def climb_stairs(n):
    """Number of ways to climb n stairs (1 or 2 steps)"""
    # Memoization approach
    memo = {}
    
    def helper(steps):
        if steps in memo:
            return memo[steps]
        
        if steps <= 1:
            return 1
        
        memo[steps] = helper(steps-1) + helper(steps-2)
        return memo[steps]
    
    return helper(n)

def climb_stairs_dp(n):
    """Climbing stairs using DP"""
    if n <= 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def climb_stairs_space_optimized(n):
    """Space-optimized climbing stairs"""
    if n <= 1:
        return 1
    
    prev2, prev1 = 1, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1
```

### 2. House Robber Problem

```python
def house_robber(nums):
    """Maximum money that can be robbed without robbing adjacent houses"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Memoization
    memo = {}
    
    def rob_from(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        
        # Rob current house and skip next, or skip current
        memo[i] = max(nums[i] + rob_from(i + 2), rob_from(i + 1))
        return memo[i]
    
    return rob_from(0)

def house_robber_dp(nums):
    """House robber using DP"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    
    return dp[n-1]

def house_robber_optimized(nums):
    """Space-optimized house robber"""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1
```

## Classic DP Problems

### 1. 0/1 Knapsack Problem

```python
def knapsack(weights, values, capacity):
    """0/1 Knapsack problem - maximum value with weight constraint"""
    n = len(weights)
    # dp[i][w] = maximum value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i-1][w]
            
            # Take item i-1 if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    return dp[n][capacity]

def knapsack_optimized(weights, values, capacity):
    """Space-optimized knapsack"""
    n = len(weights)
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Traverse backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```

### 2. Longest Common Subsequence (LCS)

```python
def longest_common_subsequence(text1, text2):
    """Find length of longest common subsequence"""
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS of text1[0:i] and text2[0:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

def lcs_with_sequence(text1, text2):
    """Return the actual LCS string"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))
```

### 3. Coin Change Problem

```python
def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_ways(coins, amount):
    """Number of ways to make amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0: use no coins
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]
```

## Time and Space Complexity

### Common DP Complexities

| Problem Type | Time Complexity | Space Complexity | Notes |
|--------------|----------------|------------------|-------|
| 1D DP | O(n) | O(n) or O(1) | Often space-optimizable |
| 2D Grid DP | O(m×n) | O(m×n) or O(min(m,n)) | Sometimes optimizable |
| Knapsack | O(n×W) | O(W) | W = capacity |
| LCS | O(m×n) | O(min(m,n)) | With space optimization |
| Matrix Chain Multiplication | O(n³) | O(n²) | n = number of matrices |

## Applications and Use Cases

### 1. Resource Allocation
```python
def max_profit_jobs(startTime, endTime, profit):
    """Maximum profit job scheduling"""
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)
    
    # dp[i] = max profit considering first i jobs
    dp = [0] * n
    
    dp[0] = jobs[0][2]  # Profit of first job
    
    for i in range(1, n):
        # Option 1: Don't take current job
        profit_without = dp[i-1]
        
        # Option 2: Take current job
        current_profit = jobs[i][2]
        
        # Find latest job that doesn't conflict with current job
        latest_compatible = binary_search_latest(jobs, i)
        
        if latest_compatible != -1:
            current_profit += dp[latest_compatible]
        
        dp[i] = max(profit_without, current_profit)
    
    return dp[n-1] if n > 0 else 0

def binary_search_latest(jobs, index):
    """Find latest job that finishes before jobs[index] starts"""
    start_time = jobs[index][0]
    left, right = 0, index - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        if jobs[mid][1] <= start_time:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return result
```

### 2. Game Theory
```python
def predict_the_winner(nums):
    """Predict if player 1 can win the game"""
    n = len(nums)
    # dp[i][j] = max score difference (current player - opponent) for subarray nums[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Fill diagonal (single elements)
    for i in range(n):
        dp[i][i] = nums[i]
    
    # Fill for subarrays of length 2 to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Take left element: nums[i] - opponent's best play on remaining
            take_left = nums[i] - dp[i+1][j]
            # Take right element: nums[j] - opponent's best play on remaining
            take_right = nums[j] - dp[i][j-1]
            dp[i][j] = max(take_left, take_right)
    
    return dp[0][n-1] >= 0
```

## Problem-Solving Patterns

### 1. State Machine DP
```python
def max_profit_transactions(prices, k):
    """Maximum profit with at most k transactions"""
    if not prices or k == 0:
        return 0
    
    n = len(prices)
    
    # If k >= n//2, we can do unlimited transactions
    if k >= n // 2:
        return max_profit_unlimited(prices)
    
    # buy[i][j] = max profit at day i with at most j transactions and holding stock
    # sell[i][j] = max profit at day i with at most j transactions and not holding stock
    buy = [[-float('inf')] * (k + 1) for _ in range(n)]
    sell = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(1, k + 1):
            if i == 0:
                buy[i][j] = -prices[i]
            else:
                buy[i][j] = max(buy[i-1][j], sell[i-1][j] - prices[i])
                sell[i][j] = max(sell[i-1][j], buy[i-1][j-1] + prices[i])
    
    return sell[n-1][k]

def max_profit_unlimited(prices):
    """Maximum profit with unlimited transactions"""
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
```

### 2. Interval DP
```python
def burst_balloons(nums):
    """Burst balloons to maximize coins"""
    # Add boundary balloons with value 1
    nums = [1] + nums + [1]
    n = len(nums)
    
    # dp[i][j] = max coins obtainable from bursting balloons between i and j (exclusive)
    dp = [[0] * n for _ in range(n)]
    
    # Length of interval
    for length in range(2, n):  # At least 2 elements between i and j
        for left in range(n - length):
            right = left + length
            
            # Try each balloon as the last to burst
            for k in range(left + 1, right):
                coins = nums[left] * nums[k] * nums[right]
                total = dp[left][k] + coins + dp[k][right]
                dp[left][right] = max(dp[left][right], total)
    
    return dp[0][n-1]
```

### 3. Digit DP
```python
def count_numbers_with_unique_digits(n):
    """Count numbers with unique digits"""
    if n == 0:
        return 1
    if n == 1:
        return 10
    
    # dp[i] = count of i-digit numbers with unique digits
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 9  # First digit can be 1-9
    
    result = 10  # 0 and 1-digit numbers
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] * (11 - i)  # Available choices decrease
        result += dp[i]
    
    return result
```

## Advanced DP Concepts

### 1. Bitmask DP
```python
def shortest_superstring(words):
    """Find shortest superstring containing all words as substrings"""
    n = len(words)
    
    # Precompute overlaps: overlap[i][j] = overlap of words[i] and words[j]
    overlap = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                # Find maximum overlap of words[i]'s suffix with words[j]'s prefix
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break
    
    # dp[mask][i] = minimum length to visit all words in mask, ending at word i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    # Initialize: start at each word
    for i in range(n):
        dp[1 << i][i] = len(words[i])
    
    # Fill DP table
    for mask in range(1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            
            for j in range(n):
                if mask & (1 << j):
                    continue
                
                next_mask = mask | (1 << j)
                new_len = dp[mask][i] + len(words[j]) - overlap[i][j]
                
                if new_len < dp[next_mask][j]:
                    dp[next_mask][j] = new_len
                    parent[next_mask][j] = i
    
    # Find minimum length tour
    final_mask = (1 << n) - 1
    min_len = min(dp[final_mask])
    
    # Reconstruct path (simplified)
    return min_len
```

### 2. Tree DP
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob_house_tree(root):
    """Rob houses arranged in tree structure"""
    def dfs(node):
        # Returns [max money if rob current, max money if don't rob current]
        if not node:
            return [0, 0]
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # Rob current: can't rob children
        rob_current = node.val + left[1] + right[1]
        # Don't rob current: can rob or not rob children (take max)
        not_rob_current = max(left) + max(right)
        
        return [rob_current, not_rob_current]
    
    return max(dfs(root))
```

### 3. Game Theory DP
```python
def stone_game(piles):
    """Stone game where players take stones from ends"""
    n = len(piles)
    # dp[i][j] = max stones current player can get more than opponent
    # from piles[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # Fill diagonal
    for i in range(n):
        dp[i][i] = piles[i]
    
    # Fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # Take left pile: get piles[i] + (remaining game value)
            take_left = piles[i] - dp[i+1][j]
            # Take right pile: get piles[j] + (remaining game value)
            take_right = piles[j] - dp[i][j-1]
            dp[i][j] = max(take_left, take_right)
    
    # If dp[0][n-1] > 0, first player wins
    return dp[0][n-1] > 0
```

## Practice Problems

### Beginner Level
1. **Fibonacci Number**: Basic DP concept
2. **Climbing Stairs**: Simple recurrence relation
3. **House Robber**: Decision-making DP

### Intermediate Level
1. **Coin Change**: Counting/minimization DP
2. **Longest Increasing Subsequence**: Subsequence DP
3. **Unique Paths**: Grid DP

### Advanced Level
1. **Edit Distance**: String transformation DP
2. **Regular Expression Matching**: Complex state transitions
3. **Wildcard Matching**: Pattern matching DP

## Summary

Dynamic Programming is a powerful technique for optimization problems:

1. **Core Concept**: Break problems into overlapping subproblems
2. **Approaches**: Memoization (top-down) vs. tabulation (bottom-up)
3. **Patterns**: Recognize common DP problem types
4. **Optimization**: Space optimization where possible
5. **Applications**: Wide range of optimization problems

DP requires practice to recognize patterns and formulate state transitions effectively. The next topic will cover Greedy Algorithms, which make locally optimal choices in hopes of finding global optima.