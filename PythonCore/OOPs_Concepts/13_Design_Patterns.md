# Design Patterns in Object-Oriented Programming

## Introduction

Design patterns are reusable solutions to commonly occurring problems in software design. They represent best practices evolved over time by experienced object-oriented software developers. Design patterns provide templates for solving problems that can be used in many different situations.

## Categories of Design Patterns

Design patterns are typically grouped into three categories:

1. **Creational Patterns**: Deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.
2. **Structural Patterns**: Concerned with how classes and objects are composed to form larger structures.
3. **Behavioral Patterns**: Focus on communication between objects.

## Creational Patterns

### Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.

```python
class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Prevent re-initialization
        if not self._initialized:
            self.value = 0
            Singleton._initialized = True

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

singleton1.value = 100
print(singleton2.value)  # Output: 100 (same instance)
print(singleton1 is singleton2)  # Output: True (same object)

# Thread-safe Singleton
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Double-checked locking pattern
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.value = 0
            self.initialized = True
```

### Factory Pattern

The Factory pattern defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.

```python
from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Cow(Animal):
    def speak(self):
        return "Moo!"

# Factory class
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        elif animal_type.lower() == "cow":
            return Cow()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
cat = factory.create_animal("cat")
cow = factory.create_animal("cow")

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(cow.speak())  # Output: Moo!

# Abstract Factory Pattern
class AnimalFactoryInterface(ABC):
    @abstractmethod
    def create_pet(self):
        pass
    
    @abstractmethod
    def create_wild_animal(self):
        pass

class DogFactory(AnimalFactoryInterface):
    def create_pet(self):
        return Dog()
    
    def create_wild_animal(self):
        return Wolf()

class CatFactory(AnimalFactoryInterface):
    def create_pet(self):
        return Cat()
    
    def create_wild_animal(self):
        return Tiger()

class Wolf(Animal):
    def speak(self):
        return "Howl!"

class Tiger(Animal):
    def speak(self):
        return "Roar!"
```

### Builder Pattern

The Builder pattern constructs complex objects step by step, allowing you to create different representations of an object using the same construction process.

```python
class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
    
    def __str__(self):
        ingredients = []
        if self.size:
            ingredients.append(f"Size: {self.size}")
        if self.cheese:
            ingredients.append("Cheese")
        if self.pepperoni:
            ingredients.append("Pepperoni")
        if self.mushrooms:
            ingredients.append("Mushrooms")
        if self.onions:
            ingredients.append("Onions")
        
        return f"Pizza with: {', '.join(ingredients)}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self
    
    def add_onions(self):
        self.pizza.onions = True
        return self
    
    def build(self):
        return self.pizza

# Usage
pizza = (PizzaBuilder()
         .set_size("Large")
         .add_cheese()
         .add_pepperoni()
         .add_mushrooms()
         .build())

print(pizza)  # Output: Pizza with: Size: Large, Cheese, Pepperoni, Mushrooms
```

## Structural Patterns

### Adapter Pattern

The Adapter pattern allows incompatible interfaces to work together by converting the interface of a class into another interface clients expect.

```python
class EuropeanSocket:
    def voltage(self):
        return 230
    
    def live(self):
        return 1
    
    def neutral(self):
        return -1
    
    def earth(self):
        return 0

class USASocket:
    def voltage(self):
        return 120
    
    def live(self):
        return 1
    
    def neutral(self):
        return 0

class SocketAdapter:
    def __init__(self, socket):
        self.socket = socket
    
    def voltage(self):
        return self.socket.voltage()
    
    def live(self):
        return self.socket.live()
    
    def neutral(self):
        return self.socket.neutral()
    
    def earth(self):
        # European sockets have earth, USA sockets don't
        if hasattr(self.socket, 'earth'):
            return self.socket.earth()
        return 0

class Device:
    def __init__(self, power):
        self.power = power
    
    def recharge(self):
        return f"Charging at {self.power.voltage()}V..."

# Usage
european_socket = EuropeanSocket()
usa_socket = USASocket()

# Using adapter for European socket
european_adapter = SocketAdapter(european_socket)
device = Device(european_adapter)
print(device.recharge())  # Output: Charging at 230V...

# Using adapter for USA socket
usa_adapter = SocketAdapter(usa_socket)
device = Device(usa_adapter)
print(device.recharge())  # Output: Charging at 120V...
```

### Decorator Pattern

The Decorator pattern allows behavior to be added to individual objects, either statically or dynamically, without affecting the behavior of other objects from the same class.

```python
from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def cost(self):
        pass
    
    @abstractmethod
    def description(self):
        pass

class SimpleCoffee(Coffee):
    def cost(self):
        return 2.0
    
    def description(self):
        return "Simple coffee"

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()

class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.5
    
    def description(self):
        return self._coffee.description() + ", milk"
    
    def __init__(self, coffee):
        super().__init__(coffee)

class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.2
    
    def description(self):
        return self._coffee.description() + ", sugar"
    
    def __init__(self, coffee):
        super().__init__(coffee)

class Whip(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.7
    
    def description(self):
        return self._coffee.description() + ", whip"
    
    def __init__(self, coffee):
        super().__init__(coffee)

# Usage
coffee = SimpleCoffee()
print(f"{coffee.description()} costs ${coffee.cost()}")  # Output: Simple coffee costs $2.0

coffee = Milk(coffee)
coffee = Sugar(coffee)
print(f"{coffee.description()} costs ${coffee.cost()}")  # Output: Simple coffee, milk, sugar costs $2.7

coffee = Whip(coffee)
print(f"{coffee.description()} costs ${coffee.cost()}")  # Output: Simple coffee, milk, sugar, whip costs $3.4
```

## Behavioral Patterns

### Observer Pattern

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified automatically.

```python
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify()

class NewsAgency(Subject):
    def __init__(self):
        super().__init__()
        self._news = ""
    
    @property
    def news(self):
        return self._news
    
    @news.setter
    def news(self, value):
        self._news = value
        self.state = value  # This triggers notifications

class NewsChannel(Observer):
    def __init__(self, name):
        self.name = name
        self.news = ""
    
    def update(self, subject):
        if isinstance(subject, NewsAgency):
            self.news = subject.news
            print(f"{self.name} received news: {self.news}")

# Usage
agency = NewsAgency()
channel1 = NewsChannel("CNN")
channel2 = NewsChannel("BBC")
channel3 = NewsChannel("Fox News")

agency.attach(channel1)
agency.attach(channel2)
agency.attach(channel3)

agency.news = "Breaking: Major event occurred!"  # All channels receive this news

agency.detach(channel3)  # Fox News unsubscribes
agency.news = "Update: Situation resolved"  # Only CNN and BBC receive this
```

### Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.

```python
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount):
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        return f"Paid ${amount} using PayPal account {self.email}"

class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        return f"Paid ${amount} using Bitcoin to address {self.wallet_address[:10]}..."

class ShoppingCart:
    def __init__(self):
        self.items = []
        self.payment_strategy = None
    
    def add_item(self, item, price):
        self.items.append((item, price))
    
    def calculate_total(self):
        return sum(price for item, price in self.items)
    
    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy
    
    def checkout(self):
        if self.payment_strategy is None:
            raise Exception("Payment strategy not set")
        
        total = self.calculate_total()
        return self.payment_strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)

# Pay with credit card
credit_card = CreditCardPayment("1234567890123456", "123")
cart.set_payment_strategy(credit_card)
print(cart.checkout())  # Output: Paid $1029.98 using Credit Card ending in 3456

# Pay with PayPal
paypal = PayPalPayment("user@example.com")
cart.set_payment_strategy(paypal)
print(cart.checkout())  # Output: Paid $1029.98 using PayPal account user@example.com
```

### Command Pattern

The Command pattern turns a request into a stand-alone object that contains all information about the request. This transformation allows for parameterization of clients with queues, requests, and operations.

```python
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass

class Light:
    def __init__(self, name):
        self.name = name
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        return f"{self.name} light is ON"
    
    def turn_off(self):
        self.is_on = False
        return f"{self.name} light is OFF"

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light
        self.previous_state = light.is_on
    
    def execute(self):
        self.previous_state = self.light.is_on
        return self.light.turn_on()
    
    def undo(self):
        if self.previous_state:
            return self.light.turn_on()
        else:
            return self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
        self.previous_state = light.is_on
    
    def execute(self):
        self.previous_state = self.light.is_on
        return self.light.turn_off()
    
    def undo(self):
        if self.previous_state:
            return self.light.turn_on()
        else:
            return self.light.turn_off()

class RemoteControl:
    def __init__(self):
        self.commands = {}
        self.history = []
    
    def set_command(self, slot, command):
        self.commands[slot] = command
    
    def press_button(self, slot):
        if slot in self.commands:
            result = self.commands[slot].execute()
            self.history.append(self.commands[slot])
            return result
        return "No command assigned to this slot"
    
    def undo_last(self):
        if self.history:
            last_command = self.history.pop()
            return last_command.undo()
        return "No commands to undo"

# Usage
living_room_light = Light("Living Room")
bedroom_light = Light("Bedroom")

light_on = LightOnCommand(living_room_light)
light_off = LightOffCommand(living_room_light)

remote = RemoteControl()
remote.set_command("on", light_on)
remote.set_command("off", light_off)

print(remote.press_button("on"))   # Output: Living Room light is ON
print(remote.press_button("off"))  # Output: Living Room light is OFF
print(remote.undo_last())          # Output: Living Room light is ON
```

### Template Method Pattern

The Template Method pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

```python
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def process_data(self):
        """Template method defining the algorithm structure"""
        raw_data = self.load_data()
        processed_data = self.transform_data(raw_data)
        validated_data = self.validate_data(processed_data)
        self.save_data(validated_data)
        return "Data processing completed"
    
    @abstractmethod
    def load_data(self):
        pass
    
    @abstractmethod
    def transform_data(self, data):
        pass
    
    @abstractmethod
    def validate_data(self, data):
        pass
    
    @abstractmethod
    def save_data(self, data):
        pass

class CSVDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from CSV file...")
        return ["row1", "row2", "row3"]
    
    def transform_data(self, data):
        print("Transforming CSV data...")
        return [row.upper() for row in data]
    
    def validate_data(self, data):
        print("Validating CSV data...")
        return [row for row in data if len(row) > 0]
    
    def save_data(self, data):
        print(f"Saving {len(data)} records to database...")

class JSONDataProcessor(DataProcessor):
    def load_data(self):
        print("Loading data from JSON file...")
        return {"name": "John", "age": 30}
    
    def transform_data(self, data):
        print("Transforming JSON data...")
        return {k: str(v).upper() for k, v in data.items()}
    
    def validate_data(self, data):
        print("Validating JSON data...")
        return data if "NAME" in data else {}
    
    def save_data(self, data):
        print(f"Saving JSON data to database...")

# Usage
csv_processor = CSVDataProcessor()
print(csv_processor.process_data())
print()

json_processor = JSONDataProcessor()
print(json_processor.process_data())
```

## Benefits of Using Design Patterns

### 1. Reusability
Design patterns provide proven solutions that can be applied to similar problems in different contexts.

### 2. Maintainability
Patterns make code more readable and maintainable by providing common vocabulary and structure.

### 3. Scalability
Well-designed patterns make it easier to extend and modify applications.

### 4. Communication
Patterns provide a common language for developers to discuss solutions.

## Common Anti-Patterns to Avoid

### 1. Over-engineering
Applying patterns where simpler solutions would suffice.

### 2. Pattern Obsession
Forcing patterns into inappropriate situations just to use them.

### 3. God Object
Creating objects that know too much or do too much.

### 4. Spaghetti Code
Writing code with complex control structures that are difficult to follow.

## When to Use Design Patterns

- When facing a recurring problem that matches a known pattern
- When you need to improve code maintainability and readability
- When building systems that need to be extensible
- When working in teams to establish common understanding

## Conclusion

Design patterns are essential tools for any object-oriented programmer. They represent best practices and solutions that have been tested and refined over time. However, they should be used judiciously and only when they genuinely solve a problem. The key is to understand the patterns well enough to recognize when they're appropriate and when simpler solutions would be better.

Remember that design patterns are not silver bullets but rather guidelines that help create more maintainable, flexible, and reusable code. The most important thing is to understand the problem you're trying to solve and choose the most appropriate solution, whether it's a design pattern or a simpler approach.