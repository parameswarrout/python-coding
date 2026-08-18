import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
🏛️ OOP CONCEPTS: INHERITANCE (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 01_inheritance_interactive.py
2. Run a specific cell (e.g., Cell 3):
   python 01_inheritance_interactive.py 3
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Basic Single Inheritance & Method Reusability
# Inheritance allows a child class to derive attributes and methods from a parent class.
# It promotes code reuse (DRY principle) and models "IS-A" relationships.

# %% [code]
def cell_1():
    """Cell 1: Single Inheritance (Animal -> Dog)"""
    print("=" * 60)
    print("▶ CELL 1: Single Inheritance (Animal Base Class & Dog Subclass)")
    print("=" * 60)

    class Animal:
        def __init__(self, name: str, species: str):
            self.name = name
            self.species = species

        def make_sound(self) -> str:
            return f"{self.name} makes a generic sound."

        def sleep(self) -> str:
            return f"{self.name} is sleeping peacefully."

        def info(self) -> str:
            return f"{self.name} is a {self.species}."

    # Dog inherits from Animal
    class Dog(Animal):
        def __init__(self, name: str, breed: str):
            # Call parent __init__ using super()
            super().__init__(name, species="Canine")
            self.breed = breed

        # Method Overriding: Specialized implementation
        def make_sound(self) -> str:
            return f"{self.name} barks: Woof! Woof!"

        # Subclass-specific method
        def fetch(self, item: str) -> str:
            return f"{self.name} enthusiastically fetches the {item}!"

    # Testing Cell 1
    generic = Animal("Generic Creature", "Unknown")
    buddy = Dog("Buddy", "Golden Retriever")

    print("[Parent Instance]")
    print(f"  Info:  {generic.info()}")
    print(f"  Sound: {generic.make_sound()}")
    print(f"  Sleep: {generic.sleep()}")

    print("\n[Subclass Instance - Overridden & Inherited Methods]")
    print(f"  Info (Inherited):       {buddy.info()}")
    print(f"  Sound (Overridden):     {buddy.make_sound()}")
    print(f"  Sleep (Inherited):      {buddy.sleep()}")
    print(f"  Fetch (Unique to Dog):  {buddy.fetch('tennis ball')}")
    print(f"  isinstance(buddy, Animal): {isinstance(buddy, Animal)}")


# %% [markdown]
# ### 📌 Cell 2: Hierarchical Inheritance (Single Parent, Multiple Children)
# Multiple specialized child classes inheriting common behaviors from one base class.

# %% [code]
def cell_2():
    """Cell 2: Hierarchical Inheritance (Vehicle -> Car, Motorcycle, ElectricCar)"""
    print("=" * 60)
    print("▶ CELL 2: Hierarchical Inheritance (Vehicle Hierarchy)")
    print("=" * 60)

    class Vehicle:
        def __init__(self, brand: str, model: str, speed_kmh: float):
            self.brand = brand
            self.model = model
            self.speed_kmh = speed_kmh

        def move(self) -> str:
            return f"{self.brand} {self.model} is traveling at {self.speed_kmh} km/h."

        def fuel_type(self) -> str:
            return "Standard Fuel"

    class Car(Vehicle):
        def __init__(self, brand: str, model: str, speed_kmh: float, doors: int = 4):
            super().__init__(brand, model, speed_kmh)
            self.doors = doors

        def honk(self) -> str:
            return f"{self.brand} {self.model}: Beep beep!"

    class Motorcycle(Vehicle):
        def __init__(self, brand: str, model: str, speed_kmh: float, has_sidecar: bool = False):
            super().__init__(brand, model, speed_kmh)
            self.has_sidecar = has_sidecar

        def wheelie(self) -> str:
            return f"{self.brand} {self.model} performs a wheelie!"

    class ElectricCar(Car):  # Multi-level inheritance
        def __init__(self, brand: str, model: str, speed_kmh: float, battery_kwh: int):
            super().__init__(brand, model, speed_kmh, doors=4)
            self.battery_kwh = battery_kwh

        def fuel_type(self) -> str:
            return f"Electric ({self.battery_kwh} kWh battery)"

    audi = Car("Audi", "Q7", 240, doors=4)
    harley = Motorcycle("Harley", "Iron 883", 180)
    tesla = ElectricCar("Tesla", "Model S Plaid", 320, battery_kwh=100)

    print(audi.move(), "|", audi.honk())
    print(harley.move(), "|", harley.wheelie())
    print(tesla.move(), "| Fuel:", tesla.fuel_type())


# %% [markdown]
# ### 📌 Cell 3: Multiple Inheritance & Method Resolution Order (MRO)
# Python supports inheriting from multiple parents. The C3 Linearization algorithm determines method lookup order.

# %% [code]
def cell_3():
    """Cell 3: Multiple Inheritance & The Diamond Problem (C3 Linearization)"""
    print("=" * 60)
    print("▶ CELL 3: Multiple Inheritance & MRO (The Diamond Problem)")
    print("=" * 60)

    class Device:
        def __init__(self, name: str, **kwargs):
            super().__init__(**kwargs)
            self.name = name
            print(f"  [Init Device]: {name}")

        def power_on(self):
            return f"Device {self.name} powered ON."

    class Camera(Device):
        def __init__(self, resolution_mp: int = 12, **kwargs):
            super().__init__(**kwargs)
            self.resolution_mp = resolution_mp
            print(f"  [Init Camera]: {resolution_mp}MP")

        def capture_photo(self) -> str:
            return f"Captured {self.resolution_mp}MP photo."

    class Phone(Device):
        def __init__(self, phone_number: str = "N/A", **kwargs):
            super().__init__(**kwargs)
            self.phone_number = phone_number
            print(f"  [Init Phone]: {phone_number}")

        def make_call(self, recipient: str) -> str:
            return f"Calling {recipient} from {self.phone_number}..."

    # Smartphone inherits from BOTH Camera and Phone (Diamond Pattern)
    class Smartphone(Camera, Phone):
        def __init__(self, name: str, phone_number: str, resolution_mp: int):
            # cooperative multiple inheritance using super() and kwargs
            super().__init__(name=name, phone_number=phone_number, resolution_mp=resolution_mp)
            print(f"  [Init Smartphone]: Complete")

    phone = Smartphone("Galaxy Ultra", "+1-555-0199", 200)
    print("\n[Calling Capabilities from multiple parents]:")
    print(" ", phone.power_on())
    print(" ", phone.capture_photo())
    print(" ", phone.make_call("Alice"))

    print("\n[Method Resolution Order (MRO)]:")
    for idx, cls in enumerate(Smartphone.__mro__):
        print(f"  Step {idx + 1}: {cls.__name__}")


# %% [markdown]
# ### 📌 Cell 4: `super()` and Cooperative Multiple Inheritance Gotchas
# Understanding parameter forwarding in `*args, **kwargs` across cooperative inheritance chains.

# %% [code]
def cell_4():
    """Cell 4: Cooperative super() with **kwargs"""
    print("=" * 60)
    print("▶ CELL 4: Cooperative Multiple Inheritance with **kwargs")
    print("=" * 60)

    class Base:
        def __init__(self, **kwargs):
            # Base consumes all extra kwargs so object.__init__ receives nothing
            super().__init__()
            print("  [Base initialized]")

    class LoggerMixin(Base):
        def __init__(self, logger_name="DefaultLogger", **kwargs):
            super().__init__(**kwargs)
            self.logger_name = logger_name
            print(f"  [LoggerMixin initialized]: {self.logger_name}")

        def log(self, message: str):
            print(f"[{self.logger_name}] {message}")

    class AuthMixin(Base):
        def __init__(self, auth_token="secret-123", **kwargs):
            super().__init__(**kwargs)
            self.auth_token = auth_token
            print(f"  [AuthMixin initialized]: token={self.auth_token}")

        def authenticate(self) -> bool:
            return self.auth_token == "secret-123"

    class SecuredService(LoggerMixin, AuthMixin):
        def __init__(self, service_name: str, **kwargs):
            super().__init__(**kwargs)
            self.service_name = service_name
            print(f"  [SecuredService initialized]: {self.service_name}")

    print("Instantiating SecuredService with cooperative kwargs:")
    svc = SecuredService(
        service_name="PaymentService", 
        logger_name="PaymentAuditLog", 
        auth_token="secret-123"
    )
    svc.log("Executing transaction #99482...")
    print(f"Authentication valid? {svc.authenticate()}")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Single Inheritance (Animal & Dog)", cell_1),
    2: ("Hierarchical & Multi-level (Vehicles)", cell_2),
    3: ("Multiple Inheritance & MRO (Smartphone Diamond)", cell_3),
    4: ("Cooperative super() & Mixins with **kwargs", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 01_INHERITANCE_INTERACTIVE.PY")
    print("#" * 70 + "\n")
    for num in sorted(CELLS.keys()):
        CELLS[num][1]()
        print()


def show_menu():
    print("\n" + "=" * 60)
    print("📚 OOP INHERITANCE NOTEBOOK - AVAILABLE CELLS:")
    print("=" * 60)
    for num, (name, _) in sorted(CELLS.keys()):
        print(f"  [{num}] {name}")
    print("  [0] Run All Cells")
    print("=" * 60)


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
                print("Usage: python 01_inheritance_interactive.py [cell_number | --all]")
    else:
        # Default: Run all cells sequentially like a notebook export
        run_all()
