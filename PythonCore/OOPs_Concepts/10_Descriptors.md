# Descriptors in Python

## Introduction

Descriptors are a powerful feature in Python that allow you to customize the behavior of attribute access (getting, setting, deleting) in classes. A descriptor is an object that defines one or more of the following methods: `__get__()`, `__set__()`, or `__delete__()`. When these methods are defined, they override the default behavior of attribute access.

## What Are Descriptors?

Descriptors provide a way to customize what happens when you access an attribute on an object. They are implemented using the descriptor protocol, which consists of the special methods `__get__()`, `__set__()`, and `__delete__()`.

## Descriptor Protocol Methods

### `__get__(self, obj, objtype)`
Called when the attribute is accessed. Returns the value of the attribute or raises AttributeError.

### `__set__(self, obj, value)`
Called when the attribute is set. Sets the value of the attribute.

### `__delete__(self, obj)`
Called when the attribute is deleted.

## Types of Descriptors

### Data Descriptors
Descriptors that define both `__get__()` and `__set__()` methods. They take precedence over instance dictionaries.

### Non-Data Descriptors
Descriptors that only define `__get__()` method. Instance dictionary takes precedence over these.

## Basic Descriptor Example

```python
class ValueDescriptor:
    """A simple descriptor that stores a value"""
    
    def __init__(self, initial_value=None):
        self.value = initial_value
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self.value
    
    def __set__(self, obj, value):
        print(f"Setting value to {value}")
        self.value = value
    
    def __delete__(self, obj):
        print("Deleting value")
        del self.value

class MyClass:
    # Descriptor is defined at the class level
    attr = ValueDescriptor(10)

# Usage
obj = MyClass()
print(obj.attr)        # Output: 10
obj.attr = 20          # Output: Setting value to 20
print(obj.attr)        # Output: 20
del obj.attr           # Output: Deleting value
```

## Property-like Descriptor

```python
class TypedAttribute:
    """A descriptor that enforces type checking"""
    
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"{self.name} must be of type {self.expected_type.__name__}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        if self.name in obj.__dict__:
            del obj.__dict__[self.name]

class Person:
    name = TypedAttribute('name', str)
    age = TypedAttribute('age', int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Usage
person = Person("Alice", 30)
print(f"Name: {person.name}, Age: {person.age}")  # Output: Name: Alice, Age: 30

# This will raise a TypeError
try:
    person.age = "thirty"
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: age must be of type int
```

## Validation Descriptor

```python
class PositiveNumber:
    """A descriptor that ensures the value is positive"""
    
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)
    
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.name} must be positive, got {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        if self.name in obj.__dict__:
            del obj.__dict__[self.name]

class Rectangle:
    width = PositiveNumber('width')
    height = PositiveNumber('height')
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def area(self):
        return self.width * self.height

# Usage
rect = Rectangle(5, 3)
print(f"Area: {rect.area}")  # Output: Area: 15

# This will raise a ValueError
try:
    rect.width = -5
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: width must be positive, got -5
```

## Lazy Property Descriptor

```python
class LazyProperty:
    """A descriptor that computes a value once and caches it"""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        # Compute the value and cache it
        value = self.func(obj)
        # Store the computed value in the object's __dict__
        obj.__dict__[self.name] = value
        return value

class ExpensiveObject:
    def __init__(self, data):
        self.data = data
    
    @LazyProperty
    def processed_data(self):
        """This will only be computed once"""
        print("Processing data...")  # This will only print once
        return [x * 2 for x in self.data]

# Usage
obj = ExpensiveObject([1, 2, 3, 4, 5])
print(obj.processed_data)  # Output: Processing data...\n[2, 4, 6, 8, 10]
print(obj.processed_data)  # Output: [2, 4, 6, 8, 10] (no "Processing data..." message)
```

## Descriptor with Owner Information

```python
class LoggedAttribute:
    """A descriptor that logs all access operations"""
    
    def __init__(self, name, default=None):
        self.name = name
        self.default = default
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.name, self.default)
        print(f"Getting {self.name}: {value}")
        return value
    
    def __set__(self, obj, value):
        print(f"Setting {self.name} to {value}")
        obj.__dict__[self.name] = value
    
    def __delete__(self, obj):
        if self.name in obj.__dict__:
            print(f"Deleting {self.name}")
            del obj.__dict__[self.name]

class Product:
    name = LoggedAttribute('name')
    price = LoggedAttribute('price')
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Usage
product = Product("Laptop", 999.99)
print(f"Product: {product.name}, Price: ${product.price}")
product.price = 899.99
del product.name
```

## Advanced Descriptor: Range Validator

```python
class RangeValidator:
    """A descriptor that validates values are within a specified range"""
    
    def __init__(self, min_val=None, max_val=None):
        self.min_val = min_val
        self.max_val = max_val
    
    def __set_name__(self, owner, name):
        """Called when the descriptor is assigned to a class attribute"""
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.name} must be >= {self.min_val}, got {value}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.name} must be <= {self.max_val}, got {value}")
        setattr(obj, self.private_name, value)

class Student:
    age = RangeValidator(0, 150)  # Age between 0 and 150
    score = RangeValidator(0, 100)  # Score between 0 and 100
    
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# Usage
student = Student("Alice", 20, 85)
print(f"Student: {student.name}, Age: {student.age}, Score: {student.score}")

# These will raise ValueErrors
try:
    student.age = -5
except ValueError as e:
    print(f"Age error: {e}")

try:
    student.score = 105
except ValueError as e:
    print(f"Score error: {e}")
```

## Descriptor for Caching Expensive Operations

```python
import time

class CachedAttribute:
    """A descriptor that caches expensive computations"""
    
    def __init__(self, func):
        self.func = func
        self.name = func.__name__
        self.cache_name = f'_cached_{self.name}'
        self.time_name = f'_time_{self.name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        # Check if we have a cached value and when it was computed
        current_time = time.time()
        cache_time = getattr(obj, self.time_name, 0)
        
        # Cache expires after 5 seconds
        if current_time - cache_time > 5:
            print(f"Computing {self.name}...")
            value = self.func(obj)
            setattr(obj, self.cache_name, value)
            setattr(obj, self.time_name, current_time)
        else:
            print(f"Using cached {self.name}")
            value = getattr(obj, self.cache_name)
        
        return value

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @CachedAttribute
    def processed_result(self):
        """Simulate an expensive computation"""
        time.sleep(1)  # Simulate expensive operation
        return sum(x ** 2 for x in self.data)

# Usage
processor = DataProcessor([1, 2, 3, 4, 5])

start = time.time()
result1 = processor.processed_result  # Will compute
print(f"Time taken: {time.time() - start:.2f}s")

start = time.time()
result2 = processor.processed_result  # Will use cache
print(f"Time taken: {time.time() - start:.2f}s")
```

## Descriptor for Managing Related Objects

```python
class ForeignKey:
    """A descriptor that manages foreign key relationships"""
    
    def __init__(self, related_class):
        self.related_class = related_class
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        if value is not None and not isinstance(value, self.related_class):
            raise TypeError(f"Expected {self.related_class.__name__}, got {type(value).__name__}")
        setattr(obj, self.private_name, value)

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    author = ForeignKey(Author)
    
    def __init__(self, title, author=None):
        self.title = title
        self.author = author
    
    def __str__(self):
        author_name = self.author.name if self.author else "Unknown"
        return f"'{self.title}' by {author_name}"

# Usage
author = Author("J.K. Rowling")
book = Book("Harry Potter", author)
print(book)  # Output: 'Harry Potter' by J.K. Rowling

# This will raise a TypeError
try:
    book.author = "Not an Author object"
except TypeError as e:
    print(f"Error: {e}")
```

## Descriptor vs Property Comparison

```python
# Using a property (limited to a single class)
class TemperatureWithProperty:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value

# Using a descriptor (reusable across multiple classes)
class ValidatedAttribute:
    def __init__(self, validator_func):
        self.validator_func = validator_func
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, None)
    
    def __set__(self, obj, value):
        if not self.validator_func(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        setattr(obj, self.private_name, value)

def temp_validator(value):
    return value >= -273.15

class TemperatureWithDescriptor:
    celsius = ValidatedAttribute(temp_validator)
    
    def __init__(self, celsius=0):
        self.celsius = celsius

class PressureWithDescriptor:
    pascals = ValidatedAttribute(lambda x: x >= 0)  # Pressure must be non-negative
    
    def __init__(self, pascals=0):
        self.pascals = pascals

# Both classes use the same validation logic
temp = TemperatureWithDescriptor(25)
pressure = PressureWithDescriptor(101325)

print(f"Temperature: {temp.celsius}°C")
print(f"Pressure: {pressure.pascals} Pa")
```

## How Descriptors Work Internally

```python
class TrackedDescriptor:
    """A descriptor that shows how attribute access works internally"""
    
    def __init__(self, value):
        self.value = value
    
    def __get__(self, obj, objtype):
        print(f"__get__ called on {self.__class__.__name__}")
        print(f"  obj: {obj}")
        print(f"  objtype: {objtype}")
        return self.value
    
    def __set__(self, obj, value):
        print(f"__set__ called on {self.__class__.__name__}")
        print(f"  obj: {obj}")
        print(f"  value: {value}")
        self.value = value

class Example:
    attr = TrackedDescriptor("initial")

# Usage
obj = Example()
print("Accessing attribute:")
value = obj.attr
print(f"Value: {value}")

print("\nSetting attribute:")
obj.attr = "new value"
```

## Summary

Descriptors are a powerful Python feature that allows you to customize attribute access in classes. They provide a way to implement managed attributes with validation, lazy evaluation, caching, and more. Key points about descriptors:

1. **Protocol**: Defined by implementing `__get__`, `__set__`, and/or `__delete__` methods
2. **Reusability**: Unlike properties, descriptors can be reused across multiple classes
3. **Power**: Provide fine-grained control over attribute access
4. **Types**: Data descriptors (with `__set__`) take precedence over instance dicts
5. **Use cases**: Validation, lazy loading, caching, ORM fields, and more

Descriptors are an advanced feature that, while not used daily, provide powerful capabilities for creating sophisticated and reusable attribute management systems.