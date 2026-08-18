import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
🧩 DSA TOPIC 09: DYNAMIC PROGRAMMING (Interactive Cell-by-Cell in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 09_Dynamic_Programming_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 09_Dynamic_Programming_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Memoization vs Tabulation (Climbing Stairs)
# - **Memoization (Top-Down)**: Recursion with caching table to eliminate overlapping subproblems.
# - **Tabulation (Bottom-Up)**: Iterative filling of DP array starting from base cases with $O(1)$ space optimization.

# %% [code]
def cell_1():
    """Cell 1: Climbing Stairs (Top-Down vs Bottom-Up vs O(1) Space)"""
    print("=" * 60)
    print("▶ CELL 1: Climbing Stairs (Memoization vs Tabulation)")
    print("=" * 60)

    # 1. Top-Down Memoization
    def climb_memo(n: int, memo={}) -> int:
        if n <= 2:
            return n
        if n not in memo:
            memo[n] = climb_memo(n - 1, memo) + climb_memo(n - 2, memo)
        return memo[n]

    # 2. Bottom-Up Tabulation with O(1) Space
    def climb_tab_optimized(n: int) -> int:
        if n <= 2:
            return n
        prev2, prev1 = 1, 2
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        return prev1

    n_steps = 10
    print(f"Distinct ways to climb {n_steps} stairs (Memoization): {climb_memo(n_steps)}")
    print(f"Distinct ways to climb {n_steps} stairs (Tabulation):  {climb_tab_optimized(n_steps)}")


# %% [markdown]
# ### 📌 Cell 2: 0/1 Knapsack Problem ($O(N \cdot W)$ 2D/1D Tabulation)
# Maximize value of items placed in knapsack without exceeding capacity $W$. Each item can be picked at most once.

# %% [code]
def cell_2():
    """Cell 2: 0/1 Knapsack Tabulation"""
    print("=" * 60)
    print("▶ CELL 2: 0/1 Knapsack Problem (1D Space-Optimized DP)")
    print("=" * 60)

    def knapsack_01(weights: list, values: list, capacity: int) -> int:
        # 1D array traversed backwards to prevent using the same item multiple times
        dp = [0] * (capacity + 1)
        for w, v in zip(weights, values):
            for cap in range(capacity, w - 1, -1):
                dp[cap] = max(dp[cap], dp[cap - w] + v)
        return dp[capacity]

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    max_val = knapsack_01(weights, values, capacity)
    print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"Maximum Obtainable Value: {max_val}")


# %% [markdown]
# ### 📌 Cell 3: Longest Common Subsequence (LCS 2D Table)
# Finding length of longest subsequence present in both strings in same relative order.

# %% [code]
def cell_3():
    """Cell 3: Longest Common Subsequence (LCS)"""
    print("=" * 60)
    print("▶ CELL 3: Longest Common Subsequence (LCS 2D Grid)")
    print("=" * 60)

    def longest_common_subsequence(text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

    s1, s2 = "abcde", "ace"
    lcs_len = longest_common_subsequence(s1, s2)
    print(f"String 1: '{s1}', String 2: '{s2}'")
    print(f"LCS Length: {lcs_len} (Subsequence is 'ace')")


# %% [markdown]
# ### 📌 Cell 4: Coin Change (Minimum Coins to Form Amount)
# Unbounded knapsack dynamic programming solving minimum steps.

# %% [code]
def cell_4():
    """Cell 4: Coin Change Minimum Coins (LC 322)"""
    print("=" * 60)
    print("▶ CELL 4: Coin Change (Minimum Coins DP)")
    print("=" * 60)

    def coin_change(coins: list, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    coins = [1, 2, 5]
    amount = 11
    min_coins = coin_change(coins, amount)
    print(f"Coins: {coins}, Amount: {amount}")
    print(f"Minimum Coins Needed: {min_coins} (5 + 5 + 1 = 11)")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Climbing Stairs (Memoization vs Tabulation)", cell_1),
    2: ("0/1 Knapsack Problem (Space-Optimized DP)", cell_2),
    3: ("Longest Common Subsequence (LCS 2D Table)", cell_3),
    4: ("Coin Change Minimum Coins (Unbounded DP)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 09_DYNAMIC_PROGRAMMING_INTERACTIVE.PY")
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
                print("Usage: python 09_Dynamic_Programming_interactive.py [cell_number | --all]")
    else:
        run_all()
