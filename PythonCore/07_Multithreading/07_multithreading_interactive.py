import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import time
import queue
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
=============================================================================
🧵 MULTITHREADING: INTERACTIVE CELL-BY-CELL NOTEBOOK IN .PY
=============================================================================
HOW TO RUN:
1. Run everything:
   python 07_multithreading_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 07_multithreading_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Race Condition & Mutex Locks (`threading.Lock`)
# Demonstrating how un-synchronized shared state leads to corrupted data and how Mutex Locks solve it.

# %% [code]
def cell_1():
    """Cell 1: Shared Counter Race Condition vs Thread Lock Synchronization"""
    print("=" * 60)
    print("▶ CELL 1: Race Conditions & Threading Lock (Mutex)")
    print("=" * 60)

    class BankVault:
        def __init__(self):
            self.balance = 0
            self.lock = threading.Lock()

        def unsafe_deposit(self, count: int):
            for _ in range(count):
                # Non-atomic read-modify-write without lock
                current = self.balance
                time.sleep(0.00001)  # Context switch simulation
                self.balance = current + 1

        def safe_deposit(self, count: int):
            for _ in range(count):
                with self.lock:  # Atomic lock acquisition
                    current = self.balance
                    time.sleep(0.00001)
                    self.balance = current + 1

    # Test 1: Unsafe Race Condition
    unsafe_vault = BankVault()
    t1 = threading.Thread(target=unsafe_vault.unsafe_deposit, args=(100,))
    t2 = threading.Thread(target=unsafe_vault.unsafe_deposit, args=(100,))
    t1.start(); t2.start()
    t1.join(); t2.join()
    print(f"  ❌ Unsafe Balance (Expected 200, Got): {unsafe_vault.balance}")

    # Test 2: Safe Synchronized Deposit
    safe_vault = BankVault()
    t3 = threading.Thread(target=safe_vault.safe_deposit, args=(100,))
    t4 = threading.Thread(target=safe_vault.safe_deposit, args=(100,))
    t3.start(); t4.start()
    t3.join(); t4.join()
    print(f"  ✅ Safe Balance with Lock (Expected 200):  {safe_vault.balance}")


# %% [markdown]
# ### 📌 Cell 2: Producer-Consumer Architecture with Thread-Safe `queue.Queue`
# Decoupling producers and consumers using blocking FIFO queues with automatic synchronization.

# %% [code]
def cell_2():
    """Cell 2: Producer-Consumer Multi-Worker Pipeline"""
    print("=" * 60)
    print("▶ CELL 2: Producer-Consumer Pipeline with queue.Queue")
    print("=" * 60)

    task_queue = queue.Queue(maxsize=5)
    stop_sentinel = object()

    def producer(num_items: int):
        for i in range(num_items):
            item = f"Order #{1000 + i}"
            task_queue.put(item)  # Blocks if queue is full
            print(f"  📦 [Producer]: Created {item}")
            time.sleep(0.02)
        # Send poison pill / sentinel to signal termination
        task_queue.put(stop_sentinel)

    def consumer(worker_id: int):
        while True:
            item = task_queue.get()  # Blocks until item is available
            if item is stop_sentinel:
                task_queue.put(stop_sentinel)  # Forward sentinel to other consumers
                task_queue.task_done()
                break
            print(f"    ⚙️ [Consumer {worker_id}]: Processed {item}")
            time.sleep(0.03)
            task_queue.task_done()

    print("Launching 1 Producer and 2 Consumers:")
    prod_thread = threading.Thread(target=producer, args=(6,))
    cons1 = threading.Thread(target=consumer, args=(1,))
    cons2 = threading.Thread(target=consumer, args=(2,))

    prod_thread.start(); cons1.start(); cons2.start()
    prod_thread.join(); cons1.join(); cons2.join()
    print("All tasks processed successfully.")


# %% [markdown]
# ### 📌 Cell 3: Modern `ThreadPoolExecutor` with `map` and `as_completed`
# Production-ready thread worker pools for parallel I/O and batch downloads.

# %% [code]
def cell_3():
    """Cell 3: ThreadPoolExecutor with as_completed Future Resolution"""
    print("=" * 60)
    print("▶ CELL 3: ThreadPoolExecutor (Parallel Task Dispatch)")
    print("=" * 60)

    def download_resource(resource_id: int, latency: float) -> dict:
        time.sleep(latency)
        return {"id": resource_id, "size_kb": resource_id * 128, "status": "DOWNLOADED"}

    workload = [(1, 0.2), (2, 0.05), (3, 0.15), (4, 0.1)]
    start = time.perf_counter()

    print("Dispatching 4 download tasks to ThreadPool(workers=4):")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(download_resource, r_id, lat): r_id for r_id, lat in workload}
        
        # as_completed yields futures as soon as they finish!
        for future in as_completed(futures):
            res = future.result()
            print(f"  📥 Finished download for Resource ID: {res['id']} (Payload: {res['size_kb']} KB)")

    total_time = time.perf_counter() - start
    print(f"\n  ⏱️ Total Parallel Time: {total_time:.4f}s (Sequential would take ~0.50s)")


# %% [markdown]
# ### 📌 Cell 4: Thread-Local Storage (`threading.local`)
# Managing thread-isolated contextual variables (e.g. database sessions or request transaction IDs).

# %% [code]
def cell_4():
    """Cell 4: Thread Local Storage Isolation"""
    print("=" * 60)
    print("▶ CELL 4: Thread-Local Storage (threading.local)")
    print("=" * 60)

    thread_local_storage = threading.local()

    def worker_action(user_id: str):
        # Storing data unique to the current thread
        thread_local_storage.current_user = user_id
        time.sleep(0.05)
        # Reading data guaranteed to belong exclusively to this thread
        print(f"  [Thread {threading.current_thread().name}] Active User: {thread_local_storage.current_user}")

    threads = [
        threading.Thread(target=worker_action, args=(f"User_{i+100}",), name=f"Worker-{i+1}")
        for i in range(3)
    ]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Thread-local state verified without cross-thread contamination.")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Race Conditions & Mutex Locks (Bank Vault)", cell_1),
    2: ("Producer-Consumer Pipeline (queue.Queue)", cell_2),
    3: ("ThreadPoolExecutor & as_completed Futures", cell_3),
    4: ("Thread-Local Storage (threading.local)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 07_MULTITHREADING_INTERACTIVE.PY")
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
                print("Usage: python 07_multithreading_interactive.py [cell_number | --all]")
    else:
        run_all()
