# Polymorphism in Object-Oriented Programming (OOP)

## Definition
Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types to be treated as instances of the same type through a common interface. The word "polymorphism" comes from Greek, meaning "many forms." It enables a single interface to represent different underlying data types or classes.

## Key Concepts

### The Principle of "One Interface, Multiple Implementations"
Polymorphism allows the same method call to behave differently depending on the object that receives the call. This means that a single interface can be used to represent different types of underlying objects.

### Dynamic Binding
In polymorphism, the method to be executed is determined at runtime rather than at compile time, which is known as dynamic binding or late binding.

## Types of Polymorphism

### 1. Compile-Time Polymorphism (Static Polymorphism)

#### Method Overloading
Method overloading allows multiple methods with the same name but different parameters within the same class.

```python
# Note: Python doesn't support traditional method overloading like Java/C++
# But we can achieve similar functionality using default parameters or *args

class Calculator:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

calc = Calculator()
print(calc.add(5))          # Output: 5
print(calc.add(5, 3))       # Output: 8
print(calc.add(5, 3, 2))    # Output: 10
```

#### Operator Overloading
Python allows operators to be redefined for custom classes using special methods.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()

# Usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Uses __add__ method
v4 = v1 * 3   # Uses __mul__ method

print(v3)  # Output: Vector(6, 8)
print(v4)  # Output: Vector(6, 9)
```

### 2. Runtime Polymorphism (Dynamic Polymorphism)

#### Method Overriding
Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its parent class.

```python
class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Duck(Animal):
    def make_sound(self):
        return "Quack!"

# Polymorphic function
def animal_sound(animal):
    print(animal.make_sound())

# Usage
animals = [Dog(), Cat(), Duck(), Animal()]

for animal in animals:
    animal_sound(animal)
# Output:
# Woof!
# Meow!
# Quack!
# Some generic sound
```

## Implementation Approaches

### 1. Inheritance-Based Polymorphism

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Polymorphic function
def print_shape_info(shape):
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("---")

# Usage
shapes = [Rectangle(5, 3), Circle(4), Triangle(6, 4, 3, 4, 5)]

for shape in shapes:
    print_shape_info(shape)
```

### 2. Duck Typing (Python's Approach)

Duck typing follows the principle: "If it walks like a duck and quacks like a duck, then it's a duck."

```python
class Dog:
    def speak(self):
        return "Woof!"
    
    def move(self):
        return "Running on four legs"

class Robot:
    def speak(self):
        return "Beep boop"
    
    def move(self):
        return "Rolling on wheels"

class Human:
    def speak(self):
        return "Hello"
    
    def move(self):
        return "Walking on two legs"

def communicate(entity):
    print(entity.speak())

def locomote(entity):
    print(entity.move())

# Usage - no inheritance required!
entities = [Dog(), Robot(), Human()]

for entity in entities:
    communicate(entity)
    locomote(entity)
    print("---")
```

## Practical Examples

### Example 1: File Processing System

```python
class FileProcessor:
    def process(self, filename):
        pass

class TextFileProcessor(FileProcessor):
    def process(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return f"Text file '{filename}' processed. Word count: {word_count}"

class ImageFileProcessor(FileProcessor):
    def process(self, filename):
        # Simulate image processing
        return f"Image file '{filename}' processed. Size: 1920x1080"

class AudioFileProcessor(FileProcessor):
    def process(self, filename):
        # Simulate audio processing
        return f"Audio file '{filename}' processed. Duration: 3:45"

def handle_file(file_processor, filename):
    return file_processor.process(filename)

# Usage
processors = [
    TextFileProcessor(),
    ImageFileProcessor(),
    AudioFileProcessor()
]

filenames = ["document.txt", "photo.jpg", "song.mp3"]

for processor, filename in zip(processors, filenames):
    print(handle_file(processor, filename))
```

### Example 2: Payment Processing System

```python
class PaymentProcessor:
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        fee = amount * 0.03  # 3% fee for credit card
        total = amount + fee
        return f"Credit card payment processed. Amount: ${amount:.2f}, Fee: ${fee:.2f}, Total: ${total:.2f}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        fee = amount * 0.025  # 2.5% fee for PayPal
        total = amount + fee
        return f"PayPal payment processed. Amount: ${amount:.2f}, Fee: ${fee:.2f}, Total: ${total:.2f}"

class BitcoinProcessor(PaymentProcessor):
    def process_payment(self, amount):
        fee = 0.0005  # Fixed fee for Bitcoin
        total = amount + fee
        return f"Bitcoin payment processed. Amount: ${amount:.2f}, Fee: ${fee:.2f}, Total: ${total:.2f}"

def execute_payment(processor, amount):
    return processor.process_payment(amount)

# Usage
processors = [CreditCardProcessor(), PayPalProcessor(), BitcoinProcessor()]
amount = 100.00

for processor in processors:
    print(execute_payment(processor, amount))
    print("---")
```

### Example 3: Game Character System

```python
class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    
    def attack(self):
        pass
    
    def defend(self):
        pass
    
    def special_ability(self):
        pass

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=120)
        self.strength = 15
    
    def attack(self):
        return f"{self.name} swings a mighty sword dealing {self.strength} damage!"
    
    def defend(self):
        return f"{self.name} raises shield, reducing incoming damage!"
    
    def special_ability(self):
        return f"{self.name} enters berserker rage, doubling attack power!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=80)
        self.mana = 100
    
    def attack(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} casts fireball dealing 20 damage! Mana remaining: {self.mana}"
        else:
            return f"{self.name} is out of mana!"
    
    def defend(self):
        return f"{self.name} creates a magical barrier!"
    
    def special_ability(self):
        self.mana = 100
        return f"{self.name} restores all mana through meditation!"

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90)
        self.arrows = 20
    
    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            return f"{self.name} shoots an arrow dealing 12 damage! Arrows remaining: {self.arrows}"
        else:
            return f"{self.name} is out of arrows!"
    
    def defend(self):
        return f"{self.name} dodges with agility!"
    
    def special_ability(self):
        self.arrows += 10
        return f"{self.name} finds a quiver with 10 arrows! Arrows: {self.arrows}"

def character_action(character):
    print(character.attack())
    print(character.defend())
    print(character.special_ability())
    print(f"Health: {character.health}")
    print("---")

# Usage
characters = [Warrior("Conan"), Mage("Gandalf"), Archer("Legolas")]

for character in characters:
    print(f"{character.__class__.__name__}: {character.name}")
    character_action(character)
```

## Benefits of Polymorphism

### 1. Code Reusability
Polymorphism allows writing generic code that works with objects of different types.

### 2. Flexibility
New classes can be added without modifying existing code that uses polymorphic functions.

### 3. Maintainability
Changes to individual classes don't affect the code that uses polymorphic interfaces.

### 4. Scalability
Systems can be extended with new functionality without major restructuring.

## Design Patterns Using Polymorphism

### Strategy Pattern

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        # Simplified bubble sort implementation
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        # Simplified quicksort implementation
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class SortContext:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def execute_sort(self, data):
        return self.strategy.sort(data[:])  # Pass a copy to avoid modifying original

# Usage
data = [64, 34, 25, 12, 22, 11, 90]

bubble_sort = BubbleSort()
quick_sort = QuickSort()

context = SortContext(bubble_sort)
print("Bubble Sort:", context.execute_sort(data))

context.set_strategy(quick_sort)
print("Quick Sort:", context.execute_sort(data))
```

## Best Practices

### 1. Use Abstract Base Classes
Define clear interfaces using abstract base classes to ensure consistent implementation.

```python
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Button(Drawable):
    def draw(self):
        return "Drawing button"

class TextBox(Drawable):
    def draw(self):
        return "Drawing textbox"
```

### 2. Follow the Liskov Substitution Principle
Subtypes must be substitutable for their base types without altering the correctness of the program.

### 3. Keep Interfaces Focused
Each class should have a single, well-defined responsibility.

### 4. Use Type Hints for Clarity
```python
from typing import List

def process_shapes(shapes: List[Shape]) -> None:
    for shape in shapes:
        print(f"Area: {shape.area()}")
```

## Common Pitfalls

### 1. Overcomplicating Hierarchies
Avoid deep inheritance chains that make polymorphism hard to follow.

### 2. Ignoring Performance
Runtime polymorphism has a slight performance cost compared to static binding.

### 3. Violating LSP
Subclasses that change the expected behavior of parent methods violate the Liskov Substitution Principle.

### 4. Inconsistent Interfaces
Make sure all implementations of an interface behave consistently.

## Conclusion

Polymorphism is a powerful concept that enables flexibility and extensibility in object-oriented programming. It allows treating objects of different types uniformly through a common interface, leading to cleaner, more maintainable code. By leveraging polymorphism effectively, developers can create systems that are easy to extend and modify without affecting existing functionality.

Understanding and implementing polymorphism correctly is essential for building robust, scalable object-oriented systems that can adapt to changing requirements over time.