import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice.db")

def init_db():
    print("Initializing practice.db SQLite database...")
    
    # Remove existing database if it exists to start fresh
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Enable foreign keys
    cursor.execute("PRAGMA foreign_keys = ON;")
    
    # Create DEPARTMENTS table
    cursor.execute("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        budget REAL NOT NULL,
        location TEXT NOT NULL
    );
    """)
    
    # Create EMPLOYEES table
    cursor.execute("""
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        hire_date TEXT NOT NULL,
        salary REAL NOT NULL,
        department_id INTEGER,
        manager_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(id),
        FOREIGN KEY (manager_id) REFERENCES employees(id)
    );
    """)
    
    # Create CUSTOMERS table
    cursor.execute("""
    CREATE TABLE customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        country TEXT NOT NULL,
        signup_date TEXT NOT NULL
    );
    """)
    
    # Create PRODUCTS table
    cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    );
    """)
    
    # Create ORDERS table
    cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER NOT NULL,
        order_date TEXT NOT NULL,
        total_amount REAL NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('Pending', 'Completed', 'Cancelled', 'Shipped')),
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    );
    """)
    
    # Create ORDER_ITEMS table
    cursor.execute("""
    CREATE TABLE order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER NOT NULL,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        unit_price REAL NOT NULL,
        FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products(id)
    );
    """)
    
    # Insert DEPARTMENTS data
    departments = [
        ("Engineering", 1500000.00, "San Francisco"),
        ("Sales", 800000.00, "New York"),
        ("Marketing", 500000.00, "London"),
        ("HR", 300000.00, "San Francisco"),
        ("Finance", 600000.00, "New York")
    ]
    cursor.executemany("INSERT INTO departments (name, budget, location) VALUES (?, ?, ?);", departments)
    
    # Insert EMPLOYEES data (establishing management hierarchy)
    # Alice (CEO/Director - no manager_id)
    cursor.execute("INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id, manager_id) VALUES ('Alice', 'Smith', 'alice.smith@company.com', '2020-01-15', 180000.00, 1, NULL);")
    alice_id = cursor.lastrowid
    
    # Bob (Engineering Manager reports to Alice)
    cursor.execute(f"INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id, manager_id) VALUES ('Bob', 'Jones', 'bob.jones@company.com', '2021-03-10', 120000.00, 1, {alice_id});")
    bob_id = cursor.lastrowid
    
    # Charlie (Sales Manager reports to Alice)
    cursor.execute(f"INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id, manager_id) VALUES ('Charlie', 'Brown', 'charlie.brown@company.com', '2021-06-01', 110000.00, 2, {alice_id});")
    charlie_id = cursor.lastrowid
    
    # Other employees reporting to managers
    employees = [
        # Engineering team (reporting to Bob)
        ("David", "Wilson", "david.wilson@company.com", "2022-08-15", 95000.00, 1, bob_id),
        ("Eva", "Davis", "eva.davis@company.com", "2023-01-10", 90000.00, 1, bob_id),
        ("Frank", "Miller", "frank.miller@company.com", "2023-09-01", 85000.00, 1, bob_id),
        # Sales team (reporting to Charlie)
        ("Grace", "Garcia", "grace.garcia@company.com", "2022-02-20", 75000.00, 2, charlie_id),
        ("Henry", "Martinez", "henry.martinez@company.com", "2022-11-05", 70000.00, 2, charlie_id),
        ("Ivy", "Robinson", "ivy.robinson@company.com", "2024-03-01", 65000.00, 2, charlie_id),
        # Marketing team (no manager, department head is Alice, reports to Alice)
        ("Jack", "Clark", "jack.clark@company.com", "2022-05-12", 80000.00, 3, alice_id),
        ("Karen", "Rodriguez", "karen.rodriguez@company.com", "2023-04-18", 78000.00, 3, alice_id),
        # HR team (reporting to Alice)
        ("Leo", "Lewis", "leo.lewis@company.com", "2021-08-01", 82000.00, 4, alice_id),
        ("Mia", "Lee", "mia.lee@company.com", "2023-11-15", 60000.00, 4, alice_id),
        # Finance team (reporting to Alice)
        ("Nathan", "Walker", "nathan.walker@company.com", "2020-10-01", 105000.00, 5, alice_id),
        ("Olivia", "Hall", "olivia.hall@company.com", "2023-07-01", 88000.00, 5, alice_id)
    ]
    cursor.executemany("INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id, manager_id) VALUES (?, ?, ?, ?, ?, ?, ?);", employees)
    
    # Insert CUSTOMERS data
    customers = [
        ("John", "Doe", "USA", "2025-01-10"),
        ("Jane", "Doe", "USA", "2025-01-12"),
        ("Michael", "Johnson", "Canada", "2025-02-01"),
        ("Emily", "Williams", "UK", "2025-02-15"),
        ("James", "Brown", "USA", "2025-03-02"),
        ("Emma", "Jones", "Australia", "2025-03-20"),
        ("Daniel", "Miller", "Germany", "2025-04-01"),
        ("Sophia", "Davis", "UK", "2025-04-05"),
        ("Alexander", "Rodriguez", "USA", "2025-05-11"),
        ("Isabella", "Martinez", "Spain", "2025-05-22"),
        ("Liam", "Hernandez", "Canada", "2025-06-01"),
        ("Olivia", "Lopez", "Mexico", "2025-06-15"),
        ("Noah", "Gonzalez", "Spain", "2025-07-01"),
        ("Ava", "Wilson", "USA", "2025-07-22"),
        ("Ethan", "Anderson", "Germany", "2025-08-05"),
        ("Mia", "Thomas", "Canada", "2025-08-19"),
        ("Lucas", "Taylor", "Australia", "2025-09-01"),
        ("Charlotte", "Moore", "UK", "2025-09-12"),
        ("Mason", "Jackson", "USA", "2025-10-02"),
        ("Amelia", "Martin", "France", "2025-10-25")
    ]
    cursor.executemany("INSERT INTO customers (first_name, last_name, country, signup_date) VALUES (?, ?, ?, ?);", customers)
    
    # Insert PRODUCTS data
    products = [
        ("Laptop", "Electronics", 1200.00, 50),
        ("Smartphone", "Electronics", 800.00, 100),
        ("Headphones", "Electronics", 150.00, 200),
        ("Desk Chair", "Furniture", 250.00, 30),
        ("Standing Desk", "Furniture", 500.00, 15),
        ("Coffee Maker", "Appliances", 100.00, 40),
        ("Blender", "Appliances", 80.00, 60),
        ("T-Shirt", "Apparel", 25.00, 500),
        ("Jeans", "Apparel", 60.00, 300),
        ("Running Shoes", "Apparel", 120.00, 80)
    ]
    cursor.executemany("INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?);", products)
    
    # Insert ORDERS data
    orders = [
        (1, "2025-01-15", 1350.00, "Completed"),
        (2, "2025-01-18", 800.00, "Completed"),
        (3, "2025-02-05", 250.00, "Completed"),
        (4, "2025-02-20", 1750.00, "Completed"),
        (1, "2025-03-01", 150.00, "Completed"),
        (5, "2025-03-10", 600.00, "Completed"),
        (6, "2025-03-25", 80.00, "Cancelled"),
        (7, "2025-04-02", 1200.00, "Completed"),
        (8, "2025-04-15", 350.00, "Completed"),
        (9, "2025-05-12", 2150.00, "Completed"),
        (10, "2025-05-28", 120.00, "Completed"),
        (11, "2025-06-05", 800.00, "Completed"),
        (12, "2025-06-20", 25.00, "Completed"),
        (13, "2025-07-02", 500.00, "Shipped"),
        (14, "2025-07-25", 1375.00, "Completed"),
        (15, "2025-08-08", 180.00, "Completed"),
        (3, "2025-08-20", 1200.00, "Completed"),
        (16, "2025-08-22", 800.00, "Completed"),
        (17, "2025-09-05", 300.00, "Completed"),
        (18, "2025-09-18", 150.00, "Completed"),
        (19, "2025-10-05", 1200.00, "Pending"),
        (20, "2025-10-28", 125.00, "Completed"),
        (1, "2025-11-02", 400.00, "Completed"),
        (4, "2025-11-15", 300.00, "Completed"),
        (8, "2025-12-01", 150.00, "Completed")
    ]
    cursor.executemany("INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES (?, ?, ?, ?);", orders)
    
    # Insert ORDER_ITEMS data
    order_items = [
        # Order 1 (Laptop + Headphones)
        (1, 1, 1, 1200.00),
        (1, 3, 1, 150.00),
        # Order 2 (Smartphone)
        (2, 2, 1, 800.00),
        # Order 3 (Desk Chair)
        (3, 4, 1, 250.00),
        # Order 4 (Laptop + Standing Desk + Coffee Maker)
        (4, 1, 1, 1200.00),
        (4, 5, 1, 500.00),
        (4, 6, 1, 50.00), # discounted
        # Order 5 (Headphones)
        (5, 3, 1, 150.00),
        # Order 6 (Standing Desk + Coffee Maker)
        (6, 5, 1, 500.00),
        (6, 6, 1, 100.00),
        # Order 7 (Blender - Cancelled)
        (7, 7, 1, 80.00),
        # Order 8 (Laptop)
        (8, 1, 1, 1200.00),
        # Order 9 (Coffee Maker + Desk Chair)
        (9, 6, 1, 100.00),
        (9, 4, 1, 250.00),
        # Order 10 (Laptop + Standing Desk + Running Shoes + T-Shirt)
        (10, 1, 1, 1200.00),
        (10, 5, 1, 500.00),
        (10, 10, 3, 120.00),
        (10, 8, 3, 25.00),
        # Order 11 (Running Shoes)
        (11, 10, 1, 120.00),
        # Order 12 (Smartphone)
        (12, 2, 1, 800.00),
        # Order 13 (T-Shirt)
        (13, 8, 1, 25.00),
        # Order 14 (Standing Desk)
        (14, 5, 1, 500.00),
        # Order 15 (Laptop + Headphones)
        (15, 1, 1, 1200.00),
        (15, 3, 1, 150.00),
        (15, 8, 1, 25.00),
        # Order 16 (Coffee Maker + Blender)
        (16, 6, 1, 100.00),
        (16, 7, 1, 80.00),
        # Order 17 (Laptop)
        (17, 1, 1, 1200.00),
        # Order 18 (Smartphone)
        (18, 2, 1, 800.00),
        # Order 19 (Desk Chair + T-Shirt)
        (19, 4, 1, 250.00),
        (19, 8, 2, 25.00),
        # Order 20 (Headphones)
        (20, 3, 1, 150.00),
        # Order 21 (Laptop - Pending)
        (21, 1, 1, 1200.00),
        # Order 22 (Running Shoes + Jeans)
        (22, 10, 1, 120.00),
        (22, 9, 2, 60.00), # discount
        # Order 23 (Standing Desk - discounted)
        (23, 5, 1, 400.00),
        # Order 24 (Desk Chair + Coffee Maker)
        (24, 4, 1, 200.00),
        (24, 6, 1, 100.00),
        # Order 25 (Headphones)
        (25, 3, 1, 150.00)
    ]
    cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?);", order_items)
    
    conn.commit()
    conn.close()
    print("Database practice.db initialized successfully!")

if __name__ == "__main__":
    init_db()
