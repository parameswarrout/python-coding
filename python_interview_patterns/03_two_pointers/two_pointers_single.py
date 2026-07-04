import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
Two Pointers Technique - Practice One Question at a Time
========================================================
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

def q1(arr):
    """Q1: Reverse an array in-place.
    Input: arr = [1, 2, 3, 4, 5]
    Expected Output: [5, 4, 3, 2, 1]
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

def q2(s):
    """Q2: Reverse vowels in a string (return new string).
    Vowels are 'a', 'e', 'i', 'o', 'u' (both case-insensitive).
    Input: s = "hello"
    Expected Output: "holle"
    """
    vowels = set("aeiouAEIOU")
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1
        while left < right and chars[right] not in vowels:
            right -= 1
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)

def q3(s):
    """Q3: Valid Palindrome (ignoring non-alphanumeric, case-insensitive).
    Input: s = "A man, a plan, a canal: Panama"
    Expected: True
    """
    # Write your logic here
    pass

def q4(numbers, target):
    """Q4: Two Sum II - Input Array Is Sorted (1-indexed).
    Input: numbers = [2, 7, 11, 15], target = 9
    Expected: [1, 2]
    """
    # Write your logic here
    pass

def q5(nums):
    """Q5: Remove Duplicates from Sorted Array (in-place).
    Return the number of unique elements. The first 'k' elements of nums should hold the unique values.
    Input: nums = [1, 1, 2]
    Expected: 2 (nums becomes [1, 2, _])
    """
    # Write your logic here
    pass

def q6(nums):
    """Q6: Remove Duplicates from Sorted Array II.
    Each unique element may appear at most twice. Return the count.
    Input: nums = [1, 1, 1, 2, 2, 3]
    Expected: 5 (nums becomes [1, 1, 2, 2, 3, _])
    """
    # Write your logic here
    pass

def q7(nums):
    """Q7: Move Zeros. Move all 0's to the end in-place while maintaining relative order of non-zeros.
    Input: nums = [0, 1, 0, 3, 12]
    Expected: [1, 3, 12, 0, 0]
    """
    # Write your logic here
    pass

def q8(nums1, m, nums2, n):
    """Q8: Merge Sorted Array. nums1 has size m+n. Merge nums2 into nums1 in-place.
    Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    Expected: [1, 2, 2, 3, 5, 6]
    """
    # Write your logic here
    pass

def q9(nums):
    """Q9: Squares of a Sorted Array. Return sorted squares of nums sorted in non-decreasing order.
    Input: nums = [-4, -1, 0, 3, 10]
    Expected: [0, 1, 9, 16, 100]
    """
    # Write your logic here
    pass

def q10(nums1, nums2):
    """Q10: Intersection of Two Sorted Arrays. Find unique common elements.
    Input: nums1 = [1, 2, 2, 3], nums2 = [2, 2, 3, 4]
    Expected: [2, 3]
    """
    # Write your logic here
    pass

def q11(nums1, nums2):
    """Q11: Union of Two Sorted Arrays. Find all unique sorted union elements.
    Input: nums1 = [1, 2, 5], nums2 = [2, 3, 5, 6]
    Expected: [1, 2, 3, 5, 6]
    """
    # Write your logic here
    pass

def q12(s):
    """Q12: Valid Palindrome II. Can delete at most one character to make it a palindrome.
    Input: s = "abca"
    Expected: True (delete 'b' to get "aca" or 'c' to get "aba")
    """
    # Write your logic here
    pass

def q13(s):
    """Q13: Reverse Words in a String III. Reverse characters in each word individually.
    Input: s = "Let's take LeetCode contest"
    Expected: "s'teL ekat edoCteeL tsetnoc"
    """
    # Write your logic here
    pass

def q14(arr1, arr2):
    """Q14: Minimum Difference Between Two Sorted Arrays. Find min absolute difference |a - b| (a from arr1, b from arr2).
    Input: arr1 = [1, 5, 10], arr2 = [3, 8, 15]
    Expected: 2 (since |5 - 3| = 2 or |10 - 8| = 2)
    """
    # Write your logic here
    pass

def q15(s, t):
    """Q15: Check if s is subsequence of t.
    Input: s = "abc", t = "ahbgdc"
    Expected: True
    """
    # Write your logic here
    pass

def q16(nums, target):
    """Q16: Find Pair with Given Difference in a sorted array (return True if pair exists).
    Input: nums = [1, 5, 10, 15, 20], target = 5
    Expected: True (since 10 - 5 = 5)
    """
    # Write your logic here
    pass

def q17(nums):
    """Q17: Sort Array By Parity. Move all even integers to the beginning followed by all odd integers.
    Input: nums = [3, 1, 2, 4]
    Expected: [2, 4, 3, 1] (or any other valid combination like [4, 2, 1, 3])
    """
    # Write your logic here
    pass

def q18(nums):
    """Q18: Sort Array By Parity II. Sort so that even indices have even values and odd indices have odd values.
    Input: nums = [4, 2, 5, 7]
    Expected: [4, 5, 2, 7] (or [2, 5, 4, 7], etc.)
    """
    # Write your logic here
    pass

def q19(nums, pivot):
    """Q19: Partition Array According to Pivot. Less than pivot on left, greater on right, preserving relative order.
    Input: nums = [9, 12, 5, 10, 14, 3, 10], pivot = 10
    Expected: [9, 5, 3, 10, 10, 12, 14]
    """
    # Write your logic here
    pass

def q20(s, t):
    """Q20: Backspace String Compare. '#' means backspace. Return True if strings are equal after backspacing.
    Input: s = "ab#c", t = "ad#c"
    Expected: True (both become "ac")
    """
    # Write your logic here
    pass

def q21(haystack, needle):
    """Q21: Find Index of First Occurrence in String.
    Input: haystack = "sadbutsad", needle = "sad"
    Expected: 0
    """
    # Write your logic here
    pass

def q22(s):
    """Q22: Longest Palindromic Substring (using two pointers expansion method).
    Input: s = "babad"
    Expected: "bab" (or "aba")
    """
    # Write your logic here
    pass

def q23(s):
    """Q23: Minimum Length of String After Deleting Similar Ends.
    Input: s = "caac"
    Expected: 0 (remove 'c's to get "aa", then remove 'a's to get "")
    """
    # Write your logic here
    pass

def q24(nums, k):
    """Q24: Find K-diff Pairs in an Array (number of unique pairs (i, j) where nums[i] - nums[j] = k).
    Input: nums = [3, 1, 4, 1, 5], k = 2
    Expected: 2 (pairs are (1, 3) and (3, 5))
    """
    # Write your logic here
    pass

def q25(g, s):
    """Q25: Assign Cookies. g is children greedy factor, s is cookie sizes. Maximize content children.
    Input: g = [1, 2, 3], s = [1, 1]
    Expected: 1
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
    """Q27: 3Sum. Find all unique triplets that sum to 0.
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Expected: [[-1, -1, 2], [-1, 0, 1]]
    """
    # Write your logic here
    pass

def q28(nums, target):
    """Q28: 3Sum Closest. Return sum of three integers closest to target.
    Input: nums = [-1, 2, 1, -4], target = 1
    Expected: 2
    """
    # Write your logic here
    pass

def q29(nums, target):
    """Q29: 3Sum Smaller. Return count of triplets index i, j, k with nums[i] + nums[j] + nums[k] < target.
    Input: nums = [-2, 0, 1, 3], target = 2
    Expected: 2 (triplets: [-2, 0, 1] and [-2, 0, 3])
    """
    # Write your logic here
    pass

def q30(nums, target):
    """Q30: 4Sum. Find all unique quadruplets that sum to target.
    Input: nums = [1, 0, -1, 0, -2, 2], target = 0
    Expected: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    """
    # Write your logic here
    pass

def q31(nums, target):
    """Q31: Two Sum Less Than K. Return maximum sum of nums[i] + nums[j] < target.
    Input: nums = [34, 23, 1, 24, 75, 33, 54, 8], target = 60
    Expected: 58 (sums of 34 and 24)
    """
    # Write your logic here
    pass

def q32(nums):
    """Q32: Sort Colors (Dutch National Flag). Sort 0s (red), 1s (white), 2s (blue) in-place.
    Input: nums = [2, 0, 2, 1, 1, 0]
    Expected: [0, 0, 1, 1, 2, 2]
    """
    # Write your logic here
    pass

def q33(target, nums):
    """Q33: Minimum Size Subarray Sum. Min length of subarray with sum >= target. Return 0 if none.
    Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    Expected: 2 (subarray is [4, 3])
    """
    # Write your logic here
    pass

def q34(s):
    """Q34: Longest Substring Without Repeating Characters.
    Input: s = "abcabcbb"
    Expected: 3 ("abc")
    """
    # Write your logic here
    pass

def q35(nums, k):
    """Q35: Max Consecutive Ones III. Longest subarray of 1's if you can flip at most k 0's.
    Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
    Expected: 6
    """
    # Write your logic here
    pass

def q36(tokens, power):
    """Q36: Bag of Tokens. Maximize score by playing tokens face up/down.
    Input: tokens = [100, 200, 300, 400], power = 200
    Expected: 2 (face up 100 (power=100, score=1), face down 400 (power=500, score=0), face up 200, 300 (power=0, score=2))
    """
    # Write your logic here
    pass

def q37(people, limit):
    """Q37: Boats to Save People. Each boat carries at most 2 people with weight sum <= limit.
    Input: people = [3, 2, 2, 1], limit = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q38(nums):
    """Q38: Minimize Maximum Pair Sum in Array. Pair elements to minimize the max pair sum.
    Input: nums = [3, 5, 2, 3]
    Expected: 7 (pairs: (2, 5) and (3, 3). Max is 7)
    """
    # Write your logic here
    pass

def q39(nums, left, right):
    """Q39: Number of Subarrays with Bounded Maximum. Subarrays where max element in [left, right].
    Input: nums = [2, 1, 4, 3], left = 2, right = 3
    Expected: 3 (subarrays: [2], [2, 1], [3])
    """
    # Write your logic here
    pass

def q40(firstList, secondList):
    """Q40: Interval List Intersections. Find intersection of two lists of closed intervals.
    Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
    Expected: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    """
    # Write your logic here
    pass

def q41(dominoes):
    """Q41: Push Dominoes. Return final state after dominoes fall ('L', 'R', '.').
    Input: dominoes = ".L.R...LR..L.."
    Expected: "LL.RR.LLRR.LL."
    """
    # Write your logic here
    pass

def q42(start, target):
    """Q42: Move Pieces to Obtain a String. Can move 'L' left and 'R' right past '.' if valid.
    Input: start = "_R_L_", target = "__RL_"
    Expected: True
    """
    # Write your logic here
    pass

def q43(s):
    """Q43: Split Two Strings to Make Palindrome. Check if split prefix of a + suffix of b is a palindrome.
    Input: s = ("x", "y") where s[0]="ulacfd", s[1]="jizalu"
    Expected: True (split at index 3: "ula" + "alu" = "ulaalu", which is a palindrome)
    """
    # Write your logic here
    pass

def q44(sentence1, sentence2):
    """Q44: Sentence Similarity III. Check if sentences can be made equal by inserting a phrase in one of them.
    Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
    Expected: True (insert "name is" in sentence2)
    """
    # Write your logic here
    pass

def q45(arr, k, x):
    """Q45: Find K Closest Elements in sorted array to target x.
    Input: arr = [1, 2, 3, 4, 5], k = 4, x = 3
    Expected: [1, 2, 3, 4]
    """
    # Write your logic here
    pass

def q46(nums):
    """Q46: Valid Triangle Number. Count triplets of indices that can form a triangle.
    Input: nums = [2, 2, 3, 4]
    Expected: 3 (triplets: [2,2,3], [2,3,4], [2,3,4] with second '2')
    """
    # Write your logic here
    pass

def q47(arr):
    """Q47: Longest Mountain in Array. Longest subarray that rises to a peak and falls.
    Input: arr = [2, 1, 4, 7, 3, 2, 5]
    Expected: 5 (subarray is [1, 4, 7, 3, 2])
    """
    # Write your logic here
    pass

def q48(nums):
    """Q48: Longest Subarray of 1's After Deleting One Element.
    Input: nums = [1, 1, 0, 1]
    Expected: 3 (delete 0 to get [1, 1, 1])
    """
    # Write your logic here
    pass

def q49(s):
    """Q49: Partition Labels. Partition string into as many parts as possible so each char appears in at most one part.
    Input: s = "ababcbacadefegdehijhklij"
    Expected: [9, 7, 8]
    """
    # Write your logic here
    pass

def q50(version1, version2):
    """Q50: Compare Version Numbers. Return -1 if v1 < v2, 1 if v1 > v2, 0 otherwise.
    Input: version1 = "1.01", version2 = "1.001"
    Expected: 0
    """
    # Write your logic here
    pass

def q51(nums):
    """Q51: Minimum Swaps to Group All 1's Together in a circular binary array.
    Input: nums = [0, 1, 1, 1, 0, 0, 1, 1, 0]
    Expected: 2
    """
    # Write your logic here
    pass

def q52(chars):
    """Q52: String Compression. Compress chars in-place. Return the new length.
    Input: chars = ["a", "a", "b", "b", "c", "c", "c"]
    Expected: 6 (chars becomes ["a", "2", "b", "2", "c", "3"])
    """
    # Write your logic here
    pass

def q53(nums):
    """Q53: Next Permutation. Rearrange numbers into lexicographically next greater permutation in-place.
    Input: nums = [1, 2, 3]
    Expected: [1, 3, 2]
    """
    # Write your logic here
    pass

def q54(s):
    """Q54: Smallest Subsequence of Distinct Characters (same as Remove Duplicate Letters).
    Input: s = "cbacdcbc"
    Expected: "acdb"
    """
    # Write your logic here
    pass

def q55(s, k):
    """Q55: Longest Substring with At Most K Distinct Characters.
    Input: s = "eceba", k = 2
    Expected: 3 ("ece")
    """
    # Write your logic here
    pass

def q56(s):
    """Q56: Number of Substrings Containing All Three Characters ('a', 'b' and 'c').
    Input: s = "abcabc"
    Expected: 10
    """
    # Write your logic here
    pass

def q57(s1, s2):
    """Q57: Permutation in String. Check if s2 contains a permutation of s1.
    Input: s1 = "ab", s2 = "eidbaooo"
    Expected: True
    """
    # Write your logic here
    pass

def q58(s, p):
    """Q58: Find All Anagrams in a String. Return start indices of p's anagrams in s.
    Input: s = "cbaebabacd", p = "abc"
    Expected: [0, 6]
    """
    # Write your logic here
    pass

def q59(nums):
    """Q59: Maximum Erasure Value. Max sum of subarray with unique elements.
    Input: nums = [4, 2, 4, 5, 6]
    Expected: 17 (subarray: [2, 4, 5, 6])
    """
    # Write your logic here
    pass

def q60(s, t, maxCost):
    """Q60: Get Equal Substrings Within Budget. Max length to change s substring to t substring within maxCost.
    Input: s = "abcd", t = "bcdf", maxCost = 3
    Expected: 3 (change "abc" to "bcd" costs 3)
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
    """Q62: Minimum Window Substring. Smallest window in s containing all characters of t.
    Input: s = "ADOBECODEBANC", t = "ABC"
    Expected: "BANC"
    """
    # Write your logic here
    pass

def q63(nums, k):
    """Q63: Subarrays with K Different Integers. Count subarrays with exactly k unique numbers.
    Input: nums = [1, 2, 1, 2, 3], k = 2
    Expected: 7
    """
    # Write your logic here
    pass

def q64(s, t):
    """Q64: Minimum Window Subsequence. Minimum window in s that contains t as a subsequence.
    Input: s = "abcdebdde", t = "bde"
    Expected: "bcde"
    """
    # Write your logic here
    pass

def q65(nums, k):
    """Q65: Subarray Product Less Than K. Count subarrays where product < k.
    Input: nums = [10, 5, 2, 6], k = 100
    Expected: 8 (subarrays: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6])
    """
    # Write your logic here
    pass

def q66(nums, k):
    """Q66: Shortest Subarray with Sum at Least K. Return min length.
    Input: nums = [2, -1, 2], k = 3
    Expected: 3
    """
    # Write your logic here
    pass

def q67(s, k):
    """Q67: Longest Repeating Character Replacement. Replace at most k characters to make all characters same.
    Input: s = "AABABBA", k = 1
    Expected: 4 (replace middle 'B' to get "AABA" -> len 4, or get "ABBA" -> len 4)
    """
    # Write your logic here
    pass

def q68(nums, k):
    """Q68: Sliding Window Maximum. Return max elements in window size k.
    Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    Expected: [3, 3, 5, 5, 6, 7]
    """
    # Write your logic here
    pass

def q69(nums, x):
    """Q69: Minimum Operations to Reduce X to Zero. Find min operations of removing elements from left/right to sum to x.
    Input: nums = [1, 1, 4, 2, 3], x = 5
    Expected: 2 (remove 2 and 3)
    """
    # Write your logic here
    pass

def q70(matrix, k):
    """Q70: Max Sum of Rectangle No Larger Than K in 2D grid.
    Input: matrix = [[1, 0, 1], [0, -2, 3]], k = 2
    Expected: 2 (rectangle is [[0, 1], [-2, 3]], sum is 2)
    """
    # Write your logic here
    pass

def q71(s1, s2):
    """Q71: Minimum Swaps to Make Strings Equal. (chars can only be 'x' or 'y').
    Input: s1 = "xx", s2 = "yy"
    Expected: 1
    """
    # Write your logic here
    pass

def q72(words, groups):
    """Q72: Expressive Words. Count words that can stretch to match query.
    Input: words = ("hellooo", ["hello", "hi", "helo"])
    Expected: 1
    """
    # Write your logic here
    pass

def q73(s, k):
    """Q73: Valid Palindrome III. Check if s can become palindrome by deleting at most k characters.
    Input: s = "abcdeca", k = 2
    Expected: True (delete 'b' and 'd' to get "aceca")
    """
    # Write your logic here
    pass

def q74(s):
    """Q74: Longest Chunked Palindrome Decomposition.
    Input: s = "ghiabcdefhelloadamhelloabcdefghi"
    Expected: 7 (split: "ghi", "abcdef", "hello", "adam", "hello", "abcdef", "ghi")
    """
    # Write your logic here
    pass

def q75(s, t):
    """Q75: Distinct Subsequences. Count occurrences of t as a subsequence of s.
    Input: s = "rabbbit", t = "rabbit"
    Expected: 3
    """
    # Write your logic here
    pass

def q76(lists):
    """Q76: Merge K Sorted Lists (input is list of lists, output is single sorted list).
    Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    Expected: [1, 1, 2, 3, 4, 4, 5, 6]
    """
    # Write your logic here
    pass

def q77(arr):
    """Q77: Shortest Subarray to be Removed to Make Array Sorted.
    Input: arr = [1, 2, 3, 10, 4, 2, 3, 5]
    Expected: 3 (remove [10, 4, 2] to get [1, 2, 3, 3, 5])
    """
    # Write your logic here
    pass

def q78(start, end):
    """Q78: Swap Adjacent in LR String. Can swap "XL" to "LX" and "RX" to "XR".
    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Expected: True
    """
    # Write your logic here
    pass

def q79(s):
    """Q79: Remove Duplicate Letters. Return lexicographically smallest result.
    Input: s = "bcabc"
    Expected: "abc"
    """
    # Write your logic here
    pass

def q80(nums, numsCompare):
    """Q80: Maximum Score of a Good Subarray. Good subarray has i <= k <= j. Score is min(nums[i..j]) * (j - i + 1).
    Input: nums = ([1, 4, 3, 7, 4, 5], 3) where index 3 is '7'
    Expected: 15 (subarray [3, 7, 4, 5] has min 3, length 5, score 3 * 5 = 15)
    """
    # Write your logic here
    pass

def q81(nums, k):
    """Q81: Subarray Sums Divisible by K. Return count.
    Input: nums = [4, 5, 0, -2, -3, 1], k = 5
    Expected: 7
    """
    # Write your logic here
    pass

def q82(s):
    """Q82: Optimal Partition of String. Min partitions so each char appears at most once in each partition.
    Input: s = "abacaba"
    Expected: 4 (partitions: "ab", "ac", "ab", "a")
    """
    # Write your logic here
    pass

def q83(nums, k):
    """Q83: Count Subarrays With Median K.
    Input: nums = ([3, 2, 1, 4, 5], 4)
    Expected: 3 (subarrays: [4], [4, 5], [1, 4, 5], [2, 1, 4, 5] - median 4)
    """
    # Write your logic here
    pass

def q84(fruits):
    """Q84: Fruit Into Baskets. Max fruits in 2 baskets (each basket contains only 1 type of fruit).
    Input: fruits = [1, 2, 3, 2, 2]
    Expected: 4 (subarray is [2, 3, 2, 2])
    """
    # Write your logic here
    pass

def q85(nums):
    """Q85: Minimum Operations to Make Array Continuous.
    Input: nums = [4, 2, 5, 3]
    Expected: 0 (already continuous)
    """
    # Write your logic here
    pass

def q86(s):
    """Q86: Replace the Substring for Balanced String. Min length of substring to replace to make each char count <= n/4.
    Input: s = "QWER"
    Expected: 0
    """
    # Write your logic here
    pass

def q87(nums, k):
    """Q87: Constrained Subsequence Sum. Max sum of subsequence where index diff <= k.
    Input: nums = [10, 2, -10, 5, 20], k = 2
    Expected: 37 (subsequence [10, 2, 5, 20])
    """
    # Write your logic here
    pass

def q88(nums, limit):
    """Q88: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
    Input: nums = [8, 2, 4, 7], limit = 4
    Expected: 2 (subarrays [2, 4] or [4, 7])
    """
    # Write your logic here
    pass

def q89(nums, k):
    """Q89: Count Subarrays Where Max Element Appears at Least K Times.
    Input: nums = ([1, 3, 2, 3, 3], 2) where max is 3, count >= 2
    Expected: 6
    """
    # Write your logic here
    pass

def q90(s):
    """Q90: Minimum Number of Flips to Make the Binary String Alternating.
    Input: s = "111000"
    Expected: 2 (type-1 shift to "000111", flip to "010101" -> 2 flips)
    """
    # Write your logic here
    pass

def q91(nums, k):
    """Q91: Split Array Largest Sum. Split nums into k subarrays to minimize maximum subarray sum.
    Input: nums = [7, 2, 5, 10, 8], k = 2
    Expected: 18 (split [7,2,5] and [10,8])
    """
    # Write your logic here
    pass

def q92(weights, days):
    """Q92: Capacity To Ship Packages Within D Days. Find min capacity of conveyor belt.
    Input: weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days = 5
    Expected: 15
    """
    # Write your logic here
    pass

def q93(piles, h):
    """Q93: Koko Eating Bananas. Min integer speed k to eat all bananas within h hours.
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
    """Q95: Reverse Nodes in k-Group. Given head (represented as list), reverse in blocks of size k.
    Input: head = [1, 2, 3, 4, 5], k = 2
    Expected: [2, 1, 4, 3, 5]
    """
    # Write your logic here
    pass

def q96(head):
    """Q96: Sort List. Given head (represented as list), sort it.
    Input: head = [4, 2, 1, 3]
    Expected: [1, 2, 3, 4]
    """
    # Write your logic here
    pass

def q97(head, x):
    """Q97: Partition List. Given head (represented as list) and x, partition so elements < x are before >= x.
    Input: head = ([1, 4, 3, 2, 5, 2], 3)
    Expected: [1, 2, 2, 4, 3, 5]
    """
    # Write your logic here
    pass

def q98(head):
    """Q98: Palindrome Linked List. Given head (represented as list), check if palindrome.
    Input: head = [1, 2, 2, 1]
    Expected: True
    """
    # Write your logic here
    pass

def q99(head):
    """Q99: Linked List Cycle II (Floyd's Tortoise and Hare). Given list, return index where cycle starts, or -1.
    Input: head = ([3, 2, 0, -4], 1) where cycle starts at index 1
    Expected: 1
    """
    # Write your logic here
    pass

def q100(nums):
    """Q100: Find the Duplicate Number (Floyd's Cycle Detection on Array). Find duplicate element in-place without modification.
    Input: nums = [1, 3, 4, 2, 2]
    Expected: 2
    """
    # Write your logic here
    pass


# ==================== TEST SUITE DICTIONARY ====================

TESTS = {
    1: {'func': q1, 'args': [[1, 2, 3, 4, 5]], 'expected': [5, 4, 3, 2, 1]},
    2: {'func': q2, 'args': ["hello"], 'expected': "holle"},
    3: {'func': q3, 'args': ["A man, a plan, a canal: Panama"], 'expected': True},
    4: {'func': q4, 'args': [[2, 7, 11, 15], 9], 'expected': [1, 2]},
    5: {'func': q5, 'args': [[1, 1, 2]], 'expected': 2},
    6: {'func': q6, 'args': [[1, 1, 1, 2, 2, 3]], 'expected': 5},
    7: {'func': q7, 'args': [[0, 1, 0, 3, 12]], 'expected': [1, 3, 12, 0, 0]},
    8: {'func': q8, 'args': [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3], 'expected': [1, 2, 2, 3, 5, 6]},
    9: {'func': q9, 'args': [[-4, -1, 0, 3, 10]], 'expected': [0, 1, 9, 16, 100]},
    10: {'func': q10, 'args': [[1, 2, 2, 3], [2, 2, 3, 4]], 'expected': [2, 3]},
    11: {'func': q11, 'args': [[1, 2, 5], [2, 3, 5, 6]], 'expected': [1, 2, 3, 5, 6]},
    12: {'func': q12, 'args': ["abca"], 'expected': True},
    13: {'func': q13, 'args': ["Let's take LeetCode contest"], 'expected': "s'teL ekat edoCteeL tsetnoc"},
    14: {'func': q14, 'args': [[1, 5, 10], [3, 8, 15]], 'expected': 2},
    15: {'func': q15, 'args': ["abc", "ahbgdc"], 'expected': True},
    16: {'func': q16, 'args': [[1, 5, 10, 15, 20], 5], 'expected': True},
    17: {'func': q17, 'args': [[3, 1, 2, 4]], 'expected': [2, 4, 3, 1]},
    18: {'func': q18, 'args': [[4, 2, 5, 7]], 'expected': [4, 5, 2, 7]},
    19: {'func': q19, 'args': [[9, 12, 5, 10, 14, 3, 10], 10], 'expected': [9, 5, 3, 10, 10, 12, 14]},
    20: {'func': q20, 'args': ["ab#c", "ad#c"], 'expected': True},
    21: {'func': q21, 'args': ["sadbutsad", "sad"], 'expected': 0},
    22: {'func': q22, 'args': ["babad"], 'expected': "bab"},
    23: {'func': q23, 'args': ["caac"], 'expected': 0},
    24: {'func': q24, 'args': [[3, 1, 4, 1, 5], 2], 'expected': 2},
    25: {'func': q25, 'args': [[1, 2, 3], [1, 1]], 'expected': 1},
    
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
            result = func(*args) if isinstance(args, list) else func(args)
            print(f"Your Output: {result}")
        
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
