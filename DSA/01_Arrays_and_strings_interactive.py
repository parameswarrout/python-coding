import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
📊 DSA TOPIC 01: ARRAYS & STRINGS (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 01_Arrays_and_strings_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 01_Arrays_and_strings_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Array Mechanics, Memory Allocation & Complexity
# Arrays store elements in contiguous memory slots, giving $O(1)$ random access by index.
# Python lists are dynamic arrays (resizing automatically by over-allocating geometric buffers).

# %% [code]
def cell_1():
    """Cell 1: Array Fundamentals & CRUD Operations"""
    print("=" * 60)
    print("▶ CELL 1: Array Fundamentals & Dynamic List Operations")
    print("=" * 60)

    # Initial array
    nums = [10, 20, 30, 40, 50, 60, 70, 80]
    print(f"Original Array: {nums}")
    print(f"  First item (index 0):  {nums[0]} [O(1)]")
    print(f"  Last item (index -1):  {nums[-1]} [O(1)]")

    # In-place modification [O(1)]
    nums[2] = 35
    print(f"  After nums[2] = 35:    {nums}")

    # Append at end [Amortized O(1)]
    nums.append(90)
    print(f"  After append(90):      {nums}")

    # Insert at beginning [O(N) due to shifting all elements right]
    nums.insert(0, 5)
    print(f"  After insert(0, 5):    {nums}")

    # Pop from end [O(1)]
    popped = nums.pop()
    print(f"  After pop():           {nums} (Popped: {popped})")

    # Remove by value [O(N) search + shift]
    nums.remove(35)
    print(f"  After remove(35):      {nums}")


# %% [markdown]
# ### 📌 Cell 2: Two-Pointer Technique (In-Place Reversal & Palindromes)
# Two pointers (left and right) converge inward in $O(N)$ time and $O(1)$ auxiliary space.

# %% [code]
def cell_2():
    """Cell 2: Two Pointers for In-Place Reversal & Palindrome Checking"""
    print("=" * 60)
    print("▶ CELL 2: Two Pointers (In-Place Array Reversal & Palindrome)")
    print("=" * 60)

    def reverse_array_inplace(arr: list):
        left, right = 0, len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    def is_palindrome_string(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    sample_arr = [1, 2, 3, 4, 5, 6]
    print(f"Array before reverse: {sample_arr}")
    reverse_array_inplace(sample_arr)
    print(f"Array after reverse:  {sample_arr}")

    test_str1 = "A man, a plan, a canal: Panama"
    test_str2 = "race a car"
    print(f"\nIs '{test_str1}' palindrome? -> {is_palindrome_string(test_str1)}")
    print(f"Is '{test_str2}' palindrome? -> {is_palindrome_string(test_str2)}")


# %% [markdown]
# ### 📌 Cell 3: Sliding Window Technique (Max Sum Subarray of Size K)
# Maintaining window sums by adding incoming element and subtracting outgoing element in $O(N)$ time.

# %% [code]
def cell_3():
    """Cell 3: Sliding Window Technique"""
    print("=" * 60)
    print("▶ CELL 3: Sliding Window Technique (Max Subarray Sum of Size K)")
    print("=" * 60)

    def max_sub_array_of_size_k(k: int, arr: list) -> int:
        if len(arr) < k:
            return 0

        # Compute initial window of size k
        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            # Slide window: add right element, subtract leftmost element
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum

    data = [2, 1, 5, 1, 3, 2]
    k_val = 3
    result = max_sub_array_of_size_k(k_val, data)
    print(f"Array: {data}, Window Size K={k_val}")
    print(f"Max Subarray Sum: {result} (Subarray is [5, 1, 3])")


# %% [markdown]
# ### 📌 Cell 4: Prefix Sum Array & Range Sum Queries in $O(1)$
# Precomputing running cumulative sums allows any range query `sum(arr[L...R])` in $O(1)$ time:
# `RangeSum(L, R) = prefix[R + 1] - prefix[L]`

# %% [code]
def cell_4():
    """Cell 4: Prefix Sum Technique for O(1) Range Queries"""
    print("=" * 60)
    print("▶ CELL 4: Prefix Sum & O(1) Subarray Range Queries")
    print("=" * 60)

    class PrefixSumArray:
        def __init__(self, nums: list):
            self.prefix = [0] * (len(nums) + 1)
            for i, num in enumerate(nums):
                self.prefix[i + 1] = self.prefix[i] + num

        def query_range(self, left: int, right: int) -> int:
            """Returns sum of elements between index left and right inclusive."""
            return self.prefix[right + 1] - self.prefix[left]

    raw_nums = [3, 1, 4, 1, 5, 9, 2, 6]
    psa = PrefixSumArray(raw_nums)
    print(f"Array: {raw_nums}")
    print(f"Prefix Table: {psa.prefix}")

    print(f"Query Range sum(index 2 to 5) [4 + 1 + 5 + 9]: {psa.query_range(2, 5)}")
    print(f"Query Range sum(index 0 to 3) [3 + 1 + 4 + 1]: {psa.query_range(0, 3)}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Array Mechanics, CRUD & Time Complexity", cell_1),
    2: ("Two-Pointer Technique (In-Place Reversals & Palindromes)", cell_2),
    3: ("Sliding Window Technique (Max Window Sum)", cell_3),
    4: ("Prefix Sum Array & O(1) Range Queries", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 01_ARRAYS_AND_STRINGS_INTERACTIVE.PY")
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
                print("Usage: python 01_Arrays_and_strings_interactive.py [cell_number | --all]")
    else:
        run_all()
