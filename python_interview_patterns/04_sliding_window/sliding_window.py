import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
Sliding Window Technique - Practice One Question at a Time
==========================================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 100)
2. Write your logic in the corresponding function (q1 to q100)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 100 QUESTIONS ====================

# --- EASY LEVEL (Q1 - Q25) ---

def q1(arr, k):
    """Q1: Maximum Sum Subarray of Size K.
    Input: arr = [2, 1, 5, 1, 3, 2], k = 3
    Expected Output: 9 (subarray [5, 1, 3])
    """
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    return max_sum

def q2(arr, k):
    """Q2: Minimum Sum Subarray of Size K.
    Input: arr = [2, 1, 5, 1, 3, 2], k = 3
    Expected Output: 6 (subarray [2, 1, 3] is not contiguous, contiguous is [2, 1, 5]=8, [1, 5, 1]=7, [5, 1, 3]=9, [1, 3, 2]=6)
    """
    if len(arr) < k:
        return 0
    window_sum = sum(arr[:k])
    min_sum = window_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        min_sum = min(min_sum, window_sum)
    return min_sum

def q3(arr, k):
    """Q3: Maximum Average Subarray I. Find a contiguous subarray of size k that has the maximum average value.
    Input: arr = [1, 12, -5, -6, 50, 3], k = 4
    Expected: 12.75 (subarray [12, -5, -6, 50] has sum 51)
    """
    # Write your logic here
    pass

def q4(nums, k):
    """Q4: Check if Array Contains Duplicates Within Distance K (Contains Duplicate II).
    Input: nums = [1, 2, 3, 1], k = 3
    Expected: True
    """
    # Write your logic here
    pass

def q5(s, k):
    """Q5: K-Beauty of a Number. Count substrings of length k that division of num by that substring is 0.
    Input: s = ("240", 2) where num is 240, substrings are "24" and "40". Both divide 240.
    Expected: 2
    """
    # Write your logic here
    pass

def q6(s):
    """Q6: Substrings of Size Three with Distinct Characters. Count how many substrings of length 3 have all unique characters.
    Input: s = "xyzzaz"
    Expected: 1 ("xyz")
    """
    # Write your logic here
    pass

def q7(code, k):
    """Q7: Defuse the Bomb (easy sliding window circular array).
    Input: code = [5, 7, 1, 4], k = 3
    Expected: [12, 10, 16, 13]
    """
    # Write your logic here
    pass

def q8(calories, k, lower, upper):
    """Q8: Diet Plan Performance.
    Input: calories = [1, 2, 3, 4, 5], k = 1, lower = 3, upper = 3
    Expected: 0
    """
    # Write your logic here
    pass

def q9(nums, k):
    """Q9: Minimum Difference Between Highest and Lowest of K Scores.
    Input: nums = [90], k = 1
    Expected: 0
    """
    # Write your logic here
    pass

def q10(s):
    """Q10: Longest Substring Without Repeating Characters.
    Input: s = "abcabcbb"
    Expected: 3
    """
    # Write your logic here
    pass

def q11(target, nums):
    """Q11: Minimum Size Subarray Sum (sum >= target).
    Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    Expected: 2
    """
    # Write your logic here
    pass

def q12(nums, k):
    """Q12: Max Consecutive Ones III. Max consecutive 1's if you can flip at most k 0's.
    Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
    Expected: 6
    """
    # Write your logic here
    pass

def q13(nums, k):
    """Q13: Subarray Product Less Than K.
    Input: nums = [10, 5, 2, 6], k = 100
    Expected: 8
    """
    # Write your logic here
    pass

def q14(fruits):
    """Q14: Fruit Into Baskets. Max elements in 2 baskets (2 unique numbers).
    Input: fruits = [1, 2, 1, 2, 3]
    Expected: 4 ([1, 2, 1, 2])
    """
    # Write your logic here
    pass

def q15(s, k):
    """Q15: Longest Substring with At Most K Distinct Characters.
    Input: s = "eceba", k = 2
    Expected: 3
    """
    # Write your logic here
    pass

def q16(s, t, maxCost):
    """Q16: Get Equal Substrings Within Budget.
    Input: s = "abcd", t = "bcdf", maxCost = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q17(nums):
    """Q17: Longest Subarray of 1's After Deleting One Element.
    Input: nums = [1, 1, 0, 1]
    Expected: 3
    """
    # Write your logic here
    pass

def q18(s, k):
    """Q18: Longest Repeating Character Replacement.
    Input: s = "AABABBA", k = 1
    Expected: 4
    """
    # Write your logic here
    pass

def q19(arr, k, threshold):
    """Q19: Number of Subarrays of Size K and Average >= Threshold.
    Input: arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
    Expected: 3
    """
    # Write your logic here
    pass

def q20(s, k):
    """Q20: Substring of Size K with Maximum Vowels.
    Input: s = "abciiidef", k = 3
    Expected: 3 ("iii")
    """
    # Write your logic here
    pass

def q21(s):
    """Q21: Number of Substrings Containing All Three Characters ('a', 'b', 'c').
    Input: s = "abcabc"
    Expected: 10
    """
    # Write your logic here
    pass

def q22(nums, target):
    """Q22: Binary Subarrays With Sum (count subarrays with sum equal to target).
    Input: nums = [1, 0, 1, 0, 1], target = 2
    Expected: 4
    """
    # Write your logic here
    pass

def q23(nums, k):
    """Q23: Count Number of Nice Subarrays (exactly k odd numbers).
    Input: nums = [1, 1, 2, 1, 1], k = 3
    Expected: 2
    """
    # Write your logic here
    pass

def q24(nums):
    """Q24: Maximum Erasure Value (max sum of subarray with unique elements).
    Input: nums = [4, 2, 4, 5, 6]
    Expected: 17
    """
    # Write your logic here
    pass

def q25(cardPoints, k):
    """Q25: Maximum Points You Can Obtain from Cards (take k cards from beginning or end).
    Input: cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3
    Expected: 12 (take 1, 6, 5 from ends)
    """
    # Write your logic here
    pass


# --- INTERMEDIATE LEVEL (Q26 - Q60) ---

def q26(nums, limit):
    """Q26: Longest Continuous Subarray With Absolute Diff <= Limit.
    Input: nums = [8, 2, 4, 7], limit = 4
    Expected: 2
    """
    # Write your logic here
    pass

def q27(s, t):
    """Q27: Minimum Window Substring.
    Input: s = "ADOBECODEBANC", t = "ABC"
    Expected: "BANC"
    """
    # Write your logic here
    pass

def q28(nums, k):
    """Q28: Subarrays with K Different Integers.
    Input: nums = [1, 2, 1, 2, 3], k = 2
    Expected: 7
    """
    # Write your logic here
    pass

def q29(nums, k):
    """Q29: Sliding Window Maximum.
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Expected: [3, 3, 5, 5, 6, 7]
    """
    # Write your logic here
    pass

def q30(nums, x):
    """Q30: Minimum Operations to Reduce X to Zero.
    Input: nums = [1, 1, 4, 2, 3], x = 5
    Expected: 2
    """
    # Write your logic here
    pass

def q31(s):
    """Q31: Replace the Substring for Balanced String.
    Input: s = "QWER"
    Expected: 0
    """
    # Write your logic here
    pass

def q32(nums, k):
    """Q32: Frequency of the Most Frequent Element.
    Input: nums = [1, 2, 4], k = 5
    Expected: 3
    """
    # Write your logic here
    pass

def q33(s, k):
    """Q33: Maximize the Confusion of an Exam.
    Input: s = "TTFF", k = 2
    Expected: 4
    """
    # Write your logic here
    pass

def q34(nums, k):
    """Q34: Maximum Beauty of an Array After Applying Operation.
    Input: nums = [4, 6, 1, 2], k = 2
    Expected: 3
    """
    # Write your logic here
    pass

def q35(nums):
    """Q35: Count Complete Subarrays in an Array.
    Input: nums = [1, 3, 1, 2, 2]
    Expected: 4
    """
    # Write your logic here
    pass

def q36(nums, k):
    """Q36: Number of Substrings With At Least K Occurrences of Max Element.
    Input: nums = ([1, 3, 2, 3, 3], 2)
    Expected: 6
    """
    # Write your logic here
    pass

def q37(s):
    """Q37: Longest Substring of One Repeating Character.
    Input: s = "bababbb"
    Expected: 3
    """
    # Write your logic here
    pass

def q38(nums):
    """Q38: Minimum Swaps to Group All 1's Together II.
    Input: nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    Expected: 2
    """
    # Write your logic here
    pass

def q39(s, k):
    """Q39: Find K-Length Substrings With No Repeated Characters.
    Input: s = ("havefunonleetcode", 5)
    Expected: 6
    """
    # Write your logic here
    pass

def q40(s, k):
    """Q40: Maximum Number of Vowels in a Substring of Given Length.
    Input: s = ("abciiidef", 3)
    Expected: 3
    ```
    """
    # Write your logic here
    pass

def q41(s, p):
    """Q41: Find All Anagrams in a String.
    Input: s = "cbaebabacd", p = "abc"
    Expected: [0, 6]
    """
    # Write your logic here
    pass

def q42(s1, s2):
    """Q42: Permutation in String.
    Input: s1 = "ab", s2 = "eidbaooo"
    Expected: True
    """
    # Write your logic here
    pass

def q43(s, t):
    """Q43: Minimum Window Subsequence.
    Input: s = "abcdebdde", t = "bde"
    Expected: "bcde"
    """
    # Write your logic here
    pass

def q44(nums, k):
    """Q44: Count Subarrays Where Max Element Appears at Least K Times.
    Input: nums = ([1, 3, 2, 3, 3], 2)
    Expected: 6
    """
    # Write your logic here
    pass

def q45(s):
    """Q45: Find Longest Awesome Substring (contains at most one odd-frequency character).
    Input: s = "3242415"
    Expected: 5 ("24241" or "24245" etc. -> "24242" can be made palindrome, wait "2424" has len 4)
    """
    # Write your logic here
    pass

def q46(s):
    """Q46: Longest Substring with At Least K Repeating Characters.
    Input: s = ("aaabb", 3)
    Expected: 3 ("aaa")
    """
    # Write your logic here
    pass

def q47(s, k):
    """Q47: Maximize the Top K Elements.
    Input: s = ([5, 2, 2, 4, 0, 6], 4)
    Expected: 5
    """
    # Write your logic here
    pass

def q48(nums):
    """Q48: Shortest Subarray to be Removed to Make Array Sorted.
    Input: nums = [1, 2, 3, 10, 4, 2, 3, 5]
    Expected: 3
    """
    # Write your logic here
    pass

def q49(s):
    """Q49: Partition Labels.
    Input: s = "ababcbacadefegdehijhklij"
    Expected: [9, 7, 8]
    """
    # Write your logic here
    pass

def q50(nums, k):
    """Q50: Number of Subarrays with Bounded Maximum.
    Input: nums = ([2, 1, 4, 3], 2, 3)
    Expected: 3
    """
    # Write your logic here
    pass

def q51(nums, k):
    """Q51: Subarray Sums Divisible by K.
    Input: nums = [4, 5, 0, -2, -3, 1], k = 5
    Expected: 7
    """
    # Write your logic here
    pass

def q52(arr):
    """Q52: Longest Mountain in Array.
    Input: arr = [2, 1, 4, 7, 3, 2, 5]
    Expected: 5
    """
    # Write your logic here
    pass

def q53(heights):
    """Q53: Trapping Rain Water (sliding window / two pointer).
    Input: heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Expected: 6
    """
    # Write your logic here
    pass

def q54(nums, k):
    """Q54: Count Subarrays with Median K.
    Input: nums = ([3, 2, 1, 4, 5], 4)
    Expected: 3
    """
    # Write your logic here
    pass

def q55(nums):
    """Q55: Maximum Product Subarray (can be done with prefix product/sliding window).
    Input: nums = [2, 3, -2, 4]
    Expected: 6
    """
    # Write your logic here
    pass

def q56(nums, k):
    """Q56: Maximum Subarray Sum with One Deletion (DP/sliding window).
    Input: nums = [1, -2, 0, 3]
    Expected: 4
    """
    # Write your logic here
    pass

def q57(nums):
    """Q57: Maximum Absolute Sum of Any Subarray.
    Input: nums = [1, -3, 2, 3, -4]
    Expected: 5
    """
    # Write your logic here
    pass

def q58(arr):
    """Q58: Subarray Product Less than K with Negatives.
    Input: arr = ([10, 5, 2, 6], 100)
    Expected: 8
    """
    # Write your logic here
    pass

def q59(s):
    """Q59: Longest Substring of All Vowels in Order.
    Input: s = "aeiaaioooaaeiouuu"
    Expected: 7 ("aaeiouuu")
    """
    # Write your logic here
    pass

def q60(nums, k):
    """Q60: Number of Nice Subarrays with At Most K Odds.
    Input: nums = ([1, 1, 2, 1, 1], 3)
    Expected: 15
    """
    # Write your logic here
    pass


# --- ADVANCED LEVEL (Q61 - Q100) ---

def q61(nums, k):
    """Q61: Minimum Swaps to Group All 1's Together.
    Input: nums = [1, 0, 1, 0, 1]
    Expected: 1
    """
    # Write your logic here
    pass

def q62(s):
    """Q62: Longest Substring with At Least K Unique Vowels.
    Input: s = ("leetcode", 2)
    Expected: 8
    """
    # Write your logic here
    pass

def q63(nums, k):
    """Q63: Find All Unique Subarrays of Size K.
    Input: nums = ([1, 2, 1, 2, 1, 3], 3)
    Expected: 3
    """
    # Write your logic here
    pass

def q64(n, edges):
    """Q64: Sliding Window on Graph (Not standard sliding window, placeholder: Maximum sum of path of length K).
    Input: n = (5, [[1, 2, 10], [2, 3, 20], [3, 4, 30]])
    Expected: 60
    """
    # Write your logic here
    pass

def q65(nums, target):
    """Q65: Longest Subarray with Sum Equal to Target.
    Input: nums = ([1, -1, 5, -2, 3], 3)
    Expected: 4
    """
    # Write your logic here
    pass

def q66(nums, k):
    """Q66: Max Sum of Subarray of Size K with No Duplicates.
    Input: nums = ([1, 5, 4, 2, 9, 9, 9], 3)
    Expected: 15
    """
    # Write your logic here
    pass

def q67(nums):
    """Q67: Find Minimum of All Subarrays of Size K.
    Input: nums = ([2, 1, 3, 4, 6, 3, 8], 3)
    Expected: [1, 1, 3, 3, 3]
    """
    # Write your logic here
    pass

def q68(nums, target):
    """Q68: Count Subarrays with Sum Less Than Target.
    Input: nums = ([2, 1, 4, 3], 5)
    Expected: 4
    """
    # Write your logic here
    pass

def q69(nums):
    """Q69: Maximum Difference in a Subarray of Size K.
    Input: nums = ([1, 3, 6, 1, 9, 2], 3)
    Expected: 8
    """
    # Write your logic here
    pass

def q70(nums, k):
    """Q70: Number of Subarrays with Product Less than K.
    Input: nums = ([10, 5, 2, 6], 100)
    Expected: 8
    """
    # Write your logic here
    pass

def q71(nums):
    """Q71: Find Longest Alternating Subarray.
    Input: nums = [1, 0, 1, 0, 1, 1, 0]
    Expected: 5
    """
    # Write your logic here
    pass

def q72(s):
    """Q72: Find Longest Substring containing even counts of vowels.
    Input: s = "eleetminicoworoep"
    Expected: 13
    """
    # Write your logic here
    pass

def q73(nums, k):
    """Q73: K-Sum Subarrays.
    Input: nums = ([1, 2, 3], 3)
    Expected: 2
    """
    # Write your logic here
    pass

def q74(s):
    """Q74: Longest Chunked Palindrome Decomposition.
    Input: s = "ghiabcdefhelloadamhelloabcdefghi"
    Expected: 7
    """
    # Write your logic here
    pass

def q75(s, t):
    """Q75: Distinct Subsequences (dynamic window).
    Input: s = "rabbbit", t = "rabbit"
    Expected: 3
    """
    # Write your logic here
    pass

def q76(lists):
    """Q76: Merge K Sorted Lists (represented as list of lists).
    Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    """
    # Write your logic here
    pass

def q77(arr):
    """Q77: Shortest Subarray to be Removed to Make Array Sorted.
    Input: arr = [1, 2, 3, 10, 4, 2, 3, 5]
    Expected: 3
    """
    # Write your logic here
    pass

def q78(start, end):
    """Q78: Swap Adjacent in LR String.
    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Expected: True
    """
    # Write your logic here
    pass

def q79(s):
    """Q79: Remove Duplicate Letters.
    Input: s = "bcabc"
    Expected: "abc"
    """
    # Write your logic here
    pass

def q80(nums, k):
    """Q80: Maximum Score of a Good Subarray.
    Input: nums = ([1, 4, 3, 7, 4, 5], 3)
    Expected: 15
    """
    # Write your logic here
    pass

def q81(nums, k):
    """Q81: Subarray Sums Divisible by K.
    Input: nums = [4, 5, 0, -2, -3, 1], k = 5
    Expected: 7
    """
    # Write your logic here
    pass

def q82(s):
    """Q82: Optimal Partition of String.
    Input: s = "abacaba"
    Expected: 4
    """
    # Write your logic here
    pass

def q83(nums, k):
    """Q83: Count Subarrays With Median K.
    Input: nums = ([3, 2, 1, 4, 5], 4)
    Expected: 3
    """
    # Write your logic here
    pass

def q84(fruits):
    """Q84: Fruit Into Baskets.
    Input: fruits = [1, 2, 3, 2, 2]
    Expected: 4
    """
    # Write your logic here
    pass

def q85(nums):
    """Q85: Minimum Operations to Make Array Continuous.
    Input: nums = [4, 2, 5, 3]
    Expected: 0
    """
    # Write your logic here
    pass

def q86(s):
    """Q86: Replace the Substring for Balanced String.
    Input: s = "QWER"
    Expected: 0
    """
    # Write your logic here
    pass

def q87(nums, k):
    """Q87: Constrained Subsequence Sum.
    Input: nums = [10, 2, -10, 5, 20], k = 2
    Expected: 37
    """
    # Write your logic here
    pass

def q88(nums, limit):
    """Q88: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Input: nums = [8, 2, 4, 7], limit = 4
    Expected: 2
    """
    # Write your logic here
    pass

def q89(nums, k):
    """Q89: Count Subarrays Where Max Element Appears at Least K Times.
    Input: nums = ([1, 3, 2, 3, 3], 2)
    Expected: 6
    """
    # Write your logic here
    pass

def q90(s):
    """Q90: Minimum Number of Flips to Make the Binary String Alternating.
    Input: s = "111000"
    Expected: 2
    """
    # Write your logic here
    pass

def q91(nums, k):
    """Q91: Split Array Largest Sum.
    Input: nums = [7, 2, 5, 10, 8], k = 2
    Expected: 18
    """
    # Write your logic here
    pass

def q92(weights, days):
    """Q92: Capacity To Ship Packages Within D Days.
    Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
    Expected: 15
    """
    # Write your logic here
    pass

def q93(piles, h):
    """Q93: Koko Eating Bananas.
    Input: piles = [3, 6, 7, 11], h = 8
    Expected: 4
    """
    # Write your logic here
    pass

def q94(nums, queries):
    """Q94: Minimum Absolute Difference Query.
    Input: nums = ([1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]])
    Expected: [2, 1, 4, 1]
    """
    # Write your logic here
    pass

def q95(head, k):
    """Q95: Reverse Nodes in k-Group.
    Input: head = [1, 2, 3, 4, 5], k = 2
    Expected: [2, 1, 4, 3, 5]
    """
    # Write your logic here
    pass

def q96(head):
    """Q96: Sort List.
    Input: head = [4, 2, 1, 3]
    Expected: [1, 2, 3, 4]
    """
    # Write your logic here
    pass

def q97(head, x):
    """Q97: Partition List.
    Input: head = ([1, 4, 3, 2, 5, 2], 3)
    Expected: [1, 2, 2, 4, 3, 5]
    """
    # Write your logic here
    pass

def q98(head):
    """Q98: Palindrome Linked List.
    Input: head = [1, 2, 2, 1]
    Expected: True
    """
    # Write your logic here
    pass

def q99(head):
    """Q99: Linked List Cycle II.
    Input: head = ([3, 2, 0, -4], 1)
    Expected: 1
    """
    # Write your logic here
    pass

def q100(nums):
    """Q100: Find the Duplicate Number.
    Input: nums = [1, 3, 4, 2, 2]
    Expected: 2
    """
    # Write your logic here
    pass


# ==================== TEST SUITE DICTIONARY ====================

TESTS = {
    1: {'func': q1, 'args': [[2, 1, 5, 1, 3, 2], 3], 'expected': 9},
    2: {'func': q2, 'args': [[2, 1, 5, 1, 3, 2], 3], 'expected': 6},
    3: {'func': q3, 'args': [[1, 12, -5, -6, 50, 3], 4], 'expected': 12.75},
    4: {'func': q4, 'args': [[1, 2, 3, 1], 3], 'expected': True},
    5: {'func': q5, 'args': ["240", 2], 'expected': 2},
    6: {'func': q6, 'args': ["xyzzaz"], 'expected': 1},
    7: {'func': q7, 'args': [[5, 7, 1, 4], 3], 'expected': [12, 10, 16, 13]},
    8: {'func': q8, 'args': [[1, 2, 3, 4, 5], 1, 3, 3], 'expected': 0},
    9: {'func': q9, 'args': [[90], 1], 'expected': 0},
    10: {'func': q10, 'args': ["abcabcbb"], 'expected': 3},
    11: {'func': q11, 'args': [7, [2, 3, 1, 2, 4, 3]], 'expected': 2},
    12: {'func': q12, 'args': [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2], 'expected': 6},
    13: {'func': q13, 'args': [[10, 5, 2, 6], 100], 'expected': 8},
    14: {'func': q14, 'args': [[1, 2, 1, 2, 3]], 'expected': 4},
    15: {'func': q15, 'args': ["eceba", 2], 'expected': 3},
    16: {'func': q16, 'args': ["abcd", "bcdf", 3], 'expected': 3},
    17: {'func': q17, 'args': [[1, 1, 0, 1]], 'expected': 3},
    18: {'func': q18, 'args': ["AABABBA", 1], 'expected': 4},
    19: {'func': q19, 'args': [[2, 2, 2, 2, 5, 5, 5, 8], 3, 4], 'expected': 3},
    20: {'func': q20, 'args': ["abciiidef", 3], 'expected': 3},
    21: {'func': q21, 'args': ["abcabc"], 'expected': 10},
    22: {'func': q22, 'args': [[1, 0, 1, 0, 1], 2], 'expected': 4},
    23: {'func': q23, 'args': [[1, 1, 2, 1, 1], 3], 'expected': 2},
    24: {'func': q24, 'args': [[4, 2, 4, 5, 6]], 'expected': 17},
    25: {'func': q25, 'args': [[1, 2, 3, 4, 5, 6, 1], 3], 'expected': 12},
    
    26: {'func': q26, 'args': [[8, 2, 4, 7], 4], 'expected': 2},
    27: {'func': q27, 'args': ["ADOBECODEBANC", "ABC"], 'expected': "BANC"},
    28: {'func': q28, 'args': [[1, 2, 1, 2, 3], 2], 'expected': 7},
    29: {'func': q29, 'args': [[1, 3, -1, -3, 5, 3, 6, 7], 3], 'expected': [3, 3, 5, 5, 6, 7]},
    30: {'func': q30, 'args': [[1, 1, 4, 2, 3], 5], 'expected': 2},
    31: {'func': q31, 'args': ["QWER"], 'expected': 0},
    32: {'func': q32, 'args': [[1, 2, 4], 5], 'expected': 3},
    33: {'func': q33, 'args': ["TTFF", 2], 'expected': 4},
    34: {'func': q34, 'args': [[4, 6, 1, 2], 2], 'expected': 3},
    35: {'func': q35, 'args': [[1, 3, 1, 2, 2]], 'expected': 4},
    36: {'func': q36, 'args': [[1, 3, 2, 3, 3], 2], 'expected': 6},
    37: {'func': q37, 'args': ["bababbb"], 'expected': 3},
    38: {'func': q38, 'args': [[0, 1, 1, 1, 0, 0, 1, 1, 0]], 'expected': 2},
    39: {'func': q39, 'args': ["havefunonleetcode", 5], 'expected': 6},
    40: {'func': q40, 'args': ["abciiidef", 3], 'expected': 3},
    41: {'func': q41, 'args': ["cbaebabacd", "abc"], 'expected': [0, 6]},
    42: {'func': q42, 'args': ["ab", "eidbaooo"], 'expected': True},
    43: {'func': q43, 'args': ["abcdebdde", "bde"], 'expected': "bcde"},
    44: {'func': q44, 'args': [[1, 3, 2, 3, 3], 2], 'expected': 6},
    45: {'func': q45, 'args': ["3242415"], 'expected': 5},
    46: {'func': q46, 'args': ["aaabb", 3], 'expected': 3},
    47: {'func': q47, 'args': [[5, 2, 2, 4, 0, 6], 4], 'expected': 5},
    48: {'func': q48, 'args': [[1, 2, 3, 10, 4, 2, 3, 5]], 'expected': 3},
    49: {'func': q49, 'args': ["ababcbacadefegdehijhklij"], 'expected': [9, 7, 8]},
    50: {'func': q50, 'args': [[2, 1, 4, 3], 2, 3], 'expected': 3},
    51: {'func': q51, 'args': [[4, 5, 0, -2, -3, 1], 5], 'expected': 7},
    52: {'func': q52, 'args': [[2, 1, 4, 7, 3, 2, 5]], 'expected': 5},
    53: {'func': q53, 'args': [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 'expected': 6},
    54: {'func': q54, 'args': [[3, 2, 1, 4, 5], 4], 'expected': 3},
    55: {'func': q55, 'args': [[2, 3, -2, 4]], 'expected': 6},
    56: {'func': q56, 'args': [[1, -2, 0, 3]], 'expected': 4},
    57: {'func': q57, 'args': [[1, -3, 2, 3, -4]], 'expected': 5},
    58: {'func': q58, 'args': [[10, 5, 2, 6], 100], 'expected': 8},
    59: {'func': q59, 'args': ["aeiaaioooaaeiouuu"], 'expected': 7},
    60: {'func': q60, 'args': [[1, 1, 2, 1, 1], 3], 'expected': 15},
    
    61: {'func': q61, 'args': [[1, 0, 1, 0, 1], 2], 'expected': 1},
    62: {'func': q62, 'args': ["leetcode", 2], 'expected': 8},
    63: {'func': q63, 'args': [[1, 2, 1, 2, 1, 3], 3], 'expected': 3},
    64: {'func': q64, 'args': [5, [[1, 2, 10], [2, 3, 20], [3, 4, 30]]], 'expected': 60},
    65: {'func': q65, 'args': [[1, -1, 5, -2, 3], 3], 'expected': 4},
    66: {'func': q66, 'args': [[1, 5, 4, 2, 9, 9, 9], 3], 'expected': 15},
    67: {'func': q67, 'args': [[2, 1, 3, 4, 6, 3, 8]], 'expected': [1, 1, 3, 3, 3]},
    68: {'func': q68, 'args': [[2, 1, 4, 3], 5], 'expected': 4},
    69: {'func': q69, 'args': [[1, 3, 6, 1, 9, 2]], 'expected': 8},
    70: {'func': q70, 'args': [[10, 5, 2, 6], 100], 'expected': 8},
    71: {'func': q71, 'args': [[1, 0, 1, 0, 1, 1, 0]], 'expected': 5},
    72: {'func': q72, 'args': ["eleetminicoworoep"], 'expected': 13},
    73: {'func': q73, 'args': [[1, 2, 3], 3], 'expected': 2},
    74: {'func': q74, 'args': ["ghiabcdefhelloadamhelloabcdefghi"], 'expected': 7},
    75: {'func': q75, 'args': ["rabbbit", "rabbit"], 'expected': 3},
    76: {'func': q76, 'args': [[[1, 4, 5], [1, 3, 4], [2, 6]]], 'expected': [1, 1, 2, 3, 4, 4, 5, 6]},
    77: {'func': q77, 'args': [[1, 2, 3, 10, 4, 2, 3, 5]], 'expected': 3},
    78: {'func': q78, 'args': ["RXXLRXRXL", "XRLXXRRLX"], 'expected': True},
    79: {'func': q79, 'args': ["bcabc"], 'expected': "abc"},
    80: {'func': q80, 'args': [[1, 4, 3, 7, 4, 5], 3], 'expected': 15},
    81: {'func': q81, 'args': [[4, 5, 0, -2, -3, 1], 5], 'expected': 7},
    82: {'func': q82, 'args': ["abacaba"], 'expected': 4},
    83: {'func': q83, 'args': [[3, 2, 1, 4, 5], 4], 'expected': 3},
    84: {'func': q84, 'args': [[1, 2, 3, 2, 2]], 'expected': 4},
    85: {'func': q85, 'args': [[4, 2, 5, 3]], 'expected': 0},
    86: {'func': q86, 'args': ["QWER"], 'expected': 0},
    87: {'func': q87, 'args': [[10, 2, -10, 5, 20], 2], 'expected': 37},
    88: {'func': q88, 'args': [[8, 2, 4, 7], 4], 'expected': 2},
    89: {'func': q89, 'args': [[1, 3, 2, 3, 3], 2], 'expected': 6},
    90: {'func': q90, 'args': ["111000"], 'expected': 2},
    91: {'func': q91, 'args': [[7, 2, 5, 10, 8], 2], 'expected': 18},
    92: {'func': q92, 'args': [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], 'expected': 15},
    93: {'func': q93, 'args': [[3, 6, 7, 11], 8], 'expected': 4},
    94: {'func': q94, 'args': [[1, 3, 4, 8], [[0, 1], [1, 2], [2, 3], [0, 3]]], 'expected': [2, 1, 4, 1]},
    95: {'func': q95, 'args': [[1, 2, 3, 4, 5], 2], 'expected': [2, 1, 4, 3, 5]},
    96: {'func': q96, 'args': [[4, 2, 1, 3]], 'expected': [1, 2, 3, 4]},
    97: {'func': q97, 'args': [[1, 4, 3, 2, 5, 2], 3], 'expected': [1, 2, 2, 4, 3, 5]},
    98: {'func': q98, 'args': [[1, 2, 2, 1]], 'expected': True},
    99: {'func': q99, 'args': [[3, 2, 0, -4], 1], 'expected': 1},
    100: {'func': q100, 'args': [[1, 3, 4, 2, 2]], 'expected': 2},
}


# ==================== RUN TEST ====================

def run_test(QUESTION_NUMBER, silent=False):
    import io
    import sys
    
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
        # We check filename to apply custom converters if they are defined
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
            commands = args[0]
            arguments = args[1]
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
                body = func_def.body
                
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
