import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
Cyclic Sort & In-Place Array Indexing - Practice One Question at a Time
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

def q1(nums: list) -> int:
    """Q1: Missing Number (LC 268). Array contains n distinct numbers in range [0, n]. Return the missing one.
    Input: nums = [3, 0, 1]
    Expected Output: 2
    """
    i = 0
    n = len(nums)
    while i < n:
        correct_idx = nums[i]
        if nums[i] < n and nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i:
            return i
    return n


def q2(nums: list) -> list:
    """Q2: Find All Numbers Disappeared in an Array (LC 448). Range [1, n] in O(n) time, O(1) extra space.
    Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
    Expected Output: [5, 6]
    """
    i = 0
    while i < len(nums):
        correct_idx = nums[i] - 1
        if nums[i] != nums[correct_idx]:
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        else:
            i += 1
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)
    return missing


def q3(nums: list) -> int:
    """Q3: Find the Duplicate Number (LC 287). Array of n + 1 integers in range [1, n].
    Input: nums = [1, 3, 4, 2, 2]
    Expected: 2
    """
    # Write your logic here
    pass


def q4(nums: list) -> list:
    """Q4: Find All Duplicates in an Array (LC 442). Range [1, n], elements appear once or twice.
    Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
    Expected: [2, 3]
    """
    # Write your logic here
    pass


def q5(nums: list) -> list:
    """Q5: Set Mismatch (LC 645). Find the duplicate number and the missing number [duplicate, missing].
    Input: nums = [1, 2, 2, 4]
    Expected: [2, 3]
    """
    # Write your logic here
    pass


def q6(nums: list) -> int:
    """Q6: First Missing Positive (LC 41). Smallest positive integer not present in unsorted array in O(n) time, O(1) space.
    Input: nums = [3, 4, -1, 1]
    Expected: 2
    """
    # Write your logic here
    pass


def q7(arr: list, k: int) -> int:
    """Q7: Kth Missing Positive Number (LC 1539).
    Input: arr = [2, 3, 4, 7, 11], k = 5
    Expected: 9
    """
    # Write your logic here
    pass


def q8(nums: list, k: int) -> list:
    """Q8: Find the First K Missing Positive Numbers.
    Input: nums = [3, -1, 4, 5, 5], k = 3
    Expected: [1, 2, 6]
    """
    # Write your logic here
    pass


def q9(nums: list) -> int:
    """Q9: Array Nesting (LC 565). Find longest set S[k] = {A[k], A[A[k]], ...}.
    Input: nums = [5, 4, 0, 3, 1, 6, 2]
    Expected: 4
    """
    # Write your logic here
    pass


def q10(nums: list) -> list:
    """Q10: Sort Colors / Dutch National Flag (LC 75). Sort array of 0s, 1s, 2s in-place.
    Input: nums = [2, 0, 2, 1, 1, 0]
    Expected: [0, 0, 1, 1, 2, 2]
    """
    # Write your logic here
    pass


def q11(nums: list) -> int:
    """Q11: Minimum Number of Swaps to Sort Array.
    Input: nums = [4, 3, 2, 1]
    Expected: 2
    """
    # Write your logic here
    pass


def q12(nums: list) -> list:
    """Q12: Rearrange Array Elements by Sign (LC 2149). Alternate positive and negative maintaining order.
    Input: nums = [3, 1, -2, -5, 2, -4]
    Expected: [3, -2, 1, -5, 2, -4]
    """
    # Write your logic here
    pass


def q13(citations: list) -> int:
    """Q13: H-Index (LC 274) using counting/bucket sort in O(n).
    Input: citations = [3, 0, 6, 1, 5]
    Expected: 3
    """
    # Write your logic here
    pass


def q14(nums: list) -> int:
    """Q14: Maximum Gap (LC 164) in linear O(n) time using Bucket Sort / Pigeonhole principle.
    Input: nums = [3, 6, 9, 1]
    Expected: 3
    """
    # Write your logic here
    pass


def q15(nums: list) -> list:
    """Q15: Wiggle Sort (LC 280). Reorder nums such that nums[0] <= nums[1] >= nums[2] <= nums[3]... in O(n) in-place.
    Input: nums = [3, 5, 2, 1, 6, 4]
    Expected: [3, 5, 1, 6, 2, 4]
    """
    # Write your logic here
    pass


def q16(nums: list) -> bool:
    """Q16: Check if Array is Sorted and Rotated (LC 1752).
    Input: nums = [3, 4, 5, 1, 2]
    Expected: True
    """
    # Write your logic here
    pass


def q17(nums: list) -> int:
    """Q17: Smallest Value of the Rearranged Number (LC 2164).
    Input: nums = [4, 1, 2, 3]
    Expected: [2, 3, 4, 1]
    """
    # Write your logic here
    pass


def q18(nums: list, target: int) -> int:
    """Q18: Minimum Operations to Make Array Equal to Target.
    Input: nums = [1, 2, 3, 4], target = 3
    Expected: 4
    """
    # Write your logic here
    pass


def q19(nums: list) -> int:
    """Q19: Find All Numbers With Unique Occurrences (LC 1207).
    Input: nums = [1, 2, 2, 1, 1, 3]
    Expected: True
    """
    # Write your logic here
    pass


def q20(nums: list) -> list:
    """Q20: Relative Sort Array (LC 1122). Sort arr1 according to the relative order defined in arr2.
    Input: arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2 = [2, 1, 4, 3, 9, 6]
    Expected: [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    """
    # Write your logic here
    pass


def q21(nums: list) -> int:
    """Q21: Maximum Product of Three Numbers (LC 628) in single pass O(n).
    Input: nums = [-10, -10, 5, 2]
    Expected: 500
    """
    # Write your logic here
    pass


def q22(nums: list) -> int:
    """Q22: Majority Element II (Boyer-Moore Voting Algorithm / LC 229). Elements appearing > n // 3 times.
    Input: nums = [3, 2, 3]
    Expected: [3]
    """
    # Write your logic here
    pass


def q23(nums: list, value: int) -> int:
    """Q23: Smallest Missing Non-Negative Value After Modulo Operations (LC 2598).
    Input: nums = [1, -10, 7, 13, 6, 8], value = 5
    Expected: 4
    """
    # Write your logic here
    pass


def q24(nums: list) -> int:
    """Q24: Find Peak Element (LC 162). Return index of any peak element.
    Input: nums = [1, 2, 3, 1]
    Expected: 2
    """
    # Write your logic here
    pass


def q25(nums: list) -> int:
    """Q25: Continuous Subarray Sum divisible by k (LC 523).
    Input: nums = [23, 2, 4, 6, 7], k = 6
    Expected: True
    """
    # Write your logic here
    pass


# ==================== TEST CASES ====================

TESTS = {
    1: {"name": "Missing Number", "func": q1, "input": [[3, 0, 1]], "expected": 2},
    2: {"name": "Find Disappeared Numbers", "func": q2, "input": [[4, 3, 2, 7, 8, 2, 3, 1]], "expected": [5, 6]},
    3: {"name": "Find Duplicate Number", "func": q3, "input": [[1, 3, 4, 2, 2]], "expected": 2},
    4: {"name": "Find All Duplicates", "func": q4, "input": [[4, 3, 2, 7, 8, 2, 3, 1]], "expected": [2, 3]},
    5: {"name": "Set Mismatch", "func": q5, "input": [[1, 2, 2, 4]], "expected": [2, 3]},
    6: {"name": "First Missing Positive", "func": q6, "input": [[3, 4, -1, 1]], "expected": 2},
    7: {"name": "Kth Missing Positive", "func": q7, "input": [[2, 3, 4, 7, 11], 5], "expected": 9},
    8: {"name": "First K Missing Positive", "func": q8, "input": [[3, -1, 4, 5, 5], 3], "expected": [1, 2, 6]},
    9: {"name": "Array Nesting", "func": q9, "input": [[5, 4, 0, 3, 1, 6, 2]], "expected": 4},
    10: {"name": "Sort Colors", "func": q10, "input": [[2, 0, 2, 1, 1, 0]], "expected": [0, 0, 1, 1, 2, 2]},
    11: {"name": "Min Swaps to Sort", "func": q11, "input": [[4, 3, 2, 1]], "expected": 2},
    12: {"name": "Rearrange by Sign", "func": q12, "input": [[3, 1, -2, -5, 2, -4]], "expected": [3, -2, 1, -5, 2, -4]},
    13: {"name": "H-Index", "func": q13, "input": [[3, 0, 6, 1, 5]], "expected": 3},
    14: {"name": "Maximum Gap", "func": q14, "input": [[3, 6, 9, 1]], "expected": 3},
    15: {"name": "Wiggle Sort", "func": q15, "input": [[3, 5, 2, 1, 6, 4]], "expected": [3, 5, 1, 6, 2, 4]},
    16: {"name": "Sorted and Rotated", "func": q16, "input": [[3, 4, 5, 1, 2]], "expected": True},
    17: {"name": "Sort Even and Odd", "func": q17, "input": [[4, 1, 2, 3]], "expected": [2, 3, 4, 1]},
    18: {"name": "Min Operations to Target", "func": q18, "input": [[1, 2, 3, 4], 3], "expected": 4},
    19: {"name": "Unique Occurrences", "func": q19, "input": [[1, 2, 2, 1, 1, 3]], "expected": True},
    20: {"name": "Relative Sort Array", "func": q20, "input": [[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]], "expected": [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]},
    21: {"name": "Max Product of Three", "func": q21, "input": [[-10, -10, 5, 2]], "expected": 500},
    22: {"name": "Majority Element II", "func": q22, "input": [[3, 2, 3]], "expected": [3]},
    23: {"name": "Smallest Missing Modulo", "func": q23, "input": [[1, -10, 7, 13, 6, 8], 5], "expected": 4},
    24: {"name": "Find Peak Element", "func": q24, "input": [[1, 2, 3, 1]], "expected": 2},
    25: {"name": "Continuous Subarray Sum", "func": q25, "input": [[23, 2, 4, 6, 7], 6], "expected": True}
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

        if question_num == 4 and isinstance(result, list):
            result = sorted(result)
            expected = sorted(expected)

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
