# Aggregation and Function

## Brief Description

In SQL, Aggregation functions are used to perform calculations on sets of rows and return a single result. They allow us to summarize data, calculate totals, averages, counts, and more. On the other hand, Built-in Functions provide a range of capabilities to manipulate data and perform specific operations.

Aggregation functions and built-in functions are powerful tools in SQL that enable us to perform calculations, manipulate data, and extract valuable insights from a database. By understanding their usage and applying them appropriately, we can efficiently analyze and transform data to meet our specific requirements.

## Aggregation Functions

### COUNT

The COUNT() function is used to count the number of rows that match a specified condition or to count the total number of rows in a table.

Example:

```
SELECT COUNT(\*) FROM customers;
```

### SUM

The SUM() function is used to calculate the sum of values in a column.

Example:

```
SELECT SUM(price) FROM orders;
```

### AVG

The AVG() function is used to calculate the average value of a column.

Example:

```
SELECT AVG(age) FROM employees;
```

### MIN

The AVG() function is used to calculate the average value of a column.

Example:

```
SELECT MIN(salary) FROM employees;
```

### MAX

The MAX() function is used to find the maximum value in a column.

Example:

```
SELECT MAX(salary) FROM employees;
```

## Built-in Functions

### String Functions

Here are the list of examples for string functions:

    - LENGTH(): Returns the length of a string.
    - UPPER(): Converts a string to uppercase.
    - LOWER(): Converts a string to lowercase.
    - SUBSTRING(): Extracts a substring from a string based on specified positions.

### Date and Time Functions

Here are the list of examples for date and time functions:

    - DATE(): Extracts the date part from a datetime value.
    - TIME(): Extracts the time part from a datetime value.
    - YEAR(): Extracts the year from a date or datetime value.
    - MONTH(): Extracts the month from a date or datetime value.

### Mathematical Functions

Here are the list of examples for mathematical functions:

    - ABS(): Returns the absolute value of a number.
    - ROUND(): Rounds a number to a specified number of decimal places.
    - POWER(): Raises a number to a specified power.

## Hands-on Examples

### Calculate Sales

```
SELECT SUM(amount) AS total_sales FROM sales;
```

### Finding Average Age

```
SELECT AVG(age) AS average_age FROM users;
```

### Extracting Month and Year from Dates

```
SELECT EXTRACT(MONTH FROM date) AS month, EXTRACT(YEAR FROM date) AS year FROM orders;
```
