import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math

"""
=============================================================================
🎭 OOP CONCEPTS: POLYMORPHISM (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 03_polymorphism_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 03_polymorphism_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Duck Typing (Dynamic Polymorphism)
# "If it walks like a duck and quacks like a duck, it's a duck."
# In Python, function interfaces care about whether an object has the required method,
# rather than its explicit class type.

# %% [code]
def cell_1():
    """Cell 1: Duck Typing with Audio Players & Streamers"""
    print("=" * 60)
    print("▶ CELL 1: Duck Typing (Behavior Over Class Hierarchy)")
    print("=" * 60)

    class SpotifyPlayer:
        def play(self, song_title: str):
            return f"Streaming '{song_title}' over Spotify Web API (High Quality OGG Vorbis)"

    class YouTubeMusicPlayer:
        def play(self, song_title: str):
            return f"Playing '{song_title}' via YouTube Music (Opus 160kbps)"

    class LocalMP3Player:
        def play(self, song_title: str):
            return f"Reading '{song_title}.mp3' from local SSD drive"

    # Polymorphic controller function: Doesn't care which class it is!
    def start_music_session(player, song: str):
        print(f"  [Player Controller]: {player.play(song)}")

    players = [SpotifyPlayer(), YouTubeMusicPlayer(), LocalMP3Player()]
    for p in players:
        start_music_session(p, "Interstellar Main Theme")


# %% [markdown]
# ### 📌 Cell 2: Method Overriding (Shape Hierarchy)
# Subclasses provide specific implementations of methods defined in their parent classes.

# %% [code]
def cell_2():
    """Cell 2: Method Overriding with Geometric Shapes"""
    print("=" * 60)
    print("▶ CELL 2: Method Overriding & Heterogeneous Collections")
    print("=" * 60)

    class Shape:
        def __init__(self, name: str):
            self.name = name

        def area(self) -> float:
            raise NotImplementedError("Subclasses must implement area()!")

        def perimeter(self) -> float:
            raise NotImplementedError("Subclasses must implement perimeter()!")

    class Rectangle(Shape):
        def __init__(self, width: float, height: float):
            super().__init__("Rectangle")
            self.width = width
            self.height = height

        def area(self) -> float:
            return self.width * self.height

        def perimeter(self) -> float:
            return 2 * (self.width + self.height)

    class Circle(Shape):
        def __init__(self, radius: float):
            super().__init__("Circle")
            self.radius = radius

        def area(self) -> float:
            return round(math.pi * (self.radius ** 2), 2)

        def perimeter(self) -> float:
            return round(2 * math.pi * self.radius, 2)

    # Polymorphic loop over heterogeneous collection of shapes
    shapes = [Rectangle(10, 5), Circle(7), Rectangle(3, 4)]
    print(f"{'Shape':<12} | {'Area':<10} | {'Perimeter':<10}")
    print("-" * 38)
    for s in shapes:
        print(f"{s.name:<12} | {s.area():<10} | {s.perimeter():<10}")


# %% [markdown]
# ### 📌 Cell 3: Operator Overloading (`__add__`, `__mul__`, `__eq__`, `__repr__`)
# Overriding Python's special double-underscore (dunder) methods allows user-defined objects
# to seamlessly integrate with Python operators (`+`, `*`, `==`, `<`, `len()`).

# %% [code]
def cell_3():
    """Cell 3: Vector 2D Class with Complete Operator Overloading"""
    print("=" * 60)
    print("▶ CELL 3: Operator Overloading (Vector2D Math Engine)")
    print("=" * 60)

    class Vector2D:
        def __init__(self, x: float, y: float):
            self.x = x
            self.y = y

        # String representation for debugging: repr(v)
        def __repr__(self) -> str:
            return f"Vector2D({self.x}, {self.y})"

        # User-friendly string: print(v)
        def __str__(self) -> str:
            return f"({self.x}i + {self.y}j)"

        # Vector Addition: v1 + v2
        def __add__(self, other):
            if isinstance(other, Vector2D):
                return Vector2D(self.x + other.x, self.y + other.y)
            return NotImplemented

        # Vector Subtraction: v1 - v2
        def __sub__(self, other):
            if isinstance(other, Vector2D):
                return Vector2D(self.x - other.x, self.y - other.y)
            return NotImplemented

        # Scalar Multiplication or Dot Product: v * 3 or v1 * v2
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return Vector2D(self.x * other, self.y * other)
            elif isinstance(other, Vector2D):
                # Dot product
                return (self.x * other.x) + (self.y * other.y)
            return NotImplemented

        # Magnitude (Length): abs(v)
        def __abs__(self) -> float:
            return math.sqrt(self.x**2 + self.y**2)

        # Equality: v1 == v2
        def __eq__(self, other) -> bool:
            if isinstance(other, Vector2D):
                return self.x == other.x and self.y == other.y
            return False

        # Less than comparison based on magnitude: v1 < v2
        def __lt__(self, other) -> bool:
            if isinstance(other, Vector2D):
                return abs(self) < abs(other)
            return NotImplemented

    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    print(f"v1 = {v1}, Magnitude = {abs(v1)}")
    print(f"v2 = {v2}, Magnitude = {abs(v2):.2f}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 3 (Scalar Multiplied) = {v1 * 3}")
    print(f"v1 * v2 (Dot Product) = {v1 * v2}")
    print(f"Is v1 == Vector2D(3, 4)? {v1 == Vector2D(3, 4)}")
    print(f"Is v2 < v1? {v2 < v1}")


# %% [markdown]
# ### 📌 Cell 4: Emulating Sequence / Container Types (`__len__`, `__getitem__`, `__iter__`)
# Custom class that behaves like a built-in Python list with slicing and iteration.

# %% [code]
def cell_4():
    """Cell 4: Custom Iterable Container (DataPacketQueue)"""
    print("=" * 60)
    print("▶ CELL 4: Emulating Built-in Sequences (__len__, __getitem__, __iter__)")
    print("=" * 60)

    class CustomDataset:
        def __init__(self, data_items: list):
            self._items = list(data_items)

        def __len__(self) -> int:
            return len(self._items)

        def __getitem__(self, index):
            # Supports indexing and slicing!
            return self._items[index]

        def __contains__(self, item) -> bool:
            # Enables 'item in dataset'
            return item in self._items

    ds = CustomDataset(["Python", "PyTorch", "SQL", "Algorithms", "SystemDesign"])
    print(f"Length of dataset len(ds): {len(ds)}")
    print(f"Index access ds[1]: {ds[1]}")
    print(f"Slicing ds[1:4]: {ds[1:4]}")
    print(f"Is 'PyTorch' in dataset? {'PyTorch' in ds}")
    print(f"Is 'Java' in dataset? {'Java' in ds}")

    print("\nIterating over dataset with for-loop:")
    for item in ds:
        print(f"  -> {item}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Duck Typing (Behavior over Class Type)", cell_1),
    2: ("Method Overriding & Shape Collection", cell_2),
    3: ("Operator Overloading (Vector2D Math Engine)", cell_3),
    4: ("Emulating Sequence Types (__getitem__, __len__)", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 03_POLYMORPHISM_INTERACTIVE.PY")
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
                print("Usage: python 03_polymorphism_interactive.py [cell_number | --all]")
    else:
        run_all()
