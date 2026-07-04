-- ============================================================
-- SQL PRACTICE - 06_SENIOR_SQL_OPTIMIZATION_DESIGN (SOLUTIONS)
-- ============================================================
-- database: practice.db (SQLite)
-- ============================================================

-- Q1: Write a query to view the execution plan of a SELECT * FROM employees where id = 5 (use EXPLAIN QUERY PLAN).
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE id = 5;

-- Q2: View the execution plan for finding an employee by email. Note if it uses SCAN (table scan) or SEARCH (indexed search).
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE email = 'bob.jones@company.com';

-- Q3: Write a command to create an index on the email column of the employees table.
CREATE INDEX idx_employees_email ON employees(email);

-- Q4: Re-run the execution plan for finding an employee by email to verify it now uses SEARCH TABLE USING INDEX.
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE email = 'bob.jones@company.com';

-- Q5: View the execution plan for finding products by name.
EXPLAIN QUERY PLAN SELECT * FROM products WHERE name = 'Laptop';

-- Q6: Write a command to create an index on the name column of the products table.
CREATE INDEX idx_products_name ON products(name);

-- Q7: Re-run the execution plan for finding products by name to verify index usage.
EXPLAIN QUERY PLAN SELECT * FROM products WHERE name = 'Laptop';

-- Q8: Create a composite index on order_items table for columns (order_id, product_id).
CREATE INDEX idx_order_items_composite ON order_items(order_id, product_id);

-- Q9: Run EXPLAIN QUERY PLAN for a query joining orders, order_items, and products to observe how SQLite handles the joins.
EXPLAIN QUERY PLAN 
SELECT o.id, p.name, oi.quantity 
FROM orders o 
INNER JOIN order_items oi ON o.id = oi.order_id 
INNER JOIN products p ON oi.product_id = p.id;

-- Q10: Drop the index created on the product name.
DROP INDEX idx_products_name;

-- Q11: Explain what normal form a table is in if it contains multi-valued attributes, and how to fix it (1NF).
-- First Normal Form (1NF): A table is in 1NF if and only if the domain of each attribute contains only atomic values, 
-- and the value of each attribute contains only a single value from that domain. 
-- Fix: Remove multi-valued attributes and place them into their own table.

-- Q12: Explain what normal form a table is in if it has partial dependencies, and how to split it (2NF).
-- Second Normal Form (2NF): A table is in 2NF if it is in 1NF and all non-key attributes are fully functionally dependent 
-- on the primary key (no partial dependencies where a column depends only on part of a composite primary key).
-- Fix: Split the table, moving partially dependent columns to a new table with their corresponding key.

-- Q13: Explain what normal form a table is in if it has transitive dependencies, and how to split it (3NF).
-- Third Normal Form (3NF): A table is in 3NF if it is in 2NF and no non-key attribute is transitively dependent on the primary key 
-- (no non-key attribute depends on another non-key attribute).
-- Fix: Move transitively dependent columns to a separate table.

-- Q14: Write a command to create a new table "suppliers" with a CHECK constraint that supplier_status must be 'Active' or 'Inactive'.
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    supplier_status TEXT CHECK(supplier_status IN ('Active', 'Inactive'))
);

-- Q15: Write a command to alter the employees table to add a constraint that salary must be greater than 0 (in SQLite, write ALTER TABLE or create new table).
-- Note: SQLite does not support adding constraints via ALTER TABLE directly. You must recreate the table, or use a trigger/rule.
-- Conceptual table structure:
-- CREATE TABLE employees_new (id INTEGER PRIMARY KEY, salary REAL CHECK(salary > 0));

-- Q16: Simulate a transaction by beginning, inserting a new department, and committing (BEGIN TRANSACTION, COMMIT).
BEGIN TRANSACTION;
INSERT INTO departments (name, budget, location) VALUES ('Security', 150000.00, 'San Francisco');
COMMIT;

-- Q17: Simulate a failed transaction rollback by beginning, inserting a new employee, and rolling back (BEGIN TRANSACTION, ROLLBACK).
BEGIN TRANSACTION;
INSERT INTO employees (first_name, last_name, email, hire_date, salary, department_id, manager_id) 
VALUES ('John', 'Doe', 'j.doe@company.com', '2026-01-01', 50000.00, 1, 1);
ROLLBACK;

-- Q18: Show how to write a SAVEPOINT and rollback to it.
SAVEPOINT my_savepoint;
INSERT INTO departments (name, budget, location) VALUES ('QA', 120000.00, 'London');
ROLLBACK TO my_savepoint;
RELEASE my_savepoint;

-- Q19: Recursive CTE: Write a query to find the complete management hierarchy path (from Bob up to CEO Alice) showing their levels.
WITH RECURSIVE org_chart AS (
    SELECT id, first_name, last_name, manager_id, 1 AS level, CAST(first_name AS TEXT) AS path
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    SELECT e.id, e.first_name, e.last_name, e.manager_id, o.level + 1, o.path || ' -> ' || e.first_name
    FROM employees e
    INNER JOIN org_chart o ON e.manager_id = o.id
)
SELECT * FROM org_chart;

-- Q20: Recursive CTE: Generate a sequence of numbers from 1 to 10 using a recursive query.
WITH RECURSIVE seq(n) AS (
    SELECT 1
    UNION ALL
    SELECT n + 1 FROM seq WHERE n < 10
)
SELECT n FROM seq;

-- Q21: Recursive CTE: Generate a list of dates for the first 7 days of January 2026.
WITH RECURSIVE date_seq(d) AS (
    SELECT '2026-01-01'
    UNION ALL
    SELECT date(d, '+1 day') FROM date_seq WHERE d < '2026-01-07'
)
SELECT d FROM date_seq;

-- Q22: Recursive CTE: Find the path of organization departments (e.g. CEO -> Manager -> Staff) for employee David.
-- Note: Conceptual matching since departments table is flat.

-- Q23: Cohort Analysis: Find the signup cohort (Year-Month) for all customers, and count how many customers are in each cohort.
SELECT strftime('%Y-%m', signup_date) AS cohort_month, COUNT(*) AS new_customers
FROM customers
GROUP BY cohort_month;

-- Q24: Customer Retention: For each signup cohort, calculate how many customers placed at least one order in the same month they signed up.
SELECT strftime('%Y-%m', c.signup_date) AS cohort_month, COUNT(DISTINCT c.id) AS retained_customers
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id
WHERE strftime('%Y-%m', c.signup_date) = strftime('%Y-%m', o.order_date)
GROUP BY cohort_month;

-- Q25: Customer Churn: Identify customers who placed an order in the first half of 2025 but have placed 0 orders since July 2025.
SELECT DISTINCT customer_id 
FROM orders 
WHERE order_date BETWEEN '2025-01-01' AND '2025-06-30'
EXCEPT
SELECT DISTINCT customer_id 
FROM orders 
WHERE order_date >= '2025-07-01';

-- Q26: Month-over-Month Revenue Growth: Calculate total revenue by month and the percentage change compared to the previous month.
WITH MonthlyRevenue AS (
    SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS revenue
    FROM orders
    GROUP BY month
),
RevenueLag AS (
    SELECT month, revenue,
           LAG(revenue, 1) OVER (ORDER BY month ASC) AS prev_revenue
    FROM MonthlyRevenue
)
SELECT month, revenue, prev_revenue,
       CASE 
           WHEN prev_revenue IS NULL THEN NULL 
           ELSE ((revenue - prev_revenue) / prev_revenue) * 100.0 
       END AS growth_pct
FROM RevenueLag;

-- Q27: Year-over-Year (YoY) Revenue Growth: Calculate the revenue of each year and the growth rate compared to the previous year.
WITH YearlyRevenue AS (
    SELECT strftime('%Y', order_date) AS year, SUM(total_amount) AS revenue
    FROM orders
    GROUP BY year
)
SELECT year, revenue,
       LAG(revenue, 1) OVER (ORDER BY year ASC) AS prev_year_revenue,
       ((revenue - LAG(revenue, 1) OVER (ORDER BY year ASC)) / LAG(revenue, 1) OVER (ORDER BY year ASC)) * 100.0 AS yoy_growth
FROM YearlyRevenue;

-- Q28: Customer Lifetime Value (CLV): Calculate the total revenue generated by each customer divided by their tenure in months.
WITH CustomerTenure AS (
    SELECT id, first_name, last_name,
           MAX(1, (2026 - CAST(strftime('%Y', signup_date) AS INT)) * 12 + 1) AS tenure_months
    FROM customers
),
CustomerSpent AS (
    SELECT customer_id, SUM(total_amount) AS spent FROM orders GROUP BY customer_id
)
SELECT ct.first_name, ct.last_name, COALESCE(cs.spent, 0) AS total_spent, ct.tenure_months,
       (COALESCE(cs.spent, 0) * 1.0 / ct.tenure_months) AS clv_monthly_index
FROM CustomerTenure ct
LEFT JOIN CustomerSpent cs ON ct.id = cs.customer_id;

-- Q29: Rolling Average Revenue: Calculate the 3-month rolling average revenue for 2025.
WITH MonthlyRevenue AS (
    SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS revenue
    FROM orders
    GROUP BY month
)
SELECT month, revenue,
       AVG(revenue) OVER (ORDER BY month ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_avg_3m
FROM MonthlyRevenue;

-- Q30: Active Users (MAU): Find the number of unique customers who placed an order in each month (Monthly Active Users).
SELECT strftime('%Y-%m', order_date) AS month, COUNT(DISTINCT customer_id) AS mau
FROM orders
GROUP BY month;

-- Q31: EXPLAIN QUERY PLAN for a subquery in the WHERE clause compared to an equivalent INNER JOIN.
EXPLAIN QUERY PLAN SELECT * FROM employees WHERE department_id IN (SELECT id FROM departments WHERE name = 'Sales');

-- Q32: Create an index on order_date in the orders table to optimize date-range queries.
CREATE INDEX idx_orders_date ON orders(order_date);

-- Q33: Run EXPLAIN QUERY PLAN on selecting orders placed in 2025-08-01 using the index on order_date.
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE order_date = '2025-08-01';

-- Q34: Create a unique index on email in the employees table.
CREATE UNIQUE INDEX idx_employees_email_uniq ON employees(email);

-- Q35: View the list of all indexes in the database (use PRAGMA index_list('employees') in SQLite).
PRAGMA index_list('employees');

-- Q36: View the details of a specific index (use PRAGMA index_info('index_name') in SQLite).
PRAGMA index_info('idx_employees_email');

-- Q37: Drop the index on email in the employees table.
DROP INDEX idx_employees_email_uniq;

-- Q38: Create a composite index on customers for (country, signup_date).
CREATE INDEX idx_customers_composite ON customers(country, signup_date);

-- Q39: Run EXPLAIN QUERY PLAN for finding customers in USA who signed up after 2025-05-01.
EXPLAIN QUERY PLAN SELECT * FROM customers WHERE country = 'USA' AND signup_date > '2025-05-01';

-- Q40: Drop the composite index on customers.
DROP INDEX idx_customers_composite;

-- Q41: Explain Boyes-Codd Normal Form (BCNF) with a text comment.
-- BCNF (Boyce-Codd Normal Form) is a slightly stronger version of 3NF. 
-- A table is in BCNF if for every one of its non-trivial functional dependencies X -> Y, X is a superkey.

-- Q42: Write a query that simulates a self-join to find employees earning more than their department's manager.
SELECT e.first_name || ' ' || e.last_name AS employee_name, e.salary,
       m.first_name || ' ' || m.last_name AS manager_name, m.salary AS manager_salary
FROM employees e
INNER JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;

-- Q43: Write a query to find departments with a budget-to-salary ratio (budget / sum(salary)) of less than 3.0.
SELECT d.name, d.budget, SUM(e.salary) AS total_salary, (d.budget / SUM(e.salary)) AS ratio
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.id
HAVING ratio < 3.0;

-- Q44: Create a view called "employee_directory" containing employee full name, email, department name, and manager name.
CREATE VIEW employee_directory AS
SELECT e.first_name || ' ' || e.last_name AS full_name, e.email, d.name AS department_name,
       m.first_name || ' ' || m.last_name AS manager_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id
LEFT JOIN employees m ON e.manager_id = m.id;

-- Q45: Query the "employee_directory" view to find all employees in the Sales department.
SELECT * FROM employee_directory WHERE department_name = 'Sales';

-- Q46: Drop the view "employee_directory".
DROP VIEW employee_directory;

-- Q47: Create a view called "monthly_sales_summary" showing year, month, total sales, and count of orders.
CREATE VIEW monthly_sales_summary AS
SELECT strftime('%Y', order_date) AS sales_year,
       strftime('%m', order_date) AS sales_month,
       SUM(total_amount) AS total_sales,
       COUNT(*) AS order_count
FROM orders
GROUP BY sales_year, sales_month;

-- Q48: Query the "monthly_sales_summary" view for the month of August 2025.
SELECT * FROM monthly_sales_summary WHERE sales_month = '08';

-- Q49: Drop the view "monthly_sales_summary".
DROP VIEW monthly_sales_summary;

-- Q50: Write a transaction that inserts a new customer and a corresponding order in a single atomic block.
BEGIN TRANSACTION;
INSERT INTO customers (first_name, last_name, country, signup_date) VALUES ('Jane', 'Doe', 'USA', '2026-01-01');
INSERT INTO orders (customer_id, order_date, total_amount, status) VALUES (last_insert_rowid(), '2026-01-01', 0.00, 'Pending');
COMMIT;

-- Q51: Recursive CTE: Count the total number of employees in Bob Jones' direct and indirect reporting line.
WITH RECURSIVE reports AS (
    SELECT id FROM employees WHERE manager_id = (SELECT id FROM employees WHERE first_name = 'Bob' AND last_name = 'Jones')
    UNION ALL
    SELECT e.id FROM employees e INNER JOIN reports r ON e.manager_id = r.id
)
SELECT COUNT(*) FROM reports;

-- Q52: Recursive CTE: List all employees who report directly or indirectly to CEO Alice Smith.
WITH RECURSIVE reports AS (
    SELECT id, first_name, last_name FROM employees WHERE manager_id = (SELECT id FROM employees WHERE first_name = 'Alice' AND last_name = 'Smith')
    UNION ALL
    SELECT e.id, e.first_name, e.last_name FROM employees e INNER JOIN reports r ON e.manager_id = r.id
)
SELECT * FROM reports;

-- Q53: Recursive CTE: Generate a date series for every Sunday in the year 2026.
WITH RECURSIVE sundays(d) AS (
    SELECT '2026-01-04' -- First Sunday of 2026
    UNION ALL
    SELECT date(d, '+7 days') FROM sundays WHERE d < '2026-12-25'
)
SELECT d FROM sundays;

-- Q54: Cumulative running total of quantity sold by product category.
SELECT oi.id, p.category, oi.quantity,
       SUM(oi.quantity) OVER (PARTITION BY p.category ORDER BY oi.id ASC) AS category_running_qty
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id;

-- Q55: Calculate the average order value (AOV) for each country.
SELECT c.country, AVG(o.total_amount) AS aov
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.country;

-- Q56: Find the top 3 spending customers in each country using a window function.
WITH CustomerSpending AS (
    SELECT c.id, c.first_name, c.last_name, c.country, SUM(o.total_amount) AS spent,
           DENSE_RANK() OVER (PARTITION BY c.country ORDER BY SUM(o.total_amount) DESC) AS rank
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id
)
SELECT * FROM CustomerSpending WHERE rank <= 3;

-- Q57: Calculate the inventory turnover ratio (total quantity sold / remaining stock) for each product.
SELECT p.name, COALESCE(SUM(oi.quantity), 0) AS total_sold, p.stock,
       (COALESCE(SUM(oi.quantity), 0) * 1.0 / MAX(1, p.stock)) AS turnover_ratio
FROM products p
LEFT JOIN order_items oi ON p.id = oi.product_id
GROUP BY p.id;

-- Q58: Find products that represent the top 50% of total revenue generated (ABC analysis / Pareto Principle).
WITH ProductSales AS (
    SELECT product_id, SUM(quantity * unit_price) AS sales
    FROM order_items
    GROUP BY product_id
),
RunningSales AS (
    SELECT product_id, sales,
           SUM(sales) OVER (ORDER BY sales DESC) AS cumulative_sales,
           SUM(sales) OVER () AS total_sales
    FROM ProductSales
)
SELECT rs.*, p.name 
FROM RunningSales rs
INNER JOIN products p ON rs.product_id = p.id
WHERE (rs.cumulative_sales - rs.sales) < (rs.total_sales * 0.50);

-- Q59: Find the average days between orders for repeat customers (customers with > 1 order).
WITH OrderIntervals AS (
    SELECT customer_id, order_date,
           julianday(order_date) - julianday(LAG(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date ASC)) AS diff_days
    FROM orders
)
SELECT customer_id, AVG(diff_days) AS avg_days_between_orders
FROM OrderIntervals
WHERE diff_days IS NOT NULL
GROUP BY customer_id;

-- Q60: Calculate the percentage of orders that were cancelled, group by customer country.
SELECT c.country,
       SUM(CASE WHEN o.status = 'Cancelled' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS cancellation_rate
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
GROUP BY c.country;

-- Q61: EXPLAIN QUERY PLAN for a correlated subquery vs an uncorrelated subquery.
EXPLAIN QUERY PLAN SELECT * FROM products p WHERE price > (SELECT AVG(price) FROM products WHERE category = p.category);

-- Q62: Create an index on department_id in the employees table.
CREATE INDEX idx_employees_dept ON employees(department_id);

-- Q63: EXPLAIN QUERY PLAN for joining employees and departments after indexing department_id.
EXPLAIN QUERY PLAN 
SELECT * FROM employees e INNER JOIN departments d ON e.department_id = d.id;

-- Q64: Drop the index on department_id.
DROP INDEX idx_employees_dept;

-- Q65: View the schema table details using SQLite system table `sqlite_master`.
SELECT * FROM sqlite_master WHERE type = 'table';

-- Q66: Select all index names from the `sqlite_master` table.
SELECT name FROM sqlite_master WHERE type = 'index';

-- Q67: Select all table names from the `sqlite_master` table.
SELECT name FROM sqlite_master WHERE type = 'table';

-- Q68: Create a index on (status, total_amount) in the orders table.
CREATE INDEX idx_orders_status_amount ON orders(status, total_amount);

-- Q69: EXPLAIN QUERY PLAN for selecting pending orders with amount > 500 using the index.
EXPLAIN QUERY PLAN SELECT * FROM orders WHERE status = 'Pending' AND total_amount > 500;

-- Q70: Drop the index on (status, total_amount).
DROP INDEX idx_orders_status_amount;

-- Q71: Write a transaction that deletes an order and all its corresponding order items atomically.
BEGIN TRANSACTION;
DELETE FROM order_items WHERE order_id = 7;
DELETE FROM orders WHERE id = 7;
COMMIT;

-- Q72: Simulate a nested transaction savepoint structure in SQLite.
SAVEPOINT outer_sp;
SAVEPOINT inner_sp;
RELEASE inner_sp;
RELEASE outer_sp;

-- Q73: Recursive CTE: Find the max depth of the employee hierarchy (company hierarchy depth).
WITH RECURSIVE org_depth AS (
    SELECT id, manager_id, 1 AS depth FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.manager_id, od.depth + 1 FROM employees e INNER JOIN org_depth od ON e.manager_id = od.id
)
SELECT MAX(depth) AS max_depth FROM org_depth;

-- Q74: Recursive CTE: Concatenate the names of the entire management path for employee Eva Davis.
WITH RECURSIVE org_path AS (
    SELECT id, manager_id, CAST(first_name || ' ' || last_name AS TEXT) AS path 
    FROM employees 
    WHERE first_name = 'Eva' AND last_name = 'Davis'
    
    UNION ALL
    
    SELECT e.id, e.manager_id, op.path || ' -> ' || e.first_name || ' ' || e.last_name
    FROM employees e
    INNER JOIN org_path op ON op.manager_id = e.id
)
SELECT path FROM org_path WHERE manager_id IS NULL;

-- Q75: Cohort Analysis: Group customers by signup month, and show the percentage of customers who placed an order in month 1, month 2, etc.
-- Conceptual outline

-- Q76: Find the month-over-month growth in Monthly Active Users (MAU).
WITH MonthlyUsers AS (
    SELECT strftime('%Y-%m', order_date) AS month, COUNT(DISTINCT customer_id) AS active_users
    FROM orders
    GROUP BY month
)
SELECT month, active_users,
       LAG(active_users, 1) OVER (ORDER BY month ASC) AS prev_users,
       (active_users - LAG(active_users, 1) OVER (ORDER BY month ASC)) * 100.0 / LAG(active_users, 1) OVER (ORDER BY month ASC) AS growth_rate
FROM MonthlyUsers;

-- Q77: Find the weekly revenue generated throughout 2025.
SELECT strftime('%W', order_date) AS week, SUM(total_amount) AS revenue
FROM orders
WHERE order_date LIKE '2025%'
GROUP BY week;

-- Q78: Find the daily rolling 3-day total sales revenue.
SELECT order_date, SUM(total_amount) AS daily_sales,
       SUM(SUM(total_amount)) OVER (ORDER BY order_date ASC ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rolling_3d_sales
FROM orders
GROUP BY order_date;

-- Q79: Find the product category that has the highest average days in stock (assuming daily sales rate).
-- Conceptual proxy

-- Q80: Find the customer country that has the highest user retention rate (orders placed in 2 different quarters).
-- Conceptual proxy

-- Q81: EXPLAIN QUERY PLAN on ordering by a non-indexed column vs an indexed column.
EXPLAIN QUERY PLAN SELECT * FROM employees ORDER BY salary DESC;

-- Q82: Create an index on salary in the employees table.
CREATE INDEX idx_employees_salary ON employees(salary);

-- Q83: EXPLAIN QUERY PLAN for selecting the top 3 highest paid employees using the index on salary.
EXPLAIN QUERY PLAN SELECT * FROM employees ORDER BY salary DESC LIMIT 3;

-- Q84: Drop the index on salary.
DROP INDEX idx_employees_salary;

-- Q85: Write a command to rename the tables if needed (use ALTER TABLE ... RENAME TO).
-- ALTER TABLE departments RENAME TO company_departments;

-- Q86: Write a command to add a new column "notes" to the departments table.
ALTER TABLE departments ADD COLUMN notes TEXT;

-- Q87: Write a command to drop the "notes" column from the departments table.
-- Note: SQLite versions before 3.35.0 do not support DROP COLUMN. We can conceptualize it:
-- ALTER TABLE departments DROP COLUMN notes;

-- Q88: Create a composite index on order_items (product_id, quantity).
CREATE INDEX idx_order_items_prod_qty ON order_items(product_id, quantity);

-- Q89: EXPLAIN QUERY PLAN for finding the total quantity sold of product 1.
EXPLAIN QUERY PLAN SELECT SUM(quantity) FROM order_items WHERE product_id = 1;

-- Q90: Drop the index on order_items (product_id, quantity).
DROP INDEX idx_order_items_prod_qty;

-- Q91: Write a query to find the department with the highest ratio of managers to staff.
-- Conceptual matching

-- Q92: Find employees who earn more than the average salary of the location they work in.
WITH LocationAvg AS (
    SELECT d.location, AVG(e.salary) AS avg_sal
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id
    GROUP BY d.location
)
SELECT e.*, d.location
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
INNER JOIN LocationAvg la ON d.location = la.location
WHERE e.salary > la.avg_sal;

-- Q93: Create a view showing the current stock status, unit price, and total stock value of all products.
CREATE VIEW stock_status AS
SELECT name, price, stock, (price * stock) AS stock_value FROM products;

-- Q94: Find customers who bought the most expensive product but never bought the cheapest product.
SELECT DISTINCT customer_id FROM orders o INNER JOIN order_items oi ON o.id = oi.order_id
WHERE oi.product_id = (SELECT id FROM products ORDER BY price DESC LIMIT 1)
EXCEPT
SELECT DISTINCT customer_id FROM orders o INNER JOIN order_items oi ON o.id = oi.order_id
WHERE oi.product_id = (SELECT id FROM products ORDER BY price ASC LIMIT 1);

-- Q95: Find products that have been bought by all customers in the USA.
-- Count of customers in USA
WITH USACustomersCount AS (
    SELECT COUNT(*) AS total FROM customers WHERE country = 'USA'
)
SELECT product_id 
FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.id
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'USA'
GROUP BY product_id
HAVING COUNT(DISTINCT c.id) = (SELECT total FROM USACustomersCount);

-- Q96: Calculate the churn rate of customers per month in 2025.
-- Conceptual cohort math

-- Q97: Find the department where the salary distribution has the highest standard deviation (or variance).
-- SQLite does not have STDEV. We can use variance formula: (SUM(x^2) - SUM(x)^2/N)/N
SELECT department_id, 
       (SUM(salary * salary) - (SUM(salary) * SUM(salary) / COUNT(*))) / COUNT(*) AS variance
FROM employees
GROUP BY department_id
ORDER BY variance DESC
LIMIT 1;

-- Q98: Find the correlation between product price and total quantity sold (simulate correlation calculation in SQLite).
-- Conceptual proxy

-- Q99: Find the date of the week with the highest average order value.
SELECT strftime('%w', order_date) AS day_of_week, AVG(total_amount) AS avg_value
FROM orders
GROUP BY day_of_week
ORDER BY avg_value DESC
LIMIT 1;

-- Q100: Find the customer who has the highest lifetime order count, and show their rank.
WITH CustomerOrderCounts AS (
    SELECT customer_id, COUNT(*) AS order_count,
           RANK() OVER (ORDER BY COUNT(*) DESC) AS rank
    FROM orders
    GROUP BY customer_id
)
SELECT coc.*, c.first_name, c.last_name 
FROM CustomerOrderCounts coc
INNER JOIN customers c ON coc.customer_id = c.id
WHERE coc.rank = 1;
