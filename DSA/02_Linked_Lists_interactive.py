import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
🔗 DSA TOPIC 02: LINKED LISTS (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 02_Linked_Lists_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 02_Linked_Lists_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Singly Linked List Implementation from Scratch
# Linked lists use pointers rather than contiguous memory, enabling $O(1)$ insertions/deletions at the head.

# %% [code]
def cell_1():
    """Cell 1: Singly Linked List Node, Insertion & Traversal"""
    print("=" * 60)
    print("▶ CELL 1: Singly Linked List Implementation & Traversal")
    print("=" * 60)

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, val):
            new_node = ListNode(val)
            if not self.head:
                self.head = new_node
                return
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

        def prepend(self, val):
            new_node = ListNode(val, next=self.head)
            self.head = new_node

        def to_list(self) -> list:
            result = []
            curr = self.head
            while curr:
                result.append(curr.val)
                curr = curr.next
            return result

        def display(self):
            nodes = [str(x) for x in self.to_list()]
            print(" -> ".join(nodes) + " -> NULL")

    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    print("Linked List after insertions:")
    ll.display()


# %% [markdown]
# ### 📌 Cell 2: In-Place Reversal of a Linked List (Iterative $O(N)$ time, $O(1)$ space)
# Swapping pointers using `prev`, `curr`, and `next_node`.

# %% [code]
def cell_2():
    """Cell 2: In-Place Linked List Reversal"""
    print("=" * 60)
    print("▶ CELL 2: In-Place Linked List Reversal (Iterative)")
    print("=" * 60)

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def reverse_list(head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Save next
            curr.next = prev       # Reverse pointer
            prev = curr            # Advance prev
            curr = next_node       # Advance curr
        return prev

    def print_list(node: ListNode):
        vals = []
        while node:
            vals.append(str(node.val))
            node = node.next
        print(" -> ".join(vals) + " -> NULL")

    # Build: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Original List:")
    print_list(head)

    reversed_head = reverse_list(head)
    print("\nReversed List:")
    print_list(reversed_head)


# %% [markdown]
# ### 📌 Cell 3: Floyd's Tortoise and Hare (Cycle Detection & Middle Node)
# Using slow pointer (1 step) and fast pointer (2 steps) to detect cycles or find middle in single pass.

# %% [code]
def cell_3():
    """Cell 3: Fast and Slow Pointers (Cycle Detection & Middle of Linked List)"""
    print("=" * 60)
    print("▶ CELL 3: Fast & Slow Pointers (Floyd's Cycle Detection)")
    print("=" * 60)

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def has_cycle(head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def find_middle_node(head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Create acyclic list: 1 -> 2 -> 3 -> 4 -> 5
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    print(f"Has Cycle in linear list? -> {has_cycle(n1)}")
    mid = find_middle_node(n1)
    print(f"Middle node value of [1,2,3,4,5]: {mid.val}")

    # Introduce cycle: 5 points back to 2
    n5.next = n2
    print(f"Has Cycle after connecting tail to node 2? -> {has_cycle(n1)}")


# %% [markdown]
# ### 📌 Cell 4: Merge Two Sorted Linked Lists ($O(N + M)$ time)
# Merging two sorted lists using dummy head pointer.

# %% [code]
def cell_4():
    """Cell 4: Merge Two Sorted Lists"""
    print("=" * 60)
    print("▶ CELL 4: Merging Two Sorted Linked Lists")
    print("=" * 60)

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def merge_two_sorted(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next

    def list_to_str(node: ListNode) -> str:
        res = []
        while node:
            res.append(str(node.val))
            node = node.next
        return " -> ".join(res) + " -> NULL"

    # L1: 1 -> 3 -> 5
    l1 = ListNode(1, ListNode(3, ListNode(5)))
    # L2: 2 -> 4 -> 6 -> 8
    l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))

    print(f"List 1: {list_to_str(l1)}")
    print(f"List 2: {list_to_str(l2)}")

    merged = merge_two_sorted(l1, l2)
    print(f"\nMerged Sorted List:\n{list_to_str(merged)}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Singly Linked List Implementation & CRUD", cell_1),
    2: ("In-Place Reversal of Linked List (Iterative)", cell_2),
    3: ("Floyd's Fast & Slow Pointers (Cycle & Middle Node)", cell_3),
    4: ("Merge Two Sorted Linked Lists", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 02_LINKED_LISTS_INTERACTIVE.PY")
    print("#" * 70 + "\n")
    for num in sorted(CELLS.keys()):
        CELLS[num][1]()
        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip()
        if arg in ["--all", "all", "0"]:
            run_all()
        else:
            try:
                cell_no = int(arg)
                if cell_no in CELLS:
                    CELLS[cell_no][1]()
                else:
                    print(f"❌ Invalid Cell {cell_no}. Choose from: {list(CELLS.keys())}")
            except ValueError:
                print("Usage: python 02_Linked_Lists_interactive.py [cell_number | --all]")
    else:
        run_all()
