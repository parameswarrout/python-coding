import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import time
import functools

"""
=============================================================================
🎨 DECORATORS: INTERACTIVE CELL-BY-CELL NOTEBOOK IN .PY
=============================================================================
HOW TO RUN:
1. Run everything:
   python 03_decorators_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 03_decorators_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Fundamentals of Decorators & `functools.wraps`
# A decorator wraps a function to extend its behavior without modifying its code.
# `functools.wraps` preserves original function name, docstrings, and signatures.

# %% [code]
def cell_1():
    """Cell 1: Basic Timing & Logging Decorator with functools.wraps"""
    print("=" * 60)
    print("▶ CELL 1: Timing Decorator & Metadata Preservation")
    print("=" * 60)

    def execution_timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            duration = time.perf_counter() - start
            print(f"  ⏱️ [{func.__name__}] Executed in {duration:.6f}s")
            return result
        return wrapper

    @execution_timer
    def heavy_calculation(n: int) -> int:
        """Calculates sum of squares from 0 to n."""
        return sum(i * i for i in range(n))

    print(f"Function Name: {heavy_calculation.__name__}")
    print(f"Docstring:     {heavy_calculation.__doc__}")
    res = heavy_calculation(500000)
    print(f"Result:        {res:,}")


# %% [markdown]
# ### 📌 Cell 2: Decorators with Arguments (Parameterized Decorator Factory)
# To pass arguments into decorators (e.g., `@retry(max_attempts=3, delay_sec=0.5)`),
# we write an outer decorator factory that returns the actual decorator.

# %% [code]
def cell_2():
    """Cell 2: Parameterized Retry Decorator with Backoff"""
    print("=" * 60)
    print("▶ CELL 2: Parameterized Retry Decorator (Fault Tolerance)")
    print("=" * 60)

    def retry(max_attempts: int = 3, delay_sec: float = 0.1):
        """Decorator factory to automatically retry failing functions."""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                attempts = 0
                while attempts < max_attempts:
                    try:
                        attempts += 1
                        return func(*args, **kwargs)
                    except Exception as e:
                        print(f"  ⚠️ Attempt {attempts}/{max_attempts} failed: {e}")
                        if attempts >= max_attempts:
                            raise
                        time.sleep(delay_sec)
            return wrapper
        return decorator

    # Simulated flaky API
    attempt_counter = 0

    @retry(max_attempts=4, delay_sec=0.05)
    def fetch_user_data(user_id: int):
        nonlocal attempt_counter
        attempt_counter += 1
        if attempt_counter < 3:
            raise ConnectionError("Network timeout connecting to database!")
        return {"user_id": user_id, "status": "ACTIVE", "name": "Alice"}

    print("Calling flaky API with automatic retry:")
    data = fetch_user_data(101)
    print(f"  ✅ Final Response: {data}")


# %% [markdown]
# ### 📌 Cell 3: Chaining Multiple Decorators & Execution Order
# Multiple decorators are applied bottom-up and executed top-down.

# %% [code]
def cell_3():
    """Cell 3: Chaining Decorators (Auth + Logging + Output Formatting)"""
    print("=" * 60)
    print("▶ CELL 3: Chaining Multiple Decorators & Execution Order")
    print("=" * 60)

    def bold(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<b>{func(*args, **kwargs)}</b>"
        return wrapper

    def italic(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f"<i>{func(*args, **kwargs)}</i>"
        return wrapper

    def uppercase(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).upper()
        return wrapper

    # Applied bottom-up: uppercase -> italic -> bold
    @bold
    @italic
    @uppercase
    def greet(name: str) -> str:
        return f"Welcome, {name}"

    print(f"Greet Result: {greet('Parameswar')}")
    # Expected: <b><i>WELCOME, PARAMESWAR</i></b>


# %% [markdown]
# ### 📌 Cell 4: Class-Based Stateful Decorators & Memoization Cache
# Class decorators implement `__call__` and can maintain persistent state across function calls.

# %% [code]
def cell_4():
    """Cell 4: Class-Based Memoization Cache Decorator"""
    print("=" * 60)
    print("▶ CELL 4: Class-Based Memoization Cache Decorator")
    print("=" * 60)

    class MemoizeCache:
        def __init__(self, func):
            self.func = func
            self.cache = {}
            functools.update_wrapper(self, func)

        def __call__(self, *args):
            if args not in self.cache:
                print(f"  [Cache MISS for args={args}]: Computing...")
                self.cache[args] = self.func(*args)
            else:
                print(f"  [Cache HIT for args={args}]: Returning cached value.")
            return self.cache[args]

        def clear(self):
            self.cache.clear()

    @MemoizeCache
    def fibonacci(n: int) -> int:
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    print("Computing fibonacci(6):")
    res = fibonacci(6)
    print(f"Fibonacci(6) = {res}")
    print("\nCalling fibonacci(6) a second time:")
    res2 = fibonacci(6)
    print(f"Fibonacci(6) = {res2}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Execution Timer & functools.wraps Metadata", cell_1),
    2: ("Parameterized Retry Decorator with Backoff", cell_2),
    3: ("Chaining Multiple Decorators (HTML Formatter)", cell_3),
    4: ("Class-Based Stateful Memoization Cache", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 03_DECORATORS_INTERACTIVE.PY")
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
                print("Usage: python 03_decorators_interactive.py [cell_number | --all]")
    else:
        run_all()
