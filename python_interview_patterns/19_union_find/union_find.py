import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
Union-Find (Disjoint Set Union - DSU) - Practice One Question at a Time
=====================================================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 25)
2. Write your logic in the corresponding function (q1 to q25)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== DSU BASE CLASS TEMPLATE ====================
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i, root_j = self.find(i), self.find(j)
        if root_i == root_j:
            return False
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        self.count -= 1
        return True


# ==================== ALL 25 QUESTIONS ====================

def q1(n: int, edges: list) -> int:
    """Q1: Number of Connected Components in an Undirected Graph (LC 323).
    Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
    Expected Output: 2
    """
    uf = UnionFind(n)
    for u, v in edges:
        uf.union(u, v)
    return uf.count


def q2(edges: list) -> list:
    """Q2: Redundant Connection (LC 684). Return the edge that creates a cycle in a 1-indexed graph.
    Input: edges = [[1, 2], [1, 3], [2, 3]]
    Expected Output: [2, 3]
    """
    n = len(edges)
    uf = UnionFind(n + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]
    return []


def q3(isConnected: list) -> int:
    """Q3: Number of Provinces (LC 547 / Friend Circles).
    Input: isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    Expected: 2
    """
    # Write your logic here
    pass


def q4(n: int, edges: list) -> bool:
    """Q4: Graph Valid Tree (LC 261). Check if given n nodes and edges form a valid single tree.
    Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    Expected: True
    """
    # Write your logic here
    pass


def q5(accounts: list) -> list:
    """Q5: Accounts Merge (LC 721). Merge accounts having the same email address.
    Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    Expected: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    """
    # Write your logic here
    pass


def q6(equations: list) -> bool:
    """Q6: Satisfiability of Equality Equations (LC 990). Given equations like ["a==b","b!=c","c==a"], check consistency.
    Input: equations = ["a==b", "b!=a"]
    Expected: False
    """
    # Write your logic here
    pass


def q7(s: str, pairs: list) -> str:
    """Q7: Smallest String With Swaps (LC 1202).
    Input: s = "dcab", pairs = [[0, 3], [1, 2]]
    Expected: "bacd"
    """
    # Write your logic here
    pass


def q8(n: int, connections: list) -> int:
    """Q8: Number of Operations to Make Network Connected (LC 1319).
    Input: n = 4, connections = [[0, 1], [0, 2], [1, 2]]
    Expected: 1
    """
    # Write your logic here
    pass


def q9(n: int, edges: list) -> int:
    """Q9: Count Unreachable Pairs of Nodes in an Undirected Graph (LC 2316).
    Input: n = 7, edges = [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]
    Expected: 14
    """
    # Write your logic here
    pass


def q10(points: list) -> int:
    """Q10: Min Cost to Connect All Points (Kruskal's MST / LC 1584).
    Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    Expected: 20
    """
    # Write your logic here
    pass


def q11(stones: list) -> int:
    """Q11: Most Stones Removed with Same Row or Column (LC 947).
    Input: stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    Expected: 5
    """
    # Write your logic here
    pass


def q12(grid: list) -> int:
    """Q12: Swim in Rising Water (LC 778). Find minimum time t to reach bottom-right.
    Input: grid = [[0, 2], [1, 3]]
    Expected: 3
    """
    # Write your logic here
    pass


def q13(nums: list) -> int:
    """Q13: Longest Consecutive Sequence using DSU or Hash Set (LC 128).
    Input: nums = [100, 4, 200, 1, 3, 2]
    Expected: 4
    """
    # Write your logic here
    pass


def q14(n: int, edges: list, source: int, destination: int) -> bool:
    """Q14: Find if Path Exists in Graph (LC 1971).
    Input: n = 3, edges = [[0, 1], [1, 2], [2, 0]], source = 0, destination = 2
    Expected: True
    """
    # Write your logic here
    pass


def q15(grid: list) -> int:
    """Q15: Max Area of Island (LC 695).
    Input: grid = [[0, 1], [1, 1]]
    Expected: 3
    """
    # Write your logic here
    pass


def q16(grid: list) -> int:
    """Q16: Making A Large Island (LC 827). Change at most one 0 to 1 to maximize island area.
    Input: grid = [[1, 0], [0, 1]]
    Expected: 3
    """
    # Write your logic here
    pass


def q17(grid: list) -> int:
    """Q17: Regions Cut By Slashes (LC 959).
    Input: grid = [" /", "/ "]
    Expected: 2
    """
    # Write your logic here
    pass


def q18(row: list) -> int:
    """Q18: Couples Holding Hands (LC 765). Min swaps so every couple sits together.
    Input: row = [0, 2, 1, 3]
    Expected: 1
    """
    # Write your logic here
    pass


def q19(words1: list, words2: list, pairs: list) -> bool:
    """Q19: Sentence Similarity II (LC 737). Transitive similarity between words.
    Input: words1 = ["great", "acting", "skills"], words2 = ["fine", "drama", "talent"], pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
    Expected: True
    """
    # Write your logic here
    pass


def q20(strs: list) -> int:
    """Q20: Similar String Groups (LC 839). Group words that differ by at most 2 character swaps.
    Input: strs = ["tars", "rats", "arts", "star"]
    Expected: 2
    """
    # Write your logic here
    pass


def q21(n: int, edges: list) -> bool:
    """Q21: Is Graph Bipartite using Union-Find (LC 785).
    Input: n = 4, edges = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    Expected: False
    """
    # Write your logic here
    pass


def q22(n: int, edges: list) -> int:
    """Q22: Min Cost to Connect All Nodes (LC 1584 MST with Manhattan Distance).
    Input: n = 3, edges = [[0, 1, 5], [1, 2, 3], [0, 2, 10]]
    Expected: 8
    """
    # Write your logic here
    pass


def q23(m: int, n: int, positions: list) -> list:
    """Q23: Number of Islands II (LC 305). Dynamic island count after each land addition.
    Input: m = 3, n = 3, positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    Expected: [1, 1, 2, 3]
    """
    # Write your logic here
    pass


def q24(edges: list) -> list:
    """Q24: Redundant Connection II (Directed Graph Cycle/Two-Parents) (LC 685).
    Input: edges = [[1, 2], [1, 3], [2, 3]]
    Expected: [2, 3]
    """
    # Write your logic here
    pass


def q25(n: int, edge_list: list, queries: list) -> list:
    """Q25: Checking Existence of Edge Length Limited Paths (Offline Query + DSU) (LC 1697).
    Input: n = 3, edge_list = [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], queries = [[0, 1, 2], [0, 2, 5]]
    Expected: [False, True]
    """
    # Write your logic here
    pass


# ==================== TEST CASES ====================

TESTS = {
    1: {"name": "Connected Components", "func": q1, "input": [5, [[0, 1], [1, 2], [3, 4]]], "expected": 2},
    2: {"name": "Redundant Connection", "func": q2, "input": [[[1, 2], [1, 3], [2, 3]]], "expected": [2, 3]},
    3: {"name": "Number of Provinces", "func": q3, "input": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "expected": 2},
    4: {"name": "Graph Valid Tree", "func": q4, "input": [5, [[0, 1], [0, 2], [0, 3], [1, 4]]], "expected": True},
    5: {"name": "Accounts Merge", "func": q5, "input": [[["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]], "expected": [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]},
    6: {"name": "Satisfiability Equations", "func": q6, "input": [["a==b", "b!=a"]], "expected": False},
    7: {"name": "Smallest String With Swaps", "func": q7, "input": ["dcab", [[0, 3], [1, 2]]], "expected": "bacd"},
    8: {"name": "Network Connected", "func": q8, "input": [4, [[0, 1], [0, 2], [1, 2]]], "expected": 1},
    9: {"name": "Count Unreachable Pairs", "func": q9, "input": [7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]], "expected": 14},
    10: {"name": "Min Cost to Connect Points", "func": q10, "input": [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]], "expected": 20},
    11: {"name": "Most Stones Removed", "func": q11, "input": [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]], "expected": 5},
    12: {"name": "Swim in Rising Water", "func": q12, "input": [[[0, 2], [1, 3]]], "expected": 3},
    13: {"name": "Longest Consecutive Sequence", "func": q13, "input": [[100, 4, 200, 1, 3, 2]], "expected": 4},
    14: {"name": "Find Path Exists", "func": q14, "input": [3, [[0, 1], [1, 2], [2, 0]], 0, 2], "expected": True},
    15: {"name": "Max Area of Island", "func": q15, "input": [[[0, 1], [1, 1]]], "expected": 3},
    16: {"name": "Making A Large Island", "func": q16, "input": [[[1, 0], [0, 1]]], "expected": 3},
    17: {"name": "Regions Cut By Slashes", "func": q17, "input": [[" /", "/ "]], "expected": 2},
    18: {"name": "Couples Holding Hands", "func": q18, "input": [[0, 2, 1, 3]], "expected": 1},
    19: {"name": "Sentence Similarity II", "func": q19, "input": [["great", "acting", "skills"], ["fine", "drama", "talent"], [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]], "expected": True},
    20: {"name": "Similar String Groups", "func": q20, "input": [["tars", "rats", "arts", "star"]], "expected": 2},
    21: {"name": "Is Graph Bipartite", "func": q21, "input": [4, [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]], "expected": False},
    22: {"name": "Min Cost Connecting Edges", "func": q22, "input": [3, [[0, 1, 5], [1, 2, 3], [0, 2, 10]]], "expected": 8},
    23: {"name": "Number of Islands II", "func": q23, "input": [3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]]], "expected": [1, 1, 2, 3]},
    24: {"name": "Redundant Connection II", "func": q24, "input": [[[1, 2], [1, 3], [2, 3]]], "expected": [2, 3]},
    25: {"name": "Edge Length Limited Paths", "func": q25, "input": [3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]], "expected": [False, True]}
}


def run_test(question_num, silent=False):
    if question_num not in TESTS:
        if not silent:
            print(f"Question {question_num} does not exist. (Valid: 1 - 25)")
        return False

    test = TESTS[question_num]
    func = test["func"]
    args = test["input"]
    expected = test["expected"]

    old_stdout = sys.stdout
    if silent:
        import io
        sys.stdout = io.StringIO()

    try:
        if not silent:
            print(f"--- Running Q{question_num}: {test['name']} ---")
            print(f"Input: {args}")
            print(f"Expected: {expected}")

        if isinstance(args, list) and len(args) > 0 and isinstance(args[0], list) and len(args) == 1:
            result = func(args[0])
        elif isinstance(args, list):
            result = func(*args)
        else:
            result = func(args)

        if question_num == 5 and isinstance(result, list):
            # Sort accounts for normalized comparison
            result = sorted([[x[0]] + sorted(x[1:]) for x in result])
            expected = sorted([[x[0]] + sorted(x[1:]) for x in expected])

        if not silent:
            print(f"Your Output: {result}")

        if result == expected:
            if not silent:
                print("\n✅ PASS - Correct!")
            return True
        else:
            if not silent:
                print("\n❌ FAIL - Output doesn't match expected")
            return False
    except Exception as e:
        if not silent:
            print(f"\n❌ ERROR: {e}")
        return False
    finally:
        sys.stdout = old_stdout


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            QUESTION_NUMBER = int(sys.argv[1])
        except ValueError:
            pass

    if QUESTION_NUMBER is None or QUESTION_NUMBER == 0:
        import ast
        import inspect

        detected_q = 1
        for q_num in sorted(TESTS.keys(), reverse=True):
            test = TESTS[q_num]
            func = test['func']
            try:
                source = inspect.getsource(func)
                tree = ast.parse(source)
                func_def = tree.body[0]
                body = getattr(func_def, 'body', [])

                non_empty = False
                for stmt in body:
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                        continue
                    if isinstance(stmt, ast.Pass):
                        continue
                    non_empty = True
                    break

                if non_empty:
                    detected_q = q_num
                    break
            except Exception:
                pass
        QUESTION_NUMBER = detected_q

    run_test(QUESTION_NUMBER, silent=False)
