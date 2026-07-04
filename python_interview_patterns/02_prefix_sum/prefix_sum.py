import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
Prefix Sum - Practice One Question at a Time
=============================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve
2. Write your logic in the corresponding function
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 100 QUESTIONS ====================


def q1(arr):
    """Q1: Build Prefix Sum Array - arr = [1, 2, 3, 4, 5]"""
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix


def q2(arr, left, right):
    """Q2: Range Sum Query - arr = [1,2,3,4,5,6], left=2, right=4"""
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if left == 0:
        return prefix[right]
    else:
        return prefix[right] - prefix[left - 1]


def q3(arr):
    """Q3: Total Sum Using Prefix - arr = [5, 10, 15, 20, 25]"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix[n-1]


def q4(arr, index):
    """Q4: Sum from Start to Index - arr = [2,4,6,8,10], index=3"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * (index + 1)
    prefix[0] = arr[0]
    for i in range(1, index + 1):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix[index]


def q5(arr, queries):
    """Q5: Multiple Range Queries"""
    # Write your logic here
    result = []
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    for query in queries:
        if query[0] == 0:
            result.append(prefix[query[1]])
        else:
            result.append(prefix[query[1]]-prefix[query[0]-1])
    return result


def q6(arr):
    """Q6: Prefix Sum with Negative Numbers"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix


def q7(arr, left, right):
    """Q7: Sum Between Two Indices (Exclusive)"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if left == 0:
        return prefix[right]
    else:
        return prefix[right-1] - prefix[left]


def q8(arr):
    """Q8: Compare sum of first half and second half"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    mid = n // 2
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix[mid-1] == prefix[n-1] - prefix[mid-1]


def q9(arr):
    """Q9: Running Sum at Each Index"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix


def q10(arr):
    """Q10: Maximum Prefix Sum"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix[n-1]


def q11(arr):
    """Q11: Minimum Prefix Sum"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    min_num = prefix[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
        if prefix[i] < min_num:
            min_num = prefix[i]
    return min_num


def q12(arr):
    """Q12: Count Positive Prefix Sums"""
    # Write your logic here
    count = 0
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    if prefix[0] > 0:
        count += 1

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        if prefix[i] > 0:
            count += 1
    print(prefix)
    return count


def q13(arr, k):
    """Q13: First Index Where Prefix Sum > K"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    if prefix[0] > k:
        return 0
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
        if prefix[i] > k:
            return i


def q14(arr, k):
    """Q14: Last Index Where Prefix Sum < K"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1]+arr[i]
    for i in range(n-1, -1, -1):
        if prefix[i] < k:
            return i
    return -1


def q15(arr, n):
    """Q15: Sum of First N Elements"""
    # Write your logic here
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1]+arr[i]
    return prefix[-1]


def q16(arr, n):
    """Q16: Sum of Last N Elements"""
    # Write your logic here
    length = len(arr)
    prefix = [0] * length
    prefix[0] = arr[0]
    for i in range(1, length):
        prefix[i] = prefix[i-1] + arr[i]
    if n == length:
        return prefix[length-1]
    return prefix[length-1] - prefix[length-n-1]


def q17(arr, left, right):
    """Q17: Average of Range"""
    # Write your logic here
    n = len(arr)
    prefix = [0] *n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if left == 0:
        result = prefix[right]
    else:
        result = prefix[right] - prefix[left-1]
    return result/(right-left+1)


def q18(arr):
    """Q18: Prefix Sum with Zeros"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix


def q19(arr, index):
    """Q19: Range Sum with Single Element"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if index == 0:
        return prefix[index]
    return prefix[index] - prefix[index-1]


def q20(arr, left, right):
    """Q20: Validate Range Sum"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for_loop_result = 0
    for j in range(left, right+1):
        for_loop_result += arr[j]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if left == 0:
        result = prefix[right]
    else:
        result = prefix[right] - prefix[left-1]
    return for_loop_result == result


def q21(arr):
    """Q21: Prefix Sum of Even Numbers Only"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    if arr[0] % 2 == 0:
        prefix[0] = arr[0]
    else:
        prefix[0] = 0
    for i in range(1, n):
        if arr[i] % 2 == 0:
            prefix[i] = prefix[i-1] + arr[i]
        else:
            prefix[i] = prefix[i-1]
    return prefix


def q22(arr):
    """Q22: Prefix Sum of Odd Numbers Only"""
    n = len(arr)
    prefix = [0] * n
    if arr[0] % 2 != 0:
        prefix[0] = arr[0]
    else:
        prefix[0] = 0

    for i in range(1, n):
        if arr[i] % 2 != 0:
            prefix[i] = prefix[i-1] + arr[i]
        else:
            prefix[i] = prefix[i-1]
    return prefix


def q23(arr, left, right):
    if not arr:
        return 0
    return right - left + 1


def q24(arr):
    """Q24: Suffix Sum (Prefix Sum Reversed)"""
    # Write your logic here
    n = len(arr)
    suffix = [0] * n
    suffix[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix[i] = arr[i] + suffix[i+1]
    return suffix


def q25(arr, left, right):
    """Q25: Difference Between Two Prefix Sums"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    if left == 0:
        return prefix[right]
    return prefix[right-1] - prefix[left]


def q26(arr):
    """Q26: Find if Subarray with Sum 0 Exists"""
    # Write your logic here
    prefix_sum = 0
    seen = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0:
            return True
        if prefix_sum in seen:
            return True
        seen.add(prefix_sum)
    return False


def q27(arr, k):
    """Q27: Count Subarrays with Sum K"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    count = 0

    for i in range(n):
        for j in range(i, n):
            if i == 0:
                sub_sum = prefix[j]
            else:
                sub_sum = prefix[j] - prefix[i - 1]
            if sub_sum == k:
                count += 1
    return count


def q28(arr, k):
    """Q28: Longest Subarray with Sum K"""
    # Write your logic here
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]

    result = 0
    for i in range(n):
        for j in range(i, n):
            if i == 0:
                result


def q29(arr):
    """Q29: Maximum Subarray Sum"""
    # Write your logic here
    pass


def q30(arr):
    """Q30: Minimum Subarray Sum"""
    # Write your logic here
    pass


def q31(arr, k):
    """Q31: Count Subarrays with Sum Divisible by K"""
    # Write your logic here
    pass


def q32(arr):
    """Q32: Find Equilibrium Index"""
    # Write your logic here
    pass


def q33(arr):
    """Q33: Product of Array Except Self"""
    # Write your logic here
    pass


def q34(arr, queries):
    """Q34: Range Sum Query - Immutable"""
    # Write your logic here
    pass


def q35(arr, n):
    """Q35: Find Missing Number Using Sum"""
    # Write your logic here
    pass


def q36(arr):
    """Q36: Count Subarrays with Odd Sum"""
    # Write your logic here
    pass


def q37(arr):
    """Q37: Count Subarrays with Even Sum"""
    # Write your logic here
    pass


def q38(arr, k):
    """Q38: Maximum Sum Subarray of Size K"""
    # Write your logic here
    pass


def q39(arr, k):
    """Q39: Minimum Sum Subarray of Size K"""
    # Write your logic here
    pass


def q40(arr, sum_left, sum_right):
    """Q40: Count Subarrays with Sum in Range"""
    # Write your logic here
    pass


def q41(arr, n):
    """Q41: Find Duplicate Using Sum"""
    # Write your logic here
    pass


def q42(arr):
    """Q42: Alternating Sum"""
    # Write your logic here
    pass


def q43(arr):
    """Q43: Cumulative Frequency"""
    # Write your logic here
    pass


def q44(arr, target):
    """Q44: Subarray with Given Sum (Positive Numbers)"""
    # Write your logic here
    pass


def q45(arr, target):
    """Q45: Subarray with Given Sum (Including Negative)"""
    # Write your logic here
    pass


def q46(arr, k):
    """Q46: Maximum Sum of Two Non-Overlapping Subarrays"""
    # Write your logic here
    pass


def q47(arr, k):
    """Q47: Find All Subarrays with Sum K"""
    # Write your logic here
    pass


def q48(arr, k):
    """Q48: Count Subarrays with Sum Less Than K"""
    # Write your logic here
    pass


def q49(arr, k):
    """Q49: Count Subarrays with Sum Greater Than K"""
    # Write your logic here
    pass


def q50(arr, k):
    """Q50: Subarray Product Less Than K"""
    # Write your logic here
    pass


def q51(arr):
    """Q51: Find Pivot Index"""
    # Write your logic here
    pass


def q52(arr):
    """Q52: Middle Index with Equal Sums"""
    # Write your logic here
    pass


def q53(arr, k):
    """Q53: Subarray Sum Multiple of K"""
    # Write your logic here
    pass


def q54(arr, k):
    """Q54: Continuous Subarray Sum Multiple of K"""
    # Write your logic here
    pass


def q55(arr, range_min, range_max):
    """Q55: Subarray Sum in Range"""
    # Write your logic here
    pass


def q56(arr):
    """Q56: Maximum Sum Circular Subarray"""
    # Write your logic here
    pass


def q57(arr, target):
    """Q57: Minimum Size Subarray Sum"""
    # Write your logic here
    pass


def q58(arr, k):
    """Q58: Subarray Sum Closest to K"""
    # Write your logic here
    pass


def q59(arr):
    """Q59: Most Frequent Subarray Sum"""
    # Write your logic here
    pass


def q60(arr):
    """Q60: Longest Subarray with Equal 0s and 1s"""
    # Write your logic here
    pass


def q61(matrix):
    """Q61: Build 2D Prefix Sum"""
    # Write your logic here
    pass


def q62(matrix, row1, col1, row2, col2):
    """Q62: 2D Range Sum Query"""
    # Write your logic here
    pass


def q63(matrix):
    """Q63: Maximum Sum Rectangle in 2D"""
    # Write your logic here
    pass


def q64(matrix):
    """Q64: Count Negative Numbers in Sorted Matrix"""
    # Write your logic here
    pass


def q65(nums):
    """Q65: Running Sum of 1D Array"""
    # Write your logic here
    pass


def q66(n):
    """Q66: Find N Unique Integers Sum up to Zero"""
    # Write your logic here
    pass


def q67(nums):
    """Q67: Decompress Run-Length Encoded List"""
    # Write your logic here
    pass


def q68(grid, k):
    """Q68: Shift 2D Grid"""
    # Write your logic here
    pass


def q69(mat, k):
    """Q69: Matrix Block Sum"""
    # Write your logic here
    pass


def q70(trips, capacity):
    """Q70: Car Pooling"""
    # Write your logic here
    pass


def q71(bookings, n):
    """Q71: Corporate Flight Bookings"""
    # Write your logic here
    pass


def q72(n):
    """Q72: Minimum Operations to Make Array Equal"""
    # Write your logic here
    pass


def q73(nums):
    """Q73: Find All Duplicates in Array"""
    # Write your logic here
    pass


def q74(nums, n):
    """Q74: Find All Numbers Disappeared in Array"""
    # Write your logic here
    pass


def q75(nums, k):
    """Q75: Subarray Sums Divisible by K"""
    # Write your logic here
    pass


def q76(nums, k):
    """Q76: Subarray Sum Equals K (Binary Array)"""
    # Write your logic here
    pass


def q77(nums):
    """Q77: Contiguous Array"""
    # Write your logic here
    pass


def q78(nums):
    """Q78: Maximum Length of Subarray with Positive Product"""
    # Write your logic here
    pass


def q79(nums):
    """Q79: Maximum Product Subarray"""
    # Write your logic here
    pass


def q80(nums, k):
    """Q80: Count Subarray Product Less Than K"""
    # Write your logic here
    pass


def q81(nums):
    """Q81: Find Subarrays With Equal Sum"""
    # Write your logic here
    pass


def q82(nums):
    """Q82: Partition Array Into Two Arrays with Equal Sum"""
    # Write your logic here
    pass


def q83(nums, target):
    """Q83: Target Sum"""
    # Write your logic here
    pass


def q84(nums):
    """Q84: Minimum Average Difference"""
    # Write your logic here
    pass


def q85(nums, k):
    """Q85: Count Prefix Sums Divisible by K"""
    # Write your logic here
    pass


def q86(n, updates):
    """Q86: Range Addition"""
    # Write your logic here
    pass


def q87(arr):
    """Q87: Find Longest Subarray with Equal Number of 0s and 1s"""
    # Write your logic here
    pass


def q88(arr, k):
    """Q88: Maximum Sum After Partitioning"""
    # Write your logic here
    pass


def q89(arr):
    """Q89: Subarray Sum Closest to Zero"""
    # Write your logic here
    pass


def q90(matrix):
    """Q90: Count Submatrices With Sum Zero"""
    # Write your logic here
    pass


def q91(arr, k):
    """Q91: Find K-th Smallest Subarray Sum"""
    # Write your logic here
    pass


def q92(arr, k):
    """Q92: Maximum Sum of Subarray of Length at Least K"""
    # Write your logic here
    pass


def q93(arr, target):
    """Q93: Subarray with Given Sum in Binary Array"""
    # Write your logic here
    pass


def q94(arr, k):
    """Q94: Count Subarrays with Median K"""
    # Write your logic here
    pass


def q95(arr):
    """Q95: Find Longest Subarray with Maximum Sum"""
    # Write your logic here
    pass


def q96(arr, k):
    """Q96: Subarray Sum Equals K with Removal"""
    # Write your logic here
    pass


def q97(arr, k):
    """Q97: Maximum Sum of Two Overlapping Subarrays"""
    # Write your logic here
    pass


def q98(arr, k):
    """Q98: Count Subarrays with Score Less Than K"""
    # Write your logic here
    pass


def q99(arr, ratio):
    """Q99: Find Subarray with Sum Ratio"""
    # Write your logic here
    pass


def q100(arr):
    """Q100: Complete Prefix Sum Challenge"""
    # Write your logic here
    pass


# ==================== TEST DATA ====================

TESTS = {
    1: {'func': q1, 'args': [[1, 2, 3, 4, 5]], 'expected': [1, 3, 6, 10, 15]},
    2: {'func': q2, 'args': [[1, 2, 3, 4, 5, 6], 2, 4], 'expected': 12},
    3: {'func': q3, 'args': [[5, 10, 15, 20, 25]], 'expected': 75},
    4: {'func': q4, 'args': [[2, 4, 6, 8, 10], 3], 'expected': 20},
    5: {'func': q5, 'args': [[1,2,3,4,5,6,7,8,9,10], [(0,4), (2,6), (5,9)]], 'expected': [15, 25, 40]},
    6: {'func': q6, 'args': [[5, -3, 2, -1, 4]], 'expected': [5, 2, 4, 3, 7]},
    7: {'func': q7, 'args': [[1,2,3,4,5,6,7], 2, 5], 'expected': 9},
    8: {'func': q8, 'args': [[2,3,5,7,1,4,6,8]], 'expected': False},
    9: {'func': q9, 'args': [[1, 2, 3, 4, 5]], 'expected': [1, 3, 6, 10, 15]},
    10: {'func': q10, 'args': [[3, -1, 4, -2, 5]], 'expected': 9},
    11: {'func': q11, 'args': [[2, -5, 3, -1, 4]], 'expected': -3},
    12: {'func': q12, 'args': [[5, -3, -2, 4, -1]], 'expected': 4},
    13: {'func': q13, 'args': [[2, 3, 4, 5, 1, 2], 10], 'expected': 3},
    14: {'func': q14, 'args': [[1, 2, 3, 4, 5, 6], 15], 'expected': 3},
    15: {'func': q15, 'args': [[10,20,30,40,50,60,70], 5], 'expected': 150},
    16: {'func': q16, 'args': [[1,2,3,4,5,6,7,8], 4], 'expected': 26},
    17: {'func': q17, 'args': [[5,10,15,20,25,30,35], 2, 6], 'expected': 25.0},
    18: {'func': q18, 'args': [[5, 0, 3, 0, 7]], 'expected': [5, 5, 8, 8, 15]},
    19: {'func': q19, 'args': [[10, 20, 30, 40, 50], 3], 'expected': 40},
    20: {'func': q20, 'args': [[3, 5, 7, 9, 11], 1, 3], 'expected': True},
    21: {'func': q21, 'args': [[1, 2, 3, 4, 5, 6]], 'expected': [0, 2, 2, 6, 6, 12]},
    22: {'func': q22, 'args': [[1, 2, 3, 4, 5, 6]], 'expected': [1, 1, 4, 4, 9, 9]},
    23: {'func': q23, 'args': [[5, 10, 15, 20, 25], 1, 4], 'expected': 4},
    24: {'func': q24, 'args': [[1, 2, 3, 4, 5]], 'expected': [15, 14, 12, 9, 5]},
    25: {'func': q25, 'args': [[2,4,6,8,10,12], 2, 5], 'expected': 18},
    26: {'func': q26, 'args': [[4, -3, 2, 1, -4]], 'expected': True},
    27: {'func': q27, 'args': [[1, 2, 3, 4, 5, 6], 10], 'expected': 1},
    28: {'func': q28, 'args': [[5, 10, 3, 2, 7, 1, 4], 15], 'expected': 3},
    29: {'func': q29, 'args': [[3, -1, 4, -2, 5, -3]], 'expected': 9},
    30: {'func': q30, 'args': [[2, -5, 3, -1, 4, -6]], 'expected': -6},
    31: {'func': q31, 'args': [[1, 2, 3, 4, 5], 3], 'expected': 5},
    32: {'func': q32, 'args': [[1, 2, 3, 4, 3, 2, 1]], 'expected': 3},
    33: {'func': q33, 'args': [[1, 2, 3, 4]], 'expected': [24, 12, 8, 6]},
    34: {'func': q34, 'args': [[5,3,7,2,8,4,6], [(0,3), (2,5), (1,6)]], 'expected': [17, 21, 30]},
    35: {'func': q35, 'args': [[1,2,3,5,6,7,8], 8], 'expected': 4},
    36: {'func': q36, 'args': [[1, 2, 3, 4]], 'expected': 4},
    37: {'func': q37, 'args': [[1, 2, 3, 4]], 'expected': 6},
    38: {'func': q38, 'args': [[2, 1, 5, 1, 3, 2], 3], 'expected': 9},
    39: {'func': q39, 'args': [[5, 2, 8, 1, 6, 3], 3], 'expected': 10},
    40: {'func': q40, 'args': [[1, 2, 3, 4, 5], 5, 10], 'expected': 7},
    41: {'func': q41, 'args': [[1,2,3,4,5,3], 5], 'expected': 3},
    42: {'func': q42, 'args': [[1, 2, 3, 4, 5]], 'expected': [1, -1, 4, 0, 5]},
    43: {'func': q43, 'args': [[1, 1, 2, 2, 2, 3]], 'expected': [1, 2, 3, 4, 5, 6]},
    44: {'func': q44, 'args': [[1, 2, 3, 7, 5], 12], 'expected': [3, 4]},
    45: {'func': q45, 'args': [[3, 4, -7, 1, 2, 5], 5], 'expected': True},
    46: {'func': q46, 'args': [[1,2,3,4,5,6,7], 2], 'expected': 13},
    47: {'func': q47, 'args': [[1, 1, 1], 2], 'expected': [(0, 1), (1, 2)]},
    48: {'func': q48, 'args': [[1, 2, 3, 4, 5], 10], 'expected': 10},
    49: {'func': q49, 'args': [[1, 2, 3, 4, 5], 10], 'expected': 5},
    50: {'func': q50, 'args': [[10, 5, 2, 6], 100], 'expected': 7},
    51: {'func': q51, 'args': [[1, 7, 3, 6, 5, 6]], 'expected': 3},
    52: {'func': q52, 'args': [[2, 3, -1, 8, 4]], 'expected': 3},
    53: {'func': q53, 'args': [[23, 2, 4, 6, 7], 6], 'expected': True},
    54: {'func': q54, 'args': [[23, 2, 4, 6, 7], 6], 'expected': True},
    55: {'func': q55, 'args': [[1, 2, 3, 4, 5], 8, 12], 'expected': True},
    56: {'func': q56, 'args': [[5, -3, 5]], 'expected': 7},
    57: {'func': q57, 'args': [[2,3,1,2,4,3], 7], 'expected': 2},
    58: {'func': q58, 'args': [[1, 2, 3, 4, 5], 11], 'expected': 11},
    59: {'func': q59, 'args': [[1, 2, 1, 2, 1]], 'expected': 3},
    60: {'func': q60, 'args': [[0, 1, 0, 1, 1, 0, 0]], 'expected': 6},
    61: {'func': q61, 'args': [[[1,2,3],[4,5,6],[7,8,9]]], 'expected': '2D matrix'},
    62: {'func': q62, 'args': [[[1,2,3,4],[5,6,7,8],[9,10,11,12]], 1, 1, 2, 2], 'expected': 40},
    63: {'func': q63, 'args': [[[1,-2,3],[-4,5,-6],[7,-8,9]]], 'expected': 9},
    64: {'func': q64, 'args': [[[-3,-2,-1,0],[-2,0,1,2],[-1,1,2,3]]], 'expected': 6},
    65: {'func': q65, 'args': [[1, 2, 3, 4]], 'expected': [1, 3, 6, 10]},
    66: {'func': q66, 'args': [5], 'expected': 'sum=0'},
    67: {'func': q67, 'args': [[1, 2, 3, 4]], 'expected': [2, 4, 4, 4]},
    68: {'func': q68, 'args': [[[1,2,3],[4,5,6],[7,8,9]], 1], 'expected': 'shifted'},
    69: {'func': q69, 'args': [[[1,2,3],[4,5,6],[7,8,9]], 1], 'expected': 'matrix'},
    70: {'func': q70, 'args': [[[2,1,5],[3,3,7]], 4], 'expected': False},
    71: {'func': q71, 'args': [[[1,2,10],[2,3,20],[2,5,25]], 5], 'expected': [10,55,45,25,25]},
    72: {'func': q72, 'args': [5], 'expected': 6},
    73: {'func': q73, 'args': [[4,3,2,7,8,2,3,1]], 'expected': [2, 3]},
    74: {'func': q74, 'args': [[4,3,2,7,8,2,3,1], 8], 'expected': [5, 6]},
    75: {'func': q75, 'args': [[4,5,0,-2,-3,1], 5], 'expected': 7},
    76: {'func': q76, 'args': [[1, 0, 1, 0, 1], 2], 'expected': 4},
    77: {'func': q77, 'args': [[0, 1, 0, 0, 1, 1, 0]], 'expected': 6},
    78: {'func': q78, 'args': [[1, -2, -3, 4]], 'expected': 4},
    79: {'func': q79, 'args': [[2, 3, -2, 4]], 'expected': 6},
    80: {'func': q80, 'args': [[10, 5, 2, 6], 100], 'expected': 7},
    81: {'func': q81, 'args': [[1, 2, 3, 4, 5]], 'expected': 'bool'},
    82: {'func': q82, 'args': [[1, 5, 11, 5]], 'expected': True},
    83: {'func': q83, 'args': [[1,1,1,1,1], 3], 'expected': 5},
    84: {'func': q84, 'args': [[2, 5, 3, 9, 5, 3]], 'expected': 'index'},
    85: {'func': q85, 'args': [[3, 6, 9, 12, 15], 3], 'expected': 5},
    86: {'func': q86, 'args': [5, [[1,3,2],[2,4,3]]], 'expected': [0,2,5,5,3]},
    87: {'func': q87, 'args': [[0, 0, 1, 0, 1, 1, 1]], 'expected': 4},
    88: {'func': q88, 'args': [[1,15,7,9,2,5,10], 3], 'expected': 84},
    89: {'func': q89, 'args': [[5, -3, 2, -1, 4]], 'expected': 'sum'},
    90: {'func': q90, 'args': [[[1,-1],[-1,1]]], 'expected': 3},
    91: {'func': q91, 'args': [[1, 2, 3, 4], 3], 'expected': 3},
    92: {'func': q92, 'args': [[1,2,3,-5,6,7,8], 3], 'expected': 21},
    93: {'func': q93, 'args': [[1,0,1,1,0,1], 3], 'expected': 'indices'},
    94: {'func': q94, 'args': [[3,2,1,4,5], 3], 'expected': 5},
    95: {'func': q95, 'args': [[1, 2, -1, 2, 3]], 'expected': 'length'},
    96: {'func': q96, 'args': [[1, 2, 3, 4, 5], 10], 'expected': True},
    97: {'func': q97, 'args': [[1,2,3,4,5,6], 2], 'expected': 'sum'},
    98: {'func': q98, 'args': [[2, 1, 4, 3, 5], 10], 'expected': 'count'},
    99: {'func': q99, 'args': [[1, 2, 3, 4, 5], 3.0], 'expected': 'subarray'},
    100: {'func': q100, 'args': [[5,3,8,2,7,1,4,6]], 'expected': 'results'},
}


# ==================== RUN TEST ====================


def run_test(QUESTION_NUMBER, silent=False):
    import io
    import sys
    
    # Resolve PyCharm warnings for dynamic helper references
    to_linked_list = globals().get('to_linked_list')
    to_list = globals().get('to_list')
    ListNode = globals().get('ListNode')
    to_tree = globals().get('to_tree')
    TreeNode = globals().get('TreeNode')
    
    old_stdout = sys.stdout
    captured = io.StringIO()
    if silent:
        sys.stdout = captured
        
    try:
        test = TESTS.get(QUESTION_NUMBER)
        if not test:
            if not silent:
                print(f"❌ Question {QUESTION_NUMBER} not found!")
            return False
            
        func = test['func']
        args = test['args']
        expected = test['expected']
        
        if not silent:
            print(f"\n{'='*60}")
            print(f"Question {QUESTION_NUMBER}: {func.__doc__.splitlines()[0] if func.__doc__ else 'No docstring'}")
            print(f"{'='*60}")
            print(f"Input: {args}")
            print(f"Expected: {expected}")
            print("-" * 60)
            
        # Run conversion logic if applicable (Linked Lists / Trees)
        import os
        filename = os.path.basename(__file__)
        
        if filename == "linked_lists.py" and QUESTION_NUMBER <= 25 and QUESTION_NUMBER != 19:
            processed_args = []
            if QUESTION_NUMBER == 2:
                list_vals = args[0]
                target_val = args[1]
                head = to_linked_list(list_vals)
                curr = head
                target_node = None
                while curr:
                    if curr.val == target_val:
                        target_node = curr
                        break
                    curr = curr.next
                func(target_node)
                result = to_list(head)
            elif QUESTION_NUMBER == 8:
                list_vals = args[0]
                cycle_pos = args[1]
                head = to_linked_list(list_vals)
                if cycle_pos != -1:
                    curr = head
                    cycle_node = None
                    tail = None
                    idx = 0
                    while curr:
                        if idx == cycle_pos:
                            cycle_node = curr
                        tail = curr
                        curr = curr.next
                        idx += 1
                    if tail and cycle_node:
                        tail.next = cycle_node
                result = func(head)
            elif QUESTION_NUMBER == 9:
                listA = args[0]
                listB = args[1]
                skipA = args[2]
                skipB = args[3]
                headA = to_linked_list(listA[:skipA])
                headB = to_linked_list(listB[:skipB])
                intersect = to_linked_list(listA[skipA:])
                if headA:
                    curr = headA
                    while curr.next:
                        curr = curr.next
                    curr.next = intersect
                else:
                    headA = intersect
                if headB:
                    curr = headB
                    while curr.next:
                        curr = curr.next
                    curr.next = intersect
                else:
                    headB = intersect
                res_node = func(headA, headB)
                result = to_list(res_node)
            elif QUESTION_NUMBER == 23:
                list_nodes = [to_linked_list(arr) for arr in args[0]]
                res_node = func(list_nodes)
                result = to_list(res_node)
            elif QUESTION_NUMBER == 25:
                list_vals = args[0]
                cycle_pos = args[1]
                head = to_linked_list(list_vals)
                if cycle_pos != -1:
                    curr = head
                    cycle_node = None
                    tail = None
                    idx = 0
                    while curr:
                        if idx == cycle_pos:
                            cycle_node = curr
                        tail = curr
                        curr = curr.next
                        idx += 1
                    if tail and cycle_node:
                        tail.next = cycle_node
                res_node = func(head)
                if not res_node:
                    result = -1
                else:
                    curr = head
                    idx = 0
                    result = -1
                    for _ in range(100):
                        if curr == res_node:
                            result = idx
                            break
                        curr = curr.next
                        idx += 1
            else:
                for arg in args:
                    if isinstance(arg, list):
                        processed_args.append(to_linked_list(arg))
                    else:
                        processed_args.append(arg)
                res_node = func(*processed_args) if len(processed_args) > 1 else func(processed_args[0])
                result = to_list(res_node) if isinstance(res_node, ListNode) else res_node
                
        elif filename == "trees_and_bst.py" and QUESTION_NUMBER <= 25:
            processed_args = []
            for arg in args:
                if isinstance(arg, list):
                    processed_args.append(to_tree(arg))
                else:
                    processed_args.append(arg)
            res_val = func(*processed_args) if len(processed_args) > 1 else func(processed_args[0])
            if isinstance(res_val, TreeNode):
                result = to_list(res_val)
            else:
                result = res_val
                
        elif filename == "tries.py":
            # Tries test runner class-based instantiation and method calling
            commands = args[0] if isinstance(args[0], (list, tuple)) else []
            arguments = args[1] if isinstance(args[1], (list, tuple)) else []
            obj = func() # Instantiate the class (Trie or MapSum)
            result = [None]
            for i in range(1, len(commands)):
                cmd = commands[i]
                arg = arguments[i]
                method = getattr(obj, cmd)
                res = method(*arg) if arg else method()
                result.append(res)
                
        else:
            # Standard input/output check
            result = func(*args) if isinstance(args, list) else func(args)
            
        # Custom result sorting for combinations/subsets/permutations
        if filename == "backtracking.py" and QUESTION_NUMBER in [1, 2, 4, 13, 20]:
            if result and isinstance(result, list):
                result = sorted([sorted(x) if isinstance(x, list) else x for x in result])
                expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected])
        elif filename == "bit_manipulation.py" and QUESTION_NUMBER in [9, 11]:
            if result and isinstance(result, list):
                result = sorted([sorted(x) if isinstance(x, list) else x for x in result])
                expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected])
        elif filename == "loop_basics.py" and QUESTION_NUMBER in [41]:
            if result and isinstance(result, list):
                result = sorted([sorted(x) if isinstance(x, list) else x for x in result])
                expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                
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
    import sys
    # Check CLI arguments first
    if len(sys.argv) > 1:
        try:
            QUESTION_NUMBER = int(sys.argv[1])
        except ValueError:
            pass

    # If QUESTION_NUMBER is None or 0, auto-detect the highest-numbered non-empty question
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
                
                # Check if there are non-docstring, non-pass statements
                non_empty = False
                for stmt in body:
                    # Ignore docstrings
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, (ast.Constant, ast.Str)):
                        continue
                    # Ignore pass
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

    # Run the selected question in verbose mode
    run_test(QUESTION_NUMBER, silent=False)
