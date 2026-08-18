import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
🦅 DSA TOPIC 10: GREEDY ALGORITHMS (Interactive Cell-by-Cell in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 10_Greedy_Algorithms_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 10_Greedy_Algorithms_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Activity Selection / Interval Scheduling
# Making locally optimal choice (earliest finish time) to maximize total non-overlapping activities.

# %% [code]
def cell_1():
    """Cell 1: Activity Selection by Earliest Finish Time"""
    print("=" * 60)
    print("▶ CELL 1: Activity Selection (Earliest Finish Time)")
    print("=" * 60)

    def max_activities(activities: list) -> list:
        # Sort by finish time (activity[1])
        sorted_acts = sorted(activities, key=lambda x: x[1])
        selected = [sorted_acts[0]]
        last_finish = sorted_acts[0][1]

        for i in range(1, len(sorted_acts)):
            start, finish = sorted_acts[i]
            if start >= last_finish:
                selected.append((start, finish))
                last_finish = finish

        return selected

    # Activities: (start_time, finish_time)
    acts = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    scheduled = max_activities(acts)
    print(f"Total Available Activities: {len(acts)}")
    print(f"Maximum Non-overlapping Activities ({len(scheduled)}):")
    for s, f in scheduled:
        print(f"  [{s:02d} -> {f:02d}]")


# %% [markdown]
# ### 📌 Cell 2: Fractional Knapsack Problem
# Selecting items with the highest value-to-weight ratio first (allows taking fractions of items).

# %% [code]
def cell_2():
    """Cell 2: Fractional Knapsack by Value/Weight Ratio"""
    print("=" * 60)
    print("▶ CELL 2: Fractional Knapsack (Value/Weight Density)")
    print("=" * 60)

    class Item:
        def __init__(self, value, weight, name):
            self.value = value
            self.weight = weight
            self.name = name
            self.ratio = value / weight

    def fractional_knapsack(items: list, capacity: float) -> float:
        # Sort by value/weight ratio descending
        items.sort(key=lambda x: x.ratio, reverse=True)
        total_value = 0.0
        remaining_cap = capacity

        for item in items:
            if remaining_cap <= 0:
                break
            if item.weight <= remaining_cap:
                total_value += item.value
                remaining_cap -= item.weight
                print(f"  Took 100% of {item.name:<8} (wt={item.weight}, val={item.value})")
            else:
                fraction = remaining_cap / item.weight
                total_value += item.value * fraction
                print(f"  Took {fraction*100:.1f}% of {item.name:<8} (wt={remaining_cap}, val={item.value * fraction:.2f})")
                remaining_cap = 0

        return total_value

    items = [Item(60, 10, "Gold"), Item(100, 20, "Silver"), Item(120, 30, "Bronze")]
    cap = 50
    print(f"Knapsack Capacity: {cap} kg")
    max_val = fractional_knapsack(items, cap)
    print(f"Total Maximum Value: ${max_val:.2f}")


# %% [markdown]
# ### 📌 Cell 3: Jump Game ($O(N)$ Greedy Reachable Boundary)
# Tracking the maximum reachable index at every step.

# %% [code]
def cell_3():
    """Cell 3: Jump Game (LC 55)"""
    print("=" * 60)
    print("▶ CELL 3: Jump Game (Greedy Max Reachable Window)")
    print("=" * 60)

    def can_jump(nums: list) -> bool:
        max_reachable = 0
        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + jump)
        return True

    arr1 = [2, 3, 1, 1, 4]
    arr2 = [3, 2, 1, 0, 4]
    print(f"Array {arr1} can reach end? -> {can_jump(arr1)}")
    print(f"Array {arr2} can reach end? -> {can_jump(arr2)}")


# %% [markdown]
# ### 📌 Cell 4: Gas Station Circular Tour ($O(N)$ Greedy Single Pass)
# Finding unique starting station to complete circular route.

# %% [code]
def cell_4():
    """Cell 4: Gas Station Circular Circuit (LC 134)"""
    print("=" * 60)
    print("▶ CELL 4: Gas Station Circular Circuit (Single Pass Greedy)")
    print("=" * 60)

    def can_complete_circuit(gas: list, cost: list) -> int:
        if sum(gas) < sum(cost):
            return -1  # Total gas insufficient

        total_tank = 0
        start_idx = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            # If tank dips negative, cannot start from start_idx through i
            if total_tank < 0:
                start_idx = i + 1
                total_tank = 0

        return start_idx

    gas_supply = [1, 2, 3, 4, 5]
    gas_costs  = [3, 4, 5, 1, 2]
    start = can_complete_circuit(gas_supply, gas_costs)
    print(f"Gas Supplies: {gas_supply}")
    print(f"Travel Costs: {gas_costs}")
    print(f"Valid Starting Station Index: {start} (Station {start})")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Activity Selection (Earliest Finish Time)", cell_1),
    2: ("Fractional Knapsack (Value/Weight Density)", cell_2),
    3: ("Jump Game (Max Reachable Window)", cell_3),
    4: ("Gas Station Circular Circuit (Single Pass Greedy)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 10_GREEDY_ALGORITHMS_INTERACTIVE.PY")
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
                print("Usage: python 10_Greedy_Algorithms_interactive.py [cell_number | --all]")
    else:
        run_all()
