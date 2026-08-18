# CLAUDE.md

## Project Overview
Comprehensive Python Engineering, DSA Interview Patterns (22 patterns, 95%+ coverage), 3-Tier PyTorch AI Systems (Attention, LoRA, KV-Cache), and SQL Practice repository.

## Commands
- **Run PythonCore Module:** `python PythonCore/<topic>/<topic>_interactive.py --all`
- **Run PythonCore Single Cell:** `python PythonCore/<topic>/<topic>_interactive.py <cell_number>`
- **Run DSA Module:** `python DSA/<topic>_interactive.py --all`
- **Run DSA Single Cell:** `python DSA/<topic>_interactive.py <cell_number>`
- **Run LeetCode Pattern Tests:** `python python_interview_patterns/<folder>/<file>.py [question_number]`
- **Run PyTorch AI Tests:** `python AI/<tier>/<file>.py`
- **Init SQL Database:** `python sql_practice/init_db.py`

## Architecture & Code Style
- **Python Version:** 3.10+ / 3.11+
- **Interactive Cells:** `# %% [markdown]` and `# %% [code]`
- **Self-Testing Harnesses:** All practice files contain built-in validation assertions and test runners.
- **Type Annotations:** Strictly used across all function inputs and outputs.
- **Encoding:** Ensure standard UTF-8 stdout configuration at top of scripts.
