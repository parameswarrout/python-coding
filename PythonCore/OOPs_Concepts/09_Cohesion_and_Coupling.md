# Cohesion and Coupling in Object-Oriented Programming

## Introduction

Cohesion and coupling are two fundamental principles in software engineering that help evaluate the quality of class design and system architecture. These principles guide developers toward creating maintainable, reusable, and understandable code.

## Cohesion

Cohesion refers to how closely related and focused the responsibilities of a single module (class, function, etc.) are. High cohesion means that a class or module has a single, well-defined purpose with all its methods and attributes supporting that purpose.

### Types of Cohesion

#### 1. High Cohesion (Desirable)

**Functional Cohesion**: All elements of a module work together to perform a single, well-defined task.

```python
class Calculator:
    """High cohesion - all methods relate to mathematical calculations"""
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        return base ** exponent

# Usage
calc = Calculator()
print(calc.add(5, 3))      # Output: 8
print(calc.multiply(4, 7)) # Output: 28
```

**Sequential Cohesion**: Elements contribute to a sequence of operations where the output of one element becomes the input of the next.

```python
class DataProcessor:
    """High cohesion - methods form a sequence of data processing steps"""
    
    def read_data(self, source):
        """Read data from source"""
        return f"Data from {source}"
    
    def clean_data(self, raw_data):
        """Clean the raw data"""
        return raw_data.replace(" ", "_").lower()
    
    def process_data(self, cleaned_data):
        """Process the cleaned data"""
        return f"Processed: {cleaned_data}"
    
    def save_data(self, processed_data, destination):
        """Save processed data to destination"""
        return f"Saved {processed_data} to {destination}"

# Usage
processor = DataProcessor()
raw = processor.read_data("database")
clean = processor.clean_data(raw)
processed = processor.process_data(clean)
result = processor.save_data(processed, "file.txt")
print(result)  # Output: Saved Processed: data_from_database to file.txt
```

#### 2. Low Cohesion (Undesirable)

**Coincidental Cohesion**: Elements are grouped arbitrarily with no meaningful relationship.

```python
class PoorlyDesignedClass:
    """Low cohesion - unrelated methods grouped together"""
    
    def calculate_tax(self, income):
        """Financial calculation"""
        return income * 0.1
    
    def send_email(self, recipient, message):
        """Communication function"""
        return f"Email sent to {recipient}"
    
    def format_date(self, date_str):
        """Date formatting"""
        return f"Formatted: {date_str}"
    
    def compress_image(self, image_path):
        """Image processing"""
        return f"Compressed: {image_path}"

# This class violates the Single Responsibility Principle
# It has multiple reasons to change
```

**Logical Cohesion**: Elements perform similar functions but are grouped logically rather than functionally.

```python
class InputHandler:
    """Medium cohesion - similar but not related operations"""
    
    def handle_mouse_click(self):
        return "Mouse clicked"
    
    def handle_keyboard_input(self):
        return "Keyboard pressed"
    
    def handle_touch_gesture(self):
        return "Touch gesture detected"
    
    def handle_voice_command(self):
        return "Voice command received"
    
    def handle_sensor_data(self):
        return "Sensor data processed"

# While these are all input-related, they might belong in separate classes
```

### Benefits of High Cohesion

1. **Maintainability**: Changes are localized to a single module
2. **Reusability**: Highly cohesive modules are more likely to be reusable
3. **Testability**: Modules with a single purpose are easier to test
4. **Readability**: Code is easier to understand when each module has a clear purpose

## Coupling

Coupling refers to the degree of interdependence between modules (classes, functions, etc.). Low coupling means that modules are minimally dependent on each other, which is desirable.

### Types of Coupling

#### 1. Low Coupling (Desirable)

**Loose Coupling with Dependency Injection**: Dependencies are injected rather than hardcoded.

```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailService(NotificationService):
    def send_notification(self, message):
        return f"Email sent: {message}"

class SMSService(NotificationService):
    def send_notification(self, message):
        return f"SMS sent: {message}"

class OrderProcessor:
    """Low coupling - depends on abstraction, not concrete implementation"""
    
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
    
    def process_order(self, order_details):
        # Process the order
        result = f"Order processed: {order_details}"
        
        # Send notification using injected service
        notification = self.notification_service.send_notification(
            f"Order {order_details} processed successfully"
        )
        
        return result, notification

# Usage - can easily swap notification services
email_service = EmailService()
sms_service = SMSService()

order_processor_with_email = OrderProcessor(email_service)
order_processor_with_sms = OrderProcessor(sms_service)

print(order_processor_with_email.process_order("Laptop"))
print(order_processor_with_sms.process_order("Phone"))
```

**Interface-based Coupling**: Classes depend on abstractions rather than concrete implementations.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class StripePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via Stripe"

class PayPalPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"

class ShoppingCart:
    """Low coupling - depends on PaymentProcessor interface"""
    
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
        self.items = []
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def checkout(self):
        total = sum(price for item, price in self.items)
        return self.payment_processor.process_payment(total)

# Usage - can easily switch payment processors
stripe_processor = StripePaymentProcessor()
paypal_processor = PayPalPaymentProcessor()

cart1 = ShoppingCart(stripe_processor)
cart2 = ShoppingCart(paypal_processor)

cart1.add_item("Book", 29.99)
cart2.add_item("Game", 59.99)

print(cart1.checkout())  # Output: Processing $29.99 via Stripe
print(cart2.checkout())  # Output: Processing $59.99 via PayPal
```

#### 2. High Coupling (Undesirable)

**Tight Coupling with Concrete Dependencies**: Classes depend directly on specific implementations.

```python
class EmailService:
    def send_email(self, recipient, subject, body):
        return f"Email to {recipient}: {subject} - {body}"

class Customer:
    """High coupling - directly depends on EmailService"""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Direct instantiation creates tight coupling
        self.email_service = EmailService()
    
    def notify_order(self, order_details):
        return self.email_service.send_email(
            self.email,
            "Order Confirmation",
            f"Thank you for your order: {order_details}"
        )

# Problems with this approach:
# 1. Cannot easily change notification method
# 2. Difficult to test without sending real emails
# 3. Customer class is tightly coupled to EmailService
```

**Global Variable Coupling**: Classes depend on global state.

```python
# Global configuration - creates coupling
config = {
    'api_key': 'secret_key',
    'debug_mode': True,
    'database_url': 'localhost:5432'
}

class APIClient:
    """High coupling - depends on global config"""
    
    def make_request(self, endpoint):
        # Depends on global variable
        api_key = config['api_key']
        debug = config['debug_mode']
        
        return f"Request to {endpoint} with key {api_key}, debug={debug}"

class DatabaseManager:
    """High coupling - also depends on global config"""
    
    def connect(self):
        # Also depends on global variable
        db_url = config['database_url']
        return f"Connecting to {db_url}"

# This creates tight coupling between classes and global state
```

### Benefits of Low Coupling

1. **Maintainability**: Changes in one module don't affect others
2. **Flexibility**: Modules can be modified or replaced independently
3. **Testability**: Modules can be tested in isolation
4. **Reusability**: Loosely coupled modules are more reusable in different contexts

## Balancing Cohesion and Coupling

### The Ideal Balance

The goal is to achieve high cohesion and low coupling simultaneously:

```python
from abc import ABC, abstractmethod

# High cohesion: Logger class focuses solely on logging
class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        return f"[FILE] {message}"

class ConsoleLogger(Logger):
    def log(self, message):
        return f"[CONSOLE] {message}"

# High cohesion: PaymentValidator focuses solely on validation
class PaymentValidator:
    def validate_amount(self, amount):
        return amount > 0
    
    def validate_card_number(self, card_number):
        return len(card_number) == 16 and card_number.isdigit()

# Low coupling: PaymentProcessor depends on Logger abstraction
class PaymentProcessor:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.validator = PaymentValidator()
    
    def process_payment(self, amount, card_number):
        # Validate inputs
        if not self.validator.validate_amount(amount):
            self.logger.log("Invalid amount")
            return False
        
        if not self.validator.validate_card_number(card_number):
            self.logger.log("Invalid card number")
            return False
        
        # Process payment
        self.logger.log(f"Processing payment of ${amount}")
        return True

# Usage - high cohesion, low coupling
console_logger = ConsoleLogger()
file_logger = FileLogger()

processor1 = PaymentProcessor(console_logger)
processor2 = PaymentProcessor(file_logger)

print(processor1.process_payment(100, "1234567890123456"))
print(processor2.process_payment(50, "invalid_card"))
```

## Practical Examples

### Example 1: Refactoring from Low to High Cohesion

**Before (Low Cohesion):**

```python
class UtilityClass:
    """Poor cohesion - handles multiple unrelated tasks"""
    
    def calculate_area(self, length, width):
        return length * width
    
    def send_message(self, recipient, message):
        return f"Message to {recipient}: {message}"
    
    def format_currency(self, amount):
        return f"${amount:.2f}"
    
    def hash_password(self, password):
        return f"hashed_{password}"
    
    def resize_image(self, image_path, width, height):
        return f"Resized {image_path} to {width}x{height}"
```

**After (High Cohesion):**

```python
class GeometryCalculator:
    """High cohesion - only geometry calculations"""
    
    def calculate_rectangle_area(self, length, width):
        return length * width
    
    def calculate_circle_area(self, radius):
        return 3.14159 * radius ** 2

class MessageService:
    """High cohesion - only messaging functions"""
    
    def send_message(self, recipient, message):
        return f"Message to {recipient}: {message}"

class CurrencyFormatter:
    """High cohesion - only currency formatting"""
    
    def format_usd(self, amount):
        return f"${amount:.2f}"
    
    def format_eur(self, amount):
        return f"€{amount:.2f}"

class SecurityUtils:
    """High cohesion - only security-related functions"""
    
    def hash_password(self, password):
        return f"hashed_{password}"
    
    def verify_password(self, password, hashed):
        return f"hashed_{password}" == hashed
```

### Example 2: Reducing Coupling

**Before (High Coupling):**

```python
class DatabaseConnection:
    def connect(self):
        return "Connected to database"

class UserRepository:
    def __init__(self):
        # Tight coupling - hardcoded dependency
        self.db = DatabaseConnection()
    
    def save_user(self, user_data):
        self.db.connect()  # Direct dependency
        return f"User saved: {user_data}"

class UserService:
    def __init__(self):
        # Tight coupling - hardcoded dependency
        self.user_repo = UserRepository()
    
    def register_user(self, user_data):
        return self.user_repo.save_user(user_data)
```

**After (Low Coupling):**

```python
from abc import ABC, abstractmethod

class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

class DatabaseConnection(DatabaseInterface):
    def connect(self):
        return "Connected to database"

class MockDatabaseConnection(DatabaseInterface):
    def connect(self):
        return "Connected to mock database"

class UserRepository:
    def __init__(self, db_connection: DatabaseInterface):
        # Low coupling - depends on interface
        self.db = db_connection
    
    def save_user(self, user_data):
        self.db.connect()
        return f"User saved: {user_data}"

class UserService:
    def __init__(self, user_repository: UserRepository):
        # Low coupling - depends on repository interface
        self.user_repo = user_repository
    
    def register_user(self, user_data):
        return self.user_repo.save_user(user_data)

# Usage - can easily swap implementations
real_db = DatabaseConnection()
mock_db = MockDatabaseConnection()

real_repo = UserRepository(real_db)
mock_repo = UserRepository(mock_db)

real_service = UserService(real_repo)
mock_service = UserService(mock_repo)

print(real_service.register_user("John Doe"))
print(mock_service.register_user("Jane Doe"))
```

## Best Practices

### For High Cohesion:
1. Apply the Single Responsibility Principle (SRP)
2. Group related methods and attributes together
3. Ensure each class has a clear, single purpose
4. Use meaningful class and method names that reflect their purpose

### For Low Coupling:
1. Depend on abstractions rather than concrete implementations
2. Use dependency injection
3. Minimize direct dependencies between classes
4. Use interfaces and protocols to define contracts
5. Avoid global variables and state
6. Apply the Dependency Inversion Principle (DIP)

## Measuring Cohesion and Coupling

### Signs of Good Design:
- Each class has a clear, single responsibility
- Classes have few dependencies on other classes
- Changes to one class rarely require changes to others
- Classes are easy to test in isolation
- Code is reusable in different contexts

### Signs of Poor Design:
- Classes have many responsibilities
- Classes depend on many other classes
- Changes to one class often require changes to others
- Classes are difficult to test in isolation
- Code is hard to reuse

## Conclusion

Cohesion and coupling are fundamental principles that significantly impact the quality of object-oriented designs. High cohesion ensures that each module has a clear, focused purpose, while low coupling ensures that modules can evolve independently. Together, they promote maintainable, testable, and reusable code.

Striving for high cohesion and low coupling should be a primary goal in software design. While achieving the perfect balance can be challenging, consistently applying these principles leads to more robust and maintainable systems.