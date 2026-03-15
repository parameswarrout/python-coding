# Advanced Functions in Python

## Table of Contents
1. [Lambda Functions](#lambda-functions)
2. [Higher-Order Functions](#higher-order-functions)
3. [Map, Filter, Reduce](#map-filter-reduce)
4. [Function Annotations](#function-annotations)
5. [Closures](#closures)
6. [Partial Functions](#partial-functions)
7. [Decorators (Overview)](#decorators-overview)
8. [Advanced Parameter Handling](#advanced-parameter-handling)
9. [Generator Functions](#generator-functions)
10. [Function Introspection](#function-introspection)
11. [Best Practices](#best-practices)

## Lambda Functions {#lambda-functions}

Lambda functions are small anonymous functions that can have any number of arguments but can only have one expression.

### Basic Syntax
```python
lambda arguments: expression
```

### Simple Examples

```python
# Basic lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# Lambda with conditional expression
max_value = lambda x, y: x if x > y else y
print(max_value(10, 7))  # Output: 10
```

### Practical Use Cases

```python
# Sorting with lambda
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)  # Output: [('Bob', 90), ('Alice', 85), ('Charlie', 78)]

# Filtering with lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Mapping with lambda
words = ['hello', 'world', 'python']
capitalized = list(map(lambda word: word.capitalize(), words))
print(capitalized)  # Output: ['Hello', 'World', 'Python']
```

## Higher-Order Functions {#higher-order-functions}

Higher-order functions are functions that take other functions as arguments or return functions as results.

### Functions as Arguments

```python
def apply_operation(func, value):
    """Apply a function to a value"""
    return func(value)

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# Using higher-order function
print(apply_operation(square, 5))  # Output: 25
print(apply_operation(cube, 3))    # Output: 27

# More complex example
def process_data(data, transformer, validator):
    """Process data with a transformer and validator"""
    transformed = [transformer(item) for item in data]
    return [item for item in transformed if validator(item)]

numbers = [1, 2, 3, 4, 5]
doubled_positive = process_data(
    numbers,
    lambda x: x * 2,
    lambda x: x > 0
)
print(doubled_positive)  # Output: [2, 4, 6, 8, 10]
```

### Functions Returning Functions

```python
def create_multiplier(factor):
    """Returns a function that multiplies by the factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(4))  # Output: 12

# More advanced example - function factories
def create_validator(min_val, max_val):
    """Creates a validator function for a range"""
    def validator(x):
        return min_val <= x <= max_val
    return validator

age_validator = create_validator(0, 120)
score_validator = create_validator(0, 100)

print(age_validator(25))   # Output: True
print(age_validator(150))  # Output: False
print(score_validator(85)) # Output: True
print(score_validator(105))# Output: False
```

## Map, Filter, Reduce {#map-filter-reduce}

### Map Function

The `map()` function applies a function to all items in an input list.

```python
from functools import reduce

# Basic map usage
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Map with multiple iterables
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
summed = list(map(lambda x, y: x + y, list1, list2))
print(summed)  # Output: [11, 22, 33, 44]

# Map with built-in functions
strings = ['hello', 'world', 'python']
lengths = list(map(len, strings))
print(lengths)  # Output: [5, 5, 6]
```

### Filter Function

The `filter()` function filters elements based on a condition.

```python
# Basic filter usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# Filter with custom function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 20)
primes = list(filter(is_prime, numbers))
print(primes)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]

# Filter with strings
words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)  # Output: ['banana', 'cherry', 'elderberry']
```

### Reduce Function

The `reduce()` function applies a rolling computation to sequential pairs of values.

```python
from functools import reduce

# Basic reduce usage
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Sum using reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15

# Find maximum using reduce
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # Output: 5

# Concatenate strings using reduce
words = ['Hello', ' ', 'world', '!']
sentence = reduce(lambda x, y: x + y, words)
print(sentence)  # Output: Hello world!

# More complex example: flatten a list
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda acc, sublist: acc + sublist, nested_list, [])
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]
```

## Function Annotations {#function-annotations}

Function annotations provide metadata about function parameters and return values.

### Basic Annotations

```python
def greet(name: str, age: int) -> str:
    """Greet someone by name and age"""
    return f"Hello {name}, you are {age} years old"

# Accessing annotations
print(greet.__annotations__)
# Output: {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}

# Using annotations
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle
    
    Args:
        length: Length of the rectangle
        width: Width of the rectangle
    
    Returns:
        Area of the rectangle
    """
    return length * width

print(calculate_area(5.0, 3.0))  # Output: 15.0
```

### Complex Type Annotations

```python
from typing import List, Dict, Tuple, Optional, Union

def process_data(
    items: List[str], 
    mapping: Dict[str, int], 
    threshold: float = 0.5
) -> Tuple[List[str], int]:
    """
    Process a list of items using a mapping dictionary
    
    Args:
        items: List of strings to process
        mapping: Dictionary mapping strings to integers
        threshold: Threshold value for filtering
    
    Returns:
        Tuple of filtered items and count of processed items
    """
    filtered_items = [item for item in items if mapping.get(item, 0) > threshold]
    return filtered_items, len(filtered_items)

# Example usage
items = ["apple", "banana", "cherry", "date"]
mapping = {"apple": 1, "banana": 3, "cherry": 2, "date": 0.3}
result, count = process_data(items, mapping, 1.5)
print(f"Filtered: {result}, Count: {count}")  # Output: Filtered: ['banana', 'cherry'], Count: 2
```

### Using Type Hints with Classes

```python
from typing import TypeVar, Generic, Callable

T = TypeVar('T')

class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value
    
    def get_value(self) -> T:
        return self.value

def apply_function(container: Container[T], func: Callable[[T], T]) -> Container[T]:
    """Apply a function to the value in a container"""
    new_value = func(container.value)
    return Container(new_value)

# Example usage
container = Container(5)
doubled_container = apply_function(container, lambda x: x * 2)
print(doubled_container.get_value())  # Output: 10
```

## Closures {#closures}

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

### Basic Closure Example

```python
def outer_function(x):
    """Outer function that returns a closure"""
    def inner_function(y):
        """Inner function that captures x from outer scope"""
        return x + y
    return inner_function

# Create closures
add_10 = outer_function(10)
add_20 = outer_function(20)

print(add_10(5))  # Output: 15
print(add_20(5))  # Output: 25

# Check closure properties
print(add_10.__closure__)  # Shows the closure cell
print(add_10.__closure__[0].cell_contents)  # Output: 10
```

### Practical Closure Examples

```python
def create_counter(initial_value=0, step=1):
    """Create a counter function with closure"""
    count = [initial_value]  # Use list to make it mutable
    
    def counter():
        count[0] += step
        return count[0]
    
    return counter

# Create different counters
counter1 = create_counter(0, 1)
counter2 = create_counter(100, 5)

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 105
print(counter2())  # Output: 110

# Configuration closure
def create_multiplier(factor):
    """Create a multiplier function"""
    def multiplier(number):
        return number * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # Output: 10
print(triple(4))  # Output: 12
```

### Closure with Mutable State

```python
def create_accumulator(initial_value=0):
    """Create an accumulator that keeps track of running total"""
    total = [initial_value]
    
    def accumulator(value=0):
        total[0] += value
        return total[0]
    
    def get_total():
        return total[0]
    
    def reset():
        total[0] = initial_value
    
    # Attach helper functions to the main function
    accumulator.get_total = get_total
    accumulator.reset = reset
    return accumulator

# Usage
acc = create_accumulator(10)
print(acc(5))  # Output: 15
print(acc(3))  # Output: 18
print(acc.get_total())  # Output: 18
acc.reset()
print(acc.get_total())  # Output: 10
```

## Partial Functions {#partial-functions}

Partial functions allow you to fix a certain number of arguments of a function and generate a new function.

### Using functools.partial

```python
from functools import partial

def multiply(x, y, z):
    """Multiply three numbers"""
    return x * y * z

# Create partial functions with fixed arguments
double = partial(multiply, 2, 1)  # Fix x=2, y=1
triple = partial(multiply, 3, 1)  # Fix x=3, y=1

print(double(5))  # Output: 10 (2 * 1 * 5)
print(triple(4))  # Output: 12 (3 * 1 * 4)

# More practical example
def power(base, exponent):
    """Calculate base raised to the power of exponent"""
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # Output: 25
print(cube(3))    # Output: 27
```

### Partial Functions in Practice

```python
from functools import partial

def process_data(data, operation, multiplier=1, offset=0):
    """Process data with an operation, multiplier, and offset"""
    result = []
    for item in data:
        processed = operation(item) * multiplier + offset
        result.append(processed)
    return result

# Create specialized functions
square_and_double = partial(process_data, operation=lambda x: x**2, multiplier=2)
add_offset = partial(process_data, operation=lambda x: x, offset=10)

data = [1, 2, 3, 4, 5]
print(square_and_double(data))  # [2, 8, 18, 32, 50]
print(add_offset(data))         # [11, 12, 13, 14, 15]

# Partial with string operations
def format_string(template, value, prefix="", suffix=""):
    """Format a string with template, prefix, and suffix"""
    formatted = template.format(value)
    return f"{prefix}{formatted}{suffix}"

# Create specialized formatters
email_formatter = partial(format_string, "user{}@example.com", prefix="[", suffix="]")
phone_formatter = partial(format_string, "({})-{}-{}", prefix="Tel: ", suffix=" ext.001")

print(email_formatter(12345))  # Output: [user12345@example.com]
print(phone_formatter("555", "123", "4567"))  # Output: Tel: (555)-123-4567 ext.001
```

## Decorators (Overview) {#decorators-overview}

Decorators are a powerful feature that allows you to modify or enhance functions without changing their code.

### Basic Decorator Example

```python
def my_decorator(func):
    """Basic decorator that adds functionality"""
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

# Usage
say_hello("Alice")
# Output:
# Before function call
# Hello, Alice!
# After function call
```

### Timing Decorator Example

```python
import time
from functools import wraps

def timing_decorator(func):
    """Decorator that measures execution time"""
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Simulate a slow function"""
    time.sleep(0.1)
    return "Done!"

result = slow_function()
# Output: slow_function took 0.1001 seconds
```

### Parameterized Decorator

```python
def repeat(times):
    """Decorator factory that repeats function execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")
# Output:
# Hello, Bob!
# Hello, Bob!
# Hello, Bob!
```

## Advanced Parameter Handling {#advanced-parameter-handling}

### *args and **kwargs

```python
def flexible_function(*args, **kwargs):
    """Function that accepts any number of positional and keyword arguments"""
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    
    # Process positional arguments
    for i, arg in enumerate(args):
        print(f"  Arg {i}: {arg}")
    
    # Process keyword arguments
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Usage examples
flexible_function(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
#   Arg 0: 1
#   Arg 1: 2
#   Arg 2: 3
#   name: Alice
#   age: 30

# Unpacking arguments
def create_person(name, age, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}"

args = ["Alice", 30]
kwargs = {"city": "New York"}
person = create_person(*args, **kwargs)
print(person)  # Output: Alice is 30 years old and lives in New York
```

### Keyword-Only Arguments

```python
def process_data(data, *, validate=True, format_output=True, log_level="INFO"):
    """
    Process data with keyword-only arguments
    
    Args:
        data: The data to process
        validate: Whether to validate the data (keyword-only)
        format_output: Whether to format the output (keyword-only)
        log_level: Logging level (keyword-only)
    """
    if validate:
        print(f"Validating data with level {log_level}")
    
    processed = [item.upper() if isinstance(item, str) else item for item in data]
    
    if format_output:
        processed = f"PROCESSED: {processed}"
    
    return processed

# Usage - keyword arguments required after *
result = process_data(["hello", "world"], validate=True, format_output=True)
print(result)  # Output: PROCESSED: ['HELLO', 'WORLD']

# This would cause an error:
# result = process_data(["hello", "world"], True, True)  # TypeError
```

### Positional-Only Arguments (Python 3.8+)

```python
def calculate_price(base_price, /, tax=0.1, *, discount=0):
    """
    Calculate final price with positional-only, regular, and keyword-only params
    
    Args:
        base_price: Must be passed positionally (positional-only)
        tax: Regular parameter with default
        discount: Must be passed as keyword (keyword-only)
    """
    taxed_price = base_price * (1 + tax)
    final_price = taxed_price * (1 - discount)
    return round(final_price, 2)

# Usage
price = calculate_price(100, tax=0.08, discount=0.1)
print(price)  # Output: 97.2

# These work:
price1 = calculate_price(100)  # Uses defaults
price2 = calculate_price(100, 0.15)  # Specify tax
price3 = calculate_price(100, tax=0.12, discount=0.05)  # Specify both

# This would cause an error (can't pass base_price as keyword):
# price = calculate_price(base_price=100, discount=0.1)  # TypeError
```

## Generator Functions {#generator-functions}

Generator functions use yield instead of return to produce a series of values lazily.

### Basic Generator Example

```python
def count_up_to(maximum):
    """Generator that yields numbers from 1 to maximum"""
    count = 1
    while count <= maximum:
        yield count
        count += 1

# Using the generator
counter = count_up_to(5)
for num in counter:
    print(num, end=" ")  # Output: 1 2 3 4 5

print()  # New line

# Generators can be used once, then exhausted
print(list(count_up_to(3)))  # Output: [1, 2, 3]
```

### Generator with Processing

```python
def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Usage
fibonacci_sequence = list(fibonacci_generator(10))
print(fibonacci_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator for file processing
def read_large_file(file_path):
    """Generator to read a large file line by line"""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Example with simulated content
def generate_numbers(start, end, step=1):
    """Generate numbers in a range"""
    current = start
    while current < end:
        yield current
        current += step

numbers = list(generate_numbers(0, 10, 2))
print(numbers)  # Output: [0, 2, 4, 6, 8]
```

### Generator Expressions

```python
# Generator expression vs list comprehension
gen_expr = (x ** 2 for x in range(5) if x % 2 == 0)
list_comp = [x ** 2 for x in range(5) if x % 2 == 0]

print(type(gen_expr))  # Output: <class 'generator'>
print(type(list_comp)) # Output: <class 'list'>

print(list(gen_expr))  # Output: [0, 4, 16]
print(list_comp)       # Output: [0, 4, 16]

# Memory-efficient processing with generators
def process_large_dataset(data_source):
    """Process data efficiently using generators"""
    # Generator to filter and transform data
    processed = (item.upper() for item in data_source if len(item) > 3)
    
    # Generator to add prefixes
    with_prefix = (f"PROCESSED: {item}" for item in processed)
    
    return with_prefix

data = ["hi", "hello", "bye", "world", "python"]
result_gen = process_large_dataset(data)

for item in result_gen:
    print(item)
# Output:
# PROCESSED: hello
# PROCESSED: world
# PROCESSED: python
```

## Function Introspection {#function-introspection}

Python provides tools to examine function properties and signatures.

### Using the inspect Module

```python
import inspect

def sample_function(param1: str, param2: int = 10, *args, **kwargs) -> str:
    """
    Sample function for introspection
    
    Args:
        param1: A string parameter
        param2: An integer parameter with default
        *args: Additional positional arguments
        **kwargs: Additional keyword arguments
    
    Returns:
        A formatted string
    """
    return f"{param1}-{param2}"

# Get function signature
sig = inspect.signature(sample_function)
print(f"Signature: {sig}")

# Iterate through parameters
for param_name, param in sig.parameters.items():
    print(f"Parameter: {param_name}, Default: {param.default}, Annotation: {param.annotation}")

# Get return annotation
print(f"Return annotation: {sig.return_annotation}")

# Get function docstring
print(f"Docstring: {sample_function.__doc__}")

# Get source code (if available)
try:
    source = inspect.getsource(sample_function)
    print("Source code retrieved")
except OSError:
    print("Source code not available")
```

### Function Metadata

```python
def enhanced_function(a: int, b: str = "default") -> bool:
    """An enhanced function with metadata"""
    return len(b) > a

# Access function metadata
print(f"Function name: {enhanced_function.__name__}")
print(f"Function qualname: {enhanced_function.__qualname__}")
print(f"Module: {enhanced_function.__module__}")
print(f"Annotations: {enhanced_function.__annotations__}")
print(f"Defaults: {enhanced_function.__defaults__}")
print(f"Code object: {enhanced_function.__code__}")

# Check if it's a built-in or user-defined function
print(f"Is built-in: {inspect.isbuiltin(enhanced_function)}")
print(f"Is function: {inspect.isfunction(enhanced_function)}")
```

### Dynamic Function Analysis

```python
def analyze_function(func):
    """Analyze a function and return its properties"""
    sig = inspect.signature(func)
    
    analysis = {
        'name': func.__name__,
        'docstring': inspect.getdoc(func),
        'parameters': [],
        'has_var_args': False,
        'has_var_kwargs': False,
        'return_annotation': sig.return_annotation if sig.return_annotation != inspect.Signature.empty else None
    }
    
    for param_name, param in sig.parameters.items():
        param_info = {
            'name': param_name,
            'kind': param.kind.name,
            'has_default': param.default != inspect.Parameter.empty,
            'default': param.default if param.default != inspect.Parameter.empty else None,
            'annotation': param.annotation if param.annotation != inspect.Parameter.empty else None
        }
        
        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            analysis['has_var_args'] = True
        elif param.kind == inspect.Parameter.VAR_KEYWORD:
            analysis['has_var_kwargs'] = True
            
        analysis['parameters'].append(param_info)
    
    return analysis

# Analyze different functions
def test_func(a: int, b: str = "test", *args, **kwargs) -> str:
    """Test function for analysis"""
    return f"{a}-{b}"

analysis = analyze_function(test_func)
print(f"Analysis of {analysis['name']}:")
for param in analysis['parameters']:
    print(f"  {param['name']}: {param['kind']}, default={param['default']}")
print(f"  Has *args: {analysis['has_var_args']}")
print(f"  Has **kwargs: {analysis['has_var_kwargs']}")
```

## Best Practices {#best-practices}

### 1. Use Descriptive Names for Lambda Functions

```python
# Less clear
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))

# More clear - assign to a named function if used multiple times
def square(x):
    return x ** 2

result = list(map(square, numbers))
```

### 2. Prefer List Comprehensions Over Map/Filter When Appropriate

```python
# Map/filter approach
numbers = [1, 2, 3, 4, 5]
evens_squared = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))

# List comprehension approach (often clearer)
evens_squared = [x ** 2 for x in numbers if x % 2 == 0]
```

### 3. Use Type Hints Consistently

```python
from typing import List, Optional

def process_items(items: List[str], prefix: str = "") -> List[str]:
    """Process a list of items with an optional prefix."""
    return [f"{prefix}{item}" for item in items]

def find_item(items: List[str], target: str) -> Optional[int]:
    """Find the index of an item, or None if not found."""
    try:
        return items.index(target)
    except ValueError:
        return None
```

### 4. Be Mindful of Closure Pitfalls

```python
# Common pitfall with closures in loops
functions = []
for i in range(3):
    functions.append(lambda: i)  # All lambdas will return 2!

results = [f() for f in functions]
print(results)  # Output: [2, 2, 2] - probably not what was intended

# Solution: capture the value at creation time
functions = []
for i in range(3):
    functions.append(lambda x=i: x)  # Capture i as default parameter

results = [f() for f in functions]
print(results)  # Output: [0, 1, 2] - correct!
```

### 5. Use functools.wraps in Decorators

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Summary

Advanced functions in Python provide powerful tools for writing more expressive and efficient code:

1. **Lambda functions** offer concise inline function definitions
2. **Higher-order functions** enable functional programming patterns
3. **Map, filter, reduce** provide elegant ways to transform data
4. **Function annotations** improve code documentation and tooling
5. **Closures** allow functions to capture and maintain state
6. **Partial functions** create specialized versions of existing functions
7. **Generators** provide memory-efficient iteration
8. **Introspection tools** enable runtime analysis of functions

Understanding these concepts will make you a more effective Python programmer and open up new possibilities for solving complex problems elegantly.