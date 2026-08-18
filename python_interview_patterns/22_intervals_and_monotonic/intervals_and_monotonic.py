import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
Intervals & Monotonic Deque / Stack - Practice One Question at a Time
=====================================================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 25)
2. Write your logic in the corresponding function (q1 to q25)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 25 QUESTIONS ====================

def q1(intervals: list) -> list:
    """Q1: Merge Intervals (LC 56). Merge all overlapping intervals.
    Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Expected Output: [[1, 6], [8, 10], [15, 18]]
    """
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


def q2(intervals: list, newInterval: list) -> list:
    """Q2: Insert Interval (LC 57). Insert and merge newInterval into sorted non-overlapping intervals.
    Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
    Expected Output: [[1, 5], [6, 9]]
    """
    res = []
    i = 0
    n = len(intervals)
    # Add all intervals that come before newInterval
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    # Add remaining intervals
    while i < n:
        res.append(intervals[i])
        i += 1
    return res


def q3(intervals: list) -> int:
    """Q3: Non-overlapping Intervals (LC 435). Min number of intervals to remove to make remainder non-overlapping.
    Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    Expected: 1
    """
    # Write your logic here
    pass


def q4(intervals: list) -> bool:
    """Q4: Meeting Rooms (LC 252). Determine if a person can attend all meetings.
    Input: intervals = [[0, 30], [5, 10], [15, 20]]
    Expected: False
    """
    # Write your logic here
    pass


def q5(intervals: list) -> int:
    """Q5: Meeting Rooms II (LC 253 / Sweep-line). Find minimum number of conference rooms required.
    Input: intervals = [[0, 30], [5, 10], [15, 20]]
    Expected: 2
    """
    # Write your logic here
    pass


def q6(points: list) -> int:
    """Q6: Minimum Number of Arrows to Burst Balloons (LC 452).
    Input: points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    Expected: 2
    """
    # Write your logic here
    pass


def q7(firstList: list, secondList: list) -> list:
    """Q7: Interval List Intersections (LC 986).
    Input: firstList = [[0, 2], [5, 10], [13, 23], [24, 25]], secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    Expected: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    """
    # Write your logic here
    pass


def q8(trips: list, capacity: int) -> bool:
    """Q8: Car Pooling (LC 1094 / Difference Array / Sweep-line).
    Input: trips = [[2, 1, 5], [3, 3, 7]], capacity = 4
    Expected: False
    """
    # Write your logic here
    pass


def q9(nums: list, k: int) -> list:
    """Q9: Sliding Window Maximum using Monotonic Deque (LC 239) in O(n) time.
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Expected: [3, 3, 5, 5, 6, 7]
    """
    # Write your logic here
    pass


def q10(nums: list, limit: int) -> int:
    """Q10: Longest Continuous Subarray With Absolute Diff <= Limit (LC 1438) using two monotonic deques.
    Input: nums = [8, 2, 4, 7], limit = 4
    Expected: 2
    """
    # Write your logic here
    pass


def q11(nums: list, k: int) -> int:
    """Q11: Jump Game VI (LC 1696 Monotonic Queue DP). Max score to reach last index.
    Input: nums = [1, -1, -2, 4, -7, 3], k = 2
    Expected: 7
    """
    # Write your logic here
    pass


def q12(nums: list, k: int) -> int:
    """Q12: Constrained Subsequence Sum (LC 1425).
    Input: nums = [10, 2, -10, 5, 20], k = 2
    Expected: 37
    """
    # Write your logic here
    pass


def q13(nums: list, k: int) -> int:
    """Q13: Shortest Subarray with Sum at Least K (LC 862 Monotonic Deque + Prefix Sum).
    Input: nums = [2, -1, 2], k = 3
    Expected: 3
    """
    # Write your logic here
    pass


def q14(temperatures: list) -> list:
    """Q14: Daily Temperatures (LC 739 Monotonic Decreasing Stack).
    Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    """
    # Write your logic here
    pass


def q15(heights: list) -> int:
    """Q15: Largest Rectangle in Histogram (LC 84 Monotonic Stack).
    Input: heights = [2, 1, 5, 6, 2, 3]
    Expected: 10
    """
    # Write your logic here
    pass


def q16(matrix: list) -> int:
    """Q16: Maximal Rectangle in Binary Matrix (LC 85).
    Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    Expected: 6
    """
    # Write your logic here
    pass


def q17(arr: list) -> int:
    """Q17: Sum of Subarray Minimums (LC 907 Monotonic Stack). Return sum modulo 10^9 + 7.
    Input: arr = [3, 1, 2, 4]
    Expected: 17
    """
    # Write your logic here
    pass


def q18(nums: list) -> int:
    """Q18: Sum of Subarray Ranges (LC 2104). Sum of (max - min) over all contiguous subarrays.
    Input: nums = [1, 2, 3]
    Expected: 4
    """
    # Write your logic here
    pass


def q19(nums: list) -> bool:
    """Q19: 132 Pattern (LC 456 Monotonic Stack).
    Input: nums = [3, 1, 4, 2]
    Expected: True
    """
    # Write your logic here
    pass


def q20(heights: list) -> list:
    """Q20: Number of Visible People in a Queue (LC 1944).
    Input: heights = [10, 6, 8, 5, 11, 9]
    Expected: [3, 1, 2, 1, 1, 0]
    """
    # Write your logic here
    pass


def q21(nums: list, k: int) -> int:
    """Q21: Subarrays with K Different Integers (LC 992 Exact K = AtMost(K) - AtMost(K - 1)).
    Input: nums = [1, 2, 1, 2, 3], k = 2
    Expected: 7
    """
    # Write your logic here
    pass


def q22(s: str, k: int) -> int:
    """Q22: Substring with At Least K Repeating Characters (LC 395).
    Input: s = "aaabb", k = 3
    Expected: 3
    """
    # Write your logic here
    pass


def q23(nums: list, k: int) -> int:
    """Q23: Maximum Subarray Sum with One Deletion (LC 1186).
    Input: nums = [1, -2, 0, 3]
    Expected: 4
    """
    # Write your logic here
    pass


def q24(schedule: list) -> list:
    """Q24: Employee Free Time (LC 759 Interval Sweep).
    Input: schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    Expected: [[3, 4]]
    """
    # Write your logic here
    pass


def q25(nums: list, k: int) -> int:
    """Q25: Minimum Operations to Reduce X to Zero (LC 1658 Sliding Window Inversion).
    Input: nums = [1, 1, 4, 2, 3], k = 5
    Expected: 2
    """
    # Write your logic here
    pass


# ==================== TEST CASES ====================

TESTS = {
    1: {"name": "Merge Intervals", "func": q1, "input": [[[1, 3], [2, 6], [8, 10], [15, 18]]], "expected": [[1, 6], [8, 10], [15, 18]]},
    2: {"name": "Insert Interval", "func": q2, "input": [[[1, 3], [6, 9]], [2, 5]], "expected": [[1, 5], [6, 9]]},
    3: {"name": "Non-overlapping Intervals", "func": q3, "input": [[[1, 2], [2, 3], [3, 4], [1, 3]]], "expected": 1},
    4: {"name": "Meeting Rooms", "func": q4, "input": [[[0, 30], [5, 10], [15, 20]]], "expected": False},
    5: {"name": "Meeting Rooms II", "func": q5, "input": [[[0, 30], [5, 10], [15, 20]]], "expected": 2},
    6: {"name": "Burst Balloons Arrows", "func": q6, "input": [[[10, 16], [2, 8], [1, 6], [7, 12]]], "expected": 2},
    7: {"name": "Interval Intersections", "func": q7, "input": [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]], "expected": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]},
    8: {"name": "Car Pooling", "func": q8, "input": [[[2, 1, 5], [3, 3, 7]], 4], "expected": False},
    9: {"name": "Sliding Window Maximum", "func": q9, "input": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [3, 3, 5, 5, 6, 7]},
    10: {"name": "Longest Subarray Diff Limit", "func": q10, "input": [[8, 2, 4, 7], 4], "expected": 2},
    11: {"name": "Jump Game VI", "func": q11, "input": [[1, -1, -2, 4, -7, 3], 2], "expected": 7},
    12: {"name": "Constrained Subsequence Sum", "func": q12, "input": [[10, 2, -10, 5, 20], 2], "expected": 37},
    13: {"name": "Shortest Subarray Sum >= K", "func": q13, "input": [[2, -1, 2], 3], "expected": 3},
    14: {"name": "Daily Temperatures", "func": q14, "input": [[73, 74, 75, 71, 69, 72, 76, 73]], "expected": [1, 1, 4, 2, 1, 1, 0, 0]},
    15: {"name": "Largest Rectangle Histogram", "func": q15, "input": [[2, 1, 5, 6, 2, 3]], "expected": 10},
    16: {"name": "Maximal Rectangle", "func": q16, "input": [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]], "expected": 6},
    17: {"name": "Sum Subarray Minimums", "func": q17, "input": [[3, 1, 2, 4]], "expected": 17},
    18: {"name": "Sum Subarray Ranges", "func": q18, "input": [[1, 2, 3]], "expected": 4},
    19: {"name": "132 Pattern", "func": q19, "input": [[3, 1, 4, 2]], "expected": True},
    20: {"name": "Visible People Queue", "func": q20, "input": [[10, 6, 8, 5, 11, 9]], "expected": [3, 1, 2, 1, 1, 0]},
    21: {"name": "Subarrays K Different Ints", "func": q21, "input": [[1, 2, 1, 2, 3], 2], "expected": 7},
    22: {"name": "At Least K Repeating Chars", "func": q22, "input": ["aaabb", 3], "expected": 3},
    23: {"name": "Max Subarray Sum Deletion", "func": q23, "input": [[1, -2, 0, 3]], "expected": 4},
    24: {"name": "Employee Free Time", "func": q24, "input": [[[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]], "expected": [[3, 4]]},
    25: {"name": "Reduce X to Zero", "func": q25, "input": [[1, 1, 4, 2, 3], 5], "expected": 2}
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
