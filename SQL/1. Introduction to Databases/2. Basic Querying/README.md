# SQL Statements

## Data Manipulation Language (DML)

### Select

The SELECT statement is used to retrieve data from one or more tables in a database. It allows you to specify which columns to retrieve, apply filtering conditions, and sort the results.

Syntax:

```
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column_name;
```

Example:

```
SELECT column1, column2
FROM employees
WHERE department = 'HR'
ORDER BY last_name;
```

In the example above, we select column1 and column2 from the employees table where the department is 'HR', and we order the results by the last_name column.

### Insert

The INSERT statement is used to add new records (rows) into a table. It allows you to specify the values to be inserted into the corresponding columns.

Syntax:

```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

Example:

```
INSERT INTO customers (name, email)
VALUES ('John Doe', 'john.doe@example.com');
```

In the example above, we insert a new record into the customers table, providing values for the name and email columns.

### Update

The UPDATE statement is used to modify existing records in a table. It allows you to specify the column(s) to be updated and the new values.

Syntax:

```
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

Example:

```
UPDATE employees
SET salary = 50000
WHERE department = 'HR';
```

In the example above, we update the salary column of the employees table to 50000 for records where the department is 'HR'.

### Delete

The DELETE statement is used to remove one or more records from a table based on specified conditions.

Syntax:

```
DELETE FROM table_name
WHERE condition;
```

Example:

```
DELETE FROM customers
WHERE id = 1;
```

In the example above, we delete the record from the customers table where the id is 1.

These DML statements provide powerful functionality to manipulate and retrieve data in SQL. Practice using these statements with different scenarios to become more comfortable with them.
