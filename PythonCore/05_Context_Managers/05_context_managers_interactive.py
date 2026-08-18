import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import os
import time
from contextlib import contextmanager, ExitStack

"""
=============================================================================
🛡️ CONTEXT MANAGERS: INTERACTIVE CELL-BY-CELL NOTEBOOK IN .PY
=============================================================================
HOW TO RUN:
1. Run everything:
   python 05_context_managers_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 05_context_managers_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Class-Based Protocol (`__enter__` and `__exit__`)
# Ensuring deterministic resource cleanup (e.g. database transaction commit vs rollback).

# %% [code]
def cell_1():
    """Cell 1: Database Transaction Rollback & Commit Simulation"""
    print("=" * 60)
    print("▶ CELL 1: Class-Based Context Manager (Database Transaction)")
    print("=" * 60)

    class TransactionSession:
        def __init__(self, session_id: str):
            self.session_id = session_id
            self.in_transaction = False

        def __enter__(self):
            print(f"  [DB Session {self.session_id}]: BEGIN TRANSACTION")
            self.in_transaction = True
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print(f"  🚨 [DB Session {self.session_id}]: ROLLBACK! Exception: {exc_val}")
                self.in_transaction = False
                # Returning False ensures exception continues propagating
                return False
            
            print(f"  ✅ [DB Session {self.session_id}]: COMMIT TRANSACTION")
            self.in_transaction = False
            return True

        def execute(self, query: str):
            print(f"    Executing: {query}")

    # Case 1: Successful Transaction
    print("[1. Executing Successful Transaction]:")
    with TransactionSession("TX-101") as tx:
        tx.execute("UPDATE accounts SET balance = balance - 500 WHERE id = 1;")
        tx.execute("UPDATE accounts SET balance = balance + 500 WHERE id = 2;")

    # Case 2: Failed Transaction with Auto-Rollback
    print("\n[2. Executing Failing Transaction with Rollback]:")
    try:
        with TransactionSession("TX-102") as tx:
            tx.execute("UPDATE inventory SET stock = stock - 1 WHERE item = 'GPU';")
            raise ValueError("Payment card declined by issuer!")
            tx.execute("INSERT INTO orders (item) VALUES ('GPU');")
    except ValueError as e:
        print(f"  Caught handled error in outer scope: {e}")


# %% [markdown]
# ### 📌 Cell 2: `@contextlib.contextmanager` Generator Syntax
# Simplifying context managers by writing a single generator function with `yield`.

# %% [code]
def cell_2():
    """Cell 2: High-Precision Code Block Execution Timer"""
    print("=" * 60)
    print("▶ CELL 2: Generator-Based Context Manager (@contextmanager)")
    print("=" * 60)

    @contextmanager
    def performance_timer(block_name: str):
        """Measures execution time of the enclosed with-block."""
        start_time = time.perf_counter()
        print(f"  ⏱️ Starting timer for '{block_name}'...")
        try:
            yield start_time  # Yields to user code block
        finally:
            elapsed = time.perf_counter() - start_time
            print(f"  ⏱️ Finished '{block_name}': Elapsed = {elapsed:.6f}s")

    with performance_timer("Matrix Multiplication"):
        total = sum(i * j for i in range(500) for j in range(500))
        print(f"    Computed matrix sum: {total:,}")


# %% [markdown]
# ### 📌 Cell 3: Exception Suppression (`contextlib.suppress`)
# Selectively muting expected exceptions without noisy `try...except pass` boilerplate.

# %% [code]
def cell_3():
    """Cell 3: Exception Suppression and File Cleanup"""
    print("=" * 60)
    print("▶ CELL 3: Exception Suppression (contextlib.suppress)")
    print("=" * 60)
    from contextlib import suppress

    temp_file = "temp_scratch_test.tmp"
    
    # Create temporary file
    with open(temp_file, "w") as f:
        f.write("temporary data")

    # Safe removal ignoring FileNotFoundError if file already deleted
    with suppress(FileNotFoundError):
        os.remove(temp_file)
        print(f"  Removed '{temp_file}' successfully.")

    # Attempting second remove: Normally raises FileNotFoundError, but cleanly suppressed!
    with suppress(FileNotFoundError):
        os.remove(temp_file)
        print("  This line will not print because remove raises FileNotFoundError.")
        
    print("  ✅ Safely executed suppression without crashing!")


# %% [markdown]
# ### 📌 Cell 4: Managing Dynamic Resource Stacks with `ExitStack`
# Opening a variable/dynamic number of files or resources simultaneously without nesting 10 `with` blocks.

# %% [code]
def cell_4():
    """Cell 4: Dynamic Multi-Resource Management with ExitStack"""
    print("=" * 60)
    print("▶ CELL 4: Dynamic Multi-Resource Management with ExitStack")
    print("=" * 60)

    @contextmanager
    def managed_channel(channel_id: int):
        print(f"  [Channel {channel_id}]: Connected")
        try:
            yield f"Socket-{channel_id}"
        finally:
            print(f"  [Channel {channel_id}]: Disconnected & Cleaned up")

    num_channels = 3
    print(f"Opening {num_channels} network channels dynamically:")
    
    with ExitStack() as stack:
        # Dynamically push multiple context managers onto the stack
        sockets = [stack.enter_context(managed_channel(i + 1)) for i in range(num_channels)]
        print(f"\n  Active Sockets in block: {sockets}")
        print("  Transmitting packets across all sockets...\n")
        
    print("All sockets successfully closed on ExitStack exit.")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Class-Based Protocol (__enter__, __exit__ & Rollback)", cell_1),
    2: ("Generator-Based Timer (@contextmanager)", cell_2),
    3: ("Exception Suppression (contextlib.suppress)", cell_3),
    4: ("Dynamic Resource Management with ExitStack", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 05_CONTEXT_MANAGERS_INTERACTIVE.PY")
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
                print("Usage: python 05_context_managers_interactive.py [cell_number | --all]")
    else:
        run_all()
