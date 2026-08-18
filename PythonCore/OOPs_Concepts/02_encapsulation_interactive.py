import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

"""
=============================================================================
🛡️ OOP CONCEPTS: ENCAPSULATION (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 02_encapsulation_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 02_encapsulation_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Access Modifiers & Name Mangling
# Python uses naming conventions to signal intent:
# - `public`: accessible everywhere (`self.name`)
# - `_protected`: internal convention, subclass-accessible (`self._balance`)
# - `__private`: name-mangled by Python interpreter (`self.__pin` -> `_ClassName__pin`)

# %% [code]
def cell_1():
    """Cell 1: Public, Protected & Private Access Modifiers + Name Mangling"""
    print("=" * 60)
    print("▶ CELL 1: Public, Protected, and Private (__mangled) Modifiers")
    print("=" * 60)

    class BankAccount:
        def __init__(self, owner: str, initial_balance: float, pin: str):
            self.owner = owner            # Public: direct access
            self._balance = initial_balance # Protected: internal convention
            self.__pin = pin              # Private: name mangled to _BankAccount__pin

        def verify_pin(self, entered_pin: str) -> bool:
            return self.__pin == entered_pin

    acc = BankAccount("Parameswar", 10000.0, "9876")

    print("[1. Public Access]:")
    print(f"  acc.owner = {acc.owner}")

    print("\n[2. Protected Access (Allowed by convention, but discouraged)]:")
    print(f"  acc._balance = {acc._balance}")

    print("\n[3. Private Access Attempt (Direct access raises AttributeError)]:")
    try:
        print(acc.__pin)
    except AttributeError as e:
        print(f"  Caught expected error: {e}")

    print("\n[4. Name Mangling Inspection]:")
    print(f"  Actual attribute name in dict: _BankAccount__pin = {acc._BankAccount__pin}")
    print(f"  All instance attributes: {list(acc.__dict__.keys())}")


# %% [markdown]
# ### 📌 Cell 2: Pythonic `@property` Getters, Setters & Validation
# Using `@property` allows getter and setter methods to behave like natural attributes
# while enforcing strict validation rules and encapsulation boundaries.

# %% [code]
def cell_2():
    """Cell 2: Pythonic @property with Validation & Deleters"""
    print("=" * 60)
    print("▶ CELL 2: Getters, Setters & Deleters with Data Validation")
    print("=" * 60)

    class Employee:
        def __init__(self, name: str, salary: float):
            self.name = name
            self.salary = salary  # Automatically invokes the setter for validation!

        @property
        def salary(self) -> float:
            """Getter: Returns current salary"""
            return self._salary

        @salary.setter
        def salary(self, value: float):
            """Setter: Validates salary before assignment"""
            if not isinstance(value, (int, float)):
                raise TypeError("Salary must be a numerical value!")
            if value < 0:
                raise ValueError("Salary cannot be negative!")
            self._salary = float(value)

        @salary.deleter
        def salary(self):
            """Deleter: Cleanly resets salary"""
            print("  [Deleter triggered]: Resetting salary to 0.0")
            self._salary = 0.0

    emp = Employee("Rahul Sharma", 75000)
    print(f"Initial Salary: Rs. {emp.salary:,.2f}")

    emp.salary = 90000
    print(f"Updated Salary: Rs. {emp.salary:,.2f}")

    print("\n[Attempting invalid negative salary update]:")
    try:
        emp.salary = -5000
    except ValueError as e:
        print(f"  Validation blocked invalid update: {e}")

    del emp.salary
    print(f"Salary after deletion: Rs. {emp.salary:,.2f}")


# %% [markdown]
# ### 📌 Cell 3: Read-Only Computed Properties & Caching
# Properties can dynamically calculate values without storing redundant state.

# %% [code]
def cell_3():
    """Cell 3: Read-Only Computed Properties (Temperature Converter & Circle)"""
    print("=" * 60)
    print("▶ CELL 3: Read-Only Computed Properties (Circle & Temperature)")
    print("=" * 60)
    import math

    class Circle:
        def __init__(self, radius: float):
            self.radius = radius

        @property
        def radius(self) -> float:
            return self._radius

        @radius.setter
        def radius(self, value: float):
            if value <= 0:
                raise ValueError("Radius must be strictly positive!")
            self._radius = float(value)

        # Read-only computed property: No setter defined
        @property
        def area(self) -> float:
            return round(math.pi * (self._radius ** 2), 2)

        @property
        def circumference(self) -> float:
            return round(2 * math.pi * self._radius, 2)

    c = Circle(radius=5.0)
    print(f"Radius: {c.radius}")
    print(f"Computed Area: {c.area}")
    print(f"Computed Circumference: {c.circumference}")

    print("\n[Attempting to assign directly to computed property]:")
    try:
        c.area = 100.0  # Raises AttributeError because no setter exists
    except AttributeError as e:
        print(f"  Caught expected error: {e}")


# %% [markdown]
# ### 📌 Cell 4: Real-World Banking Ledger with Full Encapsulation
# Encapsulating internal transaction history, maintaining audit logs, and exposing clean APIs.

# %% [code]
def cell_4():
    """Cell 4: Production-Grade Encapsulated Banking Ledger"""
    print("=" * 60)
    print("▶ CELL 4: Production-Grade Encapsulated Banking System")
    print("=" * 60)
    import datetime

    class SecureLedgerAccount:
        def __init__(self, account_id: str, initial_deposit: float):
            self.__account_id = account_id
            self.__balance = 0.0
            self.__transaction_log = []
            if initial_deposit > 0:
                self.deposit(initial_deposit, note="Initial Account Opening Deposit")

        @property
        def balance(self) -> float:
            return self.__balance

        @property
        def account_id(self) -> str:
            # Masked account ID for privacy
            return f"***-***-{self.__account_id[-4:]}"

        def deposit(self, amount: float, note: str = "Deposit") -> bool:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive!")
            self.__balance += amount
            self.__record_transaction(type="CREDIT", amount=amount, note=note)
            return True

        def withdraw(self, amount: float, note: str = "Withdrawal") -> bool:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive!")
            if amount > self.__balance:
                raise ValueError(f"Insufficient funds! Available: {self.__balance}")
            self.__balance -= amount
            self.__record_transaction(type="DEBIT", amount=amount, note=note)
            return True

        def __record_transaction(self, type: str, amount: float, note: str):
            """Private method: Internal audit trail recording"""
            record = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "type": type,
                "amount": amount,
                "balance_after": self.__balance,
                "note": note
            }
            self.__transaction_log.append(record)

        def print_statement(self):
            print(f"\n--- Statement for Account: {self.account_id} ---")
            print(f"Current Balance: Rs. {self.balance:,.2f}")
            print("Transaction History:")
            for tx in self.__transaction_log:
                print(f"  [{tx['timestamp']}] {tx['type']:<6} Rs. {tx['amount']:>8,.2f} | Balance: Rs. {tx['balance_after']:>8,.2f} ({tx['note']})")

    acc = SecureLedgerAccount("ACC-9823471029", initial_deposit=5000.0)
    acc.deposit(12500.0, note="Salary Credit")
    acc.withdraw(3200.0, note="Grocery Shopping")
    acc.print_statement()


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Public, Protected & Private Name Mangling", cell_1),
    2: ("@property Getters, Setters & Data Validation", cell_2),
    3: ("Read-Only Computed Properties (Circle/Math)", cell_3),
    4: ("Secure Encapsulated Banking Ledger", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 02_ENCAPSULATION_INTERACTIVE.PY")
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
                print("Usage: python 02_encapsulation_interactive.py [cell_number | --all]")
    else:
        run_all()
