import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import time
import asyncio

"""
=============================================================================
⚡ ASYNC PROGRAMMING: INTERACTIVE CELL-BY-CELL NOTEBOOK IN .PY
=============================================================================
HOW TO RUN:
1. Run everything:
   python 06_async_programming_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 06_async_programming_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Coroutines, `asyncio.sleep` vs Blocking `time.sleep`
# Demonstrating non-blocking cooperative multitasking across concurrent tasks.

# %% [code]
def cell_1():
    """Cell 1: Sequential vs Concurrent Coroutine Execution"""
    print("=" * 60)
    print("▶ CELL 1: Coroutine Concurrency (asyncio.gather)")
    print("=" * 60)

    async def fetch_api_endpoint(name: str, delay_sec: float):
        print(f"  🚀 [Start] Requesting endpoint: {name} (latency {delay_sec}s)...")
        await asyncio.sleep(delay_sec)  # Non-blocking async sleep
        print(f"  ✅ [Done]  Received response from: {name}")
        return {"service": name, "status": 200}

    async def main_async():
        start = time.perf_counter()
        # Fire 3 requests concurrently
        results = await asyncio.gather(
            fetch_api_endpoint("User-Auth-Service", 0.3),
            fetch_api_endpoint("Payment-Gateway", 0.4),
            fetch_api_endpoint("Notification-Hub", 0.2)
        )
        total_time = time.perf_counter() - start
        print(f"\n  ⏱️ Total elapsed time: {total_time:.4f}s (Sequential would take 0.90s)")
        print(f"  Results: {results}")

    asyncio.run(main_async())


# %% [markdown]
# ### 📌 Cell 2: Controlled Concurrency & Rate Limiting with `asyncio.Semaphore`
# Limiting maximum simultaneous requests to protect databases/external servers.

# %% [code]
def cell_2():
    """Cell 2: Concurrency Throttling with asyncio.Semaphore"""
    print("=" * 60)
    print("▶ CELL 2: Rate Limiting & Semaphore Throttling")
    print("=" * 60)

    async def worker(sem: asyncio.Semaphore, task_id: int):
        async with sem:
            print(f"  [Worker {task_id:02d}]: Lock acquired. Scraping...")
            await asyncio.sleep(0.1)
            print(f"  [Worker {task_id:02d}]: Finished.")

    async def run_throttled_pool():
        # Allow at most 2 concurrent scraping tasks at any time
        semaphore = asyncio.Semaphore(2)
        tasks = [worker(semaphore, i + 1) for i in range(6)]
        await asyncio.gather(*tasks)

    print("Running 6 tasks with max_concurrency = 2:")
    asyncio.run(run_throttled_pool())


# %% [markdown]
# ### 📌 Cell 3: Asynchronous Context Managers (`async with`) & Generators (`async for`)
# Real-world async resource management and async data streaming.

# %% [code]
def cell_3():
    """Cell 3: async with (Context Manager) and async for (Streaming Generator)"""
    print("=" * 60)
    print("▶ CELL 3: Asynchronous Context Managers & Stream Generators")
    print("=" * 60)

    class AsyncDatabaseSession:
        async def __aenter__(self):
            print("  [AsyncDB] Connecting to database pool...")
            await asyncio.sleep(0.05)
            print("  [AsyncDB] Connection active.")
            return self

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("  [AsyncDB] Releasing connection back to pool...")
            await asyncio.sleep(0.02)
            print("  [AsyncDB] Disconnected.")

        async def stream_live_ticks(self, count=3):
            for i in range(count):
                await asyncio.sleep(0.08)
                yield f"TICK #{i+1}: NASDAQ=18,920.50 (+0.4%)"

    async def test_async_stream():
        async with AsyncDatabaseSession() as db:
            print("\n  Consuming live ticker with async for:")
            async for tick in db.stream_live_ticks(3):
                print(f"    📈 {tick}")
            print()

    asyncio.run(test_async_stream())


# %% [markdown]
# ### 📌 Cell 4: Offloading CPU-Bound Work to ThreadPool (`run_in_executor`)
# Mixing CPU-heavy calculations (which would block the event loop) with async I/O.

# %% [code]
def cell_4():
    """Cell 4: Offloading Blocking CPU Code with run_in_executor"""
    print("=" * 60)
    print("▶ CELL 4: Offloading Heavy CPU Computation (run_in_executor)")
    print("=" * 60)
    import concurrent.futures

    def heavy_cpu_task(n: int) -> int:
        """Synchronous CPU-bound function."""
        return sum(i * i for i in range(n))

    async def async_server():
        loop = asyncio.get_running_loop()
        print("  Starting heavy CPU computation in background thread pool...")
        
        # Offload blocking computation so the event loop stays responsive
        with concurrent.futures.ThreadPoolExecutor() as pool:
            result = await loop.run_in_executor(pool, heavy_cpu_task, 2_000_000)
            
        print(f"  ✅ Heavy CPU computation completed: {result:,}")

    asyncio.run(async_server())


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Coroutines, Event Loop & asyncio.gather", cell_1),
    2: ("Concurrency Rate Limiting with asyncio.Semaphore", cell_2),
    3: ("Async Context Managers (async with) & Streams (async for)", cell_3),
    4: ("Offloading Heavy CPU Work with run_in_executor", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 06_ASYNC_PROGRAMMING_INTERACTIVE.PY")
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
                print("Usage: python 06_async_programming_interactive.py [cell_number | --all]")
    else:
        run_all()
