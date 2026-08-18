import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
"""
Data Structure Design - Practice One Question at a Time
======================================================
HOW TO USE:
1. Change QUESTION_NUMBER below to the question you want to solve (1 to 25)
2. Write your logic in the corresponding function (q1 to q25)
3. Run the code - it will test only that question
"""

# ==================== CHANGE THIS NUMBER ====================
QUESTION_NUMBER = None  # <-- Change this to solve different questions
# ============================================================


# ==================== ALL 25 QUESTIONS ====================

def q1(operations: list, val_args: list) -> list:
    """Q1: LRU Cache (LC 146). Implement Least Recently Used (LRU) cache with get and put in O(1).
    Input: operations = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
           val_args   = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    Expected Output: [None, None, None, 1, None, -1, None, -1, 3, 4]
    """
    class DNode:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    class LRUCache:
        def __init__(self, capacity: int):
            self.cap = capacity
            self.cache = {}
            self.head = DNode()
            self.tail = DNode()
            self.head.next = self.tail
            self.tail.prev = self.head

        def _remove(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev

        def _add_to_front(self, node):
            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node

        def get(self, key: int) -> int:
            if key not in self.cache:
                return -1
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value

        def put(self, key: int, value: int) -> None:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self._remove(node)
                self._add_to_front(node)
            else:
                if len(self.cache) >= self.cap:
                    lru = self.tail.prev
                    self._remove(lru)
                    del self.cache[lru.key]
                new_node = DNode(key, value)
                self.cache[key] = new_node
                self._add_to_front(new_node)

    obj = None
    res = []
    for op, arg in zip(operations, val_args):
        if op == "LRUCache":
            obj = LRUCache(arg[0])
            res.append(None)
        elif op == "put":
            obj.put(arg[0], arg[1])
            res.append(None)
        elif op == "get":
            res.append(obj.get(arg[0]))
    return res


def q2(operations: list, val_args: list) -> list:
    """Q2: Min Stack (LC 155). Stack supporting push, pop, top, and retrieving min element in O(1).
    Input: operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
           val_args   = [[], [-2], [0], [-3], [], [], [], []]
    Expected Output: [None, None, None, None, -3, None, 0, -2]
    """
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            if not self.min_stack or val <= self.min_stack[-1]:
                self.min_stack.append(val)

        def pop(self) -> None:
            if self.stack:
                val = self.stack.pop()
                if val == self.min_stack[-1]:
                    self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]

    obj = None
    res = []
    for op, arg in zip(operations, val_args):
        if op == "MinStack":
            obj = MinStack()
            res.append(None)
        elif op == "push":
            obj.push(arg[0])
            res.append(None)
        elif op == "pop":
            obj.pop()
            res.append(None)
        elif op == "top":
            res.append(obj.top())
        elif op == "getMin":
            res.append(obj.getMin())
    return res


def q3(operations: list, val_args: list) -> list:
    """Q3: Implement Queue using Stacks (LC 232).
    Input: operations = ["MyQueue", "push", "push", "peek", "pop", "empty"]
           val_args   = [[], [1], [2], [], [], []]
    Expected: [None, None, None, 1, 1, False]
    """
    # Write your logic here
    pass


def q4(operations: list, val_args: list) -> list:
    """Q4: Time Based Key-Value Store (LC 981).
    Input: operations = ["TimeMap", "set", "get", "get", "set", "get", "get"]
           val_args   = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Expected: [None, None, "bar", "bar", None, "bar2", "bar2"]
    """
    # Write your logic here
    pass


def q5(operations: list, val_args: list) -> list:
    """Q5: Insert Delete GetRandom O(1) (LC 380).
    Input: operations = ["RandomizedSet", "insert", "remove", "insert", "remove", "insert"]
           val_args   = [[], [1], [2], [2], [1], [2]]
    Expected: [None, True, False, True, True, False]
    """
    # Write your logic here
    pass


def q6(operations: list, val_args: list) -> list:
    """Q6: Design Underground System (LC 1396).
    Input: operations = ["UndergroundSystem", "checkIn", "checkIn", "checkOut", "checkOut", "getAverageTime"]
           val_args   = [[], [45, "Leyton", 3], [32, "Paradise", 8], [45, "Waterloo", 15], [32, "Cambridge", 22], ["Paradise", "Cambridge"]]
    Expected: [None, None, None, None, None, 14.0]
    """
    # Write your logic here
    pass


def q7(operations: list, val_args: list) -> list:
    """Q7: Moving Average from Data Stream (LC 346).
    Input: operations = ["MovingAverage", "next", "next", "next", "next"]
           val_args   = [[3], [1], [10], [3], [5]]
    Expected: [None, 1.0, 5.5, 4.666666666666667, 6.0]
    """
    # Write your logic here
    pass


def q8(operations: list, val_args: list) -> list:
    """Q8: Design Browser History (LC 1472).
    Input: operations = ["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"]
           val_args   = [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]
    Expected: [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]
    """
    # Write your logic here
    pass


def q9(operations: list, val_args: list) -> list:
    """Q9: Snapshot Array (LC 1146).
    Input: operations = ["SnapshotArray", "set", "snap", "set", "get"]
           val_args   = [[3], [0, 5], [], [0, 6], [0, 0]]
    Expected: [None, None, 0, None, 5]
    """
    # Write your logic here
    pass


def q10(operations: list, val_args: list) -> list:
    """Q10: Design Circular Queue (LC 622).
    Input: operations = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
           val_args   = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    Expected: [None, True, True, True, False, 3, True, True, True, 4]
    """
    # Write your logic here
    pass


def q11(operations: list, val_args: list) -> list:
    """Q11: Find Median from Data Stream (LC 295 / MedianFinder using two heaps).
    Input: operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
           val_args   = [[], [1], [2], [], [3], []]
    Expected: [None, None, None, 1.5, None, 2.0]
    """
    # Write your logic here
    pass


def q12(operations: list, val_args: list) -> list:
    """Q12: Range Sum Query 2D - Immutable (LC 304 2D Prefix Sum design).
    Input: operations = ["NumMatrix", "sumRegion", "sumRegion"]
           val_args   = [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2]]
    Expected: [None, 8, 11]
    """
    # Write your logic here
    pass


def q13(operations: list, val_args: list) -> list:
    """Q13: Seat Reservation Manager (LC 1845 using Min-Heap).
    Input: operations = ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
           val_args   = [[5], [], [], [2], [], [], [], [], [5]]
    Expected: [None, 1, 2, None, 2, 3, 4, 5, None]
    """
    # Write your logic here
    pass


def q14(operations: list, val_args: list) -> list:
    """Q14: Smallest Number in Infinite Set (LC 2336).
    Input: operations = ["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
           val_args   = [[], [2], [], [], [], [1], [], [], []]
    Expected: [None, None, 1, 2, 3, None, 1, 4, 5]
    """
    # Write your logic here
    pass


def q15(operations: list, val_args: list) -> list:
    """Q15: Stock Price Fluctuation (LC 2034 with Hash Map + Two Heaps).
    Input: operations = ["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
           val_args   = [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
    Expected: [None, None, None, 5, 10, None, 5, None, 2]
    """
    # Write your logic here
    pass


def q16(operations: list, val_args: list) -> list:
    """Q16: Design Twitter (LC 355). Post tweets, follow/unfollow, and fetch recent 10 news feeds.
    Input: operations = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
           val_args   = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Expected: [None, None, [5], None, None, [6, 5], None, [5]]
    """
    # Write your logic here
    pass


def q17(operations: list, val_args: list) -> list:
    """Q17: Range Sum Query - Mutable (LC 307 Binary Indexed Tree / Segment Tree).
    Input: operations = ["NumArray", "sumRange", "update", "sumRange"]
           val_args   = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
    Expected: [None, 9, None, 8]
    """
    # Write your logic here
    pass


def q18(operations: list, val_args: list) -> list:
    """Q18: Simple Bank System (LC 2043).
    Input: operations = ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
           val_args   = [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
    Expected: [None, True, True, True, False, False]
    """
    # Write your logic here
    pass


def q19(operations: list, val_args: list) -> list:
    """Q19: Design Front Middle Back Queue (LC 1670).
    Input: operations = ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
           val_args   = [[], [1], [2], [3], [4], [], [], [], [], []]
    Expected: [None, None, None, None, None, 1, 3, 4, 2, -1]
    """
    # Write your logic here
    pass


def q20(operations: list, val_args: list) -> list:
    """Q20: Design Hit Counter (LC 362). Return number of hits in past 300 seconds (5 min).
    Input: operations = ["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
           val_args   = [[], [1], [2], [3], [4], [300], [300], [301]]
    Expected: [None, None, None, None, 3, None, 4, 3]
    """
    # Write your logic here
    pass


def q21(operations: list, val_args: list) -> list:
    """Q21: LFU Cache (LC 460 Least Frequently Used Cache).
    Input: operations = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
           val_args   = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    Expected: [None, None, None, 1, None, -1, 3, None, -1, 3, 4]
    """
    # Write your logic here
    pass


def q22(operations: list, val_args: list) -> list:
    """Q22: Max Stack (LC 716). Stack with getMax and popMax in O(log n) / O(1).
    Input: operations = ["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
           val_args   = [[], [5], [1], [5], [], [], [], [], [], []]
    Expected: [None, None, None, None, 5, 5, 1, 5, 1, 5]
    """
    # Write your logic here
    pass


def q23(operations: list, val_args: list) -> list:
    """Q23: Design Authentication Manager (LC 1797).
    Input: operations = ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
           val_args   = [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
    Expected: [None, None, None, 1, None, None, None, 0]
    """
    # Write your logic here
    pass


def q24(operations: list, val_args: list) -> list:
    """Q24: Peeking Iterator (LC 284).
    Input: operations = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
           val_args   = [[[1, 2, 3]], [], [], [], [], []]
    Expected: [None, 1, 2, 2, 3, False]
    """
    # Write your logic here
    pass


def q25(operations: list, val_args: list) -> list:
    """Q25: All O`one Data Structure (LC 432 Doubly Linked List of Sets).
    Input: operations = ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
           val_args   = [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
    Expected: [None, None, None, "hello", "hello", None, "hello", "leet"]
    """
    # Write your logic here
    pass


# ==================== TEST CASES ====================

TESTS = {
    1: {"name": "LRU Cache", "func": q1, "input": [["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]], "expected": [None, None, None, 1, None, -1, None, -1, 3, 4]},
    2: {"name": "Min Stack", "func": q2, "input": [["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], [[], [-2], [0], [-3], [], [], [], []]], "expected": [None, None, None, None, -3, None, 0, -2]},
    3: {"name": "Queue using Stacks", "func": q3, "input": [["MyQueue", "push", "push", "peek", "pop", "empty"], [[], [1], [2], [], [], []]], "expected": [None, None, None, 1, 1, False]},
    4: {"name": "Time Based KV Store", "func": q4, "input": [["TimeMap", "set", "get", "get", "set", "get", "get"], [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]], "expected": [None, None, "bar", "bar", None, "bar2", "bar2"]},
    5: {"name": "Insert Delete GetRandom", "func": q5, "input": [["RandomizedSet", "insert", "remove", "insert", "remove", "insert"], [[], [1], [2], [2], [1], [2]]], "expected": [None, True, False, True, True, False]},
    6: {"name": "Underground System", "func": q6, "input": [["UndergroundSystem", "checkIn", "checkIn", "checkOut", "checkOut", "getAverageTime"], [[], [45, "Leyton", 3], [32, "Paradise", 8], [45, "Waterloo", 15], [32, "Cambridge", 22], ["Paradise", "Cambridge"]]], "expected": [None, None, None, None, None, 14.0]},
    7: {"name": "Moving Average", "func": q7, "input": [["MovingAverage", "next", "next", "next", "next"], [[3], [1], [10], [3], [5]]], "expected": [None, 1.0, 5.5, 4.666666666666667, 6.0]},
    8: {"name": "Browser History", "func": q8, "input": [["BrowserHistory", "visit", "visit", "visit", "back", "back", "forward", "visit", "forward", "back", "back"], [["leetcode.com"], ["google.com"], ["facebook.com"], ["youtube.com"], [1], [1], [1], ["linkedin.com"], [2], [2], [7]]], "expected": [None, None, None, None, "facebook.com", "google.com", "facebook.com", None, "linkedin.com", "google.com", "leetcode.com"]},
    9: {"name": "Snapshot Array", "func": q9, "input": [["SnapshotArray", "set", "snap", "set", "get"], [[3], [0, 5], [], [0, 6], [0, 0]]], "expected": [None, None, 0, None, 5]},
    10: {"name": "Circular Queue", "func": q10, "input": [["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"], [[3], [1], [2], [3], [4], [], [], [], [4], []]], "expected": [None, True, True, True, False, 3, True, True, True, 4]},
    11: {"name": "Median Finder", "func": q11, "input": [["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []]], "expected": [None, None, None, 1.5, None, 2.0]},
    12: {"name": "Range Sum 2D", "func": q12, "input": [["NumMatrix", "sumRegion", "sumRegion"], [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2]]], "expected": [None, 8, 11]},
    13: {"name": "Seat Manager", "func": q13, "input": [["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"], [[5], [], [], [2], [], [], [], [], [5]]], "expected": [None, 1, 2, None, 2, 3, 4, 5, None]},
    14: {"name": "Smallest Infinite Set", "func": q14, "input": [["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"], [[], [2], [], [], [], [1], [], [], []]], "expected": [None, None, 1, 2, 3, None, 1, 4, 5]},
    15: {"name": "Stock Price Fluctuation", "func": q15, "input": [["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"], [[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]], "expected": [None, None, None, 5, 10, None, 5, None, 2]},
    16: {"name": "Design Twitter", "func": q16, "input": [["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"], [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]], "expected": [None, None, [5], None, None, [6, 5], None, [5]]},
    17: {"name": "Range Sum Mutable", "func": q17, "input": [["NumArray", "sumRange", "update", "sumRange"], [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]], "expected": [None, 9, None, 8]},
    18: {"name": "Simple Bank System", "func": q18, "input": [["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"], [[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]], "expected": [None, True, True, True, False, False]},
    19: {"name": "Front Middle Back Queue", "func": q19, "input": [["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"], [[], [1], [2], [3], [4], [], [], [], [], []]], "expected": [None, None, None, None, None, 1, 3, 4, 2, -1]},
    20: {"name": "Hit Counter", "func": q20, "input": [["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"], [[], [1], [2], [3], [4], [300], [300], [301]]], "expected": [None, None, None, None, 3, None, 4, 3]},
    21: {"name": "LFU Cache", "func": q21, "input": [["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]], "expected": [None, None, None, 1, None, -1, 3, None, -1, 3, 4]},
    22: {"name": "Max Stack", "func": q22, "input": [["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"], [[], [5], [1], [5], [], [], [], [], [], []]], "expected": [None, None, None, None, 5, 5, 1, 5, 1, 5]},
    23: {"name": "Authentication Manager", "func": q23, "input": [["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"], [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]], "expected": [None, None, None, 1, None, None, None, 0]},
    24: {"name": "Peeking Iterator", "func": q24, "input": [["PeekingIterator", "next", "peek", "next", "next", "hasNext"], [[[1, 2, 3]], [], [], [], [], []]], "expected": [None, 1, 2, 2, 3, False]},
    25: {"name": "All O`one Structure", "func": q25, "input": [["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"], [[], ["hello"], ["hello"], [], [], ["leet"], [], []]], "expected": [None, None, None, "hello", "hello", None, "hello", "leet"]}
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
            print(f"Operations: {args[0]}")
            print(f"Arguments: {args[1]}")
            print(f"Expected: {expected}")

        result = func(args[0], args[1])

        # Floating point tolerance comparison for moving average
        if question_num in [6, 7, 11] and isinstance(result, list):
            match = len(result) == len(expected)
            for r, e in zip(result, expected):
                if isinstance(r, float) and isinstance(e, float):
                    if abs(r - e) > 1e-5:
                        match = False
                elif r != e:
                    match = False
            if match:
                result = expected

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
