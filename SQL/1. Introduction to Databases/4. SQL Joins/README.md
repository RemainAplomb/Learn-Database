# SQL Joins

SQL joins are used to combine rows from two or more tables based on a related column between them. Joins allow you to retrieve data from multiple tables in a single query by specifying how the tables should be connected.

It's important to note that when performing joins, you need to specify the columns to select, the tables to join, and the join condition using the ON clause.

To learn more about SQL joins and their usage, you can refer to the official documentation of the specific database management system you are using or various online SQL tutorials and resources.

## Inner Join

Returns only the matching rows from both tables based on the specified condition.

Syntax:

```
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

## Left Join

Left Join (or Left Outer Join): Returns all the rows from the left table and the matching rows from the right table. If there is no match, NULL values are returned for the right table.

Syntax:

```
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

## Right Join

Right Join (or Right Outer Join): Returns all the rows from the right table and the matching rows from the left table. If there is no match, NULL values are returned for the left table.

Syntax:

```
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

## Full Join

Full Join (or Full Outer Join): Returns all the rows from both tables. If there is no match, NULL values are returned for the non-matching side.

Syntax:

```
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

## Cross Join

Cross Join (or Cartesian Join): Returns the Cartesian product of the two tables, i.e., all possible combinations of rows from both tables.

Syntax:

```
SELECT columns
FROM table1
CROSS JOIN table2;
```

## Self-Join

Self Join: Joins a table with itself to retrieve related information from different rows within the same table.

Syntax:

```
SELECT columns
FROM table1 t1
JOIN table1 t2
ON t1.column = t2.column;
```
