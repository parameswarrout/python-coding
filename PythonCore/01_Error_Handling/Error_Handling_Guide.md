# Python Error Handling Guide

## Table of Contents
1. [Introduction to Error Handling](#introduction)
2. [Types of Errors in Python](#types-of-errors)
3. [Try-Except Blocks](#try-except-blocks)
4. [Handling Specific Exceptions](#handling-specific-exceptions)
5. [Else and Finally Clauses](#else-and-finally-clauses)
6. [Raising Exceptions](#raising-exceptions)
7. [Custom Exceptions](#custom-exceptions)
8. [Best Practices](#best-practices)
9. [Advanced Error Handling Techniques](#advanced-techniques)

## Introduction {#introduction}

Error handling is a critical aspect of writing robust Python applications. Python provides a structured way to handle errors using try-except blocks, which allow your program to gracefully handle unexpected situations without crashing.

## Types of Errors in Python {#types-of-errors}

Python has three main types of errors:

### 1. Syntax Errors
These occur when Python can't interpret your code due to incorrect syntax.

```python
# Syntax Error Example
# print("Hello World"  # Missing closing parenthesis
```

### 2. Runtime Errors (Exceptions)
These occur during program execution when something unexpected happens.

```python
# Runtime Error Example
def divide_by_zero():
    result = 10 / 0  # ZeroDivisionError
    return result

# This will raise an exception
# divide_by_zero()
```

### 3. Logical Errors
These occur when the code runs without crashing but produces incorrect results.

```python
# Logical Error Example
def calculate_average(numbers):
    # Incorrect: dividing by length of original list instead of filtered list
    positive_numbers = [n for n in numbers if n > 0]
    return sum(positive_numbers) / len(numbers)  # Should be len(positive_numbers)

# This gives wrong result
result = calculate_average([1, 2, -3, 4, 5])  # Expected ~3.0, but gets ~2.4
```

## Try-Except Blocks {#try-except-blocks}

The basic structure for handling exceptions in Python:

```python
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None

# Usage
print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Error: Cannot divide by zero! \n None
```

### Multiple Except Clauses

```python
def process_data(data, index, divisor):
    try:
        value = data[index]
        result = value / divisor
        return result
    except IndexError:
        print(f"Index {index} is out of range")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid data type provided")
        return None

# Usage examples
print(process_data([1, 2, 3], 1, 2))    # Output: 1.0
print(process_data([1, 2, 3], 5, 2))    # Output: Index 5 is out of range
print(process_data([1, 2, 3], 1, 0))    # Output: Cannot divide by zero
print(process_data("not a list", 1, 2))  # Output: Invalid data type provided
```

## Handling Specific Exceptions {#handling-specific-exceptions}

### Catching Multiple Exceptions in One Block

```python
def safe_operation(operation, *args):
    try:
        if operation == "divide":
            return args[0] / args[1]
        elif operation == "index":
            return args[0][args[1]]
        elif operation == "convert":
            return int(args[0])
    except (ZeroDivisionError, IndexError, ValueError) as e:
        print(f"An error occurred: {type(e).__name__} - {e}")
        return None

# Usage
print(safe_operation("divide", 10, 2))      # Output: 5.0
print(safe_operation("divide", 10, 0))      # Output: An error occurred: ZeroDivisionError - division by zero
print(safe_operation("index", [1, 2, 3], 5))  # Output: An error occurred: IndexError - list index out of range
print(safe_operation("convert", "not_a_num"))  # Output: An error occurred: ValueError - invalid literal for int()
```

### Accessing Exception Information

```python
import traceback

def detailed_error_handling(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Exception Type: {type(e).__name__}")
        print(f"Exception Message: {str(e)}")
        print("Full Traceback:")
        traceback.print_exc()
        return None

def problematic_function(x, y):
    if y == 0:
        raise ValueError("Y cannot be zero")
    return x / y

# Usage
result = detailed_error_handling(problematic_function, 10, 0)
```

## Else and Finally Clauses {#else-and-finally-clauses}

### Else Clause
The else block executes only if no exception occurred in the try block.

```python
def process_file(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    else:
        # This runs only if no exception occurred
        print(f"File {filename} opened successfully")
        content = file.read()
        file.close()
        return content
    finally:
        # This always runs, regardless of exceptions
        print("File processing completed")

# Usage
content = process_file("nonexistent.txt")  # File not found
# content = process_file("existing.txt")    # File opened successfully
```

### Finally Clause
The finally block always executes, whether an exception occurred or not.

```python
def database_operation():
    connection = None
    try:
        print("Connecting to database...")
        # Simulate connection
        connection = "connected"
        
        # Simulate some operation that might fail
        import random
        if random.choice([True, False]):
            raise Exception("Database operation failed")
        
        print("Database operation successful")
        return "Success"
    
    except Exception as e:
        print(f"Database error: {e}")
        return "Failed"
    
    finally:
        # Always close the connection
        if connection:
            print("Closing database connection")
        print("Cleanup completed")

# Usage
result = database_operation()
print(f"Result: {result}")
```

## Raising Exceptions {#raising-exceptions}

### Basic Exception Raising

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

def register_user(name, age):
    try:
        validate_age(age)
        print(f"User {name} registered successfully with age {age}")
    except ValueError as e:
        print(f"Registration failed: {e}")

# Usage
register_user("Alice", 25)   # Success
register_user("Bob", -5)     # Failed: Age cannot be negative
register_user("Charlie", 200) # Failed: Age seems unrealistic
```

### Re-raising Exceptions

```python
def process_data_with_logging(data):
    try:
        # Some processing that might fail
        result = 100 / data
        return result
    except ZeroDivisionError as e:
        print(f"Logging: Division by zero error occurred with value {data}")
        # Re-raise the same exception
        raise
    except Exception as e:
        print(f"Logging: Unexpected error occurred: {e}")
        # Re-raise the same exception
        raise

# Usage
try:
    result = process_data_with_logging(0)
except ZeroDivisionError:
    print("Caught the re-raised exception")
```

## Custom Exceptions {#custom-exceptions}

### Creating Custom Exception Classes

```python
class InsufficientFundsError(Exception):
    """Raised when account doesn't have enough funds"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, Tried to withdraw ${amount}")

class AccountFrozenError(Exception):
    """Raised when account is frozen"""
    pass

class BankAccount:
    def __init__(self, initial_balance=0, account_holder=""):
        self.balance = initial_balance
        self.account_holder = account_holder
        self.is_frozen = False
    
    def withdraw(self, amount):
        if self.is_frozen:
            raise AccountFrozenError("Account is frozen")
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        return self.balance

# Usage
account = BankAccount(100, "John Doe")

try:
    account.withdraw(150)  # Raises InsufficientFundsError
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
    print(f"Balance: ${e.balance}, Requested: ${e.amount}")

try:
    account.is_frozen = True
    account.withdraw(50)  # Raises AccountFrozenError
except AccountFrozenError as e:
    print(f"Transaction failed: {e}")
```

### Inheritance in Custom Exceptions

```python
class ValidationError(Exception):
    """Base exception for validation errors"""
    pass

class EmailValidationError(ValidationError):
    """Raised when email format is invalid"""
    pass

class PasswordValidationError(ValidationError):
    """Raised when password doesn't meet requirements"""
    pass

def validate_email(email):
    if "@" not in email or "." not in email:
        raise EmailValidationError(f"Invalid email format: {email}")

def validate_password(password):
    if len(password) < 8:
        raise PasswordValidationError("Password must be at least 8 characters")
    if not any(c.isdigit() for c in password):
        raise PasswordValidationError("Password must contain at least one digit")

def create_user(email, password):
    try:
        validate_email(email)
        validate_password(password)
        return {"email": email, "password": "*" * len(password)}
    except ValidationError as e:
        print(f"Validation error: {e}")
        return None

# Usage
user1 = create_user("invalid-email", "weak")           # Both validations fail
user2 = create_user("valid@email.com", "strongpass123") # Success
```

## Best Practices {#best-practices}

### 1. Be Specific with Exceptions

```python
# Good: Catch specific exceptions
def safe_file_read(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except PermissionError:
        print(f"Permission denied for {filename}")
        return None

# Avoid: Catching all exceptions
def bad_file_read(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except:  # Too broad
        print("Something went wrong")
        return None
```

### 2. Use Context Managers

```python
# Good: Using context manager (automatically handles cleanup)
def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None

# Less ideal: Manual resource management
def read_file_manual_close(filename):
    file = None
    try:
        file = open(filename, 'r')
        return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    finally:
        if file:
            file.close()
```

### 3. Don't Ignore Exceptions

```python
# Bad: Ignoring exceptions
def bad_exception_handling():
    try:
        result = 10 / 0
    except:
        pass  # Silent failure - very bad!

# Good: At least log the exception
import logging

def good_exception_handling():
    try:
        result = 10 / 0
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        # Handle appropriately
```

### 4. Fail Fast Principle

```python
def calculate_discount(price, discount_percent):
    # Validate inputs early
    if price < 0:
        raise ValueError("Price cannot be negative")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")
    
    return price * (discount_percent / 100)

# Usage
try:
    discount = calculate_discount(-10, 20)  # Fails immediately with clear error
except ValueError as e:
    print(f"Error: {e}")
```

## Advanced Error Handling Techniques {#advanced-techniques}

### 1. Exception Chaining

```python
class DataProcessingError(Exception):
    pass

def parse_config(config_text):
    try:
        # Simulate parsing that might fail
        if "invalid" in config_text.lower():
            raise ValueError("Invalid configuration format")
        return {"parsed": config_text}
    except ValueError as e:
        # Chain exceptions to preserve context
        raise DataProcessingError("Configuration parsing failed") from e

# Usage
try:
    config = parse_config("invalid config")
except DataProcessingError as e:
    print(f"Top-level error: {e}")
    print(f"Original error: {e.__cause__}")
```

### 2. Contextual Error Information

```python
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def make_request(self, endpoint, data=None):
        try:
            # Simulate API request
            if endpoint == "/error":
                raise ConnectionError("Network timeout")
            return {"status": "success", "data": data}
        except Exception as e:
            # Add contextual information
            e.request_context = {
                "base_url": self.base_url,
                "endpoint": endpoint,
                "data": data
            }
            raise

# Usage
client = APIClient("https://api.example.com")
try:
    response = client.make_request("/error", {"key": "value"})
except Exception as e:
    print(f"Error: {e}")
    if hasattr(e, 'request_context'):
        print(f"Context: {e.request_context}")
```

### 3. Decorator for Error Handling

```python
from functools import wraps

def handle_exceptions(*exception_classes, default_return=None, log_error=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_classes as e:
                if log_error:
                    print(f"Handled {type(e).__name__} in {func.__name__}: {e}")
                return default_return
        return wrapper
    return decorator

@handle_exceptions(ValueError, TypeError, default_return="Error occurred")
def safe_convert_to_int(value):
    return int(value)

@handle_exceptions(ZeroDivisionError, default_return=float('inf'))
def safe_divide(a, b):
    return a / b

# Usage
print(safe_convert_to_int("123"))    # Output: 123
print(safe_convert_to_int("abc"))    # Output: Error occurred
print(safe_divide(10, 2))            # Output: 5.0
print(safe_divide(10, 0))            # Output: inf
```

### 4. Error Handling in Iterables

```python
def safe_process_list(items, processor_func):
    results = []
    errors = []
    
    for i, item in enumerate(items):
        try:
            result = processor_func(item)
            results.append(result)
        except Exception as e:
            errors.append({
                "index": i,
                "item": item,
                "error": str(e)
            })
            results.append(None)  # Placeholder for failed item
    
    return results, errors

def risky_operation(x):
    if x == 0:
        raise ValueError("Cannot process zero")
    return 1 / x

# Usage
items = [1, 2, 0, 4, 5]
results, errors = safe_process_list(items, risky_operation)

print(f"Results: {results}")
print(f"Errors: {errors}")
```

## Summary

Effective error handling in Python involves:

1. Understanding the different types of errors
2. Using try-except blocks appropriately
3. Handling specific exceptions rather than catching all
4. Using else and finally clauses when needed
5. Creating custom exceptions for domain-specific errors
6. Following best practices like "fail fast" and not ignoring exceptions
7. Using advanced techniques like exception chaining and decorators

Remember that error handling should make your code more robust, not more complex. Always aim for clear, specific error handling that helps both developers and users understand what went wrong and why.