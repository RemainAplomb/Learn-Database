-- Calculate total sales
SELECT SUM(amount) AS total_sales
FROM sales;

-- Find average age
SELECT AVG(age) AS average_age
FROM users;

-- Extract month and year
SELECT EXTRACT(MONTH FROM date) AS month, EXTRACT(YEAR FROM date) AS year
FROM orders;
