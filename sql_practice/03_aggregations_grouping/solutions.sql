-- ============================================================
-- SQL PRACTICE - 03_AGGREGATIONS_GROUPING (SOLUTIONS)
-- ============================================================
-- database: practice.db (SQLite)
-- ============================================================

-- Q1: Find the total number of employees in the company.
SELECT COUNT(*) AS total_employees FROM employees;

-- Q2: Find the total budget allocated across all departments.
SELECT SUM(budget) AS total_budget FROM departments;

-- Q3: Find the average salary of all employees.
SELECT AVG(salary) AS average_salary FROM employees;

-- Q4: Find the maximum salary earned in the company.
SELECT MAX(salary) AS max_salary FROM employees;

-- Q5: Find the minimum salary earned in the company.
SELECT MIN(salary) AS min_salary FROM employees;

-- Q6: Find the total stock count of all products combined.
SELECT SUM(stock) AS total_stock FROM products;

-- Q7: Find the average price of all products.
SELECT AVG(price) AS average_price FROM products;

-- Q8: Find the maximum price of a product in the category "Electronics".
SELECT MAX(price) AS max_electronics_price FROM products WHERE category = 'Electronics';

-- Q9: Find the minimum price of a product in the category "Appliances".
SELECT MIN(price) AS min_appliances_price FROM products WHERE category = 'Appliances';

-- Q10: Find the total number of orders placed.
SELECT COUNT(*) AS total_orders FROM orders;

-- Q11: Find the total amount spent on all orders in the orders table.
SELECT SUM(total_amount) AS total_spent FROM orders;

-- Q12: Find the average order total.
SELECT AVG(total_amount) AS average_order FROM orders;

-- Q13: Find the total number of customers registered.
SELECT COUNT(*) AS total_customers FROM customers;

-- Q14: Find the total number of unique countries customers are from.
SELECT COUNT(DISTINCT country) AS unique_countries FROM customers;

-- Q15: Count how many employees belong to department_id 1.
SELECT COUNT(*) AS dept1_employees FROM employees WHERE department_id = 1;

-- Q16: Find the average salary of employees in department_id 2.
SELECT AVG(salary) AS dept2_avg_salary FROM employees WHERE department_id = 2;

-- Q17: Find the total number of products categorized as "Furniture".
SELECT COUNT(*) AS furniture_count FROM products WHERE category = 'Furniture';

-- Q18: Count how many orders have a status of "Completed".
SELECT COUNT(*) AS completed_orders FROM orders WHERE status = 'Completed';

-- Q19: Find the total quantity of items ordered in all order_items combined.
SELECT SUM(quantity) AS total_quantity FROM order_items;

-- Q20: Find the average quantity of items per order item line.
SELECT AVG(quantity) AS average_quantity FROM order_items;

-- Q21: Find the total number of employees in each department (GROUP BY department_id).
SELECT department_id, COUNT(*) AS employee_count FROM employees GROUP BY department_id;

-- Q22: Find the average salary of employees in each department (GROUP BY department_id).
SELECT department_id, AVG(salary) AS average_salary FROM employees GROUP BY department_id;

-- Q23: Find the maximum and minimum salary in each department.
SELECT department_id, MAX(salary) AS max_salary, MIN(salary) AS min_salary FROM employees GROUP BY department_id;

-- Q24: Find the total budget by location (GROUP BY location).
SELECT location, SUM(budget) AS total_budget FROM departments GROUP BY location;

-- Q25: Count the number of departments in each location.
SELECT location, COUNT(*) AS department_count FROM departments GROUP BY location;

-- Q26: Find the total quantity sold for each product (GROUP BY product_id).
SELECT product_id, SUM(quantity) AS total_sold FROM order_items GROUP BY product_id;

-- Q27: Find the average unit price of each product category.
SELECT category, AVG(price) AS average_price FROM products GROUP BY category;

-- Q28: Count the number of products in each category.
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category;

-- Q29: Find the total stock value (sum of stock * price) for each category.
SELECT category, SUM(stock * price) AS total_stock_value FROM products GROUP BY category;

-- Q30: Find the total number of orders placed by each customer (GROUP BY customer_id).
SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY customer_id;

-- Q31: Find the total amount spent by each customer (sum of total_amount).
SELECT customer_id, SUM(total_amount) AS total_spent FROM orders GROUP BY customer_id;

-- Q32: Find the average order amount for each customer.
SELECT customer_id, AVG(total_amount) AS average_spent FROM orders GROUP BY customer_id;

-- Q33: Count the number of customers in each country.
SELECT country, COUNT(*) AS customer_count FROM customers GROUP BY country;

-- Q34: Count the number of customers who signed up in each month of 2025.
SELECT strftime('%m', signup_date) AS month, COUNT(*) AS signups
FROM customers
WHERE signup_date LIKE '2025%'
GROUP BY month;

-- Q35: Count the number of orders placed in each month of 2025.
SELECT strftime('%m', order_date) AS month, COUNT(*) AS order_count
FROM orders
WHERE order_date LIKE '2025%'
GROUP BY month;

-- Q36: Find the total revenue generated in each month of 2025.
SELECT strftime('%m', order_date) AS month, SUM(total_amount) AS monthly_revenue
FROM orders
WHERE order_date LIKE '2025%'
GROUP BY month;

-- Q37: Find the average order total by order status.
SELECT status, AVG(total_amount) AS average_total FROM orders GROUP BY status;

-- Q38: Count the number of orders by status.
SELECT status, COUNT(*) AS order_count FROM orders GROUP BY status;

-- Q39: Find the maximum order total for each status.
SELECT status, MAX(total_amount) AS max_amount FROM orders GROUP BY status;

-- Q40: Count the number of employees reporting to each manager_id.
SELECT manager_id, COUNT(*) AS direct_reports FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id;

-- Q41: Find the average salary of employees reporting to each manager_id.
SELECT manager_id, AVG(salary) AS average_salary FROM employees WHERE manager_id IS NOT NULL GROUP BY manager_id;

-- Q42: Find departments with more than 3 employees (HAVING clause).
SELECT department_id, COUNT(*) AS employee_count 
FROM employees 
GROUP BY department_id 
HAVING employee_count > 3;

-- Q43: Find departments with an average salary greater than 80000.
SELECT department_id, AVG(salary) AS avg_salary 
FROM employees 
GROUP BY department_id 
HAVING avg_salary > 80000;

-- Q44: Find departments with a total salary expense greater than 200000.
SELECT department_id, SUM(salary) AS total_salaries
FROM employees 
GROUP BY department_id 
HAVING total_salaries > 200000;

-- Q45: Find product categories containing more than 2 products.
SELECT category, COUNT(*) AS product_count 
FROM products 
GROUP BY category 
HAVING product_count > 2;

-- Q46: Find product categories with average price greater than 100.
SELECT category, AVG(price) AS average_price 
FROM products 
GROUP BY category 
HAVING average_price > 100;

-- Q47: Find customers who have placed more than 2 orders.
SELECT customer_id, COUNT(*) AS order_count 
FROM orders 
GROUP BY customer_id 
HAVING order_count > 2;

-- Q48: Find customers who have spent a total of more than 1000 in orders.
SELECT customer_id, SUM(total_amount) AS total_spent 
FROM orders 
GROUP BY customer_id 
HAVING total_spent > 1000;

-- Q49: Find customers with average order total greater than 500.
SELECT customer_id, AVG(total_amount) AS average_order 
FROM orders 
GROUP BY customer_id 
HAVING average_order > 500;

-- Q50: Find countries with more than 3 customers.
SELECT country, COUNT(*) AS customer_count 
FROM customers 
GROUP BY country 
HAVING customer_count > 3;

-- Q51: Find locations with a total department budget exceeding 1000000.
SELECT location, SUM(budget) AS total_budget 
FROM departments 
GROUP BY location 
HAVING total_budget > 1000000;

-- Q52: Find managers who manage more than 2 employees.
SELECT manager_id, COUNT(*) AS direct_reports 
FROM employees 
WHERE manager_id IS NOT NULL 
GROUP BY manager_id 
HAVING direct_reports > 2;

-- Q53: Find product_ids that have been ordered a total quantity of more than 5.
SELECT product_id, SUM(quantity) AS total_quantity 
FROM order_items 
GROUP BY product_id 
HAVING total_quantity > 5;

-- Q54: Find orders containing more than 3 order items.
SELECT order_id, COUNT(*) AS item_count 
FROM order_items 
GROUP BY order_id 
HAVING item_count > 3;

-- Q55: Find the maximum salary of a department with budget > 500000.
SELECT e.department_id, MAX(e.salary) AS max_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.budget > 500000
GROUP BY e.department_id;

-- Q56: Find the average price of products in categories having at least 3 products.
SELECT category, AVG(price) AS average_price
FROM products
GROUP BY category
HAVING COUNT(id) >= 3;

-- Q57: Find the total amount spent by customers from USA.
SELECT c.country, SUM(o.total_amount) AS total_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'USA'
GROUP BY c.country;

-- Q60: Find the average quantity sold per order for products in the Electronics category.
SELECT p.category, AVG(oi.quantity) AS avg_quantity
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
WHERE p.category = 'Electronics'
GROUP BY p.category;

-- Q61: Count the number of employees hired in each year.
SELECT strftime('%Y', hire_date) AS hire_year, COUNT(*) AS hires_count
FROM employees
GROUP BY hire_year;

-- Q62: Find the total revenue by year (based on order_date).
SELECT strftime('%Y', order_date) AS order_year, SUM(total_amount) AS revenue
FROM orders
GROUP BY order_year;

-- Q63: Find the total number of items sold by product name (JOIN + GROUP BY).
SELECT p.name AS product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
GROUP BY p.name;

-- Q64: Find the average amount spent per order by country (JOIN + GROUP BY).
SELECT c.country, AVG(o.total_amount) AS average_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.country;

-- Q65: Find the total salary expense for each department name (JOIN + GROUP BY).
SELECT d.name AS department_name, SUM(e.salary) AS total_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.name;

-- Q66: Find the average salary of employees by department location.
SELECT d.location, AVG(e.salary) AS average_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.location;

-- Q67: Find the total quantity ordered of "Smartphone" (JOIN + GROUP BY).
SELECT p.name AS product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
WHERE p.name = 'Smartphone'
GROUP BY p.name;

-- Q68: Count the number of completed orders for each customer name.
SELECT c.first_name || ' ' || c.last_name AS customer_name, COUNT(o.id) AS completed_orders
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'Completed'
GROUP BY c.id;

-- Q69: Find the total revenue generated by each product name, sorted by revenue descending.
SELECT p.name AS product_name, SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
GROUP BY p.name
ORDER BY total_revenue DESC;

-- Q70: Find the average rating/revenue by product category, sorted by average descending.
SELECT p.category, AVG(oi.quantity * oi.unit_price) AS average_line_value
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
GROUP BY p.category
ORDER BY average_line_value DESC;

-- Q71: Find the count of employees who earn more than 90000 in each department.
SELECT d.name AS department_name, COUNT(e.id) AS high_earners
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE e.salary > 90000
GROUP BY d.name;

-- Q72: Find the average salary in departments having more than 2 employees earning > 80000.
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING SUM(CASE WHEN salary > 80000 THEN 1 ELSE 0 END) > 2;

-- Q73: Find customers who have placed orders in at least 2 different months.
SELECT customer_id, COUNT(DISTINCT strftime('%m', order_date)) AS unique_months
FROM orders
GROUP BY customer_id
HAVING unique_months >= 2;

-- Q74: Find products that have been ordered in at least 3 different orders.
SELECT product_id, COUNT(DISTINCT order_id) AS unique_orders
FROM order_items
GROUP BY product_id
HAVING unique_orders >= 3;

-- Q75: Find the customer name with the maximum total spending.
SELECT c.first_name || ' ' || c.last_name AS customer_name, SUM(o.total_amount) AS total_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.id
ORDER BY total_spent DESC
LIMIT 1;

-- Q76: Find the product name with the highest quantity sold.
SELECT p.name AS product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
GROUP BY p.id
ORDER BY total_sold DESC
LIMIT 1;

-- Q77: Find the department name with the highest average salary.
SELECT d.name AS department_name, AVG(e.salary) AS average_salary
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.id
ORDER BY average_salary DESC
LIMIT 1;

-- Q78: Find the manager name who manages the highest total salary sum.
SELECT m.first_name || ' ' || m.last_name AS manager_name, SUM(e.salary) AS managed_salary_sum
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
GROUP BY m.id
ORDER BY managed_salary_sum DESC
LIMIT 1;

-- Q79: Find the location with the highest number of employees.
SELECT d.location, COUNT(e.id) AS employee_count
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.location
ORDER BY employee_count DESC
LIMIT 1;

-- Q80: Find the total budget by location, showing only locations with average employee salary > 80000.
SELECT d.location, SUM(d.budget) AS total_budget
FROM departments d
WHERE d.location IN (
    SELECT d2.location
    FROM employees e2
    INNER JOIN departments d2 ON e2.department_id = d2.id
    GROUP BY d2.location
    HAVING AVG(e2.salary) > 80000
)
GROUP BY d.location;

-- Q81: Count how many orders are placed on each day of the week (0 = Sunday, 1 = Monday, etc.).
SELECT strftime('%w', order_date) AS day_of_week, COUNT(*) AS order_count
FROM orders
GROUP BY day_of_week;

-- Q82: Find the total revenue generated on weekends (Saturday & Sunday).
SELECT SUM(total_amount) AS weekend_revenue
FROM orders
WHERE strftime('%w', order_date) IN ('0', '6');

-- Q83: Count the number of customers signing up in each quarter of 2025.
-- Quarters: Q1 (Jan-Mar), Q2 (Apr-Jun), Q3 (Jul-Sep), Q4 (Oct-Dec)
SELECT 
    CASE 
        WHEN strftime('%m', signup_date) BETWEEN '01' AND '03' THEN 'Q1'
        WHEN strftime('%m', signup_date) BETWEEN '04' AND '06' THEN 'Q2'
        WHEN strftime('%m', signup_date) BETWEEN '07' AND '09' THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    COUNT(*) AS signup_count
FROM customers
WHERE signup_date LIKE '2025%'
GROUP BY quarter;

-- Q84: Find the total amount of orders placed in each quarter of 2025.
SELECT 
    CASE 
        WHEN strftime('%m', order_date) BETWEEN '01' AND '03' THEN 'Q1'
        WHEN strftime('%m', order_date) BETWEEN '04' AND '06' THEN 'Q2'
        WHEN strftime('%m', order_date) BETWEEN '07' AND '09' THEN 'Q3'
        ELSE 'Q4'
    END AS quarter,
    SUM(total_amount) AS revenue
FROM orders
WHERE order_date LIKE '2025%'
GROUP BY quarter;

-- Q85: Find the average salary of employees by length of tenure in years (assume current year is 2026).
SELECT (2026 - CAST(strftime('%Y', hire_date) AS INT)) AS tenure_years, AVG(salary) AS average_salary
FROM employees
GROUP BY tenure_years;

-- Q86: Count the number of products with stock levels: Low (< 20), Medium (20-50), High (> 50).
SELECT 
    CASE 
        WHEN stock < 20 THEN 'Low (< 20)'
        WHEN stock BETWEEN 20 AND 50 THEN 'Medium (20-50)'
        ELSE 'High (> 50)'
    END AS stock_level,
    COUNT(*) AS product_count
FROM products
GROUP BY stock_level;

-- Q87: Find the total amount of orders classified as Small (< 200), Medium (200-1000), Large (> 1000).
SELECT 
    CASE 
        WHEN total_amount < 200 THEN 'Small (< 200)'
        WHEN total_amount BETWEEN 200 AND 1000 THEN 'Medium (200-1000)'
        ELSE 'Large (> 1000)'
    END AS order_size,
    COUNT(*) AS order_count,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY order_size;

-- Q88: Count the number of employees earning more than their manager's salary.
SELECT COUNT(e.id) AS employee_count
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- Q89: Find the total budget of departments that have at least 1 employee earning > 100000.
SELECT SUM(budget) AS total_budget
FROM departments
WHERE id IN (
    SELECT DISTINCT department_id
    FROM employees
    WHERE salary > 100000
);

-- Q90: Count the number of active products (stock > 0) in each category.
SELECT category, COUNT(*) AS active_products
FROM products
WHERE stock > 0
GROUP BY category;

-- Q91: Find the average price of active products (stock > 0) in each category.
SELECT category, AVG(price) AS average_price
FROM products
WHERE stock > 0
GROUP BY category;

-- Q92: Find the total quantity sold for products that are out of stock (stock < 5).
SELECT p.name, SUM(oi.quantity) AS quantity_sold
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
WHERE p.stock < 5
GROUP BY p.name;

-- Q93: Find the total spending by customer country, sorted by total spending descending.
SELECT c.country, SUM(o.total_amount) AS total_spent
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.country
ORDER BY total_spent DESC;

-- Q94: Count the number of orders placed by customers from Germany.
SELECT c.country, COUNT(o.id) AS order_count
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'Germany'
GROUP BY c.country;

-- Q95: Find the average order total for completed orders placed by customers from Canada.
SELECT c.country, AVG(o.total_amount) AS average_order
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'Completed' AND c.country = 'Canada'
GROUP BY c.country;

-- Q96: Find the department name with the lowest total salary expense.
SELECT d.name AS department_name, SUM(e.salary) AS salary_expense
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.id
ORDER BY salary_expense ASC
LIMIT 1;

-- Q97: Find the location with the lowest average department budget.
SELECT location, AVG(budget) AS average_budget
FROM departments
GROUP BY location
ORDER BY average_budget ASC
LIMIT 1;

-- Q98: Find the manager name who has the lowest number of direct reports.
SELECT m.first_name || ' ' || m.last_name AS manager_name, COUNT(e.id) AS reports_count
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
GROUP BY m.id
ORDER BY reports_count ASC
LIMIT 1;

-- Q99: Find the product category with the highest total stock value.
SELECT category, SUM(stock * price) AS stock_value
FROM products
GROUP BY category
ORDER BY stock_value DESC
LIMIT 1;

-- Q100: Find the customer country with the highest average order total.
SELECT c.country, AVG(o.total_amount) AS average_order
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.country
ORDER BY average_order DESC
LIMIT 1;
