# Composition vs Inheritance in Object-Oriented Programming

## Introduction

In object-oriented programming, both composition and inheritance are fundamental techniques for code reuse and building complex systems. Understanding when to use each approach is crucial for designing maintainable and flexible software architectures.

## Definitions

### Inheritance
Inheritance is an "is-a" relationship where a class derives properties and methods from a parent class. The child class extends or specializes the parent class functionality.

### Composition
Composition is a "has-a" relationship where a class contains objects of other classes as members. It builds complex functionality by combining simpler components.

## Inheritance: The "Is-A" Relationship

Inheritance establishes an "is-a" relationship between classes, where a subclass is a specialized version of a superclass.

```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started"
    
    def stop_engine(self):
        return f"{self.brand} {self.model} engine stopped"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors
    
    def honk(self):
        return f"{self.brand} {self.model} goes beep beep!"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def wheelie(self):
        return f"{self.brand} {self.model} pops a wheelie!"

# Usage
car = Car("Toyota", "Camry", 4)
bike = Motorcycle("Harley", "Street 750", "750cc")

print(car.start_engine())  # Output: Toyota Camry engine started
print(car.honk())          # Output: Toyota Camry goes beep beep!
print(bike.wheelie())      # Output: Harley Street 750 pops a wheelie!
```

## Composition: The "Has-A" Relationship

Composition builds objects by combining other objects, creating a "has-a" relationship.

```python
class Engine:
    def __init__(self, horsepower, fuel_type="gasoline"):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False
    
    def start(self):
        self.running = True
        return f"Engine with {self.horsepower} HP started"
    
    def stop(self):
        self.running = False
        return f"Engine with {self.horsepower} HP stopped"

class Wheels:
    def __init__(self, count, tire_size):
        self.count = count
        self.tire_size = tire_size
    
    def rotate(self):
        return f"{self.count} wheels rotating with {self.tire_size} tires"

class GPS:
    def __init__(self, map_version):
        self.map_version = map_version
    
    def navigate(self, destination):
        return f"Navigating to {destination} using map v{self.map_version}"

class Car:
    def __init__(self, brand, model, engine_horsepower, tire_size):
        self.brand = brand
        self.model = model
        # Composition: Car HAS-A Engine, Wheels, and GPS
        self.engine = Engine(engine_horsepower)
        self.wheels = Wheels(4, tire_size)
        self.gps = GPS("2023.1")
    
    def start_journey(self, destination):
        engine_status = self.engine.start()
        wheel_status = self.wheels.rotate()
        navigation = self.gps.navigate(destination)
        
        return f"{engine_status}\n{wheel_status}\n{navigation}"

# Usage
my_car = Car("Honda", "Civic", 158, "205/55R16")
journey_details = my_car.start_journey("Downtown")
print(journey_details)
```

## Comparison: Inheritance vs Composition

| Aspect | Inheritance | Composition |
|--------|-------------|-------------|
| Relationship | "Is-a" | "Has-a" |
| Code Reuse | Through inheritance hierarchy | Through object aggregation |
| Flexibility | Limited by inheritance structure | High flexibility at runtime |
| Maintenance | Changes in parent can affect children | Changes in components don't affect container |
| Coupling | Tight coupling between parent and child | Loose coupling between components |
| Testing | Harder to test due to dependencies | Easier to test components independently |

## Advantages of Inheritance

### 1. Code Reuse
Inheritance allows sharing common functionality among related classes.

```python
class Shape:
    def __init__(self, color="white"):
        self.color = color
    
    def get_area(self):
        raise NotImplementedError("Subclass must implement")
    
    def describe(self):
        return f"A {self.color} shape with area {self.get_area()}"

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def get_area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

circle = Circle("red", 5)
rectangle = Rectangle("blue", 4, 6)

print(circle.describe())    # Output: A red shape with area 78.53975
print(rectangle.describe()) # Output: A blue shape with area 24
```

### 2. Polymorphism Support
Inheritance naturally supports polymorphism through method overriding.

```python
def process_shapes(shapes):
    for shape in shapes:
        print(f"Processing: {shape.describe()}")

shapes = [Circle("green", 3), Rectangle("yellow", 2, 8)]
process_shapes(shapes)
```

## Advantages of Composition

### 1. Greater Flexibility
Components can be swapped at runtime, providing greater flexibility.

```python
class EmailService:
    def send_email(self, recipient, subject, body):
        return f"Email sent to {recipient}: {subject}"

class SMSService:
    def send_sms(self, phone, message):
        return f"SMS sent to {phone}: {message}"

class NotificationManager:
    def __init__(self, notification_service):
        # Service can be swapped at runtime
        self.notification_service = notification_service
    
    def notify(self, recipient, message):
        if hasattr(self.notification_service, 'send_email'):
            return self.notification_service.send_email(recipient, "Notification", message)
        elif hasattr(self.notification_service, 'send_sms'):
            return self.notification_service.send_sms(recipient, message)

# Can switch services at runtime
email_service = EmailService()
sms_service = SMSService()

email_notifier = NotificationManager(email_service)
sms_notifier = NotificationManager(sms_service)

print(email_notifier.notify("user@example.com", "Hello!"))
print(sms_notifier.notify("+1234567890", "Hello!"))
```

### 2. Better Testability
Components can be easily mocked or replaced for testing purposes.

```python
class MockEmailService:
    def __init__(self):
        self.sent_emails = []
    
    def send_email(self, recipient, subject, body):
        self.sent_emails.append((recipient, subject, body))
        return f"Mock email sent to {recipient}"

# Testing with mock service
mock_service = MockEmailService()
notifier = NotificationManager(mock_service)
notifier.notify("test@example.com", "Test message")

assert len(mock_service.sent_emails) == 1
print("Test passed: Email was sent")
```

### 3. Looser Coupling
Classes are less dependent on each other, making the system more modular.

## When to Use Inheritance

### 1. Clear "Is-A" Relationship
Use inheritance when there's a genuine "is-a" relationship between classes.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Dog(Animal):  # Dog IS-A Animal
    def make_sound(self):
        return f"{self.name} says woof!"

class Cat(Animal):  # Cat IS-A Animal
    def make_sound(self):
        return f"{self.name} says meow!"
```

### 2. Shared Common Behavior
When classes share significant common behavior that should be centralized.

```python
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def get_info(self):
        return f"Employee: {self.name}, ID: {self.employee_id}"

class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department
```

## When to Use Composition

### 1. "Has-A" Relationship
Use composition when one object contains or uses another object.

```python
class Engine:
    def start(self):
        return "Engine started"

class Radio:
    def turn_on(self):
        return "Radio turned on"

class Car:
    def __init__(self):
        # Car HAS-A Engine and HAS-A Radio
        self.engine = Engine()
        self.radio = Radio()
    
    def start_car(self):
        engine_status = self.engine.start()
        radio_status = self.radio.turn_on()
        return f"{engine_status}, {radio_status}"
```

### 2. Building Complex Objects
When building complex objects from simpler components.

```python
class CPU:
    def process(self):
        return "CPU processing data"

class Memory:
    def store(self, data):
        return f"Memory storing: {data}"

class Storage:
    def save(self, data):
        return f"Storage saving: {data}"

class Computer:
    def __init__(self):
        # Computer composed of multiple components
        self.cpu = CPU()
        self.memory = Memory()
        self.storage = Storage()
    
    def boot_up(self):
        cpu_result = self.cpu.process()
        memory_result = self.memory.store("boot data")
        storage_result = self.storage.save("system files")
        
        return f"Booting: {cpu_result}, {memory_result}, {storage_result}"
```

### 3. Runtime Flexibility
When you need to change behavior at runtime.

```python
class FileLogger:
    def log(self, message):
        return f"Logging to file: {message}"

class ConsoleLogger:
    def log(self, message):
        return f"Logging to console: {message}"

class DatabaseLogger:
    def log(self, message):
        return f"Logging to database: {message}"

class Application:
    def __init__(self, logger):
        self.logger = logger
    
    def set_logger(self, new_logger):
        self.logger = new_logger  # Runtime flexibility
    
    def run_task(self, task):
        result = f"Running {task}"
        self.logger.log(result)
        return result

# Can change logging strategy at runtime
app = Application(FileLogger())
print(app.run_task("backup"))

app.set_logger(ConsoleLogger())
print(app.run_task("update"))
```

## The "Favor Composition Over Inheritance" Principle

This principle suggests that composition should be preferred over inheritance when possible because:

1. **Flexibility**: Components can be changed at runtime
2. **Maintainability**: Changes to one component don't affect others
3. **Testability**: Individual components can be tested separately
4. **Loose Coupling**: Less dependency between classes

```python
# Inheritance approach (less flexible)
class Bird:
    def fly(self):
        return "Flying high!"

class Eagle(Bird):
    def hunt(self):
        return "Hunting prey"

class Penguin(Bird):  # Problem: Penguins can't fly!
    def swim(self):
        return "Swimming underwater"

# Composition approach (more flexible)
class Flyable:
    def fly(self):
        return "Flying high!"

class Swimmable:
    def swim(self):
        return "Swimming underwater!"

class Animal:
    def __init__(self, abilities=None):
        self.abilities = abilities or []

class Eagle:
    def __init__(self):
        self.abilities = [Flyable()]
    
    def perform_abilities(self):
        results = []
        for ability in self.abilities:
            if hasattr(ability, 'fly'):
                results.append(ability.fly())
        return results

class Penguin:
    def __init__(self):
        self.abilities = [Swimmable()]
    
    def perform_abilities(self):
        results = []
        for ability in self.abilities:
            if hasattr(ability, 'swim'):
                results.append(ability.swim())
        return results
```

## Practical Example: A More Complex System

Let's compare both approaches in a more complex scenario:

### Inheritance Approach
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        return f"{self.brand} vehicle started"
    
    def stop(self):
        return f"{self.brand} vehicle stopped"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        return f"Charging {self.brand} with {self.battery_capacity}kWh battery"

class GasVehicle(Vehicle):
    def __init__(self, brand, fuel_capacity):
        super().__init__(brand)
        self.fuel_capacity = fuel_capacity
    
    def refuel(self):
        return f"Refueling {self.brand} with {self.fuel_capacity}L tank"
```

### Composition Approach
```python
class ElectricEngine:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity
    
    def start(self):
        return f"Electric engine started with {self.battery_capacity}kWh battery"
    
    def charge(self):
        return f"Charging electric engine with {self.battery_capacity}kWh battery"

class GasEngine:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity
    
    def start(self):
        return f"Gas engine started with {self.fuel_capacity}L fuel capacity"
    
    def refuel(self):
        return f"Refueling gas engine with {self.fuel_capacity}L tank"

class Vehicle:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Vehicle HAS-A Engine
    
    def start(self):
        return f"{self.brand} {self.engine.start()}"
    
    def perform_engine_operation(self):
        if hasattr(self.engine, 'charge'):
            return self.engine.charge()
        elif hasattr(self.engine, 'refuel'):
            return self.engine.refuel()

# Creating vehicles with different engines
electric_car = Vehicle("Tesla", ElectricEngine(75))
gas_car = Vehicle("Ford", GasEngine(60))

print(electric_car.start())  # Tesla Electric engine started with 75kWh battery
print(gas_car.start())       # Ford Gas engine started with 60L fuel capacity

print(electric_car.perform_engine_operation())  # Charging electric engine...
print(gas_car.perform_engine_operation())       # Refueling gas engine...
```

## Summary

Both inheritance and composition are valuable tools in object-oriented programming, each with their own strengths:

- **Use inheritance** when there's a clear "is-a" relationship and shared common behavior
- **Use composition** when there's a "has-a" relationship and you need flexibility
- **Favor composition over inheritance** when possible for better maintainability and flexibility
- **Consider the trade-offs** between code reuse (inheritance) and flexibility (composition)

The choice between inheritance and composition often depends on the specific problem domain and the anticipated changes to the system over time.