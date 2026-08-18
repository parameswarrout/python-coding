import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from abc import ABC, abstractmethod

"""
=============================================================================
🧩 OOP CONCEPTS: ABSTRACTION (Interactive Cell-by-Cell Notebook in .py)
=============================================================================
HOW TO RUN:
1. Run everything:
   python 04_abstraction_interactive.py
2. Run a specific cell (e.g., Cell 2):
   python 04_abstraction_interactive.py 2
3. In VS Code / PyCharm: Click 'Run Cell' above any `# %%` marker!
=============================================================================
"""

# %% [markdown]
# ### 📌 Cell 1: Abstract Base Classes (ABC) & Enforcement of Contracts
# An Abstract Class defines WHAT methods must exist without detailing HOW they work.
# Any subclass that fails to implement all `@abstractmethod`s CANNOT be instantiated (TypeError).

# %% [code]
def cell_1():
    """Cell 1: ABC Contract Enforcement with Payment Gateways"""
    print("=" * 60)
    print("▶ CELL 1: Abstract Base Classes (Payment Gateway Contract)")
    print("=" * 60)

    class PaymentGateway(ABC):
        @abstractmethod
        def authenticate(self, api_key: str) -> bool:
            """Authenticate with gateway"""
            pass

        @abstractmethod
        def process_payment(self, amount: float, currency: str) -> str:
            """Process the financial transaction"""
            pass

    class StripeGateway(PaymentGateway):
        def authenticate(self, api_key: str) -> bool:
            return api_key.startswith("sk_live_")

        def process_payment(self, amount: float, currency: str) -> str:
            return f"[Stripe] Successfully charged {amount} {currency}."

    class IncompleteGateway(PaymentGateway):
        # Missing process_payment() implementation!
        def authenticate(self, api_key: str) -> bool:
            return True

    print("[Instantiating Valid Implementation (StripeGateway)]:")
    stripe = StripeGateway()
    print("  Auth status:", stripe.authenticate("sk_live_992138401"))
    print("  Payment:", stripe.process_payment(2500.0, "USD"))

    print("\n[Attempting to instantiate IncompleteGateway]:")
    try:
        incomplete = IncompleteGateway()
    except TypeError as e:
        print(f"  Python strictly blocked instantiation:\n  -> {e}")


# %% [markdown]
# ### 📌 Cell 2: Abstract Properties (`@property` + `@abstractmethod`)
# Enforcing that subclasses must provide specific computed or stored properties.

# %% [code]
def cell_2():
    """Cell 2: Abstract Properties (Database Connector)"""
    print("=" * 60)
    print("▶ CELL 2: Abstract Properties (@property + @abstractmethod)")
    print("=" * 60)

    class DatabaseConnector(ABC):
        @property
        @abstractmethod
        def connection_string(self) -> str:
            """Subclass must define its specific connection URL"""
            pass

        @abstractmethod
        def execute_query(self, sql: str) -> list:
            pass

    class PostgreSQLConnector(DatabaseConnector):
        def __init__(self, host: str, port: int, db: str, user: str):
            self.host = host
            self.port = port
            self.db = db
            self.user = user

        @property
        def connection_string(self) -> str:
            return f"postgresql://{self.user}@{self.host}:{self.port}/{self.db}"

        def execute_query(self, sql: str) -> list:
            return [{"status": "success", "query": sql, "engine": "PostgreSQL"}]

    pg = PostgreSQLConnector("localhost", 5432, "production_db", "admin")
    print(f"Connection URI: {pg.connection_string}")
    print(f"Query Result:   {pg.execute_query('SELECT * FROM users LIMIT 5;')}")


# %% [markdown]
# ### 📌 Cell 3: Template Method Pattern with Abstraction
# An abstract base class defines the skeleton of an algorithm in a concrete method (`generate_report`),
# while deferring specific steps (`fetch_data`, `format_body`) to subclasses.

# %% [code]
def cell_3():
    """Cell 3: Template Method Pattern (Data Report Generator)"""
    print("=" * 60)
    print("▶ CELL 3: Template Method Pattern (Automated Report Generator)")
    print("=" * 60)

    class ReportGenerator(ABC):
        def generate(self):
            """Template Method: Defines invariant skeleton algorithm"""
            print("  --- BEGIN REPORT GENERATION ---")
            self._print_header()
            data = self._fetch_data()
            self._format_content(data)
            self._print_footer()
            print("  --- REPORT GENERATION COMPLETE ---\n")

        def _print_header(self):
            print("  [Header] Enterprise System Analytics Report")

        def _print_footer(self):
            print("  [Footer] Confidential - Generated Automatically")

        # Hook / Abstract steps that subclasses must customize
        @abstractmethod
        def _fetch_data(self) -> list:
            pass

        @abstractmethod
        def _format_content(self, data: list):
            pass

    class FinancialQuarterlyReport(ReportGenerator):
        def _fetch_data(self) -> list:
            return [("Revenue", "$4.2M"), ("Expenses", "$2.8M"), ("Net Profit", "$1.4M")]

        def _format_content(self, data: list):
            print("  [Body: Financial Metrics]")
            for k, v in data:
                print(f"    * {k:<12}: {v}")

    class SecurityAuditReport(ReportGenerator):
        def _fetch_data(self) -> list:
            return ["0 Critical Vulnerabilities", "2 Low Warnings Resolved", "100% 2FA Adoption"]

        def _format_content(self, data: list):
            print("  [Body: Security Status]")
            for item in data:
                print(f"    * {item}")

    fin_report = FinancialQuarterlyReport()
    fin_report.generate()

    sec_report = SecurityAuditReport()
    sec_report.generate()


# %% [markdown]
# ### 📌 Cell 4: Dependency Injection via Abstract Interface
# High-level modules should not depend on low-level modules; both should depend on abstractions (DIP).

# %% [code]
def cell_4():
    """Cell 4: Dependency Inversion Principle (Notification System)"""
    print("=" * 60)
    print("▶ CELL 4: Dependency Injection with Abstract Interfaces")
    print("=" * 60)

    class NotificationSender(ABC):
        @abstractmethod
        def send(self, recipient: str, message: str) -> bool:
            pass

    class EmailNotificationSender(NotificationSender):
        def send(self, recipient: str, message: str) -> bool:
            print(f"  [SMTP Email -> {recipient}]: {message}")
            return True

    class SMSNotificationSender(NotificationSender):
        def send(self, recipient: str, message: str) -> bool:
            print(f"  [Twilio SMS -> {recipient}]: {message}")
            return True

    # High-level service depends solely on the NotificationSender abstraction
    class UserAlertService:
        def __init__(self, sender: NotificationSender):
            self.sender = sender

        def notify_user_login(self, user_contact: str, ip: str):
            msg = f"Security Alert: New login detected from IP {ip}."
            self.sender.send(user_contact, msg)

    print("[Injecting Email Sender]:")
    email_service = UserAlertService(EmailNotificationSender())
    email_service.notify_user_login("admin@company.com", "192.168.1.100")

    print("\n[Injecting SMS Sender without modifying UserAlertService]:")
    sms_service = UserAlertService(SMSNotificationSender())
    sms_service.notify_user_login("+1-555-0144", "192.168.1.100")


# =============================================================================
# INTERACTIVE CELL EXECUTION RUNNER
# =============================================================================
CELLS = {
    1: ("Abstract Base Classes (ABC Contract Enforcement)", cell_1),
    2: ("Abstract Properties (@property + @abstractmethod)", cell_2),
    3: ("Template Method Design Pattern", cell_3),
    4: ("Dependency Injection via Abstract Interfaces", cell_4),
}


def run_all():
    print("\n" + "#" * 70)
    print("🚀 RUNNING ALL CELLS IN 04_ABSTRACTION_INTERACTIVE.PY")
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
                print("Usage: python 04_abstraction_interactive.py [cell_number | --all]")
    else:
        run_all()
