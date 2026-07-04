import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
Heaps & Priority Queues - Practice One Question at a Time
=========================================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 100)
2. Write your logic in the corresponding function (q1 to q100)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 100 QUESTIONS ====================

import heapq

# --- EASY LEVEL (Q1 - Q25) ---

def q1(nums, k):
    """Q1: Kth Largest Element in an Array. Return the kth largest element in sorted order.
    Input: nums = [3, 2, 1, 5, 6, 4], k = 2
    Expected Output: 5
    """
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

def q2(stones):
    """Q2: Last Stone Weight. Smash heaviest two stones. Return weight of last stone or 0.
    Input: stones = [2, 7, 4, 1, 8, 1]
    Expected Output: 1
    """
    max_heap = [-s for s in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        s1 = -heapq.heappop(max_heap)
        s2 = -heapq.heappop(max_heap)
        if s1 != s2:
            heapq.heappush(max_heap, -(s1 - s2))
    return -max_heap[0] if max_heap else 0

def q3(score):
    """Q3: Relative Ranks. Assign placement ranks: Gold, Silver, Bronze, or numerical ranks.
    Input: score = [5, 4, 3, 2, 1]
    Expected: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    """
    # Write your logic here
    pass

def q4(matrix, k):
    """Q4: Kth Smallest Element in a Sorted Matrix (rows and cols sorted ascending).
    Input: matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
    Expected: 13
    """
    # Write your logic here
    pass

def q5(points, k):
    """Q5: K Closest Points to Origin on X-Y plane.
    Input: points = [[1,3],[-2,2]], k = 1
    Expected: [[-2,2]]
    """
    # Write your logic here
    pass

def q6(nums, k):
    """Q6: Top K Frequent Elements. Return elements in any order.
    Input: nums = [1,1,1,2,2,3], k = 2
    Expected: [1, 2]
    """
    # Write your logic here
    pass

def q7(words, k):
    """Q7: Top K Frequent Words. Sort alphabetically if frequencies match.
    Input: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Expected: ["i", "love"]
    """
    # Write your logic here
    pass

def q8(lists):
    """Q8: Merge K Sorted Lists (lists contains sorted arrays). Return single sorted array.
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    """
    # Write your logic here
    pass

def q9(s):
    """Q9: Reorganize String. Rearrange chars so no two adjacent are same. Return "" if impossible.
    Input: s = "aab"
    Expected: "aba" (or "aba" etc.)
    """
    # Write your logic here
    pass

def q10(nums1, nums2, k):
    """Q10: Find K Pairs with Smallest Sums. (u, v) pairs where u from nums1, v from nums2.
    Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Expected: [[1,2],[1,4],[1,6]]
    """
    # Write your logic here
    pass

def q11(heights, bricks, ladders):
    """Q11: Furthest Building You Can Reach. Use bricks or ladders to jump to next building if height increases.
    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Expected: 4
    """
    # Write your logic here
    pass

def q12(tasks):
    """Q12: Single-Threaded CPU. tasks = [[enqueueTime, processingTime]]. Return order of index executed.
    Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
    Expected: [0, 2, 3, 1]
    """
    # Write your logic here
    pass

def q13(trips, capacity):
    """Q13: Car Pooling. trips = [[numPassengers, from, to]]. Return True if possible within capacity.
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Expected: False
    """
    # Write your logic here
    pass

def q14(sticks):
    """Q14: Minimum Cost to Connect Sticks. Cost is sum of two stick lengths connected.
    Input: sticks = [2, 4, 3]
    Expected: 14 (connect 2, 3 cost 5, stick list becomes [5, 4]. connect 5, 4 cost 9. total 5+9=14)
    """
    # Write your logic here
    pass

def q15(n, primes):
    """Q15: Super Ugly Number. Ugly number whose prime factors are in primes list. Find nth.
    Input: n = 12, primes = [2, 7, 13, 19]
    Expected: 32
    """
    # Write your logic here
    pass

def q16(nums):
    """Q16: Find Median from Data Stream (represented as passing array for continuous insertion and median calculation).
    Returns list of median values after each insertion.
    Input: nums = [1, 2, 3]
    Expected: [1.0, 1.5, 2.0]
    """
    # Write your logic here
    pass

def q17(nums, k):
    """Q17: Sliding Window Median. Return list of medians for each window of size k.
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Expected: [1.0,-1.0,-1.0,3.0,5.0,6.0]
    """
    # Write your logic here
    pass

def q18(k, w, profits, capital):
    """Q18: IPO (Maximize capital: select at most k projects under capital w).
    Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
    Expected: 4 (start w=0, take project 0 profit 1 -> w=1. take project 2 profit 3 -> w=4)
    """
    # Write your logic here
    pass

def q19(nums):
    """Q19: Smallest Range Covering Elements from K Lists. Find range that contains at least one number from each list.
    Input: nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
    Expected: [20, 24]
    """
    # Write your logic here
    pass

def q20(buildings):
    """Q20: The Skyline Problem. buildings = [[left, right, height]]. Return key points representing outline.
    Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    Expected: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    """
    # Write your logic here
    pass

def q21(s, k):
    """Q21: Rearrange String k Distance Apart. Identical characters must be at least distance k apart.
    Input: s = "aabbcc", k = 3
    Expected: "abcabc" (or "acbacb" etc.)
    """
    # Write your logic here
    pass

def q22(target, startFuel, stations):
    """Q22: Minimum Number of Refueling Stops. stations = [[position, fuel]].
    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
    Expected: 2
    """
    # Write your logic here
    pass

def q23(n, speed, efficiency, k):
    """Q23: Maximum Performance of a Team (select at most k engineers. perf = sum(speed) * min(efficiency)).
    Return performance modulo 10^9 + 7.
    Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
    Expected: 60 (select index 1 and 4 -> speed sum 15, min eff 4. 15 * 4 = 60)
    """
    # Write your logic here
    pass

def q24(quality, wage, k):
    """Q24: Minimum Cost to Hire K Workers (according to quality/wage ratios).
    Input: quality = [10,20,5], wage = [70,50,30], k = 2
    Expected: 105.0 (hire worker 0 and 2. quality sum 15, ratio paid based on worker 0's wage/qual = 7.0. 15 * 7 = 105.0)
    """
    # Write your logic here
    pass

def q25(courses):
    """Q25: Course Schedule III. courses = [[duration, lastDay]].
    Input: courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
    Expected: 3
    """
    # Write your logic here
    pass


# --- INTERMEDIATE LEVEL (Q26 - Q60) ---

def q26(height):
    """Q26: Container With Most Water.
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Expected: 49
    """
    # Write your logic here
    pass

def q27(nums):
    """Q27: 3Sum.
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Expected: [[-1, -1, 2], [-1, 0, 1]]
    """
    # Write your logic here
    pass

def q28(nums, target):
    """Q28: 3Sum Closest.
    Input: nums = [-1, 2, 1, -4], target = 1
    Expected: 2
    """
    # Write your logic here
    pass

def q29(nums, target):
    """Q29: 3Sum Smaller.
    Input: nums = [-2, 0, 1, 3], target = 2
    Expected: 2
    """
    # Write your logic here
    pass

def q30(nums, target):
    """Q30: 4Sum.
    Input: nums = [1, 0, -1, 0, -2, 2], target = 0
    Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    """
    # Write your logic here
    pass

def q31(nums, target):
    """Q31: Two Sum Less Than K.
    Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], target = 60
    Expected: 58
    """
    # Write your logic here
    pass

def q32(nums):
    """Q32: Sort Colors.
    Input: nums = [2, 0, 2, 1, 1, 0]
    Expected: [0, 0, 1, 1, 2, 2]
    """
    # Write your logic here
    pass

def q33(target, nums):
    """Q33: Minimum Size Subarray Sum.
    Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    Expected: 2
    """
    # Write your logic here
    pass

def q34(s):
    """Q34: Longest Substring Without Repeating Characters.
    Input: s = "abcabcbb"
    Expected: 3
    """
    # Write your logic here
    pass

def q35(nums, k):
    """Q35: Max Consecutive Ones III.
    Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
    Expected: 6
    """
    # Write your logic here
    pass

def q36(tokens, power):
    """Q36: Bag of Tokens.
    Input: tokens = [100, 200, 300, 400], power = 200
    Expected: 2
    """
    # Write your logic here
    pass

def q37(people, limit):
    """Q37: Boats to Save People.
    Input: people = [3, 2, 2, 1], limit = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q38(nums):
    """Q38: Minimize Maximum Pair Sum in Array.
    Input: nums = [3, 5, 2, 3]
    Expected: 7
    """
    # Write your logic here
    pass

def q39(nums, left, right):
    """Q39: Number of Subarrays with Bounded Maximum.
    Input: nums = [2, 1, 4, 3], left = 2, right = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q40(firstList, secondList):
    """Q40: Interval List Intersections.
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Expected: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    """
    # Write your logic here
    pass

def q41(dominoes):
    """Q41: Push Dominoes.
    Input: dominoes = ".L.R...LR..L.."
    Expected: "LL.RR.LLRR.LL."
    """
    # Write your logic here
    pass

def q42(start, target):
    """Q42: Move Pieces to Obtain a String.
    Input: start = "_R_L_", target = "__RL_"
    Expected: True
    """
    # Write your logic here
    pass

def q43(s):
    """Q43: Split Two Strings to Make Palindrome.
    Input: s = ("x", "y") where s[0]="ulacfd", s[1]="jizalu"
    Expected: True
    """
    # Write your logic here
    pass

def q44(sentence1, sentence2):
    """Q44: Sentence Similarity III.
    Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
    Expected: True
    """
    # Write your logic here
    pass

def q45(arr, k, x):
    """Q45: Find K Closest Elements.
    Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
    Expected: [1, 2, 3, 4]
    """
    # Write your logic here
    pass

def q46(nums):
    """Q46: Valid Triangle Number.
    Input: nums = [2, 2, 3, 4]
    Expected: 3
    """
    # Write your logic here
    pass

def q47(arr):
    """Q47: Longest Mountain in Array.
    Input: arr = [2, 1, 4, 7, 3, 2, 5]
    Expected: 5
    """
    # Write your logic here
    pass

def q48(nums):
    """Q48: Longest Subarray of 1's After Deleting One Element.
    Input: nums = [1, 1, 0, 1]
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

def q50(version1, version2):
    """Q50: Compare Version Numbers.
    Input: version1 = "1.01", version2 = "1.001"
    Expected: 0
    """
    # Write your logic here
    pass

def q51(nums):
    """Q51: Minimum Swaps to Group All 1's Together.
    Input: nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    Expected: 2
    """
    # Write your logic here
    pass

def q52(chars):
    """Q52: String Compression.
    Input: chars = ["a", "a", "b", "b", "c", "c", "c"]
    Expected: 6
    """
    # Write your logic here
    pass

def q53(nums):
    """Q53: Next Permutation.
    Input: nums = [1, 2, 3]
    Expected: [1, 3, 2]
    """
    # Write your logic here
    pass

def q54(s):
    """Q54: Smallest Subsequence of Distinct Characters.
    Input: s = "cbacdcbc"
    Expected: "acdb"
    """
    # Write your logic here
    pass

def q55(s, k):
    """Q55: Longest Substring with At Most K Distinct Characters.
    Input: s = "eceba", k = 2
    Expected: 3
    """
    # Write your logic here
    pass

def q56(s):
    """Q56: Number of Substrings Containing All Three Characters.
    Input: s = "abcabc"
    Expected: 10
    """
    # Write your logic here
    pass

def q57(s1, s2):
    """Q57: Permutation in String.
    Input: s1 = "ab", s2 = "eidbaooo"
    Expected: True
    """
    # Write your logic here
    pass

def q58(s, p):
    """Q58: Find All Anagrams in a String.
    Input: s = "cbaebabacd", p = "abc"
    Expected: [0, 6]
    """
    # Write your logic here
    pass

def q59(nums):
    """Q59: Maximum Erasure Value.
    Input: nums = [4, 2, 4, 5, 6]
    Expected: 17
    """
    # Write your logic here
    pass

def q60(s, t, maxCost):
    """Q60: Get Equal Substrings Within Budget.
    Input: s = "abcd", t = "bcdf", maxCost = 3
    Expected: 3
    """
    # Write your logic here
    pass


# --- ADVANCED LEVEL (Q61 - Q100) ---

def q61(height):
    """Q61: Trapping Rain Water.
    Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Expected: 6
    """
    # Write your logic here
    pass

def q62(s, t):
    """Q62: Minimum Window Substring.
    Input: s = "ADOBECODEBANC", t = "ABC"
    Expected: "BANC"
    """
    # Write your logic here
    pass

def q63(nums, k):
    """Q63: Subarrays with K Different Integers.
    Input: nums = [1, 2, 1, 2, 3], k = 2
    Expected: 7
    """
    # Write your logic here
    pass

def q64(s, t):
    """Q64: Minimum Window Subsequence.
    Input: s = "abcdebdde", t = "bde"
    Expected: "bcde"
    """
    # Write your logic here
    pass

def q65(nums, k):
    """Q65: Subarray Product Less Than K.
    Input: nums = [10, 5, 2, 6], k = 100
    Expected: 8
    """
    # Write your logic here
    pass

def q66(nums, k):
    """Q66: Shortest Subarray with Sum at Least K.
    Input: nums = [2, -1, 2], k = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q67(s, k):
    """Q67: Longest Repeating Character Replacement.
    Input: s = "AABABBA", k = 1
    Expected: 4
    """
    # Write your logic here
    pass

def q68(nums, k):
    """Q68: Sliding Window Maximum.
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Expected: [3, 3, 5, 5, 6, 7]
    """
    # Write your logic here
    pass

def q69(nums, x):
    """Q69: Minimum Operations to Reduce X to Zero.
    Input: nums = [1, 1, 4, 2, 3], x = 5
    Expected: 2
    """
    # Write your logic here
    pass

def q70(matrix, k):
    """Q70: Max Sum of Rectangle No Larger Than K.
    Input: matrix = [[1, 0, 1], [0, -2, 3]], k = 2
    Expected: 2
    """
    # Write your logic here
    pass

def q71(s1, s2):
    """Q71: Minimum Swaps to Make Strings Equal.
    Input: s1 = "xx", s2 = "yy"
    Expected: 1
    """
    # Write your logic here
    pass

def q72(words, groups):
    """Q72: Expressive Words.
    Input: words = ("hellooo", ["hello", "hi", "helo"])
    Expected: 1
    """
    # Write your logic here
    pass

def q73(s, k):
    """Q73: Valid Palindrome III.
    Input: s = "abcdeca", k = 2
    Expected: True
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
    """Q75: Distinct Subsequences.
    Input: s = "rabbbit", t = "rabbit"
    Expected: 3
    """
    # Write your logic here
    pass

def q76(lists):
    """Q76: Merge K Sorted Lists.
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
    1: {'func': q1, 'args': [[3, 2, 1, 5, 6, 4], 2], 'expected': 5},
    2: {'func': q2, 'args': [[2, 7, 4, 1, 8, 1]], 'expected': 1},
    3: {'func': q3, 'args': [[5, 4, 3, 2, 1]], 'expected': ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]},
    4: {'func': q4, 'args': [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], 'expected': 13},
    5: {'func': q5, 'args': [[[1, 3], [-2, 2]], 1], 'expected': [[-2, 2]]},
    6: {'func': q6, 'args': [[1, 1, 1, 2, 2, 3], 2], 'expected': [1, 2]},
    7: {'func': q7, 'args': [["i", "love", "leetcode", "i", "love", "coding"], 2], 'expected': ["i", "love"]},
    8: {'func': q8, 'args': [[[1, 4, 5], [1, 3, 4], [2, 6]]], 'expected': [1, 1, 2, 3, 4, 4, 5, 6]},
    9: {'func': q9, 'args': ["aab"], 'expected': "aba"},
    10: {'func': q10, 'args': [[1, 7, 11], [2, 4, 6], 3], 'expected': [[1, 2], [1, 4], [1, 6]]},
    11: {'func': q11, 'args': [[4, 2, 7, 6, 9, 14, 12], 5, 1], 'expected': 4},
    12: {'func': q12, 'args': [[[1, 2], [2, 4], [3, 2], [4, 1]]], 'expected': [0, 2, 3, 1]},
    13: {'func': q13, 'args': [[[2, 1, 5], [3, 3, 7]], 4], 'expected': False},
    14: {'func': q14, 'args': [[2, 4, 3]], 'expected': 14},
    15: {'func': q15, 'args': [12, [2, 7, 13, 19]], 'expected': 32},
    16: {'func': q16, 'args': [[1, 2, 3]], 'expected': [1.0, 1.5, 2.0]},
    17: {'func': q17, 'args': [[1, 3, -1, -3, 5, 3, 6, 7], 3], 'expected': [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]},
    18: {'func': q18, 'args': [2, 0, [1, 2, 3], [0, 1, 1]], 'expected': 4},
    19: {'func': q19, 'args': [[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]], 'expected': [20, 24]},
    20: {'func': q20, 'args': [[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]], 'expected': [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]},
    21: {'func': q21, 'args': ["aabbcc", 3], 'expected': "abcabc"},
    22: {'func': q22, 'args': [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], 'expected': 2},
    23: {'func': q23, 'args': [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2], 'expected': 60},
    24: {'func': q24, 'args': [[10, 20, 5], [70, 50, 30], 2], 'expected': 105.0},
    25: {'func': q25, 'args': [[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]], 'expected': 3},
    
    26: {'func': q26, 'args': [[1, 8, 6, 2, 5, 4, 8, 3, 7]], 'expected': 49},
    27: {'func': q27, 'args': [[-1, 0, 1, 2, -1, -4]], 'expected': [[-1, -1, 2], [-1, 0, 1]]},
    28: {'func': q28, 'args': [[-1, 2, 1, -4], 1], 'expected': 2},
    29: {'func': q29, 'args': [[-2, 0, 1, 3], 2], 'expected': 2},
    30: {'func': q30, 'args': [[1, 0, -1, 0, -2, 2], 0], 'expected': [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]},
    31: {'func': q31, 'args': [[34, 23, 1, 24, 75, 33, 54, 8], 60], 'expected': 58},
    32: {'func': q32, 'args': [[2, 0, 2, 1, 1, 0]], 'expected': [0, 0, 1, 1, 2, 2]},
    33: {'func': q33, 'args': [7, [2, 3, 1, 2, 4, 3]], 'expected': 2},
    34: {'func': q34, 'args': ["abcabcbb"], 'expected': 3},
    35: {'func': q35, 'args': [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2], 'expected': 6},
    36: {'func': q36, 'args': [[100, 200, 300, 400], 200], 'expected': 2},
    37: {'func': q37, 'args': [[3, 2, 2, 1], 3], 'expected': 3},
    38: {'func': q38, 'args': [[3, 5, 2, 3]], 'expected': 7},
    39: {'func': q39, 'args': [[2, 1, 4, 3], 2, 3], 'expected': 3},
    40: {'func': q40, 'args': [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]]], 'expected': [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]},
    41: {'func': q41, 'args': [".L.R...LR..L.."], 'expected': "LL.RR.LLRR.LL."},
    42: {'func': q42, 'args': ["_R_L_", "__RL_"], 'expected': True},
    43: {'func': q43, 'args': [("ulacfd", "jizalu")], 'expected': True},
    44: {'func': q44, 'args': ["My name is Haley", "My Haley"], 'expected': True},
    45: {'func': q45, 'args': [[1, 2, 3, 4, 5], 4, 3], 'expected': [1, 2, 3, 4]},
    46: {'func': q46, 'args': [[2, 2, 3, 4]], 'expected': 3},
    47: {'func': q47, 'args': [[2, 1, 4, 7, 3, 2, 5]], 'expected': 5},
    48: {'func': q48, 'args': [[1, 1, 0, 1]], 'expected': 3},
    49: {'func': q49, 'args': ["ababcbacadefegdehijhklij"], 'expected': [9, 7, 8]},
    50: {'func': q50, 'args': ["1.01", "1.001"], 'expected': 0},
    51: {'func': q51, 'args': [[0, 1, 1, 1, 0, 0, 1, 1, 0]], 'expected': 2},
    52: {'func': q52, 'args': [["a", "a", "b", "b", "c", "c", "c"]], 'expected': 6},
    53: {'func': q53, 'args': [[1, 2, 3]], 'expected': [1, 3, 2]},
    54: {'func': q54, 'args': ["cbacdcbc"], 'expected': "acdb"},
    55: {'func': q55, 'args': ["eceba", 2], 'expected': 3},
    56: {'func': q56, 'args': ["abcabc"], 'expected': 10},
    57: {'func': q57, 'args': ["ab", "eidbaooo"], 'expected': True},
    58: {'func': q58, 'args': ["cbaebabacd", "abc"], 'expected': [0, 6]},
    59: {'func': q59, 'args': [[4, 2, 4, 5, 6]], 'expected': 17},
    60: {'func': q60, 'args': ["abcd", "bcdf", 3], 'expected': 3},
    
    61: {'func': q61, 'args': [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], 'expected': 6},
    62: {'func': q62, 'args': ["ADOBECODEBANC", "ABC"], 'expected': "BANC"},
    63: {'func': q63, 'args': [[1, 2, 1, 2, 3], 2], 'expected': 7},
    64: {'func': q64, 'args': ["abcdebdde", "bde"], 'expected': "bcde"},
    65: {'func': q65, 'args': [[10, 5, 2, 6], 100], 'expected': 8},
    66: {'func': q66, 'args': [[2, -1, 2], 3], 'expected': 3},
    67: {'func': q67, 'args': ["AABABBA", 1], 'expected': 4},
    68: {'func': q68, 'args': [[1, 3, -1, -3, 5, 3, 6, 7], 3], 'expected': [3, 3, 5, 5, 6, 7]},
    69: {'func': q69, 'args': [[1, 1, 4, 2, 3], 5], 'expected': 2},
    70: {'func': q70, 'args': [[[1, 0, 1], [0, -2, 3]], 2], 'expected': 2},
    71: {'func': q71, 'args': ["xx", "yy"], 'expected': 1},
    72: {'func': q72, 'args': ["hellooo", ["hello", "hi", "helo"]], 'expected': 1},
    73: {'func': q73, 'args': ["abcdeca", 2], 'expected': True},
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
            print(f"❌ Question {QUESTION_NUMBER} not found!")
            return False
    
        func = test['func']
        args = test['args']
        expected = test['expected']
    
        print(f"\n{'='*60}")
        print(f"Question {QUESTION_NUMBER}: {func.__doc__.splitlines()[0]}")
        print(f"{'='*60}")
        print(f"Input: {args}")
        print(f"Expected: {expected}")
        print("-"*60)
    
        try:
            # Mock class for q16 (Median Finder)
            if QUESTION_NUMBER == 16:
                # We will simulate stream insertion
                stream_vals = args
                # Simulate min/max heap median calculations
                res_list = []
                small_heap, large_heap = [], [] # max heap (simulated with negative), min heap
                for num in stream_vals:
                    heapq.heappush(small_heap, -num)
                    heapq.heappush(large_heap, -heapq.heappop(small_heap))
                    if len(large_heap) > len(small_heap):
                        heapq.heappush(small_heap, -heapq.heappop(large_heap))
                    if len(small_heap) > len(large_heap):
                        res_list.append(float(-small_heap[0]))
                    else:
                        res_list.append((-small_heap[0] + large_heap[0]) / 2.0)
                result = res_list
            else:
                result = func(*args) if isinstance(args, list) else func(args)
            
            print(f"Your Output: {result}")
        
            # Sort output matches if required for sets
            if QUESTION_NUMBER in [5, 6, 10]:
                if result and isinstance(result, list):
                    result = sorted([sorted(x) if isinstance(x, list) else x for x in result])
                    expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                
            if result == expected:
                print("\n✅ PASS - Correct!")
            else:
                print("\n❌ FAIL - Output doesn't match expected")
        except Exception as e:
            print(f"\n❌ ERROR: {e}")
    
        print(f"{'='*60}\n")
    except Exception as e:
        if not silent:
            print(f"\n❌ ERROR: {e}")
        return False
    finally:
        sys.stdout = old_stdout
        
    if silent:
        output_str = captured.getvalue()
        return "✅ PASS" in output_str
    return True

if __name__ == "__main__":
    import sys
    # Check CLI arguments first
    if len(sys.argv) > 1:
        try:
            QUESTION_NUMBER = int(sys.argv[1])
        except ValueError:
            pass

    # If QUESTION_NUMBER is None or 0, auto-detect the first unsolved question
    if QUESTION_NUMBER is None or QUESTION_NUMBER == 0:
        detected_q = 1
        for q_num in sorted(TESTS.keys()):
            if not run_test(q_num, silent=True):
                detected_q = q_num
                break
        else:
            detected_q = max(TESTS.keys())
        QUESTION_NUMBER = detected_q

    # Run the selected question in verbose mode
    run_test(QUESTION_NUMBER, silent=False)
