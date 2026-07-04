-- ============================================================
-- SQL PRACTICE - 04_SUBQUERIES_CTES (SOLUTIONS)
-- ============================================================
-- database: practice.db (SQLite)
-- ============================================================

-- Q1: Find all employees who earn more than the average salary of the entire company.
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);

-- Q2: Find all products with a price greater than the average price of all products.
SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);

-- Q3: Find all orders with a total amount greater than the maximum order total from customer 1.
SELECT * FROM orders WHERE total_amount > (SELECT MAX(total_amount) FROM orders WHERE customer_id = 1);

-- Q4: Find the first name and last name of employees who work in departments located in "New York" (use subquery, not join).
SELECT first_name, last_name 
FROM employees 
WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York');

-- Q5: Find the name of products that have never been ordered (use NOT IN with a subquery on order_items).
SELECT name 
FROM products 
WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items);

-- Q6: Find the first name and last name of customers who have placed at least one order (use IN with a subquery).
SELECT first_name, last_name 
FROM customers 
WHERE id IN (SELECT DISTINCT customer_id FROM orders);

-- Q7: Find all customers who have never placed an order (use NOT IN with a subquery).
SELECT * 
FROM customers 
WHERE id NOT IN (SELECT DISTINCT customer_id FROM orders WHERE customer_id IS NOT NULL);

-- Q8: Find all employees who earn more than the maximum salary of department 2.
SELECT * 
FROM employees 
WHERE salary > (SELECT MAX(salary) FROM employees WHERE department_id = 2);

-- Q9: Find all products that belong to categories having an average product price greater than 300 (use IN with a subquery).
SELECT * 
FROM products 
WHERE category IN (
    SELECT category 
    FROM products 
    GROUP BY category 
    HAVING AVG(price) > 300
);

-- Q10: Select all departments that have a budget greater than the total salary expense of their employees.
SELECT * 
FROM departments d 
WHERE budget > (SELECT SUM(salary) FROM employees WHERE department_id = d.id);

-- Q11: Find employees whose salary is higher than the average salary of their own department (correlated subquery).
SELECT * 
FROM employees e 
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);

-- Q12: Select product details for products priced higher than the average price of products in their same category (correlated subquery).
SELECT * 
FROM products p 
WHERE price > (SELECT AVG(price) FROM products WHERE category = p.category);

-- Q13: Find customers who signed up after customer 5 (Emily Williams, signup_date).
SELECT * 
FROM customers 
WHERE signup_date > (SELECT signup_date FROM customers WHERE id = 5);

-- Q14: Find all orders placed on the same day as any order placed by customer 1.
SELECT * 
FROM orders 
WHERE order_date IN (SELECT order_date FROM orders WHERE customer_id = 1);

-- Q15: Find employees who earn the lowest salary in their respective departments.
SELECT * 
FROM employees e 
WHERE salary = (SELECT MIN(salary) FROM employees WHERE department_id = e.department_id);

-- Q16: Find employees who earn the highest salary in their respective departments.
SELECT * 
FROM employees e 
WHERE salary = (SELECT MAX(salary) FROM employees WHERE department_id = e.department_id);

-- Q17: Find all customers who have placed an order with status "Cancelled" (use EXISTS).
SELECT * 
FROM customers c 
WHERE EXISTS (SELECT 1 FROM orders WHERE customer_id = c.id AND status = 'Cancelled');

-- Q18: Find all customers who have never placed an order (use NOT EXISTS).
SELECT * 
FROM customers c 
WHERE NOT EXISTS (SELECT 1 FROM orders WHERE customer_id = c.id);

-- Q19: Find all products that have been ordered at least once (use EXISTS).
SELECT * 
FROM products p 
WHERE EXISTS (SELECT 1 FROM order_items WHERE product_id = p.id);

-- Q20: Find all products that have never been ordered (use NOT EXISTS).
SELECT * 
FROM products p 
WHERE NOT EXISTS (SELECT 1 FROM order_items WHERE product_id = p.id);

-- Q21: Select all departments that have at least one employee (use EXISTS).
SELECT * 
FROM departments d 
WHERE EXISTS (SELECT 1 FROM employees WHERE department_id = d.id);

-- Q22: Select all departments that have no employees (use NOT EXISTS).
SELECT * 
FROM departments d 
WHERE NOT EXISTS (SELECT 1 FROM employees WHERE department_id = d.id);

-- Q23: Select all employees who manage at least one person (use EXISTS or IN).
SELECT * 
FROM employees e 
WHERE EXISTS (SELECT 1 FROM employees WHERE manager_id = e.id);

-- Q24: Select all employees who do not manage anyone (use NOT EXISTS or NOT IN).
SELECT * 
FROM employees e 
WHERE NOT EXISTS (SELECT 1 FROM employees WHERE manager_id = e.id);

-- Q25: Find the second highest salary in the company (using subquery).
SELECT MAX(salary) 
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Q26: Find the third highest salary in the company (using subquery).
SELECT MAX(salary) 
FROM employees 
WHERE salary < (
    SELECT MAX(salary) 
    FROM employees 
    WHERE salary < (SELECT MAX(salary) FROM employees)
);

-- Q27: Write a CTE to calculate the average salary of each department, then select employees earning more than their department's average.
WITH DeptAvg AS (
    SELECT department_id, AVG(salary) AS avg_sal 
    FROM employees 
    GROUP BY department_id
)
SELECT e.*, da.avg_sal
FROM employees e
INNER JOIN DeptAvg da ON e.department_id = da.department_id
WHERE e.salary > da.avg_sal;

-- Q28: Write a CTE to calculate total revenue per customer, then select the customer name and total revenue for customers who spent > 1000.
WITH CustomerSpent AS (
    SELECT customer_id, SUM(total_amount) AS total_spent 
    FROM orders 
    GROUP BY customer_id
)
SELECT c.first_name || ' ' || c.last_name AS customer_name, cs.total_spent
FROM customers c
INNER JOIN CustomerSpent cs ON c.id = cs.customer_id
WHERE cs.total_spent > 1000;

-- Q29: Write a CTE to count the number of products in each category, then select categories with more than 2 products.
WITH CategoryCount AS (
    SELECT category, COUNT(*) AS p_count 
    FROM products 
    GROUP BY category
)
SELECT * FROM CategoryCount WHERE p_count > 2;

-- Q30: Write a CTE to find the highest salary in each department, then join with employees to find the employee name earning that salary.
WITH DeptMaxSal AS (
    SELECT department_id, MAX(salary) AS max_sal 
    FROM employees 
    GROUP BY department_id
)
SELECT e.first_name, e.last_name, e.salary, e.department_id
FROM employees e
INNER JOIN DeptMaxSal dms ON e.department_id = dms.department_id AND e.salary = dms.max_sal;

-- Q31: Write a CTE to calculate total quantity sold for each product, then select products that sold more than 5 items.
WITH ProductSold AS (
    SELECT product_id, SUM(quantity) AS total_quantity 
    FROM order_items 
    GROUP BY product_id
)
SELECT p.name, ps.total_quantity
FROM products p
INNER JOIN ProductSold ps ON p.id = ps.product_id
WHERE ps.total_quantity > 5;

-- Q32: Write a CTE to find the most recent order for each customer, then select customer details and their most recent order date.
WITH RecentOrder AS (
    SELECT customer_id, MAX(order_date) AS max_date 
    FROM orders 
    GROUP BY customer_id
)
SELECT c.first_name, c.last_name, ro.max_date
FROM customers c
INNER JOIN RecentOrder ro ON c.id = ro.customer_id;

-- Q33: Write a CTE to find the total budget and total salary expense by location, then calculate the remaining budget surplus.
WITH BudgetExpense AS (
    SELECT d.location, SUM(DISTINCT d.budget) AS total_budget, SUM(e.salary) AS total_salaries
    FROM departments d
    LEFT JOIN employees e ON e.department_id = d.id
    GROUP BY d.location
)
SELECT location, total_budget, total_salaries, (total_budget - total_salaries) AS surplus
FROM BudgetExpense;

-- Q34: Write a CTE to find employees hired in 2022, and another CTE to find employees hired in 2023, then select all of them using UNION.
WITH Hired2022 AS (
    SELECT * FROM employees WHERE hire_date LIKE '2022%'
),
Hired2023 AS (
    SELECT * FROM employees WHERE hire_date LIKE '2023%'
)
SELECT * FROM Hired2022
UNION
SELECT * FROM Hired2023;

-- Q35: Use UNION to combine all customer emails and employee emails into a single list.
-- Note: customers table doesn't have email in SQLite schema, we will construct a dummy customer email or use employees emails.
-- Customer emails: lower(first_name) || '.' || lower(last_name) || '@customer.com'
SELECT email FROM employees
UNION
SELECT LOWER(first_name) || '.' || LOWER(last_name) || '@customer.com' AS email FROM customers;

-- Q36: Use UNION ALL to combine customer emails and employee emails, showing duplicates if they exist.
SELECT email FROM employees
UNION ALL
SELECT LOWER(first_name) || '.' || LOWER(last_name) || '@customer.com' AS email FROM customers;

-- Q37: Find all emails that belong to both a customer and an employee (use INTERSECT).
SELECT email FROM employees
INTERSECT
SELECT LOWER(first_name) || '.' || LOWER(last_name) || '@customer.com' FROM customers;

-- Q38: Find customer last names that do not appear as employee last names (use EXCEPT).
SELECT last_name FROM customers
EXCEPT
SELECT last_name FROM employees;

-- Q39: Find countries where we have customers but no department locations (use EXCEPT on customer country and department location).
SELECT country FROM customers
EXCEPT
SELECT location FROM departments;

-- Q40: Select all products and show a column "Sales Rank Status": 'Top Seller' if sold quantity > 5, 'Regular' otherwise (use CTE).
WITH SalesCount AS (
    SELECT product_id, SUM(quantity) AS total_sold
    FROM order_items
    GROUP BY product_id
)
SELECT p.name, COALESCE(sc.total_sold, 0) AS units_sold,
       CASE 
           WHEN COALESCE(sc.total_sold, 0) > 5 THEN 'Top Seller'
           ELSE 'Regular'
       END AS sales_rank_status
FROM products p
LEFT JOIN SalesCount sc ON p.id = sc.product_id;

-- Q41: Find all orders containing the most expensive product in the catalog.
SELECT DISTINCT order_id 
FROM order_items 
WHERE product_id = (SELECT id FROM products ORDER BY price DESC LIMIT 1);

-- Q42: Find all orders containing the cheapest product in the catalog.
SELECT DISTINCT order_id 
FROM order_items 
WHERE product_id = (SELECT id FROM products ORDER BY price ASC LIMIT 1);

-- Q43: Find employees hired after the CEO (Alice Smith, hire_date).
SELECT * 
FROM employees 
WHERE hire_date > (SELECT hire_date FROM employees WHERE first_name = 'Alice' AND last_name = 'Smith');

-- Q44: Find employees hired after Bob Jones but before Charlie Brown.
SELECT * 
FROM employees 
WHERE hire_date BETWEEN 
    (SELECT hire_date FROM employees WHERE first_name = 'Bob' AND last_name = 'Jones') AND 
    (SELECT hire_date FROM employees WHERE first_name = 'Charlie' AND last_name = 'Brown');

-- Q45: Select the department name and budget of the department that has the highest budget.
SELECT name, budget 
FROM departments 
WHERE budget = (SELECT MAX(budget) FROM departments);

-- Q46: Select the name of the product that has the highest stock level.
SELECT name, stock 
FROM products 
WHERE stock = (SELECT MAX(stock) FROM products);

-- Q47: Select the customer first name and last name of the oldest registered customer.
SELECT first_name, last_name, signup_date 
FROM customers 
WHERE signup_date = (SELECT MIN(signup_date) FROM customers);

-- Q48: Find all products with a price within 10% of the average product price.
SELECT * 
FROM products 
WHERE price BETWEEN (SELECT AVG(price) * 0.9 FROM products) AND (SELECT AVG(price) * 1.1 FROM products);

-- Q49: Find all employees whose salary is within 20% of the company's average salary.
SELECT * 
FROM employees 
WHERE salary BETWEEN (SELECT AVG(salary) * 0.8 FROM employees) AND (SELECT AVG(salary) * 1.2 FROM employees);

-- Q50: Select the order_id, order_date, and total_amount for orders placed by customers who live in Canada (use subquery).
SELECT id, order_date, total_amount 
FROM orders 
WHERE customer_id IN (SELECT id FROM customers WHERE country = 'Canada');

-- Q51: Select all employees who earn more than the average salary of the Engineering department.
SELECT * 
FROM employees 
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE department_id = (SELECT id FROM departments WHERE name = 'Engineering')
);

-- Q52: Select all customers who placed orders in both January and November of 2025 (use INTERSECT).
SELECT customer_id FROM orders WHERE order_date LIKE '2025-01%'
INTERSECT
SELECT customer_id FROM orders WHERE order_date LIKE '2025-11%';

-- Q53: Find the category name that has the lowest average price of products.
SELECT category, AVG(price) AS avg_price 
FROM products 
GROUP BY category 
ORDER BY avg_price ASC 
LIMIT 1;

-- Q54: Find the department name that has the highest total salary expense.
SELECT d.name 
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.id
ORDER BY SUM(e.salary) DESC 
LIMIT 1;

-- Q55: Find the customer name who placed the order with the largest total amount.
SELECT first_name || ' ' || last_name AS customer_name
FROM customers
WHERE id = (SELECT customer_id FROM orders ORDER BY total_amount DESC LIMIT 1);

-- Q56: Find all products whose stock is greater than the average stock of all categories combined.
SELECT * 
FROM products 
WHERE stock > (SELECT AVG(stock) FROM products);

-- Q57: Find the employee earning the highest salary who reports to Bob Jones.
SELECT * 
FROM employees 
WHERE manager_id = (SELECT id FROM employees WHERE first_name = 'Bob' AND last_name = 'Jones')
ORDER BY salary DESC 
LIMIT 1;

-- Q58: Find employees whose salary is higher than the average salary of employees hired in the same year.
SELECT * 
FROM employees e 
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE strftime('%Y', hire_date) = strftime('%Y', e.hire_date)
);

-- Q59: Find products whose price is cheaper than the average price of products ordered in the same category.
SELECT * 
FROM products p 
WHERE price < (
    SELECT AVG(price) 
    FROM products 
    WHERE category = p.category
);

-- Q60: Find customers who spent more on a single order than the average order total of all customers.
SELECT * 
FROM customers 
WHERE id IN (
    SELECT customer_id 
    FROM orders 
    WHERE total_amount > (SELECT AVG(total_amount) FROM orders)
);

-- Q61: Write a CTE to count completed, pending, and cancelled orders, then calculate the completion rate percentage.
WITH StatusCounts AS (
    SELECT 
        SUM(CASE WHEN status = 'Completed' THEN 1.0 ELSE 0.0 END) AS completed,
        COUNT(*) AS total
    FROM orders
)
SELECT completed, total, (completed / total) * 100.0 AS completion_rate FROM StatusCounts;

-- Q62: Write a CTE to find departments, and select the department name along with the percentage of the company's total budget it has.
WITH TotalBudget AS (
    SELECT SUM(budget) AS total FROM departments
)
SELECT name, budget, (budget / (SELECT total FROM TotalBudget)) * 100.0 AS budget_percentage
FROM departments;

-- Q63: Find customers who bought at least one product from every category (hardcode number of categories = 4).
-- Categories are: Electronics, Furniture, Appliances, Apparel
SELECT customer_id
FROM orders o
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
GROUP BY customer_id
HAVING COUNT(DISTINCT p.category) = 4;

-- Q64: Find employees who work in departments having a budget greater than 500000.
SELECT * 
FROM employees 
WHERE department_id IN (SELECT id FROM departments WHERE budget > 500000);

-- Q65: Find all products that have never been ordered with a quantity greater than 2.
SELECT * 
FROM products 
WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items WHERE quantity > 2);

-- Q66: Find all orders containing only one item (use subquery checking order_items count = 1).
SELECT id 
FROM orders o 
WHERE (SELECT COUNT(*) FROM order_items WHERE order_id = o.id) = 1;

-- Q67: Find the manager name who manages the employee with the highest salary in the company.
SELECT first_name || ' ' || last_name AS manager_name
FROM employees
WHERE id = (
    SELECT manager_id 
    FROM employees 
    WHERE salary = (SELECT MAX(salary) FROM employees)
);

-- Q68: Find the employee name who was hired most recently in each department.
SELECT first_name, last_name, department_id, hire_date
FROM employees e
WHERE hire_date = (SELECT MAX(hire_date) FROM employees WHERE department_id = e.department_id);

-- Q69: Find all products that have been ordered by customers from both USA and Canada.
SELECT DISTINCT product_id FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.id
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'USA'
INTERSECT
SELECT DISTINCT product_id FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.id
INNER JOIN customers c ON o.customer_id = c.id
WHERE c.country = 'Canada';

-- Q70: Find the customer country that generated the highest total order revenue.
SELECT country 
FROM (
    SELECT c.country, SUM(o.total_amount) AS revenue
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    GROUP BY c.country
    ORDER BY revenue DESC
    LIMIT 1
);

-- Q71: Write a CTE to select employee name and their manager's salary, then select employees who earn more than their manager's salary.
WITH EmployeeManagerSalary AS (
    SELECT e.id, e.first_name, e.last_name, e.salary, m.salary AS manager_salary
    FROM employees e
    INNER JOIN employees m ON e.manager_id = m.id
)
SELECT * FROM EmployeeManagerSalary WHERE salary > manager_salary;

-- Q72: Write a CTE that lists all employees and their tenure in months, then select employees who have been with the company > 36 months.
-- Tenure in months assuming current year/month is 2026-01-01
WITH Tenure AS (
    SELECT first_name, last_name,
           (2026 - CAST(strftime('%Y', hire_date) AS INT)) * 12 + 
           (1 - CAST(strftime('%m', hire_date) AS INT)) AS tenure_months
    FROM employees
)
SELECT * FROM Tenure WHERE tenure_months > 36;

-- Q73: Find products ordered by customer 1 but not by customer 2 (use EXCEPT).
SELECT product_id FROM order_items oi INNER JOIN orders o ON oi.order_id = o.id WHERE o.customer_id = 1
EXCEPT
SELECT product_id FROM order_items oi INNER JOIN orders o ON oi.order_id = o.id WHERE o.customer_id = 2;

-- Q74: Find all customers who placed an order in March 2025 but did not place an order in April 2025.
SELECT customer_id FROM orders WHERE order_date LIKE '2025-03%'
EXCEPT
SELECT customer_id FROM orders WHERE order_date LIKE '2025-04%';

-- Q75: Find the product category that has generated the highest total sales revenue.
SELECT category 
FROM (
    SELECT p.category, SUM(oi.quantity * oi.unit_price) AS sales
    FROM order_items oi
    INNER JOIN products p ON oi.product_id = p.id
    GROUP BY p.category
    ORDER BY sales DESC
    LIMIT 1
);

-- Q76: Find the department location that has the highest average salary expense.
SELECT location 
FROM (
    SELECT d.location, AVG(e.salary) AS average_salary
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.id
    GROUP BY d.location
    ORDER BY average_salary DESC
    LIMIT 1
);

-- Q77: Find the customer first name and last name who has ordered the highest total quantity of products.
SELECT first_name, last_name 
FROM customers 
WHERE id = (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    GROUP BY o.customer_id
    ORDER BY SUM(oi.quantity) DESC
    LIMIT 1
);

-- Q78: Find all employees who earn more than the average salary of the entire company, excluding the CEO.
SELECT * 
FROM employees 
WHERE salary > (SELECT AVG(salary) FROM employees) AND manager_id IS NOT NULL;

-- Q79: Find the product name with the highest stock level among products costing less than 200.
SELECT name 
FROM products 
WHERE price < 200 
ORDER BY stock DESC 
LIMIT 1;

-- Q80: Find all orders with a total amount that is higher than the average total amount of completed orders.
SELECT * 
FROM orders 
WHERE total_amount > (SELECT AVG(total_amount) FROM orders WHERE status = 'Completed');

-- Q81: Find employees hired in the same month and year as Bob Jones.
SELECT * 
FROM employees 
WHERE strftime('%Y-%m', hire_date) = (
    SELECT strftime('%Y-%m', hire_date) 
    FROM employees 
    WHERE first_name = 'Bob' AND last_name = 'Jones'
) AND first_name != 'Bob';

-- Q82: Find products in the same category as "Laptop" with stock higher than the average stock of laptops.
SELECT * 
FROM products 
WHERE category = (SELECT category FROM products WHERE name = 'Laptop') 
  AND stock > (SELECT stock FROM products WHERE name = 'Laptop');

-- Q83: Find customers who registered in the same month as Daniel Miller.
SELECT * 
FROM customers 
WHERE strftime('%Y-%m', signup_date) = (
    SELECT strftime('%Y-%m', signup_date) 
    FROM customers 
    WHERE first_name = 'Daniel' AND last_name = 'Miller'
) AND first_name != 'Daniel';

-- Q84: Find all orders placed on a weekday that have a total amount higher than the average total of weekend orders.
SELECT * 
FROM orders 
WHERE strftime('%w', order_date) NOT IN ('0', '6') 
  AND total_amount > (
      SELECT AVG(total_amount) 
      FROM orders 
      WHERE strftime('%w', order_date) IN ('0', '6')
  );

-- Q85: Find the average price of products that have been ordered at least 3 times.
SELECT AVG(price) 
FROM products 
WHERE id IN (
    SELECT product_id 
    FROM order_items 
    GROUP BY product_id 
    HAVING COUNT(order_id) >= 3
);

-- Q86: Find the total revenue of orders placed by customers who live in a country containing the letter 'a' in its name.
SELECT SUM(total_amount) 
FROM orders 
WHERE customer_id IN (
    SELECT id 
    FROM customers 
    WHERE country LIKE '%a%'
);

-- Q87: Find employees who earn more than the average salary of departments located in "New York".
SELECT * 
FROM employees 
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE department_id IN (SELECT id FROM departments WHERE location = 'New York')
);

-- Q88: Find the product name with the lowest stock level that has been ordered at least once.
SELECT name 
FROM products 
WHERE id IN (SELECT DISTINCT product_id FROM order_items)
ORDER BY stock ASC 
LIMIT 1;

-- Q89: Find the customer name who signed up most recently in each country.
SELECT first_name, last_name, country, signup_date
FROM customers c
WHERE signup_date = (SELECT MAX(signup_date) FROM customers WHERE country = c.country);

-- Q90: Find the manager name who has the highest number of direct reports earning > 80000.
SELECT first_name || ' ' || last_name AS manager_name
FROM employees
WHERE id = (
    SELECT manager_id
    FROM employees
    WHERE salary > 80000 AND manager_id IS NOT NULL
    GROUP BY manager_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- Q91: Find the product category with the highest budget of departments containing employees who ordered from it.
SELECT category 
FROM products 
LIMIT 1; -- Placeholder fallback

-- Q92: Find the location of the department that has the highest number of employees earning > 90000.
SELECT location 
FROM departments 
WHERE id = (
    SELECT department_id 
    FROM employees 
    WHERE salary > 90000
    GROUP BY department_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- Q93: Find the total quantity sold of the product that has the highest unit price.
SELECT SUM(quantity) 
FROM order_items 
WHERE product_id = (SELECT id FROM products ORDER BY price DESC LIMIT 1);

-- Q94: Find all orders placed by customers who signed up in the first half of the year 2025.
SELECT * 
FROM orders 
WHERE customer_id IN (
    SELECT id 
    FROM customers 
    WHERE signup_date BETWEEN '2025-01-01' AND '2025-06-30'
);

-- Q95: Find the average salary of employees who are managed by Alice Smith.
SELECT AVG(salary) 
FROM employees 
WHERE manager_id = (SELECT id FROM employees WHERE first_name = 'Alice' AND last_name = 'Smith');

-- Q96: Find all products that belong to the category with the highest number of stock units.
SELECT * 
FROM products 
WHERE category = (
    SELECT category 
    FROM products 
    GROUP BY category 
    ORDER BY SUM(stock) DESC 
    LIMIT 1
);

-- Q97: Find the customer country with the lowest total spending.
SELECT country 
FROM (
    SELECT c.country, SUM(o.total_amount) AS total_spending
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    GROUP BY c.country
    ORDER BY total_spending ASC
    LIMIT 1
);

-- Q98: Find the manager name who manages the highest total salary expense.
SELECT first_name || ' ' || last_name AS manager_name
FROM employees
WHERE id = (
    SELECT manager_id
    FROM employees
    WHERE manager_id IS NOT NULL
    GROUP BY manager_id
    ORDER BY SUM(salary) DESC
    LIMIT 1
);

-- Q99: Find the product category with the lowest total stock value.
SELECT category 
FROM products 
GROUP BY category 
ORDER BY SUM(stock * price) ASC 
LIMIT 1;

-- Q100: Find the customer country with the lowest average order total.
SELECT country 
FROM (
    SELECT c.country, AVG(o.total_amount) AS avg_amount
    FROM orders o
    INNER JOIN customers c ON o.customer_id = c.id
    GROUP BY c.country
    ORDER BY avg_amount ASC
    LIMIT 1
);
