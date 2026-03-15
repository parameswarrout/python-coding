# Mixins and Method Types in Python

## Part 1: Mixins

### Introduction to Mixins

Mixins are a design pattern that allows you to compose classes by combining multiple smaller, focused classes. A mixin is a class that provides methods to other classes but isn't meant to be instantiated on its own. Mixins are typically used to add functionality to classes without using traditional inheritance.

### Characteristics of Mixins

1. **Provide specific functionality**: Each mixin focuses on a single aspect of functionality
2. **Not meant for standalone use**: Mixins are designed to be combined with other classes
3. **Promote code reuse**: Common functionality can be shared across unrelated classes
4. **Enable multiple inheritance**: Mixins make multiple inheritance more manageable

### Basic Mixin Example

```python
class TimestampMixin:
    """Mixin to add timestamp functionality to any class"""
    
    def add_timestamp(self):
        from datetime import datetime
        return datetime.now()

class StringMixin:
    """Mixin to add string manipulation functionality"""
    
    def capitalize_words(self, text):
        return ' '.join(word.capitalize() for word in text.split())
    
    def reverse_string(self, text):
        return text[::-1]

class LoggableMixin:
    """Mixin to add logging functionality"""
    
    def log(self, message):
        timestamp = self.add_timestamp()
        print(f"[{timestamp}] {message}")

# Using mixins by multiple inheritance
class User(TimestampMixin, StringMixin, LoggableMixin):
    def __init__(self, name):
        self.name = name
        self.created_at = self.add_timestamp()
    
    def display_name(self):
        return self.capitalize_words(self.name)

class Product(TimestampMixin, LoggableMixin):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.created_at = self.add_timestamp()
    
    def update_price(self, new_price):
        old_price = self.price
        self.price = new_price
        self.log(f"Price updated from {old_price} to {new_price}")

# Usage
user = User("john doe")
print(user.display_name())  # Output: John Doe
print(f"Created at: {user.created_at}")

product = Product("Laptop", 999.99)
product.update_price(899.99)
```

### Advanced Mixin Example

```python
class SerializableMixin:
    """Mixin to add serialization capabilities"""
    
    def to_dict(self):
        """Convert object attributes to dictionary"""
        result = {}
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):  # Skip private attributes
                if hasattr(value, 'to_dict'):
                    result[attr] = value.to_dict()
                else:
                    result[attr] = value
        return result
    
    def from_dict(self, data):
        """Load object attributes from dictionary"""
        for attr, value in data.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self

class ValidatableMixin:
    """Mixin to add validation capabilities"""
    
    def validate_required_fields(self, required_fields):
        """Validate that required fields are present and not empty"""
        errors = []
        for field in required_fields:
            if not hasattr(self, field) or not getattr(self, field):
                errors.append(f"Field '{field}' is required")
        return errors
    
    def validate_types(self, field_types):
        """Validate that fields have correct types"""
        errors = []
        for field, expected_type in field_types.items():
            if hasattr(self, field):
                value = getattr(self, field)
                if not isinstance(value, expected_type):
                    errors.append(f"Field '{field}' should be of type {expected_type.__name__}")
        return errors

class ComparableMixin:
    """Mixin to add comparison capabilities"""
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__
    
    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        # Compare based on first attribute alphabetically
        first_attr = sorted(self.__dict__.keys())[0] if self.__dict__ else None
        if first_attr:
            return getattr(self, first_attr, '') < getattr(other, first_attr, '')
        return False

class Person(SerializableMixin, ValidatableMixin, ComparableMixin):
    def __init__(self, name="", age=0, email=""):
        self.name = name
        self.age = age
        self.email = email
    
    def validate(self):
        """Validate the person object"""
        errors = []
        errors.extend(self.validate_required_fields(['name', 'email']))
        errors.extend(self.validate_types({'age': int, 'name': str, 'email': str}))
        return errors

# Usage
person1 = Person("Alice", 30, "alice@example.com")
person2 = Person("Bob", 25, "bob@example.com")

# Serialization
person_dict = person1.to_dict()
print("Serialized:", person_dict)

# Validation
errors = person1.validate()
if errors:
    print("Validation errors:", errors)
else:
    print("Person is valid")

# Comparison
print(f"Person1 == Person2: {person1 == person2}")
print(f"Person1 < Person2: {person1 < person2}")
```

### Mixin with Context Manager

```python
class ContextManagerMixin:
    """Mixin to add context manager capabilities"""
    
    def __enter__(self):
        print(f"Entering context for {self.__class__.__name__}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context for {self.__class__.__name__}")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}: {exc_val}")
        return False  # Don't suppress exceptions

class ResourceManager(ContextManagerMixin):
    def __init__(self, resource_name):
        self.resource_name = resource_name
        self.active = False
    
    def activate(self):
        self.active = True
        print(f"Resource {self.resource_name} activated")
    
    def deactivate(self):
        self.active = False
        print(f"Resource {self.resource_name} deactivated")

# Usage
resource = ResourceManager("Database Connection")
with resource:
    resource.activate()
    print("Doing some work...")
    # Resource will be automatically deactivated when exiting the context
```

### Mixin with Property

```python
class PropertyMixin:
    """Mixin to add computed properties"""
    
    @property
    def full_description(self):
        """Computed property that combines multiple attributes"""
        attrs = []
        for attr, value in self.__dict__.items():
            if not attr.startswith('_') and isinstance(value, (str, int, float)):
                attrs.append(f"{attr}: {value}")
        return ", ".join(attrs)

class Product(PropertyMixin):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

# Usage
product = Product("Laptop", 999.99, "Electronics")
print(product.full_description)  # Output: name: Laptop, price: 999.99, category: Electronics
```

## Part 2: Different Types of Methods in Python

Python provides three types of methods: instance methods, class methods, and static methods. Each serves a different purpose and has different access to the class and its instances.

### Instance Methods

Instance methods are the most common type of method in Python. They receive the instance as the first argument (conventionally named `self`) and can access both instance and class attributes.

```python
class BankAccount:
    bank_name = "Python Bank"  # Class attribute
    
    def __init__(self, owner, balance=0):
        self.owner = owner      # Instance attribute
        self.balance = balance  # Instance attribute
    
    def deposit(self, amount):
        """Instance method - operates on instance data"""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        """Instance method - operates on instance data"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount"
    
    def get_account_info(self):
        """Instance method - accesses both instance and class data"""
        return f"Owner: {self.owner}, Balance: ${self.balance}, Bank: {self.bank_name}"

# Usage
account = BankAccount("Alice", 1000)
print(account.deposit(500))           # Instance method call
print(account.get_account_info())     # Accesses both instance and class data
```

### Class Methods

Class methods receive the class as the first argument (conventionally named `cls`) instead of the instance. They can access class attributes but not instance attributes directly. Class methods are defined using the `@classmethod` decorator.

```python
class Employee:
    company = "Tech Corp"     # Class attribute
    employee_count = 0        # Class attribute to track employees
    
    def __init__(self, name, position):
        self.name = name              # Instance attribute
        self.position = position      # Instance attribute
        Employee.employee_count += 1  # Increment class attribute
    
    def get_info(self):
        """Instance method"""
        return f"{self.name} works as {self.position} at {self.company}"
    
    @classmethod
    def get_company_info(cls):
        """Class method - operates on class data"""
        return f"Company: {cls.company}, Employees: {cls.employee_count}"
    
    @classmethod
    def create_manager(cls, name):
        """Class method as alternative constructor"""
        return cls(name, "Manager")
    
    @classmethod
    def create_developer(cls, name):
        """Another class method as alternative constructor"""
        return cls(name, "Developer")

# Usage
emp1 = Employee("Alice", "Developer")
emp2 = Employee.create_manager("Bob")  # Using class method as constructor
emp3 = Employee.create_developer("Carol")  # Using class method as constructor

print(emp1.get_info())
print(Employee.get_company_info())  # Called on class
print(emp2.get_info())
print(Employee.get_company_info())  # Shows updated count
```

### Static Methods

Static methods don't receive any automatic first argument (neither `self` nor `cls`). They behave like regular functions but belong to the class namespace. Static methods are defined using the `@staticmethod` decorator.

```python
class MathUtils:
    PI = 3.14159
    
    @staticmethod
    def add(x, y):
        """Static method - behaves like a regular function"""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Static method - no access to self or cls"""
        return x * y
    
    @staticmethod
    def calculate_circle_area(radius):
        """Static method - utility function related to the class"""
        return MathUtils.PI * radius ** 2
    
    @staticmethod
    def is_even(number):
        """Static method - utility function"""
        return number % 2 == 0

# Usage - can be called on class or instance
print(MathUtils.add(5, 3))                    # Called on class
print(MathUtils.multiply(4, 7))               # Called on class

math_utils = MathUtils()
print(math_utils.add(10, 20))                 # Called on instance
print(MathUtils.calculate_circle_area(5))     # Utility function
print(MathUtils.is_even(42))                  # Utility function
```

### Comprehensive Example: Combining All Method Types

```python
class Calculator:
    """A calculator class demonstrating all three method types"""
    
    calculation_count = 0  # Class attribute
    pi = 3.14159
    
    def __init__(self, name="Default Calculator"):
        self.name = name  # Instance attribute
        self.history = [] # Instance attribute
    
    # Instance method
    def add(self, a, b):
        """Instance method - operates on instance data"""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        Calculator.calculation_count += 1
        return result
    
    # Instance method
    def get_history(self):
        """Instance method - returns instance-specific data"""
        return self.history.copy()
    
    # Class method
    @classmethod
    def get_calculation_count(cls):
        """Class method - operates on class data"""
        return cls.calculation_count
    
    # Class method
    @classmethod
    def reset_calculation_count(cls):
        """Class method - modifies class data"""
        cls.calculation_count = 0
        return "Calculation count reset"
    
    # Class method as alternative constructor
    @classmethod
    def scientific_calculator(cls):
        """Class method as alternative constructor"""
        calc = cls("Scientific Calculator")
        calc.is_scientific = True
        return calc
    
    # Static method
    @staticmethod
    def power(base, exponent):
        """Static method - pure function, no access to self or cls"""
        return base ** exponent
    
    # Static method
    @staticmethod
    def factorial(n):
        """Static method - utility function"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if n == 0 or n == 1:
            return 1
        return n * Calculator.factorial(n - 1)
    
    # Static method
    @staticmethod
    def circle_area(radius):
        """Static method - utility function using class constant"""
        return Calculator.pi * radius ** 2

# Usage examples
# Instance methods
calc1 = Calculator("My Calculator")
result1 = calc1.add(10, 5)
print(f"Result: {result1}")  # Output: Result: 15
print(f"History: {calc1.get_history()}")  # Output: History: ['10 + 5 = 15']

# Class methods
print(f"Total calculations: {Calculator.get_calculation_count()}")  # Output: Total calculations: 1
calc2 = Calculator()
calc2.add(7, 3)
print(f"Total calculations: {Calculator.get_calculation_count()}")  # Output: Total calculations: 2

# Alternative constructor
sci_calc = Calculator.scientific_calculator()
print(f"Scientific calc name: {sci_calc.name}")  # Output: Scientific calc name: Scientific Calculator
print(f"Is scientific: {sci_calc.is_scientific}")  # Output: Is scientific: True

# Static methods
print(f"2^8 = {Calculator.power(2, 8)}")  # Output: 2^8 = 256
print(f"5! = {Calculator.factorial(5)}")   # Output: 5! = 120
print(f"Circle area (radius=3): {Calculator.circle_area(3)}")  # Output: Circle area (radius=3): 28.27431
```

### When to Use Each Method Type

#### Instance Methods
- When you need to access or modify instance attributes
- When you need to access both instance and class attributes
- For the majority of methods in a class

#### Class Methods
- When you need to access or modify class attributes
- For alternative constructors
- When the method logically belongs to the class but doesn't need instance data
- For factory methods

#### Static Methods
- When the method is related to the class but doesn't need access to `self` or `cls`
- For utility functions that are conceptually related to the class
- When the function could be a standalone function but belongs in the class namespace

### Practical Example: Using All Concepts Together

```python
class DatabaseRecord:
    """Example combining mixins and different method types"""
    
    table_name = "records"  # Class attribute
    record_count = 0        # Class attribute
    
    def __init__(self, data):
        self.data = data
        self.id = DatabaseRecord.record_count
        DatabaseRecord.record_count += 1
        self.created_at = self.add_timestamp()
    
    # Instance method
    def update_data(self, new_data):
        """Update the record's data"""
        self.data = new_data
        return f"Record {self.id} updated"
    
    # Class method
    @classmethod
    def get_table_info(cls):
        """Get information about the table"""
        return f"Table: {cls.table_name}, Records: {cls.record_count}"
    
    # Static method
    @staticmethod
    def validate_data(data):
        """Validate data format"""
        return isinstance(data, dict) and len(data) > 0

class TimestampMixin:
    """Mixin to add timestamp functionality"""
    
    def add_timestamp(self):
        from datetime import datetime
        return datetime.now()

class SerializableMixin:
    """Mixin to add serialization functionality"""
    
    def to_json(self):
        import json
        return json.dumps({
            'id': self.id,
            'data': self.data,
            'created_at': str(self.created_at) if hasattr(self, 'created_at') else None
        })

class ValidatableMixin:
    """Mixin to add validation functionality"""
    
    def is_valid(self):
        return self.validate_data(self.data)

class UserRecord(DatabaseRecord, TimestampMixin, SerializableMixin, ValidatableMixin):
    """Concrete class using multiple mixins"""
    
    table_name = "users"
    
    def __init__(self, username, email):
        super().__init__({"username": username, "email": email})
    
    # Instance method
    def get_username(self):
        return self.data.get('username')

# Usage
user = UserRecord("alice", "alice@example.com")
print(f"Username: {user.get_username()}")
print(f"Valid: {user.is_valid()}")
print(f"JSON: {user.to_json()}")
print(f"Table info: {UserRecord.get_table_info()}")
print(f"Data valid: {UserRecord.validate_data({'key': 'value'})}")
```

## Summary

### Mixins
- Provide a way to add functionality to classes without deep inheritance hierarchies
- Promote code reuse and separation of concerns
- Enable multiple inheritance in a controlled way
- Should focus on a single responsibility

### Method Types
- **Instance methods**: Operate on instance data, receive `self` as first parameter
- **Class methods**: Operate on class data, receive `cls` as first parameter, defined with `@classmethod`
- **Static methods**: Independent functions in class namespace, no automatic first parameter, defined with `@staticmethod`

Understanding these concepts helps you write more maintainable and flexible Python code by choosing the right approach for your specific use case.