# Class vs Instance vs Static Methods in Python

## Overview

Python classes can have three different types of methods, each serving a specific purpose and having different access to the class and its instances. Understanding the differences between these method types is crucial for proper object-oriented design.

## Instance Methods

Instance methods are the most common type of method in Python classes. They receive the instance as the first argument (conventionally named `self`) and can access both instance and class attributes.

### Characteristics:
- Receive the instance (`self`) as the first argument
- Can access and modify instance attributes
- Can access class attributes
- Called on instances of the class
- Used for operations that involve the instance's state

```python
class Person:
    species = "Homo sapiens"  # Class attribute
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    
    def introduce(self):
        """Instance method - accesses instance attributes"""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def have_birthday(self):
        """Instance method - modifies instance attribute"""
        self.age += 1
        return f"{self.name} is now {self.age} years old!"
    
    def get_species(self):
        """Instance method - accesses class attribute"""
        return f"I am a {self.species}"

# Usage
person = Person("Alice", 30)
print(person.introduce())      # Hi, I'm Alice and I'm 30 years old.
print(person.have_birthday())  # Alice is now 31 years old!
print(person.get_species())    # I am a Homo sapiens
```

### Instance Method with Class Attribute Modification

```python
class Counter:
    total_instances = 0  # Class attribute
    
    def __init__(self, start_value=0):
        self.value = start_value  # Instance attribute
        Counter.total_instances += 1  # Modify class attribute
    
    def increment(self):
        """Instance method that affects both instance and class state"""
        self.value += 1
        return self.value
    
    def get_instance_info(self):
        """Instance method returning instance-specific info"""
        return f"Counter value: {self.value}, Total counters: {Counter.total_instances}"

# Usage
counter1 = Counter(10)
counter2 = Counter(20)

print(counter1.increment())           # 11
print(counter2.increment())           # 21
print(counter1.get_instance_info())   # Counter value: 11, Total counters: 2
print(counter2.get_instance_info())   # Counter value: 21, Total counters: 2
```

## Class Methods

Class methods receive the class as the first argument (conventionally named `cls`) instead of the instance. They can access class attributes but not instance attributes directly. Class methods are defined using the `@classmethod` decorator.

### Characteristics:
- Receive the class (`cls`) as the first argument
- Can access and modify class attributes
- Cannot access instance attributes directly
- Called on the class or instance
- Often used as alternative constructors
- Used for operations that affect the class itself

```python
class Student:
    school_name = "Python High School"  # Class attribute
    student_count = 0                   # Class attribute
    
    def __init__(self, name, grade):
        self.name = name    # Instance attribute
        self.grade = grade  # Instance attribute
        Student.student_count += 1  # Increment class attribute
    
    def get_student_info(self):
        """Instance method"""
        return f"{self.name} is in grade {self.grade} at {self.school_name}"
    
    @classmethod
    def get_school_info(cls):
        """Class method - accesses class attributes only"""
        return f"School: {cls.school_name}, Students: {cls.student_count}"
    
    @classmethod
    def create_valedictorian(cls, name):
        """Class method as alternative constructor"""
        return cls(name, 12)  # Creates a 12th-grade student
    
    @classmethod
    def reset_student_count(cls):
        """Class method to modify class state"""
        cls.student_count = 0
        return "Student count reset"

# Usage
student1 = Student("John", 10)
student2 = Student.create_valedictorian("Alice")  # Using class method as constructor

print(student1.get_student_info())    # John is in grade 10 at Python High School
print(student2.get_student_info())    # Alice is in grade 12 at Python High School
print(Student.get_school_info())      # School: Python High School, Students: 2

# Can call class methods on instances too
print(student1.get_school_info())     # School: Python High School, Students: 2
```

### Class Method with Factory Pattern

```python
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f'Pizza({self.ingredients})'
    
    @classmethod
    def margherita(cls):
        """Class method as factory for specific pizza type"""
        return cls(['mozzarella', 'tomatoes'])
    
    @classmethod
    def pepperoni(cls):
        """Class method as factory for specific pizza type"""
        return cls(['mozzarella', 'tomatoes', 'pepperoni'])
    
    @classmethod
    def from_string(cls, ingredients_string):
        """Class method as flexible constructor"""
        ingredients = ingredients_string.split(', ')
        return cls(ingredients)

# Usage
pizza1 = Pizza.margherita()
pizza2 = Pizza.pepperoni()
pizza3 = Pizza.from_string('cheese, mushrooms, olives')

print(pizza1)  # Pizza(['mozzarella', 'tomatoes'])
print(pizza2)  # Pizza(['mozzarella', 'tomatoes', 'pepperoni'])
print(pizza3)  # Pizza(['cheese', 'mushrooms', 'olives'])
```

## Static Methods

Static methods don't receive any automatic first argument (neither `self` nor `cls`). They behave like regular functions but belong to the class namespace. Static methods are defined using the `@staticmethod` decorator.

### Characteristics:
- Don't receive automatic first argument
- Cannot access instance or class attributes directly
- Behave like regular functions but belong to class namespace
- Called on class or instance
- Used for utility functions related to the class

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        """Static method - behaves like a regular function"""
        return x + y
    
    @staticmethod
    def multiply(x, y):
        """Static method - no access to self or cls"""
        return x * y
    
    @staticmethod
    def is_prime(n):
        """Static method - utility function"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def calculate_distance(point1, point2):
        """Static method - utility function for calculations"""
        import math
        return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Usage - can be called on class or instance
print(MathOperations.add(5, 3))                    # 8
print(MathOperations.multiply(4, 7))               # 28
print(MathOperations.is_prime(17))                 # True
print(MathOperations.calculate_distance((0,0), (3,4)))  # 5.0

# Can also call on instances
math_ops = MathOperations()
print(math_ops.add(10, 20))                       # 30
```

### Static Method with Validation

```python
class DataValidator:
    @staticmethod
    def validate_email(email):
        """Static method for email validation"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone):
        """Static method for phone validation"""
        import re
        pattern = r'^\+?1?-?\.?\s?\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def sanitize_string(text):
        """Static method for string sanitization"""
        import re
        # Remove extra whitespace and special characters
        return re.sub(r'[^\w\s]', '', text).strip()

# Usage
print(DataValidator.validate_email("test@example.com"))    # True
print(DataValidator.validate_phone("123-456-7890"))       # True
print(DataValidator.sanitize_string("Hello, World!!!"))  # Hello World
```

## Detailed Comparison

| Aspect | Instance Method | Class Method | Static Method |
|--------|----------------|--------------|---------------|
| First Parameter | `self` (instance) | `cls` (class) | None |
| Access to Instance Variables | Yes | No | No |
| Access to Class Variables | Yes | Yes | No* |
| Called On | Instance | Class or Instance | Class or Instance |
| Decorator | None | `@classmethod` | `@staticmethod` |
| Purpose | Operate on instance data | Operate on class data | Utility functions |

*Note: Class variables can be accessed via `ClassName.variable` in static methods, but not through `cls`.

## Practical Example: Combining All Three Types

```python
class TemperatureConverter:
    """A class demonstrating all three method types"""
    
    scale_factor = 1.8  # Class attribute
    conversion_count = 0  # Class attribute to track conversions
    
    def __init__(self, celsius=0):
        self.celsius = celsius  # Instance attribute
    
    # Instance method
    def to_fahrenheit(self):
        """Instance method - operates on instance data"""
        TemperatureConverter.conversion_count += 1
        self.fahrenheit = self.celsius * self.scale_factor + 32
        return self.fahrenheit
    
    # Instance method
    def get_conversion_info(self):
        """Instance method - returns instance-specific info"""
        return f"{self.celsius}°C = {self.to_fahrenheit()}°F"
    
    # Class method
    @classmethod
    def get_conversion_stats(cls):
        """Class method - returns class-wide statistics"""
        return f"Total conversions performed: {cls.conversion_count}"
    
    # Class method
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Class method - alternative constructor"""
        celsius = (fahrenheit - 32) / cls.scale_factor
        instance = cls(celsius)
        instance.fahrenheit = fahrenheit
        cls.conversion_count += 1
        return instance
    
    # Static method
    @staticmethod
    def convert_c_to_f(celsius):
        """Static method - utility function"""
        return celsius * 1.8 + 32
    
    # Static method
    @staticmethod
    def convert_f_to_c(fahrenheit):
        """Static method - utility function"""
        return (fahrenheit - 32) / 1.8
    
    # Static method
    @staticmethod
    def is_valid_temperature(temp, scale='C'):
        """Static method - validation utility"""
        if scale.upper() == 'C':
            return temp >= -273.15  # Absolute zero in Celsius
        elif scale.upper() == 'F':
            return temp >= -459.67  # Absolute zero in Fahrenheit
        return False

# Usage examples
# Instance methods
temp1 = TemperatureConverter(25)
print(temp1.get_conversion_info())  # 25°C = 77.0°F

# Class methods
temp2 = TemperatureConverter.from_fahrenheit(100)
print(f"From Fahrenheit: {temp2.celsius}°C")  # From Fahrenheit: 37.77777777777778°C

# Static methods
print(f"0°C to °F: {TemperatureConverter.convert_c_to_f(0)}")  # 0°C to °F: 32.0
print(f"32°F to °C: {TemperatureConverter.convert_f_to_c(32)}")  # 32°F to °C: 0.0
print(f"Valid temp: {TemperatureConverter.is_valid_temperature(-300)}")  # Valid temp: False

# Class method stats
print(TemperatureConverter.get_conversion_stats())  # Total conversions performed: 4
```

## When to Use Each Method Type

### Use Instance Methods When:
- You need to access or modify instance attributes
- The method's behavior depends on the object's state
- You need to access both instance and class attributes
- You're implementing the core functionality of the object

### Use Class Methods When:
- You need to access or modify class attributes
- You want to create alternative constructors
- The method's behavior is related to the class itself, not specific instances
- You need to create factory methods
- You're implementing methods that affect the class as a whole

### Use Static Methods When:
- The function is related to the class but doesn't need access to `self` or `cls`
- You want to group utility functions with related classes
- The function could be a standalone function but belongs conceptually to the class
- You're implementing helper functions that don't depend on object state

## Common Mistakes and Best Practices

### Mistake 1: Confusing the Purpose
```python
class WrongExample:
    class_var = 10
    
    def __init__(self, value):
        self.instance_var = value
    
    # Wrong: Using instance method when class method would be better
    def get_class_var(self):  # This doesn't need instance data
        return self.class_var  # Could just use WrongExample.class_var
    
    # Better: Use class method for class data
    @classmethod
    def get_class_var_correct(cls):
        return cls.class_var
```

### Best Practice: Choose the Right Method Type
```python
class BestPractice:
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name):
        self.name = name
        BestPractice.employee_count += 1
    
    # Instance method for instance-specific operations
    def get_employee_info(self):
        return f"Employee: {self.name}, Company: {self.company}"
    
    # Class method for class-specific operations
    @classmethod
    def get_company_info(cls):
        return f"Company: {cls.company}, Employees: {cls.employee_count}"
    
    # Static method for utility functions
    @staticmethod
    def validate_name(name):
        return isinstance(name, str) and len(name) > 0
```

## Summary

Understanding the differences between instance, class, and static methods is crucial for effective Python programming:

- **Instance methods** are for operations that involve the object's state
- **Class methods** are for operations that involve the class itself
- **Static methods** are for utility functions related to the class

Choose the appropriate method type based on what data the method needs to access and what its purpose is. This leads to cleaner, more maintainable code that follows Python's design principles.