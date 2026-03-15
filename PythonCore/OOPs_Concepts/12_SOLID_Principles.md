# SOLID Principles in Object-Oriented Design

## Introduction

SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable. These principles were introduced by Robert C. Martin (Uncle Bob) and are fundamental to good object-oriented design.

The SOLID principles are:
- **S**: Single Responsibility Principle (SRP)
- **O**: Open/Closed Principle (OCP)
- **L**: Liskov Substitution Principle (LSP)
- **I**: Interface Segregation Principle (ISP)
- **D**: Dependency Inversion Principle (DIP)

## S - Single Responsibility Principle (SRP)

A class should have only one reason to change, meaning it should have only one job or responsibility.

### Violation of SRP

```python
class Employee:
    """This class violates SRP - it has multiple responsibilities"""
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def calculate_payroll(self):
        """Responsibility 1: Calculate payroll"""
        # Complex payroll calculation logic
        return f"Calculated payroll for {self.name}"
    
    def save_to_database(self):
        """Responsibility 2: Save to database"""
        # Database saving logic
        return f"Saved {self.name} to database"
    
    def generate_report(self):
        """Responsibility 3: Generate reports"""
        # Report generation logic
        return f"Generated report for {self.name}"

# This class has multiple reasons to change
```

### Following SRP

```python
class Employee:
    """Employee class - only handles employee data"""
    
    def __init__(self, name, id, hourly_rate=20):
        self.name = name
        self.id = id
        self.hourly_rate = hourly_rate

class PayrollCalculator:
    """Only handles payroll calculations"""
    
    def calculate_payroll(self, employee, hours_worked):
        return employee.hourly_rate * hours_worked

class EmployeeRepository:
    """Only handles database operations for employees"""
    
    def save(self, employee):
        # Database saving logic
        return f"Saved {employee.name} to database"
    
    def find_by_id(self, emp_id):
        # Database retrieval logic
        return f"Retrieved employee with ID {emp_id}"

class ReportGenerator:
    """Only handles report generation"""
    
    def generate_employee_report(self, employee):
        return f"Report for {employee.name}: ID {employee.id}"

# Usage
employee = Employee("John Doe", 123)
payroll_calc = PayrollCalculator()
repo = EmployeeRepository()
report_gen = ReportGenerator()

payroll = payroll_calc.calculate_payroll(employee, 40)
print(payroll)  # Output: 800 (assuming $20/hour for 40 hours)
print(repo.save(employee))
print(report_gen.generate_employee_report(employee))
```

## O - Open/Closed Principle (OCP)

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification.

### Violation of OCP

```python
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

class AreaCalculator:
    """This class violates OCP - needs modification for new shapes"""
    
    def calculate_area(self, shape):
        if shape.shape_type == "rectangle":
            # Calculate rectangle area
            return shape.width * shape.height
        elif shape.shape_type == "circle":
            # Calculate circle area
            return 3.14159 * shape.radius ** 2
        elif shape.shape_type == "triangle":
            # Calculate triangle area
            return 0.5 * shape.base * shape.height
        # If we add a new shape, we need to modify this method
```

### Following OCP

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class - open for extension"""
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class AreaCalculator:
    """Closed for modification, open for extension"""
    
    def calculate_total_area(self, shapes):
        total = 0
        for shape in shapes:
            total += shape.area()  # Polymorphism allows extension without modification
        return total

# Usage - we can add new shapes without modifying AreaCalculator
shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 4)]
calculator = AreaCalculator()
print(f"Total area: {calculator.calculate_total_area(shapes)}")

# Adding a new shape doesn't require modifying AreaCalculator
class Pentagon(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        # Approximate area of regular pentagon
        return 1.72 * self.side_length ** 2

shapes.append(Pentagon(5))
print(f"Total area with pentagon: {calculator.calculate_total_area(shapes)}")
```

## L - Liskov Substitution Principle (LSP)

Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

### Violation of LSP

```python
class Bird:
    def fly(self):
        return "Flying high!"

class Ostrich(Bird):
    def fly(self):
        raise Exception("Ostriches can't fly!")  # This violates LSP

# This breaks LSP because replacing Bird with Ostrich causes an exception
def make_bird_fly(bird):
    return bird.fly()

# This would cause an error:
# ostrich = Ostrich()
# make_bird_fly(ostrich)  # Raises exception
```

### Following LSP

```python
from abc import ABC, abstractmethod

class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class SwimmingBird(ABC):
    @abstractmethod
    def swim(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow is flying!"

class Penguin(SwimmingBird):
    def swim(self):
        return "Penguin is swimming!"

class Duck(FlyingBird, SwimmingBird):
    def fly(self):
        return "Duck is flying!"
    
    def swim(self):
        return "Duck is swimming!"

def make_flying_bird_fly(bird):
    """Works with any FlyingBird subclass"""
    return bird.fly()

def make_swimming_bird_swim(bird):
    """Works with any SwimmingBird subclass"""
    return bird.swim()

# Usage
sparrow = Sparrow()
duck = Duck()
penguin = Penguin()

print(make_flying_bird_fly(sparrow))  # Output: Sparrow is flying!
print(make_flying_bird_fly(duck))      # Output: Duck is flying!
print(make_swimming_bird_swim(duck))   # Output: Duck is swimming!
print(make_swimming_bird_swim(penguin)) # Output: Penguin is swimming!
```

## I - Interface Segregation Principle (ISP)

Clients should not be forced to depend on interfaces they do not use. Many specific interfaces are better than one general-purpose interface.

### Violation of ISP

```python
from abc import ABC, abstractmethod

class MultiFunctionPrinter(ABC):
    """This interface forces all printers to implement all methods"""
    
    @abstractmethod
    def print_document(self, document):
        pass
    
    @abstractmethod
    def scan_document(self, document):
        pass
    
    @abstractmethod
    def fax_document(self, document):
        pass

class SimplePrinter(MultiFunctionPrinter):
    """Simple printer can only print, but must implement all methods"""
    
    def print_document(self, document):
        return f"Printing: {document}"
    
    def scan_document(self, document):
        raise NotImplementedError("Simple printer cannot scan")
    
    def fax_document(self, document):
        raise NotImplementedError("Simple printer cannot fax")

# This violates ISP - SimplePrinter is forced to implement methods it doesn't use
```

### Following ISP

```python
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax_document(self, document):
        pass

class SimplePrinter(Printer):
    """Only implements what it needs"""
    
    def print_document(self, document):
        return f"Printing: {document}"

class MultiFunctionDevice(Printer, Scanner, FaxMachine):
    """Can implement multiple interfaces"""
    
    def print_document(self, document):
        return f"Multi-device printing: {document}"
    
    def scan_document(self, document):
        return f"Multi-device scanning: {document}"
    
    def fax_document(self, document):
        return f"Multi-device faxing: {document}"

# Usage
simple_printer = SimplePrinter()
multi_device = MultiFunctionDevice()

print(simple_printer.print_document("My Document"))
print(multi_device.print_document("Another Document"))
print(multi_device.scan_document("Scan This"))
```

## D - Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

### Violation of DIP

```python
class EmailService:
    """Low-level module"""
    
    def send_email(self, recipient, message):
        return f"Email sent to {recipient}: {message}"

class SMSNotification:
    """Low-level module"""
    
    def send_sms(self, phone, message):
        return f"SMS sent to {phone}: {message}"

class NotificationManager:
    """High-level module - directly depends on low-level modules"""
    
    def __init__(self):
        # Direct dependency on low-level modules
        self.email_service = EmailService()
        self.sms_service = SMSNotification()
    
    def notify_by_email(self, recipient, message):
        return self.email_service.send_email(recipient, message)
    
    def notify_by_sms(self, phone, message):
        return self.sms_service.send_sms(phone, message)

# This violates DIP - high-level module depends on low-level modules
```

### Following DIP

```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    """Abstraction"""
    
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailService(NotificationService):
    """Low-level module depends on abstraction"""
    
    def send(self, recipient, message):
        return f"Email sent to {recipient}: {message}"

class SMSService(NotificationService):
    """Low-level module depends on abstraction"""
    
    def send(self, recipient, message):
        return f"SMS sent to {recipient}: {message}"

class PushNotificationService(NotificationService):
    """Easy to add new notification service"""
    
    def send(self, recipient, message):
        return f"Push notification sent to {recipient}: {message}"

class NotificationManager:
    """High-level module depends on abstraction, not implementation"""
    
    def __init__(self, notification_service: NotificationService):
        # Depends on abstraction, not concrete implementation
        self.notification_service = notification_service
    
    def notify(self, recipient, message):
        return self.notification_service.send(recipient, message)

# Usage - high-level module doesn't need to change when adding new services
email_notifier = NotificationManager(EmailService())
sms_notifier = NotificationManager(SMSService())
push_notifier = NotificationManager(PushNotificationService())

print(email_notifier.notify("user@example.com", "Hello!"))
print(sms_notifier.notify("+1234567890", "Hello!"))
print(push_notifier.notify("device_token", "Hello!"))
```

## Complete Example: Applying All SOLID Principles

```python
from abc import ABC, abstractmethod
from enum import Enum

# S - Single Responsibility: Each class has one clear purpose

class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class User:
    """Handles user data only"""
    
    def __init__(self, username, role=UserRole.USER):
        self.username = username
        self.role = role

# O - Open/Closed: Easy to add new user types without modifying existing code
class UserPermissionChecker(ABC):
    """Open for extension, closed for modification"""
    
    @abstractmethod
    def can_access_resource(self, user, resource):
        pass

class AdminPermissionChecker(UserPermissionChecker):
    def can_access_resource(self, user, resource):
        return user.role == UserRole.ADMIN

class StandardPermissionChecker(UserPermissionChecker):
    def can_access_resource(self, user, resource):
        return user.role in [UserRole.ADMIN, UserRole.USER]

# L - Liskov Substitution: All subclasses can substitute the parent
class ResourceAccessManager:
    """Works with any UserPermissionChecker implementation"""
    
    def __init__(self, permission_checker: UserPermissionChecker):
        self.permission_checker = permission_checker
    
    def check_access(self, user, resource):
        return self.permission_checker.can_access_resource(user, resource)

# I - Interface Segregation: Specific interfaces for specific needs
class DataReader(ABC):
    @abstractmethod
    def read_data(self, source):
        pass

class DataWriter(ABC):
    @abstractmethod
    def write_data(self, destination, data):
        pass

class FileReader(DataReader):
    def read_data(self, source):
        return f"Reading data from file: {source}"

class FileWriter(DataWriter):
    def write_data(self, destination, data):
        return f"Writing data to file: {destination}: {data}"

# D - Dependency Inversion: High-level module depends on abstraction
class DataManager:
    """High-level module depending on abstractions"""
    
    def __init__(self, reader: DataReader, writer: DataWriter):
        self.reader = reader
        self.writer = writer
    
    def transfer_data(self, source, destination):
        data = self.reader.read_data(source)
        return self.writer.write_data(destination, data)

# Usage
user = User("john_doe", UserRole.USER)
admin = User("admin_user", UserRole.ADMIN)

# Different permission checkers (OCP)
standard_checker = StandardPermissionChecker()
admin_checker = AdminPermissionChecker()

# Using different checkers (LSP)
access_manager = ResourceAccessManager(standard_checker)
print(access_manager.check_access(user, "resource1"))  # True
print(access_manager.check_access(admin, "resource1"))  # True

# Using data manager with specific readers/writers (ISP & DIP)
file_manager = DataManager(FileReader(), FileWriter())
result = file_manager.transfer_data("input.txt", "output.txt")
print(result)
```

## Benefits of SOLID Principles

1. **Maintainability**: Code is easier to modify and extend
2. **Testability**: Smaller, focused classes are easier to test
3. **Flexibility**: Easy to swap implementations
4. **Readability**: Clear separation of concerns makes code more understandable
5. **Scalability**: Systems can grow without becoming unwieldy

## Summary

The SOLID principles provide a foundation for creating maintainable, scalable, and robust object-oriented software:

- **Single Responsibility**: One reason to change per class
- **Open/Closed**: Extend behavior without modifying code
- **Liskov Substitution**: Subtypes should be substitutable for their base types
- **Interface Segregation**: Small, focused interfaces are better than large ones
- **Dependency Inversion**: Depend on abstractions, not concretions

Following these principles leads to more flexible, maintainable, and testable code, though they should be applied thoughtfully rather than rigidly.