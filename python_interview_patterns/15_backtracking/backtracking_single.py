import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
Backtracking - Practice One Question at a Time
==============================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 100)
2. Write your logic in the corresponding function (q1 to q100)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = 3  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 100 QUESTIONS ====================

def q1(nums: list) -> list:
    """Q1: Subsets. Return all possible subsets (power set) of unique elements.
    Input: nums = [1, 2, 3]
    Expected Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]] (any order)
    """
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        # exclude nums[i]
        subset.pop()
        dfs(i + 1)
    dfs(0)
    return res

def q2(nums: list) -> list:
    """Q2: Subsets II. Return all subsets, avoiding duplicates if input has duplicate elements.
    Input: nums = [1, 2, 2]
    Expected Output: [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]] (any order)
    """
    nums.sort()
    res = []
    subset = []
    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return
        # include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        
        # skip duplicates
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)
    dfs(0)
    return res

def q3(n: int, k: int) -> list:
    """Q3: Combinations. Return all possible combinations of k numbers chosen from range 1 to n.
    Input: n = 4, k = 2
    Expected: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    """
    # Write your logic here
    pass

def q4(candidates: list, target: int) -> list:
    """Q4: Combination Sum. Candidates are unique, can reuse elements multiple times.
    Input: candidates = [2, 3, 6, 7], target = 7
    Expected: [[2, 2, 3], [7]]
    """
    # Write your logic here
    pass

def q5(candidates: list, target: int) -> list:
    """Q5: Combination Sum II. Candidates can contain duplicates, each number can only be used once.
    Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
    Expected: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    """
    # Write your logic here
    pass

def q6(k: int, n: int) -> list:
    """Q6: Combination Sum III. Find combinations of k numbers summing to n, unique numbers from 1 to 9.
    Input: k = 3, n = 7
    Expected: [[1, 2, 4]]
    """
    # Write your logic here
    pass

def q7(digits: str) -> list:
    """Q7: Letter Combinations of a Phone Number.
    Input: digits = "23"
    Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    """
    # Write your logic here
    pass

def q8(nums: list) -> list:
    """Q8: Permutations of distinct integers.
    Input: nums = [1, 2, 3]
    Expected: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    """
    # Write your logic here
    pass

def q9(nums: list) -> list:
    """Q9: Permutations II (contains duplicates). Return all unique permutations.
    Input: nums = [1, 1, 2]
    Expected: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    """
    # Write your logic here
    pass

def q10(s: str) -> list:
    """Q10: Palindrome Partitioning. Partition s such that every substring is a palindrome.
    Input: s = "aab"
    Expected: [["a", "a", "b"], ["aa", "b"]]
    """
    # Write your logic here
    pass

def q11(board: list, word: str) -> bool:
    """Q11: Word Search on grid.
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Expected: True
    """
    # Write your logic here
    pass

def q12(matchsticks: list) -> bool:
    """Q12: Matchsticks to Square. Check if matchsticks can be partitioned into 4 equal sides.
    Input: matchsticks = [1, 1, 2, 2, 2]
    Expected: True
    """
    # Write your logic here
    pass

def q13(s: str) -> list:
    """Q13: Restore IP Addresses. Return all possible valid IP addresses partitioned from string.
    Input: s = "25525511135"
    Expected: ["255.255.11.135", "255.255.111.35"]
    """
    # Write your logic here
    pass

def q14(n: int) -> list:
    """Q14: N-Queens. Return all distinct board configurations.
    Input: n = 4
    Expected: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
    """
    # Write your logic here
    pass

def q15(n: int) -> int:
    """Q15: N-Queens II. Return total number of distinct board configurations.
    Input: n = 4
    Expected: 2
    """
    # Write your logic here
    pass

def q16(board: list) -> list:
    """Q16: Sudoku Solver. Solve in-place, return completed grid.
    Input: board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    Expected: Completed sudoku board values
    """
    # Write your logic here
    pass

def q17(board: list, words: list) -> list:
    """Q17: Word Search II (Trie + Backtracking). Find all matching words from wordlist on board.
    Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
    Expected: ["oath", "eat"]
    """
    # Write your logic here
    pass

def q18(num: str, target: int) -> list:
    """Q18: Expression Add Operators. Add operators '+', '-', or '*' to num to get target.
    Input: num = "123", target = 6
    Expected: ["1+2+3", "1*2*3"]
    """
    # Write your logic here
    pass

def q19(grid: list) -> int:
    """Q19: Unique Paths III. Count 4-directional paths from start to end visiting every non-obstacle square exactly once.
    Input: grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    Expected: 2
    """
    # Write your logic here
    pass

def q20(n: int, k: int) -> str:
    """Q20: Permutation Sequence. Find the kth permutation sequence of numbers from 1 to n.
    Input: n = 3, k = 3
    Expected: "213"
    """
    # Write your logic here
    pass

def q21(s: str) -> int:
    """Q21: Split a String Into the Max Number of Unique Substrings.
    Input: s = "ababccc"
    Expected: 5 (split into "a", "b", "ab", "c", "cc")
    """
    # Write your logic here
    pass

def q22(n: int) -> int:
    """Q22: Beautiful Arrangement. Count combinations of indices matching index/value divisions.
    Input: n = 2
    Expected: 2
    """
    # Write your logic here
    pass

def q23(grid: list) -> int:
    """Q23: Path with Maximum Gold.
    Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
    Expected: 24 (path: 9->8->7 or 9->8->5 -> total 9+8+7 = 24)
    """
    # Write your logic here
    pass

def q24(n: int) -> list:
    """Q24: Construct the Lexicographically Largest Valid Sequence.
    Input: n = 3
    Expected: [3, 1, 2, 3, 2]
    """
    # Write your logic here
    pass

def q25(turnedOn: int) -> list:
    """Q25: Binary Watch.
    Input: turnedOn = 1
    Expected: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
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
    1: {'func': q1, 'args': [[1, 2, 3]], 'expected': [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]},
    2: {'func': q2, 'args': [[1, 2, 2]], 'expected': [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]},
    3: {'func': q3, 'args': [4, 2], 'expected': [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]},
    4: {'func': q4, 'args': [[2, 3, 6, 7], 7], 'expected': [[2, 2, 3], [7]]},
    5: {'func': q5, 'args': [[10, 1, 2, 7, 6, 1, 5], 8], 'expected': [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]},
    6: {'func': q6, 'args': [3, 7], 'expected': [[1, 2, 4]]},
    7: {'func': q7, 'args': ["23"], 'expected': ["ad","ae","af","bd","be","bf","cd","ce","cf"]},
    8: {'func': q8, 'args': [[1, 2, 3]], 'expected': [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]},
    9: {'func': q9, 'args': [[1, 1, 2]], 'expected': [[1, 1, 2], [1, 2, 1], [2, 1, 1]]},
    10: {'func': q10, 'args': ["aab"], 'expected': [["a", "a", "b"], ["aa", "b"]]},
    11: {'func': q11, 'args': [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"], 'expected': True},
    12: {'func': q12, 'args': [[1, 1, 2, 2, 2]], 'expected': True},
    13: {'func': q13, 'args': ["25525511135"], 'expected': ["255.255.11.135", "255.255.111.35"]},
    14: {'func': q14, 'args': [4], 'expected': [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]},
    15: {'func': q15, 'args': [4], 'expected': 2},
    16: {'func': q16, 'args': [[
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]], 'expected': [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]},
    17: {'func': q17, 'args': [[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]], 'expected': ["oath", "eat"]},
    18: {'func': q18, 'args': ["123", 6], 'expected': ["1+2+3", "1*2*3"]},
    19: {'func': q19, 'args': [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]], 'expected': 2},
    20: {'func': q20, 'args': [3, 3], 'expected': "213"},
    21: {'func': q21, 'args': ["ababccc"], 'expected': 5},
    22: {'func': q22, 'args': [2], 'expected': 2},
    23: {'func': q23, 'args': [[[0,6,0],[5,8,7],[0,9,0]]], 'expected': 24},
    24: {'func': q24, 'args': [3], 'expected': [3, 1, 2, 3, 2]},
    25: {'func': q25, 'args': [1], 'expected': ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]},
    
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

if __name__ == "__main__":
    test = TESTS.get(QUESTION_NUMBER)
    
    if not test:
        print(f"❌ Question {QUESTION_NUMBER} not found!")
        exit(1)
    
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
        result = func(*args) if isinstance(args, list) else func(args)
        
        # Sort values if order doesn't matter for combinations/subsets/permutations
        if QUESTION_NUMBER in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 18, 25]:
            if result and isinstance(result, list):
                result = sorted([sorted(x) if isinstance(x, list) else x for x in result])
                expected = sorted([sorted(x) if isinstance(x, list) else x for x in expected])
                
        print(f"Your Output: {result}")
        
        if result == expected:
            print("\n✅ PASS - Correct!")
        else:
            print("\n❌ FAIL - Output doesn't match expected")
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
    
    print(f"{'='*60}\n")
