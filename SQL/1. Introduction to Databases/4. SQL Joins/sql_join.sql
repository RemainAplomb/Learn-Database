-- Inner Join Example
SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;

-- Left Join Example
SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;

-- Right Join Example
SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
FROM customers
RIGHT JOIN orders ON customers.customer_id = orders.customer_id;

-- Full Join Example
SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
FROM customers
FULL JOIN orders ON customers.customer_id = orders.customer_id;

-- Cross Join Example
SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
FROM customers
CROSS JOIN orders;
