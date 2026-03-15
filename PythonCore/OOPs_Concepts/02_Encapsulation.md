# Encapsulation in Object-Oriented Programming (OOP)

## Definition
Encapsulation is a fundamental concept in object-oriented programming that involves bundling data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. It also restricts direct access to internal object components, which is a means of preventing accidental interference and misuse of the methods and data.

## Key Concepts

### Data Hiding
Encapsulation hides the internal state of an object and only allows access through a public interface. This protects the integrity of the data by preventing unauthorized access and modification.

### Access Modifiers
Languages use access modifiers to control the visibility of class members:
- **Public**: Accessible from anywhere
- **Protected**: Accessible within the class and its subclasses
- **Private**: Accessible only within the class itself

## Encapsulation in Python

Python doesn't have strict access modifiers like other languages, but it uses naming conventions to indicate the intended visibility of attributes and methods:

### Public Attributes and Methods
Attributes and methods without underscores are considered public and can be accessed from anywhere.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.age = age    # Public attribute
    
    def display_info(self):  # Public method
        return f"Student: {self.name}, Age: {self.age}"

student = Student("Alice", 20)
print(student.name)           # Output: Alice
print(student.display_info()) # Output: Student: Alice, Age: 20
```

### Protected Attributes and Methods
Attributes and methods prefixed with a single underscore `_` are considered protected by convention. This indicates they should not be accessed directly from outside the class, though Python doesn't enforce this restriction.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute
    
    def _validate_transaction(self, amount):  # Protected method
        return amount > 0 and amount <= self._balance
    
    def withdraw(self, amount):
        if self._validate_transaction(amount):
            self._balance -= amount
            return f"Withdrawal successful. New balance: {self._balance}"
        return "Invalid transaction"

account = BankAccount(1000)
print(account._balance)  # Technically accessible, but not recommended
print(account.withdraw(200))  # Output: Withdrawal successful. New balance: 800
```

### Private Attributes and Methods
Attributes and methods prefixed with double underscores `__` are name-mangled by Python, making them harder to access from outside the class.

```python
class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.__password = "admin123"  # Private attribute
        self.__serial_number = "SN123456"  # Private attribute
    
    def __display_serial(self):  # Private method
        return f"Serial Number: {self.__serial_number}"
    
    def authenticate(self, password):
        if password == self.__password:
            return self.__display_serial()
        return "Authentication failed"

computer = Computer("Dell")
print(computer.brand)  # Output: Dell
# print(computer.__password)  # This would raise AttributeError

print(computer.authenticate("admin123"))  # Output: Serial Number: SN123456
print(computer.authenticate("wrongpass"))  # Output: Authentication failed

# Accessing private attributes using name mangling (not recommended)
print(computer._Computer__password)  # Output: admin123
```

## Properties and Property Decorators

Python provides property decorators to create getter, setter, and deleter methods that maintain encapsulation while providing controlled access to attributes.

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter for celsius temperature"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius temperature with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property for Fahrenheit conversion"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for Fahrenheit that updates celsius"""
        celsius_value = (value - 32) * 5/9
        if celsius_value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
        self._celsius = celsius_value

# Usage
temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0

temp.celsius = 30
print(temp.celsius)     # Output: 30
print(temp.fahrenheit)  # Output: 86.0

temp.fahrenheit = 100
print(temp.celsius)     # Output: 37.77777777777778
print(temp.fahrenheit)  # Output: 100.0

# This will raise an exception
try:
    temp.celsius = -300
except ValueError as e:
    print(e)  # Output: Temperature cannot be below absolute zero (-273.15°C)
```

## Getter and Setter Methods

Traditional getter and setter methods provide controlled access to private attributes:

```python
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = self.__validate_age(age)
    
    def __validate_age(self, age):
        """Private method to validate age"""
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150")
        return age
    
    def get_name(self):
        """Getter for name"""
        return self.__name
    
    def set_name(self, name):
        """Setter for name with validation"""
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self.__name = name.strip()
    
    def get_age(self):
        """Getter for age"""
        return self.__age
    
    def set_age(self, age):
        """Setter for age with validation"""
        self.__age = self.__validate_age(age)
    
    def get_info(self):
        """Method to get person information"""
        return f"Name: {self.__name}, Age: {self.__age}"

# Usage
person = Person("John Doe", 30)
print(person.get_info())  # Output: Name: John Doe, Age: 30

person.set_name("Jane Smith")
person.set_age(25)
print(person.get_info())  # Output: Name: Jane Smith, Age: 25

# This will raise an exception
try:
    person.set_age(-5)
except ValueError as e:
    print(e)  # Output: Age must be between 0 and 150
```

## Real-World Examples

### Example 1: Bank Account Management System

```python
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = max(0, initial_balance)  # Ensure non-negative balance
        self.__transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Deposit amount must be positive"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        elif amount > self.__balance:
            return "Insufficient funds"
        else:
            return "Withdrawal amount must be positive"
    
    def get_balance(self):
        """Public method to access balance safely"""
        return self.__balance
    
    def get_account_number(self):
        """Public method to access account number safely"""
        return self.__account_number
    
    def get_transaction_history(self):
        """Public method to access transaction history safely"""
        return self.__transaction_history.copy()  # Return a copy to prevent modification
    
    def __str__(self):
        return f"Account {self.__account_number}: Balance ${self.__balance}"

# Usage
account = BankAccount("ACC123456", 1000)
print(account.deposit(500))      # Output: Deposited $500. New balance: $1500
print(account.withdraw(200))     # Output: Withdrew $200. New balance: $1300
print(account.get_balance())     # Output: 1300
print(account)                   # Output: Account ACC123456: Balance $1300

history = account.get_transaction_history()
for transaction in history:
    print(transaction)
# Output:
# Deposit: +$500
# Withdrawal: -$200
```

### Example 2: Library Management System

```python
class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__copies = copies
        self.__available_copies = copies
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def total_copies(self):
        return self.__copies
    
    @property
    def available_copies(self):
        return self.__available_copies
    
    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            return f"Book '{self.__title}' borrowed successfully"
        return f"No copies of '{self.__title}' available"
    
    def return_book(self):
        if self.__available_copies < self.__copies:
            self.__available_copies += 1
            return f"Book '{self.__title}' returned successfully"
        return f"All copies of '{self.__title}' are already available"
    
    def add_copies(self, num_copies):
        if num_copies > 0:
            self.__copies += num_copies
            self.__available_copies += num_copies
            return f"Added {num_copies} copies. Total: {self.__copies}"
        return "Number of copies must be positive"

class Library:
    def __init__(self):
        self.__books = {}  # Dictionary to store books by ISBN
    
    def add_book(self, book):
        if book.isbn in self.__books:
            # If book exists, increase the number of copies
            existing_book = self.__books[book.isbn]
            existing_book.add_copies(book.total_copies)
        else:
            # Add new book
            self.__books[book.isbn] = book
    
    def borrow_book(self, isbn):
        if isbn in self.__books:
            book = self.__books[isbn]
            return book.borrow_book()
        return "Book not found in library"
    
    def return_book(self, isbn):
        if isbn in self.__books:
            book = self.__books[isbn]
            return book.return_book()
        return "Book not found in library"
    
    def search_book(self, title=None, author=None):
        results = []
        for book in self.__books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()):
                results.append({
                    'title': book.title,
                    'author': book.author,
                    'isbn': book.isbn,
                    'available': book.available_copies
                })
        return results

# Usage
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", 3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 2)

library.add_book(book1)
library.add_book(book2)

print(library.borrow_book("978-0-7432-7356-5"))  # Borrow a book
print(library.borrow_book("978-0-7432-7356-5"))  # Borrow another copy
print(library.borrow_book("978-0-7432-7356-5"))  # Borrow last copy

search_results = library.search_book(title="Gatsby")
print(f"Found {len(search_results)} book(s):")
for result in search_results:
    print(f"Title: {result['title']}, Available: {result['available']}")

print(library.return_book("978-0-7432-7356-5"))  # Return a book
print(f"Now available: {library.search_book(title='Gatsby')[0]['available']}")
```

## Benefits of Encapsulation

### 1. Data Protection
Encapsulation protects data from unauthorized access and modification, ensuring data integrity.

### 2. Modularity
Code is organized into logical units, making it easier to manage and maintain.

### 3. Flexibility and Maintainability
Internal implementation can be changed without affecting external code that uses the class.

### 4. Reusability
Well-encapsulated classes can be reused in different contexts without modification.

### 5. Testing and Debugging
Encapsulation makes it easier to test and debug code since the scope of potential issues is limited.

## Best Practices

### 1. Use Properties for Simple Access
For simple attribute access with validation, use property decorators.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    @property
    def area(self):
        return self._width * self._height
```

### 2. Validate Input in Setters
Always validate input values in setters to maintain data integrity.

### 3. Use Private Attributes for Internal State
Mark attributes as private if they shouldn't be accessed directly from outside the class.

### 4. Provide Meaningful Public Interfaces
Design clear, intuitive public methods that provide controlled access to the object's functionality.

### 5. Document Your Public Interface
Clearly document what methods and properties are part of the public interface.

## Common Pitfalls

### 1. Over-Encapsulation
Making everything private can make classes difficult to extend or use effectively.

### 2. Under-Encapsulation
Exposing too much internal state can lead to fragile code that breaks easily.

### 3. Inconsistent Naming Conventions
Using inconsistent naming for public/private attributes can confuse other developers.

### 4. Exposing Internal State Directly
Returning references to mutable internal objects can break encapsulation.

```python
# Bad practice - exposes internal list directly
def get_items(self):
    return self.__items  # Returns reference to internal list

# Good practice - returns a copy
def get_items(self):
    return self.__items.copy()  # Returns a copy of the list
```

## Conclusion

Encapsulation is a crucial concept in object-oriented programming that provides data protection, modularity, and maintainability. By controlling access to an object's internal state and providing well-defined interfaces, encapsulation helps create robust, secure, and maintainable code.

Python's approach to encapsulation relies on naming conventions and property decorators rather than strict access controls, giving developers flexibility while encouraging responsible access to object internals. Understanding and implementing encapsulation properly is essential for developing high-quality object-oriented systems.