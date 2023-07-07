-- SELECT queries
SELECT * FROM customers;
SELECT * FROM items;
SELECT * FROM orders;
SELECT * FROM customers WHERE first_name = 'John';
SELECT * FROM items WHERE remaining_stock > 50;
SELECT * FROM orders WHERE date >= '2022-01-01' AND date <= '2022-12-31';


-- INSERT queries
INSERT INTO customers (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com');
INSERT INTO items (item_name, item_type, item_price, remaining_stock) VALUES ('Phone', 'Electronics', 599.99, 10);
INSERT INTO orders (seller_id, item_id, customer_id, address, date) VALUES (1, 1, 1, '123 Main St', '2023-07-07');


-- UPDATE queries
UPDATE customers SET email = 'newemail@example.com' WHERE customer_id = 1;
UPDATE items SET item_price = 499.99 WHERE item_id = 1;
UPDATE orders SET address = '456 Elm St' WHERE order_id = 1;


-- DELETE queries
DELETE FROM customers WHERE customer_id = 2;
DELETE FROM items WHERE item_id = 2;
DELETE FROM orders WHERE order_id = 2;
