import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from collections import defaultdict

"""
=============================================================================
🔑 DSA TOPIC 04: HASHING & HASH TABLES (Interactive Cell-by-Cell in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 04_Hashing_and_Hash_Tables_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 04_Hashing_and_Hash_Tables_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Hash Table Implementation from Scratch (Separate Chaining)
# How Python dictionaries and hash tables map keys to bucket indices using hash functions and handle collisions.

# %% [code]
def cell_1():
    """Cell 1: Custom HashMap with Separate Chaining Collision Resolution"""
    print("=" * 60)
    print("▶ CELL 1: Custom HashMap (Separate Chaining from Scratch)")
    print("=" * 60)

    class HashMap:
        def __init__(self, capacity=10):
            self.capacity = capacity
            self.buckets = [[] for _ in range(capacity)]
            self.size = 0

        def _hash(self, key):
            return hash(key) % self.capacity

        def put(self, key, value):
            index = self._hash(key)
            bucket = self.buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = (key, value)  # Update existing key
                    return
            bucket.append((key, value))  # Insert new pair
            self.size += 1

        def get(self, key):
            index = self._hash(key)
            bucket = self.buckets[index]
            for k, v in bucket:
                if k == key:
                    return v
            return None

        def remove(self, key):
            index = self._hash(key)
            bucket = self.buckets[index]
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    del bucket[i]
                    self.size -= 1
                    return True
            return False

    hm = HashMap(capacity=5)
    hm.put("apple", 100)
    hm.put("banana", 200)
    hm.put("orange", 300)
    hm.put("apple", 150)  # Update

    print(f"HashMap size: {hm.size}")
    print(f"  get('apple'):  {hm.get('apple')}")
    print(f"  get('banana'): {hm.get('banana')}")
    print(f"  get('grape'):  {hm.get('grape')} (Not found)")


# %% [markdown]
# ### 📌 Cell 2: Two Sum Problem ($O(N)$ with Hash Map)
# Storing complements in a hash map to achieve single-pass $O(N)$ lookups.

# %% [code]
def cell_2():
    """Cell 2: Two Sum using Complement Lookups"""
    print("=" * 60)
    print("▶ CELL 2: Two Sum (Hash Map Lookup in O(N) Time)")
    print("=" * 60)

    def two_sum(nums: list, target: int) -> list:
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

    nums = [2, 7, 11, 15]
    target = 9
    indices = two_sum(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Indices found: {indices} (Values: {nums[indices[0]]} + {nums[indices[1]]} = {target})")


# %% [markdown]
# ### 📌 Cell 3: Group Anagrams with Categorical Signatures
# Grouping words by character frequency tuples or sorted string keys.

# %% [code]
def cell_3():
    """Cell 3: Group Anagrams via Frequency Keying"""
    print("=" * 60)
    print("▶ CELL 3: Group Anagrams (Frequency Signatures)")
    print("=" * 60)

    def group_anagrams(strs: list) -> list:
        anagram_map = defaultdict(list)
        for s in strs:
            # Count character frequencies (26 lowercase English letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Tuple can be used as dictionary key because it is immutable & hashable!
            anagram_map[tuple(count)].append(s)
        return list(anagram_map.values())

    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    grouped = group_anagrams(words)
    print(f"Input Words: {words}")
    print(f"Grouped Anagrams:\n  {grouped}")


# %% [markdown]
# ### 📌 Cell 4: Longest Consecutive Sequence ($O(N)$ with Hash Set)
# Identifying sequence starts using set lookup in linear time.

# %% [code]
def cell_4():
    """Cell 4: Longest Consecutive Sequence in O(N)"""
    print("=" * 60)
    print("▶ CELL 4: Longest Consecutive Sequence (Hash Set in O(N))")
    print("=" * 60)

    def longest_consecutive(nums: list) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if num is the start of a streak
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

    sample = [100, 4, 200, 1, 3, 2]
    streak = longest_consecutive(sample)
    print(f"Array: {sample}")
    print(f"Longest Consecutive Streak Length: {streak} (Sequence: [1, 2, 3, 4])")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Custom HashMap with Separate Chaining", cell_1),
    2: ("Two Sum with Hash Map in O(N)", cell_2),
    3: ("Group Anagrams with Frequency Signatures", cell_3),
    4: ("Longest Consecutive Sequence in O(N)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 04_HASHING_AND_HASH_TABLES_INTERACTIVE.PY")
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
                print("Usage: python 04_Hashing_and_Hash_Tables_interactive.py [cell_number | --all]")
    else:
        run_all()
