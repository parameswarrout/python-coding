# AGENTS.md - Machine & Agentic LLM Guidelines 🤖

> **Context for AI Agents (Antigravity, Cursor, Codex, Claude Code, Devin, Roo Code, Copilot):**
> This repository is a standardized Python Engineering, DSA Mastery, PyTorch AI Systems, and SQL Practice workspace.
> When interacting with, generating code for, or reviewing this repository, strictly follow the architecture and rules below.

---

## 🧭 Repository Architecture Map

```
/
├── PythonCore/                      # Production Python mechanics & concurrency
│   ├── 01_Error_Handling/           # Exception hierarchies, custom exceptions, logging
│   ├── 02_Advanced_Functions/       # Closures, higher-order functions, introspection
│   ├── 03_Decorators/               # @wraps, parameterized retry, chaining, memoization
│   ├── 04_Generators_Iterators/     # Custom iterator protocol, yield from, memory streams
│   ├── 05_Context_Managers/         # __enter__/__exit__, @contextmanager, ExitStack
│   ├── 06_Async_Programming/        # Event loop, asyncio.gather, Semaphores, run_in_executor
│   ├── 07_Multithreading/           # GIL, Lock/RLock, queue.Queue, ThreadPoolExecutor
│   └── OOPs_Concepts/               # MRO, Descriptors, __slots__, Metaclasses, SOLID
│
├── DSA/                             # Core Data Structures & Algorithms Fundamentals
│   ├── 01_Arrays_and_strings_interactive.py
│   ├── 02_Linked_Lists_interactive.py
│   ├── 03_Stacks_and_Queues_interactive.py
│   ├── 04_Hashing_and_Hash_Tables_interactive.py
│   ├── 05_Trees_and_Binary_Search_Trees_interactive.py
│   ├── 06_Graphs_interactive.py
│   ├── 07_Sorting_Algorithms_interactive.py
│   ├── 08_Searching_Algorithms_interactive.py
│   ├── 09_Dynamic_Programming_interactive.py
│   └── 10_Greedy_Algorithms_interactive.py
│
├── python_interview_patterns/       # 22 Curated LeetCode Master Patterns (95%+ Coverage)
│   ├── 01_loop_basics/ .. 18_bit_manipulation/
│   ├── 19_union_find/               # Disjoint Set Union (DSU), Kruskal's MST
│   ├── 20_cyclic_sort/              # O(N) time & O(1) space in-place array indexing
│   ├── 21_data_structure_design/    # LRU/LFU Cache, MinStack, Time-Based KV Store
│   └── 22_intervals_and_monotonic/  # Monotonic Deque, Merge Intervals, Meeting Rooms
│
├── AI/                              # 3-Tier PyTorch & Deep Learning Architecture
│   ├── 01_beginner_pytorch/         # Tensors, Autograd DAG, MLPs, Custom Collate
│   ├── 02_intermediate_pytorch/     # ResNet Blocks, BiLSTM, Schedulers, EarlyStopping
│   └── 03_advanced_interview_pytorch/ # Multi-Head Attention, LoRA, AMP, KV-Cache
│
└── sql_practice/                    # SQLite Sandbox & Analytics Queries (DBeaver)
    ├── init_db.py                   # DB generator script
    ├── practice.db                  # Local SQLite database
    └── 01_.. to 06_senior_sql/      # Questions and solutions
```

---

## 🛠️ Code Conventions & Agent Execution Rules

### 1. Interactive Cell Format (`# %%`)
All educational scripts in `PythonCore/` and `DSA/` use Jupyter cell delimiters:
```python
# %% [markdown]
# ### 📌 Cell N: Topic Explanation
# Detailed explanation here...

# %% [code]
def cell_N():
    """Cell N docstring."""
    # Code implementation
```
* Every interactive file contains a `CELLS = {1: (...), 2: (...)}` registry and CLI runner.
* **To run all cells**: `python <path_to_file>.py --all`
* **To run a single cell**: `python <path_to_file>.py <cell_number>`

### 2. LeetCode Pattern Practice Format
All files in `python_interview_patterns/` follow this structure:
* `QUESTION_NUMBER = None` (Auto-detects highest implemented question when `None`).
* Functions named `q1`, `q2`, ..., `q25` with full type hints and docstrings.
* Self-testing `TESTS` dictionary containing inputs and expected outputs.
* **To run tests**: `python python_interview_patterns/<folder>/<file>.py [question_number]`

### 3. AI / PyTorch Modules
* All PyTorch files are **self-contained** with built-in assertion tests and performance benchmarks.
* Include fallback checks for CPU vs CUDA execution (`torch.cuda.is_available()`).
* **To run tests**: `python AI/<tier>/<file>.py`

### 4. Python Environment & Standard
* Target Python Version: **3.10+ / 3.11+**
* Always include UTF-8 stdout reconfiguration at the top of executable scripts:
  ```python
  import sys
  if hasattr(sys.stdout, 'reconfigure'):
      sys.stdout.reconfigure(encoding='utf-8')
  ```
* Enforce strict type annotations (`list`, `dict`, `int`, `torch.Tensor`, `tuple`).

---

## ⚡ Fast CLI Commands for Agents

```bash
# Test a DSA module
python DSA/01_Arrays_and_strings_interactive.py --all

# Test a PythonCore module
python PythonCore/03_Decorators/03_decorators_interactive.py --all

# Test a LeetCode pattern question
python python_interview_patterns/19_union_find/union_find.py 1

# Test an Advanced AI module
python AI/03_advanced_interview_pytorch/01_multihead_attention_and_transformer.py
```
