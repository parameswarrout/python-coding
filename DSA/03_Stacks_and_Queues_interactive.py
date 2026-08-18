import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from collections import deque

"""
=============================================================================
🥞 DSA TOPIC 03: STACKS & QUEUES (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 03_Stacks_and_Queues_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 03_Stacks_and_Queues_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Stack (LIFO) & Valid Parentheses Parsing
# Stacks operate on Last-In, First-Out (LIFO). Standard for syntax parsing, expression evaluation, and recursion.

# %% [code]
def cell_1():
    """Cell 1: Stack LIFO & Valid Parentheses Matcher"""
    print("=" * 60)
    print("▶ CELL 1: Stack LIFO Mechanics & Valid Parentheses")
    print("=" * 60)

    def is_valid_parentheses(s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:
                # Top element or dummy placeholder
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

    test_cases = ["()", "()[]{}", "(]", "([{}])", "((())"]
    for t in test_cases:
        print(f"  String: '{t:<8}' -> Valid? {is_valid_parentheses(t)}")


# %% [markdown]
# ### 📌 Cell 2: MinStack ($O(1)$ Time Minimum Element Retrieval)
# Maintaining an auxiliary min stack to track minimum at every stack state in $O(1)$ time.

# %% [code]
def cell_2():
    """Cell 2: MinStack Design in O(1) Time"""
    print("=" * 60)
    print("▶ CELL 2: MinStack with O(1) Time Min Element Retrieval")
    print("=" * 60)

    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int):
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self) -> int:
            if not self.stack:
                return None
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
            return val

        def top(self) -> int:
            return self.stack[-1] if self.stack else None

        def get_min(self) -> int:
            return self.min_stack[-1] if self.min_stack else None

    ms = MinStack()
    ms.push(10)
    ms.push(20)
    ms.push(5)
    ms.push(8)

    print(f"Pushed: 10, 20, 5, 8")
    print(f"  Current Top: {ms.top()}, Current Min: {ms.get_min()}")

    popped = ms.pop()
    print(f"\nPopped {popped}:")
    print(f"  Current Top: {ms.top()}, Current Min: {ms.get_min()}")

    popped = ms.pop()
    print(f"\nPopped {popped} (which was min):")
    print(f"  Current Top: {ms.top()}, Current Min: {ms.get_min()} (Restored previous min!)")


# %% [markdown]
# ### 📌 Cell 3: Queue (FIFO) using `collections.deque`
# Using double-ended queue for true $O(1)$ `popleft()` operations (standard `list.pop(0)` is $O(N)$).

# %% [code]
def cell_3():
    """Cell 3: Queue FIFO with collections.deque"""
    print("=" * 60)
    print("▶ CELL 3: Queue FIFO & Breadth-First Simulation")
    print("=" * 60)

    class RequestQueue:
        def __init__(self):
            self.queue = deque()

        def enqueue(self, item):
            self.queue.append(item)
            print(f"  [Enqueue]: Added {item}")

        def dequeue(self):
            if self.queue:
                item = self.queue.popleft()  # True O(1) FIFO removal
                print(f"  [Dequeue]: Serviced {item}")
                return item
            print("  [Queue Empty]")
            return None

        def size(self):
            return len(self.queue)

    rq = RequestQueue()
    rq.enqueue("Request #1 (Auth)")
    rq.enqueue("Request #2 (Query)")
    rq.enqueue("Request #3 (Payment)")
    print(f"\nQueue Size: {rq.size()}")
    rq.dequeue()
    rq.dequeue()
    print(f"Remaining Size: {rq.size()}")


# %% [markdown]
# ### 📌 Cell 4: Monotonic Stack (Next Greater Element in $O(N)$)
# Maintaining elements in monotonic decreasing order inside a stack to find the next greater element in linear time.

# %% [code]
def cell_4():
    """Cell 4: Monotonic Stack for Next Greater Element"""
    print("=" * 60)
    print("▶ CELL 4: Monotonic Stack (Next Greater Element)")
    print("=" * 60)

    def next_greater_elements(nums: list) -> list:
        n = len(nums)
        res = [-1] * n
        stack = []  # Stores indices

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                res[idx] = num
            stack.append(i)

        return res

    arr = [2, 1, 2, 4, 3]
    nge = next_greater_elements(arr)
    print(f"Original Array:       {arr}")
    print(f"Next Greater Element: {nge}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Stack (LIFO) & Valid Parentheses Parsing", cell_1),
    2: ("MinStack with O(1) Time Min Retrieval", cell_2),
    3: ("Queue (FIFO) Mechanics with collections.deque", cell_3),
    4: ("Monotonic Stack (Next Greater Element)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 03_STACKS_AND_QUEUES_INTERACTIVE.PY")
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
                print("Usage: python 03_Stacks_and_queues_interactive.py [cell_number | --all]")
    else:
        run_all()
