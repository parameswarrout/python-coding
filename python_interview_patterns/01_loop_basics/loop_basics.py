import sys
sys.stdout.reconfigure(encoding='utf-8')
"""
Loop Basics - Practice One Question at a Time
=============================================
HOW TO USE:
* By default, it runs the highest-numbered question you have written code for.
* The moment you write code inside the next question, the runner automatically switches to it!
"""

# ==================== CHANGE THIS NUMBER IF NEEDED ====================
QUESTION_NUMBER = None  # <-- Set to None to auto-detect your active question
# ======================================================================


# ==================== ALL 100 QUESTIONS ====================

def q1(n: int) -> list:
    """Q1: Generate list of numbers from 1 to N.
    Input: n = 5
    Expected: [1, 2, 3, 4, 5]
    """
    res = []
    for i in range(1, n + 1):
        res.append(i)
    return res

def q2(n: int) -> int:
    """Q2: Calculate sum of numbers from 1 to N.
    Input: n = 5
    Expected: 15
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def q3(n: int) -> int:
    """Q3: Calculate factorial of N.
    Input: n = 5
    Expected: 120
    """
    # Write your logic here
    pass

def q4(n: int) -> int:
    """Q4: Count the number of digits in an integer N.
    Input: n = 12345
    Expected: 5
    """
    # Write your logic here
    pass

def q5(n: int) -> int:
    """Q5: Reverse the digits of an integer N.
    Input: n = 12345
    Expected: 54321
    """
    # Write your logic here
    pass

def q6(n: int) -> bool:
    """Q6: Check if a number N is prime.
    Input: n = 7
    Expected: True
    """
    # Write your logic here
    pass

def q7(n: int) -> int:
    """Q7: Find the Nth Fibonacci number (0-indexed, F(0)=0, F(1)=1, F(2)=1, F(3)=2...).
    Input: n = 6
    Expected: 8
    """
    # Write your logic here
    pass

def q8(arr: list) -> int:
    """Q8: Find the maximum element in an array using a loop.
    Input: arr = [3, 1, 4, 1, 5, 9, 2]
    Expected: 9
    """
    # Write your logic here
    pass

def q9(arr: list) -> int:
    """Q9: Find the minimum element in an array using a loop.
    Input: arr = [3, 1, 4, 1, 5, 9, 2]
    Expected: 1
    """
    # Write your logic here
    pass

def q10(arr: list) -> int:
    """Q10: Calculate the sum of all elements in an array.
    Input: arr = [1, 2, 3, 4, 5]
    Expected: 15
    """
    # Write your logic here
    pass

def q11(n: int) -> list:
    """Q11: Generate a list of all even numbers up to N.
    Input: n = 10
    Expected: [2, 4, 6, 8, 10]
    """
    # Write your logic here
    pass

def q12(n: int) -> list:
    """Q12: Generate a list of all odd numbers up to N.
    Input: n = 9
    Expected: [1, 3, 5, 7, 9]
    """
    # Write your logic here
    pass

def q13(n: int) -> int:
    """Q13: Calculate the sum of all odd numbers up to N.
    Input: n = 9
    Expected: 25
    """
    # Write your logic here
    pass

def q14(n: int) -> int:
    """Q14: Calculate the sum of all even numbers up to N.
    Input: n = 10
    Expected: 30
    """
    # Write your logic here
    pass

def q15(n: int) -> int:
    """Q15: Count the number of divisors of a number N.
    Input: n = 12
    Expected: 6 (1, 2, 3, 4, 6, 12)
    """
    # Write your logic here
    pass

def q16(n: int) -> list:
    """Q16: Find all divisors of a number N (return as a sorted list).
    Input: n = 12
    Expected: [1, 2, 3, 4, 6, 12]
    """
    # Write your logic here
    pass

def q17(n: int) -> bool:
    """Q17: Check if N is a perfect number (sum of proper divisors equals N).
    Input: n = 28
    Expected: True
    """
    # Write your logic here
    pass

def q18(n: int) -> bool:
    """Q18: Check if N is an Armstrong number (sum of cube of digits equals N for 3-digit numbers).
    Input: n = 153
    Expected: True
    """
    # Write your logic here
    pass

def q19(n: int) -> list:
    """Q19: Generate the multiplication table of N (first 10 multiples).
    Input: n = 5
    Expected: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    """
    # Write your logic here
    pass

def q20(a: int, b: int) -> int:
    """Q20: Find the Greatest Common Divisor (GCD) of a and b using a loop.
    Input: a = 12, b = 18
    Expected: 6
    """
    # Write your logic here
    pass

def q21(a: int, b: int) -> int:
    """Q21: Find the Least Common Multiple (LCM) of a and b using a loop.
    Input: a = 12, b = 18
    Expected: 36
    """
    # Write your logic here
    pass

def q22(n: int) -> list:
    """Q22: Generate a right-angled triangle pattern of stars of height N.
    Input: n = 3
    Expected: ['*', '**', '***']
    """
    # Write your logic here
    pass

def q23(n: int) -> list:
    """Q23: Generate an inverted right-angled triangle pattern of stars of height N.
    Input: n = 3
    Expected: ['***', '**', '*']
    """
    # Write your logic here
    pass

def q24(n: int) -> list:
    """Q24: Generate a pyramid pattern of stars of height N.
    Input: n = 3
    Expected: ['  *  ', ' *** ', '*****']
    """
    # Write your logic here
    pass

def q25(n: int) -> list:
    """Q25: Generate a diamond pattern of stars of height N.
    Input: n = 3
    Expected: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    """
    # Write your logic here
    pass


# --- INTERMEDIATE LEVEL (Q26 - Q60) ---

def q26(arr):
    """Q26: Count occurrences of a target element in an array using a loop.
    Input: arr = ([1, 2, 3, 2, 4, 2], 2)
    Expected: 3
    """
    # Write your logic here
    pass

def q27(arr):
    """Q27: Check if an array is sorted in non-decreasing order using a loop.
    Input: arr = [1, 2, 3, 5, 4]
    Expected: False
    """
    # Write your logic here
    pass

def q28(arr):
    """Q28: Find the second largest element in an array using a loop.
    Input: arr = [12, 35, 1, 10, 34, 1]
    Expected: 34
    """
    # Write your logic here
    pass

def q29(arr):
    """Q29: Find the second smallest element in an array using a loop.
    Input: arr = [12, 35, 1, 10, 34, 1]
    Expected: 10
    """
    # Write your logic here
    pass

def q30(arr):
    """Q30: Count the number of positive and negative numbers in an array.
    Input: arr = [1, -2, 3, -4, 5]
    Expected: [3, 2] (3 positive, 2 negative)
    """
    # Write your logic here
    pass

def q31(arr):
    """Q31: Reverse an array in place using a loop.
    Input: arr = [1, 2, 3, 4, 5]
    Expected: [5, 4, 3, 2, 1]
    """
    # Write your logic here
    pass

def q32(arr):
    """Q32: Left rotate an array by one position using a loop.
    Input: arr = [1, 2, 3, 4, 5]
    Expected: [2, 3, 4, 5, 1]
    """
    # Write your logic here
    pass

def q33(arr_d):
    """Q33: Left rotate an array by D positions using a loop.
    Input: arr_d = ([1, 2, 3, 4, 5], 2)
    Expected: [3, 4, 5, 1, 2]
    """
    # Write your logic here
    pass

def q34(arr):
    """Q34: Move all zeros in an array to the end using a loop.
    Input: arr = [0, 1, 0, 3, 12]
    Expected: [1, 3, 12, 0, 0]
    """
    # Write your logic here
    pass

def q35(arr):
    """Q35: Remove duplicate elements from a sorted array using a loop.
    Input: arr = [1, 1, 2, 2, 3]
    Expected: [1, 2, 3]
    """
    # Write your logic here
    pass

def q36(arr):
    """Q36: Remove all occurrences of a target element from an array.
    Input: arr = ([3, 2, 2, 3], 3)
    Expected: [2, 2]
    """
    # Write your logic here
    pass

def q37(arr):
    """Q37: Find the first repeating element in an array using a loop.
    Input: arr = [10, 5, 3, 4, 3, 5, 6]
    Expected: 5
    """
    # Write your logic here
    pass

def q38(arr):
    """Q38: Find the first non-repeating element in an array using a loop.
    Input: arr = [9, 4, 9, 6, 7, 4]
    Expected: 6
    """
    # Write your logic here
    pass

def q39(arr):
    """Q39: Find the missing number in an array of size N-1 containing numbers from 1 to N.
    Input: arr = [1, 2, 4, 6, 3, 7, 8]
    Expected: 5
    """
    # Write your logic here
    pass

def q40(arr):
    """Q40: Check if there exists a pair in the array whose sum equals a target.
    Input: arr = ([1, 4, 45, 6, 10, 8], 16)
    Expected: True
    """
    # Write your logic here
    pass

def q41(arr):
    """Q41: Find all pairs in the array whose sum equals a target.
    Input: arr = ([1, 5, 7, -1, 5], 6)
    Expected: [[1, 5], [1, 5], [7, -1]]
    """
    # Write your logic here
    pass

def q42(arr):
    """Q42: Find the element that appears once in an array where all other elements appear twice.
    Input: arr = [2, 3, 5, 4, 5, 3, 4]
    Expected: 2
    """
    # Write your logic here
    pass

def q43(arr):
    """Q43: Count the number of subarrays with a sum of 0 using a loop.
    Input: arr = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    Expected: 4
    """
    # Write your logic here
    pass

def q44(arr):
    """Q44: Find the maximum sum of a contiguous subarray using a loop.
    Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    Expected: 6
    """
    # Write your logic here
    pass

def q45(arr):
    """Q45: Find the maximum product of a contiguous subarray using a loop.
    Input: arr = [2, 3, -2, 4]
    Expected: 6
    """
    # Write your logic here
    pass

def q46(s):
    """Q46: Check if a string is a palindrome using a loop.
    Input: s = "radar"
    Expected: True
    """
    # Write your logic here
    pass

def q47(s):
    """Q47: Reverse a string using a loop.
    Input: s = "hello"
    Expected: "olleh"
    """
    # Write your logic here
    pass

def q48(s):
    """Q48: Count the number of vowels and consonants in a string.
    Input: s = "leetcode"
    Expected: [4, 4] (4 vowels, 4 consonants)
    """
    # Write your logic here
    pass

def q49(s):
    """Q49: Convert a string to lowercase using a loop without built-in lower().
    Input: s = "HEllO"
    Expected: "hello"
    """
    # Write your logic here
    pass

def q50(s):
    """Q50: Convert a string to uppercase using a loop without built-in upper().
    Input: s = "HEllO"
    Expected: "HELLO"
    """
    # Write your logic here
    pass

def q51(n):
    """Q51: Check if N is a palindrome number.
    Input: n = 12321
    Expected: True
    """
    # Write your logic here
    pass

def q52(n):
    """Q52: Check if N is a Harshad (or Niven) number (divisible by the sum of its digits).
    Input: n = 18
    Expected: True
    """
    # Write your logic here
    pass

def q53(n):
    """Q53: Check if N is an Abundant number (sum of proper divisors is greater than N).
    Input: n = 12
    Expected: True
    """
    # Write your logic here
    pass

def q54(n):
    """Q54: Check if N is a Deficient number (sum of proper divisors is less than N).
    Input: n = 15
    Expected: True
    """
    # Write your logic here
    pass

def q55(n):
    """Q55: Generate first N Prime numbers.
    Input: n = 5
    Expected: [2, 3, 5, 7, 11]
    """
    # Write your logic here
    pass

def q56(limit):
    """Q56: Generate all prime numbers up to a given limit using a loop.
    Input: limit = 20
    Expected: [2, 3, 5, 7, 11, 13, 17, 19]
    """
    # Write your logic here
    pass

def q57(n):
    """Q57: Print all prime factors of N.
    Input: n = 315
    Expected: [3, 5, 7]
    """
    # Write your logic here
    pass

def q58(n):
    """Q58: Check if N is a Strong number (sum of factorial of digits equals N).
    Input: n = 145
    Expected: True
    """
    # Write your logic here
    pass

def q59(n):
    """Q59: Convert Binary to Decimal using a loop.
    Input: n = "1010"
    Expected: 10
    """
    # Write your logic here
    pass

def q60(n):
    """Q60: Convert Decimal to Binary using a loop.
    Input: n = 10
    Expected: "1010"
    """
    # Write your logic here
    pass


# --- ADVANCED LEVEL (Q61 - Q100) ---

def q61(matrix):
    """Q61: Transpose of a 2D matrix using loops.
    Input: matrix = [[1, 2], [3, 4]]
    Expected: [[1, 3], [2, 4]]
    """
    # Write your logic here
    pass

def q62(matrices):
    """Q62: Multiply two 2D matrices using nested loops.
    Input: matrices = ([[1, 2], [3, 4]], [[2, 0], [1, 2]])
    Expected: [[4, 4], [10, 8]]
    """
    # Write your logic here
    pass

def q63(matrix):
    """Q63: Rotate a 2D matrix 90 degrees clockwise using loops.
    Input: matrix = [[1, 2], [3, 4]]
    Expected: [[3, 1], [4, 2]]
    """
    # Write your logic here
    pass

def q64(matrix):
    """Q64: Find print elements of a matrix in spiral order.
    Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    # Write your logic here
    pass

def q65(arr):
    """Q65: Sort an array using Bubble Sort algorithm with loops.
    Input: arr = [5, 1, 4, 2, 8]
    Expected: [1, 2, 4, 5, 8]
    """
    # Write your logic here
    pass

def q66(arr):
    """Q66: Sort an array using Selection Sort algorithm with loops.
    Input: arr = [5, 1, 4, 2, 8]
    Expected: [1, 2, 4, 5, 8]
    """
    # Write your logic here
    pass

def q67(arr):
    """Q67: Sort an array using Insertion Sort algorithm with loops.
    Input: arr = [5, 1, 4, 2, 8]
    Expected: [1, 2, 4, 5, 8]
    """
    # Write your logic here
    pass

def q68(arr):
    """Q68: Binary Search implementation using a loop.
    Input: arr = ([1, 2, 3, 4, 5, 6], 4)
    Expected: 3
    """
    # Write your logic here
    pass

def q69(nums):
    """Q69: Find the majority element (appears more than N/2 times) using a loop (Boyer-Moore voting algorithm).
    Input: nums = [2, 2, 1, 1, 1, 2, 2]
    Expected: 2
    """
    # Write your logic here
    pass

def q70(nums):
    """Q70: Find the peak element in an array (greater than its neighbors) using a loop.
    Input: nums = [1, 2, 3, 1]
    Expected: 2 (value 3 is at index 2)
    """
    # Write your logic here
    pass

def q71(arr):
    """Q71: Find the equilibrium index of an array (left sum equals right sum).
    Input: arr = [-7, 1, 5, 2, -4, 3, 0]
    Expected: 3
    """
    # Write your logic here
    pass

def q72(arr):
    """Q72: Find the index where sum of left and right elements are equal (Pivot index).
    Input: arr = [1, 7, 3, 6, 5, 6]
    Expected: 3
    """
    # Write your logic here
    pass

def q73(arr):
    """Q73: Partition an array into two subarrays with equal sum using a loop.
    Input: arr = [1, 2, 3, 4, 5, 5]
    Expected: True
    """
    # Write your logic here
    pass

def q74(arr):
    """Q74: Find if there exists a triplet in the array whose sum equals a target.
    Input: arr = ([12, 3, 4, 1, 6, 9], 24)
    Expected: True
    """
    # Write your logic here
    pass

def q75(arr):
    """Q75: Count the number of triplets in the array whose sum is less than a target.
    Input: arr = ([-2, 0, 1, 3], 2)
    Expected: 2
    """
    # Write your logic here
    pass

def q76(n):
    """Q76: Find the square root of a number N to nearest integer using a loop (Binary Search style).
    Input: n = 8
    Expected: 2
    """
    # Write your logic here
    pass

def q77(arr):
    """Q77: Find the maximum sum of K consecutive elements in an array (Sliding Window loop).
    Input: arr = ([100, 200, 300, 400], 2)
    Expected: 700
    """
    # Write your logic here
    pass

def q78(arr):
    """Q78: Find the longest subarray containing all 1s after deleting one 0.
    Input: arr = [1, 1, 0, 1, 1, 1]
    Expected: 5
    """
    # Write your logic here
    pass

def q79(arr):
    """Q79: Count the number of subarrays having product less than K.
    Input: arr = ([10, 5, 2, 6], 100)
    Expected: 8
    """
    # Write your logic here
    pass

def q80(arr):
    """Q80: Find the longest substring without repeating characters using a loop.
    Input: arr = "abcabcbb"
    Expected: 3
    """
    # Write your logic here
    pass

def q81(n):
    """Q81: Check if N is a Happy number.
    Input: n = 19
    Expected: True
    """
    # Write your logic here
    pass

def q82(n):
    """Q82: Check if N is a Magic number (recursive sum of digits is 1).
    Input: n = 1729
    Expected: True
    """
    # Write your logic here
    pass

def q83(n):
    """Q83: Check if N is a Neon number (sum of digits of its square is equal to N).
    Input: n = 9
    Expected: True
    """
    # Write your logic here
    pass

def q84(n):
    """Q84: Check if N is a Spy number (sum of digits is equal to product of digits).
    Input: n = 1124
    Expected: True
    """
    # Write your logic here
    pass

def q85(n):
    """Q85: Check if N is an Automorphic number (square of the number ends in the number itself).
    Input: n = 25
    Expected: True
    """
    # Write your logic here
    pass

def q86(n):
    """Q86: Check if N is a Kaprekar number.
    Input: n = 45
    Expected: True
    """
    # Write your logic here
    pass

def q87(n):
    """Q87: Check if N is a Disarium number (sum of its digits powered with their respective positions is N).
    Input: n = 89
    Expected: True
    """
    # Write your logic here
    pass

def q88(n):
    """Q88: Check if N is a Keith number.
    Input: n = 197
    Expected: True
    """
    # Write your logic here
    pass

def q89(n):
    """Q89: Check if N is a Smith number.
    Input: n = 4937775
    Expected: True
    """
    # Write your logic here
    pass

def q90(n):
    """Q90: Check if N is a Narcissistic number (Armstrong style for any power).
    Input: n = 1634
    Expected: True
    """
    # Write your logic here
    pass

def q91(arr):
    """Q91: Find the count of subsegment sums divisible by K using a loop.
    Input: arr = ([4, 5, 0, -2, -3, 1], 5)
    Expected: 7
    """
    # Write your logic here
    pass

def q92(n):
    """Q92: Find the sum of all proper divisors of N.
    Input: n = 12
    Expected: 16
    """
    # Write your logic here
    pass

def q93(n):
    """Q93: Find all abundant numbers up to N.
    Input: n = 20
    Expected: [12, 18, 20]
    """
    # Write your logic here
    pass

def q94(n):
    """Q94: Find all perfect numbers up to N.
    Input: n = 30
    Expected: [6, 28]
    """
    # Write your logic here
    pass

def q95(arr):
    """Q95: Find the maximum length of a subarray of even numbers.
    Input: arr = [1, 2, 4, 3, 6, 8, 10, 5]
    Expected: 4
    """
    # Write your logic here
    pass

def q96(arr):
    """Q96: Find the maximum length of a subarray of odd numbers.
    Input: arr = [1, 2, 4, 3, 6, 8, 10, 5]
    Expected: 1
    """
    # Write your logic here
    pass

def q97(s):
    """Q97: Find the first duplicate character in a string using loops.
    Input: s = "geeksforgeeks"
    Expected: "e"
    """
    # Write your logic here
    pass

def q98(s):
    """Q98: Find the first non-duplicate character in a string using loops.
    Input: s = "geeksforgeeks"
    Expected: "f"
    """
    # Write your logic here
    pass

def q99(n):
    """Q99: Generate Pascal's Triangle up to N rows using loops.
    Input: n = 4
    Expected: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    # Write your logic here
    pass

def q100(n):
    """Q100: Print Fibonacci sequence up to N elements.
    Input: n = 5
    Expected: [0, 1, 1, 2, 3]
    """
    # Write your logic here
    pass


# ==================== TEST SUITE DICTIONARY ====================

TESTS = {
    1: {'func': q1, 'args': [5], 'expected': [1, 2, 3, 4, 5]},
    2: {'func': q2, 'args': [5], 'expected': 15},
    3: {'func': q3, 'args': [5], 'expected': 120},
    4: {'func': q4, 'args': [12345], 'expected': 5},
    5: {'func': q5, 'args': [12345], 'expected': 54321},
    6: {'func': q6, 'args': [7], 'expected': True},
    7: {'func': q7, 'args': [6], 'expected': 8},
    8: {'func': q8, 'args': [[3, 1, 4, 1, 5, 9, 2]], 'expected': 9},
    9: {'func': q9, 'args': [[3, 1, 4, 1, 5, 9, 2]], 'expected': 1},
    10: {'func': q10, 'args': [[1, 2, 3, 4, 5]], 'expected': 15},
    11: {'func': q11, 'args': [10], 'expected': [2, 4, 6, 8, 10]},
    12: {'func': q12, 'args': [9], 'expected': [1, 3, 5, 7, 9]},
    13: {'func': q13, 'args': [9], 'expected': 25},
    14: {'func': q14, 'args': [10], 'expected': 30},
    15: {'func': q15, 'args': [12], 'expected': 6},
    16: {'func': q16, 'args': [12], 'expected': [1, 2, 3, 4, 6, 12]},
    17: {'func': q17, 'args': [28], 'expected': True},
    18: {'func': q18, 'args': [153], 'expected': True},
    19: {'func': q19, 'args': [5], 'expected': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]},
    20: {'func': q20, 'args': [12, 18], 'expected': 6},
    21: {'func': q21, 'args': [12, 18], 'expected': 36},
    22: {'func': q22, 'args': [3], 'expected': ['*', '**', '***']},
    23: {'func': q23, 'args': [3], 'expected': ['***', '**', '*']},
    24: {'func': q24, 'args': [3], 'expected': ['  *  ', ' *** ', '*****']},
    25: {'func': q25, 'args': [3], 'expected': ['  *  ', ' *** ', '*****', ' *** ', '  *  ']},
    26: {'func': q26, 'args': [[1, 2, 3, 2, 4, 2], 2], 'expected': 3},
    27: {'func': q27, 'args': [[1, 2, 3, 5, 4]], 'expected': False},
    28: {'func': q28, 'args': [[12, 35, 1, 10, 34, 1]], 'expected': 34},
    29: {'func': q29, 'args': [[12, 35, 1, 10, 34, 1]], 'expected': 10},
    30: {'func': q30, 'args': [[1, -2, 3, -4, 5]], 'expected': [3, 2]},
    31: {'func': q31, 'args': [[1, 2, 3, 4, 5]], 'expected': [5, 4, 3, 2, 1]},
    32: {'func': q32, 'args': [[1, 2, 3, 4, 5]], 'expected': [2, 3, 4, 5, 1]},
    33: {'func': q33, 'args': [[1, 2, 3, 4, 5], 2], 'expected': [3, 4, 5, 1, 2]},
    34: {'func': q34, 'args': [[0, 1, 0, 3, 12]], 'expected': [1, 3, 12, 0, 0]},
    35: {'func': q35, 'args': [[1, 1, 2, 2, 3]], 'expected': [1, 2, 3]},
    36: {'func': q36, 'args': [[3, 2, 2, 3], 3], 'expected': [2, 2]},
    37: {'func': q37, 'args': [[10, 5, 3, 4, 3, 5, 6]], 'expected': 5},
    38: {'func': q38, 'args': [[9, 4, 9, 6, 7, 4]], 'expected': 6},
    39: {'func': q39, 'args': [[1, 2, 4, 6, 3, 7, 8]], 'expected': 5},
    40: {'func': q40, 'args': [[1, 4, 45, 6, 10, 8], 16], 'expected': True},
    41: {'func': q41, 'args': [[1, 5, 7, -1, 5], 6], 'expected': [[1, 5], [1, 5], [7, -1]]},
    42: {'func': q42, 'args': [[2, 3, 5, 4, 5, 3, 4]], 'expected': 2},
    43: {'func': q43, 'args': [[6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]], 'expected': 4},
    44: {'func': q44, 'args': [[-2, 1, -3, 4, -1, 2, 1, -5, 4]], 'expected': 6},
    45: {'func': q45, 'args': [[2, 3, -2, 4]], 'expected': 6},
    46: {'func': q46, 'args': ["radar"], 'expected': True},
    47: {'func': q47, 'args': ["hello"], 'expected': "olleh"},
    48: {'func': q48, 'args': ["leetcode"], 'expected': [4, 4]},
    49: {'func': q49, 'args': ["HEllO"], 'expected': "hello"},
    50: {'func': q50, 'args': ["HEllO"], 'expected': "HELLO"},
    51: {'func': q51, 'args': [12321], 'expected': True},
    52: {'func': q52, 'args': [18], 'expected': True},
    53: {'func': q53, 'args': [12], 'expected': True},
    54: {'func': q54, 'args': [15], 'expected': True},
    55: {'func': q55, 'args': [5], 'expected': [2, 3, 5, 7, 11]},
    56: {'func': q56, 'args': [20], 'expected': [2, 3, 5, 7, 11, 13, 17, 19]},
    57: {'func': q57, 'args': [315], 'expected': [3, 5, 7]},
    58: {'func': q58, 'args': [145], 'expected': True},
    59: {'func': q59, 'args': ["1010"], 'expected': 10},
    60: {'func': q60, 'args': [10], 'expected': "1010"},
    61: {'func': q61, 'args': [[[1, 2], [3, 4]]], 'expected': [[1, 3], [2, 4]]},
    62: {'func': q62, 'args': [[[1, 2], [3, 4]], [[2, 0], [1, 2]]], 'expected': [[4, 4], [10, 8]]},
    63: {'func': q63, 'args': [[[1, 2], [3, 4]]], 'expected': [[3, 1], [4, 2]]},
    64: {'func': q64, 'args': [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], 'expected': [1, 2, 3, 6, 9, 8, 7, 4, 5]},
    65: {'func': q65, 'args': [[5, 1, 4, 2, 8]], 'expected': [1, 2, 4, 5, 8]},
    66: {'func': q66, 'args': [[5, 1, 4, 2, 8]], 'expected': [1, 2, 4, 5, 8]},
    67: {'func': q67, 'args': [[5, 1, 4, 2, 8]], 'expected': [1, 2, 4, 5, 8]},
    68: {'func': q68, 'args': [[1, 2, 3, 4, 5, 6], 4], 'expected': 3},
    69: {'func': q69, 'args': [[2, 2, 1, 1, 1, 2, 2]], 'expected': 2},
    70: {'func': q70, 'args': [[1, 2, 3, 1]], 'expected': 2},
    71: {'func': q71, 'args': [[-7, 1, 5, 2, -4, 3, 0]], 'expected': 3},
    72: {'func': q72, 'args': [[1, 7, 3, 6, 5, 6]], 'expected': 3},
    73: {'func': q73, 'args': [[1, 2, 3, 4, 5, 5]], 'expected': True},
    74: {'func': q74, 'args': [[12, 3, 4, 1, 6, 9], 24], 'expected': True},
    75: {'func': q75, 'args': [[-2, 0, 1, 3], 2], 'expected': 2},
    76: {'func': q76, 'args': [8], 'expected': 2},
    77: {'func': q77, 'args': [[100, 200, 300, 400], 2], 'expected': 700},
    78: {'func': q78, 'args': [[1, 1, 0, 1, 1, 1]], 'expected': 5},
    79: {'func': q79, 'args': [[10, 5, 2, 6], 100], 'expected': 8},
    80: {'func': q80, 'args': ["abcabcbb"], 'expected': 3},
    81: {'func': q81, 'args': [19], 'expected': True},
    82: {'func': q82, 'args': [1729], 'expected': True},
    83: {'func': q83, 'args': [9], 'expected': True},
    84: {'func': q84, 'args': [1124], 'expected': True},
    85: {'func': q85, 'args': [25], 'expected': True},
    86: {'func': q86, 'args': [45], 'expected': True},
    87: {'func': q87, 'args': [89], 'expected': True},
    88: {'func': q88, 'args': [197], 'expected': True},
    89: {'func': q89, 'args': [4937775], 'expected': True},
    90: {'func': q90, 'args': [1634], 'expected': True},
    91: {'func': q91, 'args': [[4, 5, 0, -2, -3, 1], 5], 'expected': 7},
    92: {'func': q92, 'args': [12], 'expected': 16},
    93: {'func': q93, 'args': [20], 'expected': [12, 18, 20]},
    94: {'func': q94, 'args': [30], 'expected': [6, 28]},
    95: {'func': q95, 'args': [[1, 2, 4, 3, 6, 8, 10, 5]], 'expected': 4},
    96: {'func': q96, 'args': [[1, 2, 4, 3, 6, 8, 10, 5]], 'expected': 1},
    97: {'func': q97, 'args': ["geeksforgeeks"], 'expected': "e"},
    98: {'func': q98, 'args': ["geeksforgeeks"], 'expected': "f"},
    99: {'func': q99, 'args': [4], 'expected': [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]},
    100: {'func': q100, 'args': [5], 'expected': [0, 1, 1, 2, 3]},
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
