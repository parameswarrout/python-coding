-- ============================================================
-- SQL PRACTICE - 01_BASIC_SELECT_FILTERING (SOLUTIONS)
-- ============================================================
-- database: practice.db (SQLite)
-- ============================================================

-- Q1: Select all columns and all rows from the departments table.
SELECT * FROM departments;

-- Q2: Select only the name and budget columns from the departments table.
SELECT name, budget FROM departments;

-- Q3: Select all employees' first name, last name, and salary.
SELECT first_name, last_name, salary FROM employees;

-- Q4: Select all unique locations where departments are located.
SELECT DISTINCT location FROM departments;

-- Q5: Select all products and alias the name column as "Product Name".
SELECT name AS "Product Name", category, price, stock FROM products;

-- Q6: Select first name and last name of all employees, combining them as "Full Name" (use || operator).
SELECT first_name || ' ' || last_name AS "Full Name" FROM employees;

-- Q7: Select name and price of all products, displaying price with a 10% tax added (alias as "Price with Tax").
SELECT name, price * 1.10 AS "Price with Tax" FROM products;

-- Q8: Select all customers' first name, last name, and country.
SELECT first_name, last_name, country FROM customers;

-- Q9: Select all unique countries from the customers table.
SELECT DISTINCT country FROM customers;

-- Q10: Select all columns from the products table where the price is greater than 100.
SELECT * FROM products WHERE price > 100;

-- Q11: Select all employees who earn a salary of exactly 90000.
SELECT * FROM employees WHERE salary = 90000;

-- Q12: Select all departments located in "New York".
SELECT * FROM departments WHERE location = 'New York';

-- Q13: Select all orders with a total amount less than or equal to 300.
SELECT * FROM orders WHERE total_amount <= 300;

-- Q14: Select all completed orders from the orders table.
SELECT * FROM orders WHERE status = 'Completed';

-- Q15: Select all products that belong to the "Electronics" category.
SELECT * FROM products WHERE category = 'Electronics';

-- Q16: Select all employees hired before January 1, 2022.
SELECT * FROM employees WHERE hire_date < '2022-01-01';

-- Q17: Select all customers who signed up in the year 2025.
SELECT * FROM customers WHERE signup_date BETWEEN '2025-01-01' AND '2025-12-31';

-- Q18: Select all products with stock levels greater than 50.
SELECT * FROM products WHERE stock > 50;

-- Q19: Select all orders that are currently "Pending".
SELECT * FROM orders WHERE status = 'Pending';

-- Q20: Select all employees who do not report to a manager (manager_id is NULL).
SELECT * FROM employees WHERE manager_id IS NULL;

-- Q21: Select all employees who do report to a manager (manager_id is NOT NULL).
SELECT * FROM employees WHERE manager_id IS NOT NULL;

-- Q22: Select all products with a price between 100 and 500.
SELECT * FROM products WHERE price BETWEEN 100 AND 500;

-- Q23: Select all orders with a total amount between 500 and 1500.
SELECT * FROM orders WHERE total_amount BETWEEN 500 AND 1500;

-- Q24: Select all employees hired between 2021-01-01 and 2023-01-01.
SELECT * FROM employees WHERE hire_date BETWEEN '2021-01-01' AND '2023-01-01';

-- Q25: Select all products in stock levels between 10 and 50.
SELECT * FROM products WHERE stock BETWEEN 10 AND 50;

-- Q26: Select all employees working in department 1 or department 2.
SELECT * FROM employees WHERE department_id IN (1, 2);

-- Q27: Select all products that belong to either "Furniture", "Appliances", or "Apparel".
SELECT * FROM products WHERE category IN ('Furniture', 'Appliances', 'Apparel');

-- Q28: Select all customers who reside in either "USA", "Canada", or "UK".
SELECT * FROM customers WHERE country IN ('USA', 'Canada', 'UK');

-- Q29: Select all orders with status "Completed" or "Shipped".
SELECT * FROM orders WHERE status IN ('Completed', 'Shipped');

-- Q30: Select all employees whose first name starts with the letter 'J'.
SELECT * FROM employees WHERE first_name LIKE 'J%';

-- Q31: Select all employees whose last name ends with 'son'.
SELECT * FROM employees WHERE last_name LIKE '%son';

-- Q32: Select all products containing the word "Desk" in their name.
SELECT * FROM products WHERE name LIKE '%Desk%';

-- Q33: Select all customers whose email contains "company" (search employees table instead).
SELECT * FROM employees WHERE email LIKE '%company%';

-- Q34: Select all employees whose email contains "jones".
SELECT * FROM employees WHERE email LIKE '%jones%';

-- Q35: Select all products whose category does not start with 'E'.
SELECT * FROM products WHERE category NOT LIKE 'E%';

-- Q36: Select all customers whose first name is exactly 4 characters long (use LIKE with underscores).
SELECT * FROM customers WHERE first_name LIKE '____';

-- Q37: Select all employees whose first name has 'a' as the second character.
SELECT * FROM employees WHERE first_name LIKE '_a%';

-- Q38: Select all products where category is 'Electronics' and price is less than 500.
SELECT * FROM products WHERE category = 'Electronics' AND price < 500;

-- Q39: Select all employees who earn more than 80000 and were hired after 2022-01-01.
SELECT * FROM employees WHERE salary > 80000 AND hire_date > '2022-01-01';

-- Q40: Select all completed orders with a total amount greater than 1000.
SELECT * FROM orders WHERE status = 'Completed' AND total_amount > 1000;

-- Q41: Select all products with category 'Apparel' and price between 20 and 100.
SELECT * FROM products WHERE category = 'Apparel' AND price BETWEEN 20 AND 100;

-- Q42: Select all customers from "Canada" who signed up after 2025-06-01.
SELECT * FROM customers WHERE country = 'Canada' AND signup_date > '2025-06-01';

-- Q43: Select all employees who work in department 1 and have a manager_id of 2.
SELECT * FROM employees WHERE department_id = 1 AND manager_id = 2;

-- Q44: Select all products that are either in the category "Appliances" or have a price less than 50.
SELECT * FROM products WHERE category = 'Appliances' OR price < 50;

-- Q45: Select all employees who earn less than 70000 or were hired before 2021-01-01.
SELECT * FROM employees WHERE salary < 70000 OR hire_date < '2021-01-01';

-- Q46: Select all orders that are either "Cancelled" or have a total amount greater than 2000.
SELECT * FROM orders WHERE status = 'Cancelled' OR total_amount > 2000;

-- Q47: Select all customers who live in "UK" or "Germany" and signed up before 2025-07-01.
SELECT * FROM customers WHERE country IN ('UK', 'Germany') AND signup_date < '2025-07-01';

-- Q48: Select all employees whose salary is not between 70000 and 100000.
SELECT * FROM employees WHERE salary NOT BETWEEN 70000 AND 100000;

-- Q49: Select all products that do not belong to the "Electronics" or "Appliances" categories.
SELECT * FROM products WHERE category NOT IN ('Electronics', 'Appliances');

-- Q50: Select all orders that do not have a status of "Cancelled" or "Pending".
SELECT * FROM orders WHERE status NOT IN ('Cancelled', 'Pending');

-- Q51: Select all customers who do not live in "USA" or "Canada".
SELECT * FROM customers WHERE country NOT IN ('USA', 'Canada');

-- Q52: Select all employees sorted by salary in ascending order.
SELECT * FROM employees ORDER BY salary ASC;

-- Q53: Select all employees sorted by salary in descending order.
SELECT * FROM employees ORDER BY salary DESC;

-- Q54: Select all products sorted by name alphabetically.
SELECT * FROM products ORDER BY name ASC;

-- Q55: Select all products sorted by price from highest to lowest.
SELECT * FROM products ORDER BY price DESC;

-- Q56: Select all orders sorted by order_date in descending order, then by total_amount in ascending order.
SELECT * FROM orders ORDER BY order_date DESC, total_amount ASC;

-- Q57: Select all employees sorted by department_id in ascending order, then by salary in descending order.
SELECT * FROM employees ORDER BY department_id ASC, salary DESC;

-- Q58: Select the top 5 highest paid employees.
SELECT * FROM employees ORDER BY salary DESC LIMIT 5;

-- Q59: Select the 3 cheapest products.
SELECT * FROM products ORDER BY price ASC LIMIT 3;

-- Q60: Select the 5 most recent orders.
SELECT * FROM orders ORDER BY order_date DESC LIMIT 5;

-- Q61: Select the 5 oldest employees based on hire date.
SELECT * FROM employees ORDER BY hire_date ASC LIMIT 5;

-- Q62: Select the 5 highest paid employees, skipping the top 2 (use OFFSET).
SELECT * FROM employees ORDER BY salary DESC LIMIT 5 OFFSET 2;

-- Q63: Select products sorted by price descending, displaying the 4th to 6th most expensive products.
SELECT * FROM products ORDER BY price DESC LIMIT 3 OFFSET 3;

-- Q64: Select all employees and display their salary formatted with a '$' symbol.
SELECT first_name, last_name, '$' || CAST(salary AS TEXT) AS "Formatted Salary" FROM employees;

-- Q65: Select product name and price, rounding the price to the nearest integer.
SELECT name, ROUND(price) AS rounded_price FROM products;

-- Q66: Select employee first name and last name, converting them to upper case.
SELECT UPPER(first_name) AS first_name, UPPER(last_name) AS last_name FROM employees;

-- Q67: Select customer first name and last name, converting them to lower case.
SELECT LOWER(first_name) AS first_name, LOWER(last_name) AS last_name FROM customers;

-- Q68: Select all products and show the length of their names.
SELECT name, LENGTH(name) AS name_length FROM products;

-- Q69: Select order_id, order_date, and order_date formatted as 'DD/MM/YYYY' (use strftime or substr in SQLite).
-- Note: SQLite does not support standard DATE_FORMAT. We can use strftime('%d/%m/%Y', order_date)
SELECT id, order_date, strftime('%d/%m/%Y', order_date) AS formatted_date FROM orders;

-- Q70: Select all orders and display status, replacing "Cancelled" with "Void" (use CASE statement).
SELECT id, customer_id, order_date, total_amount, 
       CASE status 
           WHEN 'Cancelled' THEN 'Void' 
           ELSE status 
       END AS modified_status 
FROM orders;

-- Q71: Select all products and classify them as "Expensive" (price > 500) or "Affordable" (price <= 500).
SELECT name, price, 
       CASE 
           WHEN price > 500 THEN 'Expensive' 
           ELSE 'Affordable' 
       END AS class 
FROM products;

-- Q72: Select all employees and classify their salary into "High" (> 100000), "Medium" (70000-100000), or "Low" (< 70000).
SELECT first_name, last_name, salary,
       CASE 
           WHEN salary > 100000 THEN 'High'
           WHEN salary BETWEEN 70000 AND 100000 THEN 'Medium'
           ELSE 'Low'
       END AS salary_tier
FROM employees;

-- Q73: Select all customers and display their country, mapping "USA" to "United States" and "UK" to "United Kingdom" (use CASE).
SELECT first_name, last_name, country,
       CASE country
           WHEN 'USA' THEN 'United States'
           WHEN 'UK' THEN 'United Kingdom'
           ELSE country
       END AS full_country_name
FROM customers;

-- Q74: Select employees and return first_name, manager_id, but replace NULL manager_id with 0 (use COALESCE).
SELECT first_name, COALESCE(manager_id, 0) AS manager_id FROM employees;

-- Q75: Select all products, return name, category, stock, but replace stock with 'Out of Stock' if stock is 0 (use CASE/COALESCE).
SELECT name, category, 
       CASE 
           WHEN stock = 0 THEN 'Out of Stock'
           ELSE CAST(stock AS TEXT)
       END AS stock_status
FROM products;

-- Q76: Select all employees whose first name contains exactly one 'l' character.
-- Note: Check length of name minus length after replacing 'l' is 1
SELECT * FROM employees WHERE LENGTH(first_name) - LENGTH(REPLACE(LOWER(first_name), 'l', '')) = 1;

-- Q77: Select all products whose price ends in '.00'.
SELECT * FROM products WHERE CAST(price AS TEXT) LIKE '%.00' OR price = CAST(price AS INT);

-- Q78: Select all employees who earn more than their department's budget / 10 (hardcode department 4 budget as 300000).
SELECT * FROM employees WHERE salary > 300000 / 10;

-- Q79: Select all orders placed on a weekend (assuming SQLite date strings, use strftime('%w', order_date) in (0, 6)).
SELECT * FROM orders WHERE strftime('%w', order_date) IN ('0', '6');

-- Q80: Select all orders placed in the first half of the year 2025 (Jan 1 to Jun 30).
SELECT * FROM orders WHERE order_date BETWEEN '2025-01-01' AND '2025-06-30';

-- Q81: Select all employees hired in the month of August of any year.
SELECT * FROM employees WHERE strftime('%m', hire_date) = '08';

-- Q82: Select all customers who signed up in the first 10 days of any month.
SELECT * FROM customers WHERE strftime('%d', signup_date) BETWEEN '01' AND '10';

-- Q83: Select all products whose category starts with 'A' or 'F' and price is greater than 50.
SELECT * FROM products WHERE (category LIKE 'A%' OR category LIKE 'F%') AND price > 50;

-- Q84: Select all employees who are not engineers (department_id != 1) and earn more than 80000.
SELECT * FROM employees WHERE department_id != 1 AND salary > 80000;

-- Q85: Select all orders with status 'Completed' where the total_amount is not equal to 800.
SELECT * FROM orders WHERE status = 'Completed' AND total_amount <> 800;

-- Q86: Select all customers where the length of their last name is greater than 6 characters.
SELECT * FROM customers WHERE LENGTH(last_name) > 6;

-- Q87: Select all employees whose email contains their first name in lower case.
SELECT * FROM employees WHERE email LIKE '%' || LOWER(first_name) || '%';

-- Q88: Select all products whose stock is less than 20 or price is greater than 1000.
SELECT * FROM products WHERE stock < 20 OR price > 1000;

-- Q89: Select all employees whose hire_date is in the year 2023.
SELECT * FROM employees WHERE hire_date LIKE '2023%';

-- Q90: Select all orders where total_amount is greater than 500, sorted by total_amount descending, limited to 5.
SELECT * FROM orders WHERE total_amount > 500 ORDER BY total_amount DESC LIMIT 5;

-- Q91: Select all products where category is 'Apparel', sorted by price descending.
SELECT * FROM products WHERE category = 'Apparel' ORDER BY price DESC;

-- Q92: Select all customers who live in European countries ('Germany', 'France', 'UK', 'Spain').
SELECT * FROM customers WHERE country IN ('Germany', 'France', 'UK', 'Spain');

-- Q93: Select all employees who earn a salary between 60000 and 90000, sorted by salary ascending.
SELECT * FROM employees WHERE salary BETWEEN 60000 AND 90000 ORDER BY salary ASC;

-- Q94: Select all orders with status 'Completed' or 'Shipped' placed after 2025-06-01.
SELECT * FROM orders WHERE status IN ('Completed', 'Shipped') AND order_date > '2025-06-01';

-- Q95: Select all products where category is 'Furniture' and stock is greater than 10, sorted by stock descending.
SELECT * FROM products WHERE category = 'Furniture' AND stock > 10 ORDER BY stock DESC;

-- Q96: Select all employees hired after 2022-01-01 who are not managed by manager_id 1 (bob).
SELECT * FROM employees WHERE hire_date > '2022-01-01' AND (manager_id != 1 OR manager_id IS NULL);

-- Q97: Select all orders where status is 'Cancelled' or 'Pending', sorted by order_date ascending.
SELECT * FROM orders WHERE status IN ('Cancelled', 'Pending') ORDER BY order_date ASC;

-- Q98: Select all customers whose first name contains 'a' and last name contains 'o'.
SELECT * FROM customers WHERE first_name LIKE '%a%' AND last_name LIKE '%o%';

-- Q99: Select all products whose price is not an integer (i.e. has cents / decimal part, use price != CAST(price AS INT)).
SELECT * FROM products WHERE price != CAST(price AS INT);

-- Q100: Select all employees whose first name and last name have the same length.
SELECT * FROM employees WHERE LENGTH(first_name) = LENGTH(last_name);
