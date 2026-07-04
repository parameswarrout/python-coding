-- ============================================================
-- SQL PRACTICE - 02_JOINS (SOLUTIONS)
-- ============================================================
-- database: practice.db (SQLite)
-- ============================================================

-- Q1: Inner join employees and departments tables to show employee first name, last name, and department name.
SELECT e.first_name, e.last_name, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- Q2: Select employee email, salary, and department name for all employees in "Sales".
SELECT e.email, e.salary, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Sales';

-- Q3: Select product name, category, and quantity ordered from order_items joined with products.
SELECT p.name AS product_name, p.category, oi.quantity
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id;

-- Q4: Select order_date, total_amount, and customer first_name and last_name for all orders.
SELECT o.order_date, o.total_amount, c.first_name, c.last_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- Q5: Inner join customers and orders to show orders placed by customers from "USA".
SELECT o.id AS order_id, o.order_date, o.total_amount, c.first_name, c.last_name, c.country
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'USA';

-- Q6: Select employee first name, last name, and department location for employees working in "San Francisco".
SELECT e.first_name, e.last_name, d.location
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.location = 'San Francisco';

-- Q7: Select product name, unit_price from order_items, and order_date from orders.
SELECT p.name AS product_name, oi.unit_price, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id;

-- Q8: Select customer first name, last name, product name, and quantity ordered (requires 4-table join).
SELECT c.first_name, c.last_name, p.name AS product_name, oi.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id;

-- Q9: Select order_id, customer email, product name, and category (requires 4-table join).
SELECT o.id AS order_id, c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, p.category
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id;

-- Q10: Select employee first name, last name, and their manager's first name and last name (using self-join).
SELECT e.first_name, e.last_name, m.first_name AS manager_first_name, m.last_name AS manager_last_name
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id;

-- Q11: Select employee name and department name, including employees who do not belong to any department (LEFT JOIN).
SELECT e.first_name, e.last_name, d.name AS department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;

-- Q12: Select all customers and their order details, including customers who have never placed an order (LEFT JOIN).
SELECT c.first_name, c.last_name, o.id AS order_id, o.order_date, o.total_amount
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id;

-- Q13: Select all products and order item details, including products that have never been ordered.
SELECT p.name AS product_name, oi.order_id, oi.quantity, oi.unit_price
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id;

-- Q14: Select all departments and their employees, including departments with no employees.
SELECT d.name AS department_name, e.first_name, e.last_name
FROM departments d
LEFT JOIN employees e ON e.department_id = d.id;

-- Q15: Select employee first name, last name, and manager first name, including the CEO who has no manager (LEFT JOIN).
SELECT e.first_name, e.last_name, m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Q16: Select customer name, order_id, status, and total_amount, showing only customers who signed up in 2025.
SELECT c.first_name || ' ' || c.last_name AS customer_name, o.id AS order_id, o.status, o.total_amount
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
WHERE c.signup_date LIKE '2025%';

-- Q17: Select employee name, salary, and department budget for employees earning more than 10% of their department's budget.
SELECT e.first_name, e.last_name, e.salary, d.budget
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > (d.budget * 0.10);

-- Q18: Select customer name and order details for orders that are "Completed" or "Shipped".
SELECT c.first_name || ' ' || c.last_name AS customer_name, o.id AS order_id, o.status, o.total_amount
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
WHERE o.status IN ('Completed', 'Shipped');

-- Q19: Select product name, quantity, and total price (quantity * unit_price) for order items.
SELECT p.name AS product_name, oi.quantity, oi.quantity * oi.unit_price AS total_price
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id;

-- Q20: Select all pairs of employees who share the same manager (excluding pairs with themselves).
SELECT e1.first_name || ' ' || e1.last_name AS employee_1,
       e2.first_name || ' ' || e2.last_name AS employee_2,
       e1.manager_id
FROM employees e1
INNER JOIN employees e2 ON e1.manager_id = e2.manager_id
WHERE e1.id < e2.id AND e1.manager_id IS NOT NULL;

-- Q21: Select all pairs of employees who work in the same department and location.
SELECT e1.first_name || ' ' || e1.last_name AS employee_1,
       e2.first_name || ' ' || e2.last_name AS employee_2,
       d.name AS department, d.location
FROM employees e1
INNER JOIN employees e2 ON e1.department_id = e2.department_id
INNER JOIN departments d ON e1.department_id = d.id
WHERE e1.id < e2.id;

-- Q22: Select employee name and manager name, showing only cases where the employee earns more than their manager.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary AS employee_salary,
       m.first_name || ' ' || m.last_name AS manager_name, m.salary AS manager_salary
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- Q23: Select customer name and product name for products ordered by customers from "Canada".
SELECT DISTINCT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE c.country = 'Canada';

-- Q24: Select product name, price, order_date, and quantity for order items of products costing more than 500.
SELECT p.name AS product_name, p.price, o.order_date, oi.quantity
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE p.price > 500;

-- Q25: Select customer name and order_date, including customers with no orders, sorted by signup_date.
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.signup_date, o.order_date
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
ORDER BY c.signup_date ASC;

-- Q26: Select order_id, order_date, product name, and category for orders placed in "2025-03".
SELECT o.id AS order_id, o.order_date, p.name AS product_name, p.category
FROM orders o
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.order_date LIKE '2025-03%';

-- Q27: Select employee name and department name, showing only employees hired in 2023.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.hire_date, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.hire_date LIKE '2023%';

-- Q28: Select all products and show the count of times ordered (even if 0, LEFT JOIN).
SELECT p.name AS product_name, COUNT(oi.id) AS times_ordered
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
GROUP BY p.name;

-- Q29: Select customer name, product name, and status for orders with status "Cancelled".
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.status = 'Cancelled';

-- Q30: Select customer name and order total, showing only customers who signed up after 2025-06-01.
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.signup_date, o.id AS order_id, o.total_amount
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
WHERE c.signup_date > '2025-06-01';

-- Q31: Select employee name, manager name, and department name (requires 3-table join with self-join).
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name,
       d.name AS department_name
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
INNER JOIN departments d ON e.department_id = d.id;

-- Q32: Select all locations and employee names working at those locations (include locations with no employees).
SELECT d.location, e.first_name || ' ' || e.last_name AS employee_name
FROM departments d
LEFT JOIN employees e ON e.department_id = d.id;

-- Q33: Select all customers who signed up before 2025-05-01 and show their orders (include those with no orders).
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.signup_date, o.id AS order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE c.signup_date < '2025-05-01';

-- Q34: Select product name, category, and quantity for order items with status "Shipped".
SELECT p.name AS product_name, p.category, oi.quantity, o.status
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Shipped';

-- Q35: Select customer name and product name, showing only products in the category "Appliances".
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, p.category
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Appliances';

-- Q36: Select employee name and department budget for employees earning less than 80000.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.budget
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary < 80000;

-- Q37: Select all orders and display customer email, showing only orders placed in the first quarter of 2025.
-- First quarter: Jan, Feb, Mar (2025-01-01 to 2025-03-31)
SELECT o.id AS order_id, o.order_date, c.first_name || ' ' || c.last_name AS customer_name, o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.order_date BETWEEN '2025-01-01' AND '2025-03-31';

-- Q38: Select product name, stock, and total amount spent on that product in all orders combined.
SELECT p.name AS product_name, p.stock, SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
GROUP BY p.id;

-- Q39: Select customer name and department name for customers who share the same last name as any employee.
SELECT c.first_name || ' ' || c.last_name AS customer_name, d.name AS department_name
FROM customers c
INNER JOIN employees e ON c.last_name = e.last_name
INNER JOIN departments d ON e.department_id = d.id;

-- Q40: Select employee name and department name, showing only employees managed by manager_id 2 (Bob).
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.manager_id = 2;

-- Q41: Select all combinations of customers and products (CROSS JOIN).
SELECT c.first_name, c.last_name, p.name AS product_name
FROM customers c
CROSS JOIN products p;

-- Q42: Select all combinations of departments and products.
SELECT d.name AS department_name, p.name AS product_name
FROM departments d
CROSS JOIN products p;

-- Q43: Select employee name and manager name, showing only managers who were hired BEFORE their employee.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.hire_date AS employee_hire,
       m.first_name || ' ' || m.last_name AS manager_name, m.hire_date AS manager_hire
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE m.hire_date < e.hire_date;

-- Q44: Select employee name and manager name, showing only managers who were hired AFTER their employee.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.hire_date AS employee_hire,
       m.first_name || ' ' || m.last_name AS manager_name, m.hire_date AS manager_hire
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE m.hire_date > e.hire_date;

-- Q45: Select customer name and product name for orders containing more than 2 items of that product.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, oi.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE oi.quantity > 2;

-- Q46: Select product name and order status, showing only products with stock less than 30.
SELECT p.name AS product_name, p.stock, o.id AS order_id, o.status
FROM products p
INNER JOIN order_items oi ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE p.stock < 30;

-- Q47: Select customer name, order date, and total amount for orders exceeding 1000.
SELECT c.first_name || ' ' || c.last_name AS customer_name, o.order_date, o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.total_amount > 1000;

-- Q48: Select employee name, salary, and department name, sorted by department name, then by salary descending.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
ORDER BY d.name ASC, e.salary DESC;

-- Q49: Select product name, category, and order date, sorted by order date descending.
SELECT p.name AS product_name, p.category, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
ORDER BY o.order_date DESC;

-- Q50: Select customer name and signup date for customers who ordered "Laptop".
SELECT DISTINCT c.first_name || ' ' || c.last_name AS customer_name, c.signup_date
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE p.name = 'Laptop';

-- Q51: Select employee name and department name for employees earning between 70000 and 100000.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary BETWEEN 70000 AND 100000;

-- Q52: Select product name, stock, quantity ordered, and order date for orders in 2025.
SELECT p.name AS product_name, p.stock, oi.quantity, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.order_date LIKE '2025%';

-- Q53: Select customer name, country, and product category for products they ordered.
SELECT DISTINCT c.first_name || ' ' || c.last_name AS customer_name, c.country, p.category
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id;

-- Q54: Select employee name and manager email for employees in the "Engineering" department.
SELECT e.first_name || ' ' || e.last_name AS employee_name, m.email AS manager_email
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Engineering';

-- Q55: Select all customers who signed up on the same day as any other customer.
SELECT c1.first_name || ' ' || c1.last_name AS customer_1,
       c2.first_name || ' ' || c2.last_name AS customer_2,
       c1.signup_date
FROM customers c1
INNER JOIN customers c2 ON c1.signup_date = c2.signup_date
WHERE c1.id < c2.id;

-- Q56: Select all products with the same price as any other product.
SELECT p1.name AS product_1, p2.name AS product_2, p1.price
FROM products p1
INNER JOIN products p2 ON p1.price = p2.price
WHERE p1.id < p2.id;

-- Q57: Select employee name, department name, and manager name, showing only employees in New York.
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       d.name AS department_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN employees m ON e.manager_id = m.id
WHERE d.location = 'New York';

-- Q58: Select customer name, product name, and order date for orders placed on a Monday.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE strftime('%w', o.order_date) = '1';

-- Q59: Select product name, stock, and order status, showing only completed orders of out-of-stock items (stock < 5).
SELECT p.name AS product_name, p.stock, o.status
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Completed' AND p.stock < 5;

-- Q60: Select employee name, salary, and department location for employees earning more than 100000.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.location
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > 100000;

-- Q61: Select customer name and order count for customers from USA.
SELECT c.first_name || ' ' || c.last_name AS customer_name, COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE c.country = 'USA'
GROUP BY c.id;

-- Q62: Select product name and total quantity ordered, sorted by quantity descending.
SELECT p.name AS product_name, SUM(oi.quantity) AS total_ordered
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
GROUP BY p.id
ORDER BY total_ordered DESC;

-- Q63: Select employee name and department name, showing only employees hired in the month of August.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name, e.hire_date
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE strftime('%m', e.hire_date) = '08';

-- Q64: Select customer name, order total, and status, showing only completed orders over 500.
SELECT c.first_name || ' ' || c.last_name AS customer_name, o.total_amount, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'Completed' AND o.total_amount > 500;

-- Q65: Select product name, category, and quantity ordered, showing only electronics products.
SELECT p.name AS product_name, p.category, oi.quantity
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Electronics';

-- Q66: Select employee name and manager name, showing only employees with salary > 90000.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.salary > 90000;

-- Q67: Select customer name and product name, showing only apparel products.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, p.category
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Apparel';

-- Q68: Select employee name, department name, and salary for employees earning less than the average company salary.
-- Using simple subquery inside JOIN for reference
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name, e.salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary < (SELECT AVG(salary) FROM employees);

-- Q69: Select product name, price, and order status, showing only products costing less than 100.
SELECT DISTINCT p.name AS product_name, p.price, o.status
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE p.price < 100;

-- Q70: Select customer name, order total, and order status for pending orders.
SELECT c.first_name || ' ' || c.last_name AS customer_name, o.total_amount, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'Pending';

-- Q71: Select employee name, manager name, and manager salary (using self-join).
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name,
       m.salary AS manager_salary
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id;

-- Q72: Select customer name, country, and product name, showing only customers from Canada.
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.country, p.name AS product_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE c.country = 'Canada';

-- Q73: Select product name, category, and order date, showing only orders placed in the second half of 2025.
SELECT p.name AS product_name, p.category, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.order_date BETWEEN '2025-07-01' AND '2025-12-31';

-- Q74: Select employee name and department budget, sorted by budget descending.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.budget, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
ORDER BY d.budget DESC;

-- Q75: Select customer name, product name, and total price (quantity * unit_price) sorted by total price descending.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, oi.quantity * oi.unit_price AS total_price
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY total_price DESC;

-- Q76: Select employee name, department name, and manager name, sorted by manager name.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN employees m ON e.manager_id = m.id
ORDER BY manager_name ASC;

-- Q77: Select customer name, country, and order total for orders placed in the first half of 2025.
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.country, o.total_amount, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.order_date BETWEEN '2025-01-01' AND '2025-06-30';

-- Q78: Select product name and total stock value (stock * price).
SELECT name AS product_name, stock * price AS total_stock_value FROM products;

-- Q79: Select employee name, hire date, and manager name, sorted by hire date descending.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.hire_date,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
ORDER BY e.hire_date DESC;

-- Q80: Select customer name, product name, and order status, sorted by product name.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY product_name ASC;

-- Q81: Select employee name, department name, and salary, showing only employees in San Francisco.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name, e.salary, d.location
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.location = 'San Francisco';

-- Q82: Select customer name, country, and product category, sorted by country.
SELECT DISTINCT c.first_name || ' ' || c.last_name AS customer_name, c.country, p.category
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY c.country ASC;

-- Q83: Select product name, price, and order status, sorted by price ascending.
SELECT DISTINCT p.name AS product_name, p.price, o.status
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
ORDER BY p.price ASC;

-- Q84: Select employee name, manager name, and department budget, showing only employees with budget > 500000.
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name,
       d.budget
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
INNER JOIN departments d ON e.department_id = d.id
WHERE d.budget > 500000;

-- Q85: Select customer name, product name, and order status, showing only completed orders of laptops.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.status = 'Completed' AND p.name = 'Laptop';

-- Q86: Select employee name, salary, and department name, showing only employees in the HR department.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'HR';

-- Q87: Select customer name, product name, and quantity ordered, sorted by quantity descending.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, oi.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY oi.quantity DESC;

-- Q88: Select product name, category, and order date, showing only orders placed in 2025-08.
SELECT p.name AS product_name, p.category, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.order_date LIKE '2025-08%';

-- Q89: Select employee name, department name, and manager name, showing only employees hired before 2022-01-01.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.hire_date < '2022-01-01';

-- Q90: Select customer name, product name, and order total, sorted by order total descending.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY o.total_amount DESC;

-- Q91: Select employee name, salary, and department budget, showing only employees earning > 100000.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.budget
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > 100000;

-- Q92: Select customer name, country, and product name, sorted by customer name.
SELECT c.first_name || ' ' || c.last_name AS customer_name, c.country, p.name AS product_name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY customer_name ASC;

-- Q93: Select product name, stock, and order status, showing only pending orders.
SELECT p.name AS product_name, p.stock, o.status
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'Pending';

-- Q94: Select employee name, manager name, and department name, showing only employees in the Sales department.
SELECT e.first_name || ' ' || e.last_name AS employee_name,
       m.first_name || ' ' || m.last_name AS manager_name,
       d.name AS department_name
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Sales';

-- Q95: Select customer name, product name, and order status, showing only cancelled orders.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.status = 'Cancelled';

-- Q96: Select employee name, salary, and department name, showing only employees in the Finance department.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary, d.name AS department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Finance';

-- Q97: Select customer name, product name, and quantity ordered, showing only orders placed by customers from Germany.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, oi.quantity
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
WHERE c.country = 'Germany';

-- Q98: Select product name, category, and order date, showing only orders placed in 2025-09.
SELECT p.name AS product_name, p.category, o.order_date
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
INNER JOIN orders o ON oi.order_id = o.id
WHERE o.order_date LIKE '2025-09%';

-- Q99: Select employee name, department name, and manager name, showing only employees hired after 2023-01-01.
SELECT e.first_name || ' ' || e.last_name AS employee_name, d.name AS department_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.hire_date > '2023-01-01';

-- Q100: Select customer name, product name, and order total, sorted by order total ascending.
SELECT c.first_name || ' ' || c.last_name AS customer_name, p.name AS product_name, o.total_amount
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
INNER JOIN order_items oi ON oi.order_id = o.id
INNER JOIN products p ON oi.product_id = p.id
ORDER BY o.total_amount ASC;
