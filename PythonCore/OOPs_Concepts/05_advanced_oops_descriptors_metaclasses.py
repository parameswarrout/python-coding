import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
👑 OOP CONCEPTS: ADVANCED OOPS (Descriptors, Metaclasses, Slots & Methods)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 05_advanced_oops_descriptors_metaclasses.py
2. Run a specific cell (e.g., Cell 2):
   python 05_advanced_oops_descriptors_metaclasses.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Instance vs Class (`@classmethod`) vs Static (`@staticmethod`) Methods
# - `instance method`: receives `self` (operates on specific instance state)
# - `@classmethod`: receives `cls` (operates on class state, used for factory constructors)
# - `@staticmethod`: receives no implicit first arg (pure utility function logically grouped inside class)

# %% [code]
def cell_1():
    """Cell 1: Instance vs Class vs Static Methods"""
    print("=" * 60)
    print("▶ CELL 1: Instance, Class (@classmethod), and Static (@staticmethod)")
    print("=" * 60)

    class DateParser:
        # Class attribute
        default_timezone = "UTC"

        def __init__(self, year: int, month: int, day: int):
            self.year = year
            self.month = month
            self.day = day

        # 1. Instance Method: Accesses self
        def format_iso(self) -> str:
            return f"{self.year:04d}-{self.month:02d}-{self.day:02d} ({self.default_timezone})"

        # 2. Class Method: Alternative Factory Constructor (from string "YYYY-MM-DD")
        @classmethod
        def from_string(cls, date_str: str):
            year, month, day = map(int, date_str.split("-"))
            # Returns a new instance of cls (handles inheritance properly)
            return cls(year, month, day)

        # 3. Static Method: Standalone validation utility
        @staticmethod
        def is_leap_year(year: int) -> bool:
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    d1 = DateParser(2026, 8, 19)
    d2 = DateParser.from_string("2024-02-29")

    print(f"Direct instantiation: {d1.format_iso()}")
    print(f"Factory constructor:  {d2.format_iso()}")
    print(f"Is 2024 leap year?    {DateParser.is_leap_year(2024)}")
    print(f"Is 2026 leap year?    {DateParser.is_leap_year(2026)}")


# %% [markdown]
# ### 📌 Cell 2: Python Descriptors (`__get__`, `__set__`, `__set_name__`)
# Descriptors power `@property`, `@classmethod`, `__slots__`, and ORM field validation (like Django/SQLAlchemy models).

# %% [code]
def cell_2():
    """Cell 2: Reusable Validation Descriptors"""
    print("=" * 60)
    print("▶ CELL 2: Python Descriptor Protocol (Reusable Type Validation)")
    print("=" * 60)

    class ValidatedInteger:
        """Descriptor that enforces integer type and min/max boundaries."""
        def __init__(self, min_val: int = None, max_val: int = None):
            self.min_val = min_val
            self.max_val = max_val

        def __set_name__(self, owner, name):
            # Automatically grabs attribute name assigned on class (e.g. 'age', 'score')
            self.private_name = f"_{name}"

        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, self.private_name, None)

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError(f"Value must be an int, got {type(value).__name__}!")
            if self.min_val is not None and value < self.min_val:
                raise ValueError(f"Value cannot be less than {self.min_val}!")
            if self.max_val is not None and value > self.max_val:
                raise ValueError(f"Value cannot exceed {self.max_val}!")
            setattr(instance, self.private_name, value)

    class PlayerProfile:
        # Attributes managed by descriptors
        age = ValidatedInteger(min_val=13, max_val=100)
        score = ValidatedInteger(min_val=0, max_val=10000)

        def __init__(self, username: str, age: int, score: int):
            self.username = username
            self.age = age
            self.score = score

    p = PlayerProfile("PlayerOne", age=25, score=4500)
    print(f"Valid profile: {p.username}, Age: {p.age}, Score: {p.score}")

    print("\n[Attempting invalid age update (< 13)]:")
    try:
        p.age = 10
    except ValueError as e:
        print(f"  Descriptor caught error: {e}")


# %% [markdown]
# ### 📌 Cell 3: Memory Optimization with `__slots__`
# Standard Python objects store attributes in a dynamic `__dict__`.
# Defining `__slots__` eliminates `__dict__`, saving ~60% RAM per instance and speeding up attribute lookups.

# %% [code]
def cell_3():
    """Cell 3: __slots__ Memory Comparison & Attribute Locking"""
    print("=" * 60)
    print("▶ CELL 3: __slots__ (Memory Optimization & Attribute Restriction)")
    print("=" * 60)
    import sys

    class StandardPoint:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    class SlottedPoint:
        __slots__ = ('x', 'y', 'z')  # No __dict__ created!
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    std_pt = StandardPoint(1, 2, 3)
    slot_pt = SlottedPoint(1, 2, 3)

    print(f"Standard instance has __dict__? {hasattr(std_pt, '__dict__')}")
    print(f"Slotted instance has __dict__?  {hasattr(slot_pt, '__dict__')}")
    
    # Slotted classes prevent accidental typos / dynamic attribute creation
    print("\n[Attempting to add new arbitrary attribute to Slotted instance]:")
    try:
        slot_pt.color = "Red"
    except AttributeError as e:
        print(f"  Caught expected error: {e}")


# %% [markdown]
# ### 📌 Cell 4: Metaclasses (`type`) and Auto-Registration
# Metaclasses are "classes of classes". They intercept class creation at import/runtime
# to validate class structures, enforce standards, or auto-register plugins.

# %% [code]
def cell_4():
    """Cell 4: Custom Metaclass for Plugin Registry & Validation"""
    print("=" * 60)
    print("▶ CELL 4: Metaclasses (Plugin Auto-Registry & Attribute Validation)")
    print("=" * 60)

    # Global plugin registry populated automatically by the metaclass
    PLUGIN_REGISTRY = {}

    class PluginMeta(type):
        """Metaclass that automatically registers any subclass into PLUGIN_REGISTRY."""
        def __new__(mcs, name, bases, attrs):
            # Enforce that all plugins define a docstring
            if name != "BasePlugin" and "__doc__" not in attrs or not attrs.get("__doc__"):
                raise TypeError(f"Class '{name}' must have a docstring!")
            
            # Create the class
            new_cls = super().__new__(mcs, name, bases, attrs)
            
            # Register non-base plugins
            if name != "BasePlugin":
                plugin_id = attrs.get("plugin_id", name.lower())
                PLUGIN_REGISTRY[plugin_id] = new_cls
                print(f"  [Metaclass]: Automatically registered plugin '{plugin_id}' -> {new_cls}")
                
            return new_cls

    class BasePlugin(metaclass=PluginMeta):
        """Abstract base class for all dynamically discovered plugins."""
        def execute(self):
            raise NotImplementedError()

    # When these classes are defined, PluginMeta automatically intercepts and registers them!
    class JSONExportPlugin(BasePlugin):
        """Exports data to JSON format."""
        plugin_id = "json_export"
        def execute(self):
            return "Exporting data in JSON format."

    class CSRExportPlugin(BasePlugin):
        """Exports data to CSV format."""
        plugin_id = "csv_export"
        def execute(self):
            return "Exporting data in CSV format."

    print("\n[Inspecting Discovered Plugin Registry]:")
    for pid, p_cls in PLUGIN_REGISTRY.items():
        instance = p_cls()
        print(f"  Key: {pid:<12} | Instance Action: {instance.execute()}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Instance, Class (@classmethod) & Static Methods", cell_1),
    2: ("Descriptor Protocol (Reusable Type Validation)", cell_2),
    3: ("__slots__ Memory Optimization & Attribute Locking", cell_3),
    4: ("Metaclasses & Automated Plugin Registry", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 05_ADVANCED_OOPS_DESCRIPTORS_METACLASSES.PY")
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
                print("Usage: python 05_advanced_oops_descriptors_metaclasses.py [cell_number | --all]")
    else:
        run_all()
