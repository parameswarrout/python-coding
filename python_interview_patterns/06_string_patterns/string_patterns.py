import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
String Patterns - Practice One Question at a Time
=================================================
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

def q1(strs):
    """Q1: Longest Common Prefix. Find the longest common prefix string amongst an array of strings.
    Input: strs = ["flower", "flow", "flight"]
    Expected Output: "fl"
    """
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for other in strs:
            if other[i] != char:
                return shortest[:i]
    return shortest

def q2(haystack, needle):
    """Q2: Find the Index of the First Occurrence in a String. Return index or -1.
    Input: haystack = "sadbutsad", needle = "sad"
    Expected Output: 0
    """
    if not needle:
        return 0
    n, h = len(needle), len(haystack)
    for i in range(h - n + 1):
        if haystack[i:i+n] == needle:
            return i
    return -1

def q3(s):
    """Q3: Length of Last Word. Return length of last word in string of spaces and words.
    Input: s = "   fly me   to   the moon  "
    Expected: 4 ("moon")
    """
    # Write your logic here
    pass

def q4(s):
    """Q4: Valid Parentheses. Check bracket matching: '(', ')', '{', '}', '[', ']'.
    Input: s = "()[]{}"
    Expected: True
    """
    # Write your logic here
    pass

def q5(address):
    """Q5: Defanging an IP Address. Replace every '.' with '[.]'.
    Input: address = "1.1.1.1"
    Expected: "1[.]1[.]1[.]1"
    """
    # Write your logic here
    pass

def q6(s):
    """Q6: To Lower Case. Convert all characters in string to lower case in-place/return.
    Input: s = "Hello"
    Expected: "hello"
    """
    # Write your logic here
    pass

def q7(s):
    """Q7: Reverse Only Letters. Keep non-letters in their original locations.
    Input: s = "a-bC-dEf-ghIj"
    Expected: "j-Ih-gfE-dCba"
    """
    # Write your logic here
    pass

def q8(s):
    """Q8: Reverse Words in a String. Reverse words order, remove extra spaces.
    Input: s = "  hello world  "
    Expected: "world hello"
    """
    # Write your logic here
    pass

def q9(n):
    """Q9: Count and Say (sequence generator).
    Input: n = 4
    Expected: "1211" (say 1 is "11", say 11 is "21", say 21 is "1211")
    """
    # Write your logic here
    pass

def q10(s):
    """Q10: Repeated Substring Pattern. Check if s can be formed by repeating a substring.
    Input: s = "abab"
    Expected: True
    """
    # Write your logic here
    pass

def q11(s):
    """Q11: Valid Palindrome (considering only alphanumeric characters and ignoring cases).
    Input: s = "A man, a plan, a canal: Panama"
    Expected: True
    """
    # Write your logic here
    pass

def q12(s):
    """Q12: Valid Palindrome II. Can delete at most one character to make it a palindrome.
    Input: s = "abca"
    Expected: True
    """
    # Write your logic here
    pass

def q13(s, t):
    """Q13: Isomorphic Strings. Check if s and t are isomorphic.
    Input: s = "egg", t = "add"
    Expected: True
    """
    # Write your logic here
    pass

def q14(pattern, s):
    """Q14: Word Pattern. Check if s follows pattern.
    Input: pattern = "abba", s = "dog cat cat dog"
    Expected: True
    """
    # Write your logic here
    pass

def q15(s):
    """Q15: Longest Palindromic Substring.
    Input: s = "babad"
    Expected: "bab" (or "aba")
    """
    # Write your logic here
    pass

def q16(s):
    """Q16: Palindromic Substrings (count total palindromic substrings).
    Input: s = "aaa"
    Expected: 6 ("a", "a", "a", "aa", "aa", "aaa")
    """
    # Write your logic here
    pass

def q17(path):
    """Q17: Simplify Path (canonical path representation).
    Input: path = "/home//foo/"
    Expected: "/home/foo"
    """
    # Write your logic here
    pass

def q18(num1, num2):
    """Q18: Multiply Strings (large numbers multiplication without using big integer library).
    Input: num1 = "123", num2 = "456"
    Expected: "56088"
    """
    # Write your logic here
    pass

def q19(s):
    """Q19: Basic Calculator II (evaluate expression string containing +, -, *, /).
    Input: s = "3+2*2"
    Expected: 7
    """
    # Write your logic here
    pass

def q20(s, numRows):
    """Q20: Zigzag Conversion.
    Input: s = "PAYPALISHIRING", numRows = 3
    Expected: "PAHNAPLSIIGYIR"
    """
    # Write your logic here
    pass

def q21(s):
    """Q21: String to Integer (atoi).
    Input: s = "   -42"
    Expected: -42
    """
    # Write your logic here
    pass

def q22(num):
    """Q22: Integer to Roman.
    Input: num = 1994
    Expected: "MCMXCIV"
    """
    # Write your logic here
    pass

def q23(s):
    """Q23: Roman to Integer.
    Input: s = "MCMXCIV"
    Expected: 1994
    """
    # Write your logic here
    pass

def q24(s):
    """Q24: Decode Ways. Return number of ways to decode string numbers to letters (A->1, B->2, ... Z->26).
    Input: s = "226"
    Expected: 3 (BZ -> 2, 26; VF -> 22, 6; BBF -> 2, 2, 6)
    """
    # Write your logic here
    pass

def q25(s):
    """Q25: Restore IP Addresses. All possible valid IP addresses that can be formed from s digits.
    Input: s = "25525511135"
    Expected: ["255.255.11.135", "255.255.111.35"]
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
    """Q27: 3Sum. Unique triplets that sum to 0.
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
    1: {'func': q1, 'args': [["flower", "flow", "flight"]], 'expected': "fl"},
    2: {'func': q2, 'args': ["sadbutsad", "sad"], 'expected': 0},
    3: {'func': q3, 'args': ["   fly me   to   the moon  "], 'expected': 4},
    4: {'func': q4, 'args': ["()[]{}"], 'expected': True},
    5: {'func': q5, 'args': ["1.1.1.1"], 'expected': "1[.]1[.]1[.]1"},
    6: {'func': q6, 'args': ["Hello"], 'expected': "hello"},
    7: {'func': q7, 'args': ["a-bC-dEf-ghIj"], 'expected': "j-Ih-gfE-dCba"},
    8: {'func': q8, 'args': ["  hello world  "], 'expected': "world hello"},
    9: {'func': q9, 'args': [4], 'expected': "1211"},
    10: {'func': q10, 'args': ["abab"], 'expected': True},
    11: {'func': q11, 'args': ["A man, a plan, a canal: Panama"], 'expected': True},
    12: {'func': q12, 'args': ["abca"], 'expected': True},
    13: {'func': q13, 'args': ["egg", "add"], 'expected': True},
    14: {'func': q14, 'args': ["abba", "dog cat cat dog"], 'expected': True},
    15: {'func': q15, 'args': ["babad"], 'expected': "bab"},
    16: {'func': q16, 'args': ["aaa"], 'expected': 6},
    17: {'func': q17, 'args': ["/home//foo/"], 'expected': "/home/foo"},
    18: {'func': q18, 'args': ["123", "456"], 'expected': "56088"},
    19: {'func': q19, 'args': ["3+2*2"], 'expected': 7},
    20: {'func': q20, 'args': ["PAYPALISHIRING", 3], 'expected': "PAHNAPLSIIGYIR"},
    21: {'func': q21, 'args': ["   -42"], 'expected': -42},
    22: {'func': q22, 'args': [1994], 'expected': "MCMXCIV"},
    23: {'func': q23, 'args': ["MCMXCIV"], 'expected': 1994},
    24: {'func': q24, 'args': ["226"], 'expected': 3},
    25: {'func': q25, 'args': ["25525511135"], 'expected': ["255.255.11.135", "255.255.111.35"]},
    
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
