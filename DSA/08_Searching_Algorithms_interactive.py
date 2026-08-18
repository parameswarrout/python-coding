import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math

"""
=============================================================================
🔍 DSA TOPIC 08: SEARCHING ALGORITHMS (Interactive Cell-by-Cell in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 08_Searching_Algorithms_interactive.py
2. Run a specific cell (e.g., Cell 4):
   python 08_Searching_Algorithms_interactive.py 4
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Classic Binary Search in Sorted Array ($O(\log N)$)
# Halving search space each iteration using midpoint calculation avoiding integer overflow.

# %% [code]
def cell_1():
    """Cell 1: Standard Binary Search Algorithm"""
    print("=" * 60)
    print("▶ CELL 1: Standard Binary Search in O(log N) Time")
    print("=" * 60)

    def binary_search(nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # Prevents potential overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    arr = [-10, -3, 0, 5, 9, 12, 18, 25]
    print(f"Sorted Array: {arr}")
    print(f"Search for 9:  Index {binary_search(arr, 9)}")
    print(f"Search for 18: Index {binary_search(arr, 18)}")
    print(f"Search for 7:  Index {binary_search(arr, 7)} (Not Found)")


# %% [markdown]
# ### 📌 Cell 2: Search in Rotated Sorted Array ($O(\log N)$)
# Determining which half of the array is normally sorted to eliminate the other half.

# %% [code]
def cell_2():
    """Cell 2: Search in Rotated Sorted Array"""
    print("=" * 60)
    print("▶ CELL 2: Search in Rotated Sorted Array")
    print("=" * 60)

    def search_rotated(nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"Rotated Array: {rotated}")
    print(f"Search for 0: Index {search_rotated(rotated, 0)}")
    print(f"Search for 3: Index {search_rotated(rotated, 3)} (Not found)")


# %% [markdown]
# ### 📌 Cell 3: Find First and Last Position of Element ($O(\log N)$)
# Performing two binary search passes to find exact boundary ranges.

# %% [code]
def cell_3():
    """Cell 3: First and Last Position of Element in Sorted Array"""
    print("=" * 60)
    print("▶ CELL 3: First and Last Position of Element (Bound Search)")
    print("=" * 60)

    def search_range(nums: list, target: int) -> list:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        right = mid - 1  # Keep searching left
                    else:
                        left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return bound

        return [find_bound(True), find_bound(False)]

    data = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    bounds = search_range(data, target)
    print(f"Array: {data}, Target: {target}")
    print(f"First and Last Index: {bounds}")


# %% [markdown]
# ### 📌 Cell 4: Binary Search on Solution Space (Koko Eating Bananas)
# Searching the answer range $[1, \max(\text{piles})]$ with monotonic validation function.

# %% [code]
def cell_4():
    """Cell 4: Binary Search on Answer Space (LC 875)"""
    print("=" * 60)
    print("▶ CELL 4: Binary Search on Answer Space (Koko Eating Bananas)")
    print("=" * 60)

    def min_eating_speed(piles: list, h: int) -> int:
        def hours_required(speed: int) -> int:
            return sum(math.ceil(p / speed) for p in piles)

        # Search space for speed: [1, max(piles)]
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid_speed = left + (right - left) // 2
            if hours_required(mid_speed) <= h:
                ans = mid_speed
                right = mid_speed - 1  # Try finding smaller valid speed
            else:
                left = mid_speed + 1

        return ans

    piles = [3, 6, 7, 11]
    hours = 8
    min_k = min_eating_speed(piles, hours)
    print(f"Banana Piles: {piles}, Hours Limit: {hours}")
    print(f"Minimum Eating Speed K: {min_k} bananas/hour")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Standard Binary Search in O(log N)", cell_1),
    2: ("Search in Rotated Sorted Array", cell_2),
    3: ("Find First and Last Position of Element", cell_3),
    4: ("Binary Search on Answer Space (Koko Bananas)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 08_SEARCHING_ALGORITHMS_INTERACTIVE.PY")
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
                print("Usage: python 08_Searching_Algorithms_interactive.py [cell_number | --all]")
    else:
        run_all()
