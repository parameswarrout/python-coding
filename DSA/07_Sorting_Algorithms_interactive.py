import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
📶 DSA TOPIC 07: SORTING ALGORITHMS (Interactive Cell-by-Cell in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 07_Sorting_Algorithms_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 07_Sorting_Algorithms_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Quadratic Sorts (Bubble, Selection, Insertion Sort)
# - **Bubble Sort**: Adjacent swaps bubbling the maximum element to the right ($O(N^2)$)
# - **Selection Sort**: Find minimum in unsorted suffix and swap with prefix ($O(N^2)$)
# - **Insertion Sort**: Insert each element into its sorted left partition ($O(N)$ best case)

# %% [code]
def cell_1():
    """Cell 1: Insertion Sort & In-Place Shifting"""
    print("=" * 60)
    print("▶ CELL 1: Insertion Sort (Adaptive & Stable)")
    print("=" * 60)

    def insertion_sort(arr: list) -> list:
        a = list(arr)
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            # Shift elements greater than key to one position ahead
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        return a

    raw = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(raw)
    print(f"Original: {raw}")
    print(f"Sorted:   {sorted_arr}")


# %% [markdown]
# ### 📌 Cell 2: Merge Sort ($O(N \log N)$ Divide-and-Conquer)
# Recursively splitting array in halves, sorting, and merging two sorted subarrays in $O(N)$ time.

# %% [code]
def cell_2():
    """Cell 2: Merge Sort Algorithm"""
    print("=" * 60)
    print("▶ CELL 2: Merge Sort (O(N log N) Guaranteed & Stable)")
    print("=" * 60)

    def merge_sort(arr: list) -> list:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)

    def merge(left: list, right: list) -> list:
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    raw = [38, 27, 43, 3, 9, 82, 10]
    sorted_res = merge_sort(raw)
    print(f"Original:   {raw}")
    print(f"Merge Sort: {sorted_res}")


# %% [markdown]
# ### 📌 Cell 3: Quick Sort with Lomuto Partitioning
# Partitioning around a pivot so that elements $\le$ pivot are on the left and $>$ pivot on the right.

# %% [code]
def cell_3():
    """Cell 3: Quick Sort Algorithm"""
    print("=" * 60)
    print("▶ CELL 3: Quick Sort (In-Place Partitioning)")
    print("=" * 60)

    def quick_sort(arr: list, low: int, high: int):
        if low < high:
            pivot_idx = partition(arr, low, high)
            quick_sort(arr, low, pivot_idx - 1)
            quick_sort(arr, pivot_idx + 1, high)

    def partition(arr: list, low: int, high: int) -> int:
        pivot = arr[high]  # Pick last element as pivot
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    data = [10, 80, 30, 90, 40, 50, 70]
    print(f"Original:   {data}")
    quick_sort(data, 0, len(data) - 1)
    print(f"Quick Sort: {data}")


# %% [markdown]
# ### 📌 Cell 4: Non-Comparison Counting Sort ($O(N + K)$ Linear Time)
# Sorting non-negative integers within range $K$ using frequency tally buckets.

# %% [code]
def cell_4():
    """Cell 4: Counting Sort (Linear Time O(N + K))"""
    print("=" * 60)
    print("▶ CELL 4: Counting Sort (Linear Time for Bounded Integers)")
    print("=" * 60)

    def counting_sort(arr: list) -> list:
        if not arr:
            return []
        max_val = max(arr)
        counts = [0] * (max_val + 1)
        for num in arr:
            counts[num] += 1
        sorted_arr = []
        for val, count in enumerate(counts):
            sorted_arr.extend([val] * count)
        return sorted_arr

    ages = [4, 2, 2, 8, 3, 3, 1]
    sorted_ages = counting_sort(ages)
    print(f"Original Ages: {ages}")
    print(f"Counting Sort: {sorted_ages}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Insertion Sort (Adaptive & Stable)", cell_1),
    2: ("Merge Sort (Divide & Conquer O(N log N))", cell_2),
    3: ("Quick Sort (In-Place Partitioning)", cell_3),
    4: ("Counting Sort (Linear Time O(N + K))", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 07_SORTING_ALGORITHMS_INTERACTIVE.PY")
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
                print("Usage: python 07_Sorting_Algorithms_interactive.py [cell_number | --all]")
    else:
        run_all()
