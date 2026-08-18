import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
⚡ GENERATORS & ITERATORS: INTERACTIVE CELL-BY-CELL NOTEBOOK IN .PY
=============================================================================
HOW TO RUN:
1. Run everything:
   python 04_generators_iterators_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 04_generators_iterators_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Custom Iterator Protocol (`__iter__` and `__next__`)
# Understanding how `for` loops work under the hood using `iter()` and `next()`.

# %% [code]
def cell_1():
    """Cell 1: Custom Range Iterator Protocol from Scratch"""
    print("=" * 60)
    print("▶ CELL 1: Custom Iterator Protocol (__iter__ and __next__)")
    print("=" * 60)

    class CustomRange:
        def __init__(self, start: int, end: int, step: int = 1):
            self.current = start
            self.end = end
            self.step = step

        def __iter__(self):
            # Returns iterator object (self)
            return self

        def __next__(self):
            if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
                raise StopIteration
            val = self.current
            self.current += self.step
            return val

    print("Iterating with custom iterator for-loop:")
    for x in CustomRange(0, 10, step=2):
        print(f"  Item: {x}")

    print("\nManual next() traversal:")
    it = iter(CustomRange(10, 13))
    print(f"  next(it): {next(it)}")
    print(f"  next(it): {next(it)}")
    print(f"  next(it): {next(it)}")
    try:
        next(it)
    except StopIteration:
        print("  ✅ StopIteration correctly raised at exhaustion.")


# %% [markdown]
# ### 📌 Cell 2: Memory Efficiency (List vs Generator Expression)
# Demonstrating lazy evaluation and how generators consume $O(1)$ constant memory.

# %% [code]
def cell_2():
    """Cell 2: Memory Benchmark: List vs Generator"""
    print("=" * 60)
    print("▶ CELL 2: Memory Footprint (List Comprehension vs Generator)")
    print("=" * 60)

    n = 1_000_000
    
    # 1. Eager List Comprehension
    list_data = [x ** 2 for x in range(n)]
    list_mem_kb = sys.getsizeof(list_data) / 1024

    # 2. Lazy Generator Expression
    gen_data = (x ** 2 for x in range(n))
    gen_mem_kb = sys.getsizeof(gen_data) / 1024

    print(f"Size of {n:,} items stored in Memory:")
    print(f"  📦 List Memory:      {list_mem_kb:,.2f} KB (~{list_mem_kb/1024:.2f} MB)")
    print(f"  ⚡ Generator Memory: {gen_mem_kb:,.2f} KB ({sys.getsizeof(gen_data)} bytes)")
    print(f"  🚀 Generator saves ~{((list_mem_kb - gen_mem_kb) / list_mem_kb) * 100:.2f}% RAM!")

    print(f"\nPulling first 3 values lazily from generator:")
    print(f"  1: {next(gen_data)}")
    print(f"  2: {next(gen_data)}")
    print(f"  3: {next(gen_data)}")


# %% [markdown]
# ### 📌 Cell 3: Recursive `yield from` & Flattening Arbitrary Trees
# `yield from` transparently delegates execution to a sub-generator.

# %% [code]
def cell_3():
    """Cell 3: Arbitrary Nested List Flattening with yield from"""
    print("=" * 60)
    print("▶ CELL 3: Flattening Complex Nested Trees with yield from")
    print("=" * 60)

    def flatten(nested_iterable):
        for item in nested_iterable:
            if isinstance(item, (list, tuple, set)):
                # Delegate to recursive generator
                yield from flatten(item)
            else:
                yield item

    deeply_nested = [1, [2, [3, 4], [5, [6, 7]]], 8, [[9, 10]]]
    print("Original Deeply Nested Structure:")
    print(f"  {deeply_nested}")

    flattened_list = list(flatten(deeply_nested))
    print("\nFlattened Stream Output:")
    print(f"  {flattened_list}")


# %% [markdown]
# ### 📌 Cell 4: Composable Unix-Style Data Streaming Pipeline
# Chaining generators together to filter, parse, and aggregate log lines without reading entire files into memory.

# %% [code]
def cell_4():
    """Cell 4: Log Analysis Streaming Pipeline (Pipe Architecture)"""
    print("=" * 60)
    print("▶ CELL 4: Real-World Log Processing Streaming Pipeline")
    print("=" * 60)

    # Simulated raw web server log stream
    raw_logs = [
        "2026-08-19 00:01:23 GET /api/v1/users 200 14.2ms",
        "2026-08-19 00:01:25 POST /api/v1/login 500 120.5ms",
        "2026-08-19 00:01:28 GET /api/v1/orders 200 45.1ms",
        "2026-08-19 00:01:30 GET /api/v1/products 404 8.0ms",
        "2026-08-19 00:01:32 POST /api/v1/checkout 500 240.8ms",
    ]

    # Stage 1: Line Reader Generator
    def read_lines(log_source):
        for line in log_source:
            yield line

    # Stage 2: Filter Errors Generator (HTTP 500)
    def filter_errors(lines):
        for line in lines:
            if " 500 " in line:
                yield line

    # Stage 3: Parse Duration Generator
    def extract_durations(error_lines):
        for line in error_lines:
            parts = line.split()
            endpoint = parts[3]
            duration_str = parts[5].replace("ms", "")
            yield endpoint, float(duration_str)

    # Compose the streaming pipeline: raw_logs | read_lines | filter_errors | extract_durations
    pipeline = extract_durations(filter_errors(read_lines(raw_logs)))

    print("Processing Error Stream on-the-fly:")
    for endpoint, duration in pipeline:
        print(f"  🚨 Error on {endpoint:<18} -> Latency: {duration:.1f}ms")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Custom Iterator Protocol (__iter__ & __next__)", cell_1),
    2: ("Memory Efficiency (List vs Generator Expression)", cell_2),
    3: ("Flattening Nested Structures with yield from", cell_3),
    4: ("Streaming Data Pipeline (Log Processing Engine)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 04_GENERATORS_ITERATORS_INTERACTIVE.PY")
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
                print("Usage: python 04_generators_iterators_interactive.py [cell_number | --all]")
    else:
        run_all()
