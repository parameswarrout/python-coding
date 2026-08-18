import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from collections import deque

"""
=============================================================================
🌳 DSA TOPIC 05: TREES & BST (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 05_Trees_and_Binary_Search_Trees_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 05_Trees_and_Binary_Search_Trees_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Binary Tree Node & DFS Traversals (Pre, In, Post)
# - **Pre-order**: Root -> Left -> Right (Used for tree cloning/serialization)
# - **In-order**: Left -> Root -> Right (Produces sorted order for BST)
# - **Post-order**: Left -> Right -> Root (Used for deletion/bottom-up calculations)

# %% [code]
def cell_1():
    """Cell 1: Binary Tree Node & DFS Traversals"""
    print("=" * 60)
    print("▶ CELL 1: Binary Tree Node & DFS Traversals (In/Pre/Post-Order)")
    print("=" * 60)

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def preorder(root) -> list:
        return [root.val] + preorder(root.left) + preorder(root.right) if root else []

    def inorder(root) -> list:
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []

    def postorder(root) -> list:
        return postorder(root.left) + postorder(root.right) + [root.val] if root else []

    # Build Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))

    print(f"Pre-order  (Root->Left->Right): {preorder(root)}")
    print(f"In-order   (Left->Root->Right): {inorder(root)}")
    print(f"Post-order (Left->Right->Root): {postorder(root)}")


# %% [markdown]
# ### 📌 Cell 2: Level-Order Traversal (BFS with Queue)
# Traversing the tree row by row using a queue in $O(N)$ time.

# %% [code]
def cell_2():
    """Cell 2: Level-Order Traversal (BFS)"""
    print("=" * 60)
    print("▶ CELL 2: Level-Order Traversal (BFS with Queue)")
    print("=" * 60)

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def level_order(root) -> list:
        if not root:
            return []
        levels = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(current_level)
        return levels

    # Tree: [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    levels = level_order(root)
    print("Level-by-Level Output:")
    for idx, lvl in enumerate(levels):
        print(f"  Level {idx + 1}: {lvl}")


# %% [markdown]
# ### 📌 Cell 3: Binary Search Tree (BST) Search, Insert & Validation
# In a BST, all nodes in the left subtree $< \text{root} <$ all nodes in the right subtree.

# %% [code]
def cell_3():
    """Cell 3: BST Insertion, Search & Validation"""
    print("=" * 60)
    print("▶ CELL 3: BST Insertion, Search & Inorder Validation")
    print("=" * 60)

    class BSTNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, val):
            if not self.root:
                self.root = BSTNode(val)
                return
            curr = self.root
            while True:
                if val < curr.val:
                    if not curr.left:
                        curr.left = BSTNode(val)
                        break
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = BSTNode(val)
                        break
                    curr = curr.right

        def search(self, val) -> bool:
            curr = self.root
            while curr:
                if curr.val == val:
                    return True
                elif val < curr.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return False

        def inorder_traversal(self, node):
            return self.inorder_traversal(node.left) + [node.val] + self.inorder_traversal(node.right) if node else []

    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)

    print(f"Inserted: {elements}")
    print(f"BST Inorder Traversal (Always Sorted!): {bst.inorder_traversal(bst.root)}")
    print(f"Search 40 in BST: {bst.search(40)}")
    print(f"Search 99 in BST: {bst.search(99)}")


# %% [markdown]
# ### 📌 Cell 4: Lowest Common Ancestor (LCA) in Binary Tree
# Finding the lowest shared ancestor node between two target nodes.

# %% [code]
def cell_4():
    """Cell 4: Lowest Common Ancestor (LCA)"""
    print("=" * 60)
    print("▶ CELL 4: Lowest Common Ancestor (LCA)")
    print("=" * 60)

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        left = lowest_common_ancestor(root.left, p, q)
        right = lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    # Tree:
    #         3
    #       /   \
    #      5     1
    #     / \   / \
    #    6   2 0   8
    n6 = TreeNode(6); n2 = TreeNode(2); n0 = TreeNode(0); n8 = TreeNode(8)
    n5 = TreeNode(5, n6, n2)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    lca1 = lowest_common_ancestor(root, 5, 1)
    lca2 = lowest_common_ancestor(root, 5, 4)  # 5 and 4
    lca3 = lowest_common_ancestor(root, 6, 2)

    print(f"LCA of 5 and 1: Node({lca1.val})")
    print(f"LCA of 6 and 2: Node({lca3.val})")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Binary Tree Node & DFS (Pre/In/Post-Order)", cell_1),
    2: ("Level-Order Traversal (BFS with Queue)", cell_2),
    3: ("BST Search, Insertion & Sorted Inorder", cell_3),
    4: ("Lowest Common Ancestor (LCA)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 05_TREES_AND_BINARY_SEARCH_TREES_INTERACTIVE.PY")
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
                print("Usage: python 05_Trees_and_Binary_Search_Trees_interactive.py [cell_number | --all]")
    else:
        run_all()
