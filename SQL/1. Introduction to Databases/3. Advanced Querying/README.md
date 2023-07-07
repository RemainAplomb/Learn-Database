# Advance Query

## Data Definition Language (DDL)

### Create

The CREATE statement is used to create database objects such as tables, indexes, views, or schemas. Here's an example of creating a table:

```
CREATE TABLE customers (
customer_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100)
);
```

This statement creates a table named "customers" with columns for customer_id, first_name, last_name, and email.

### Alter

The ALTER statement is used to modify the structure of an existing database object. It allows you to add, modify, or drop columns, as well as change constraints or indexes. Here's an example of altering a table:

```
ALTER TABLE customers
ADD contact_number VARCHAR(20);
```

This statement adds a new column named "contact_number" to the existing "customers" table.

### Drop

The DROP statement is used to delete a database object, such as a table or index. Here's an example of dropping a table:

```
DROP TABLE customers;
```

This statement deletes the "customers" table from the database.

These are just basic examples of the CREATE, ALTER, and DROP statements. There are many more options and variations available for these statements depending on your specific database management system (e.g., MySQL, PostgreSQL, SQLite).

## Data Control Language (DCL)

### Grant

The GRANT statement is used to grant specific privileges or permissions to database users. These privileges determine what operations the user can perform on the database objects. Here's an example of granting privileges:

```
GRANT SELECT, INSERT ON customers TO user1;
```

This statement grants the SELECT and INSERT privileges on the "customers" table to the user named "user1".

### Revoke

The REVOKE statement is used to revoke previously granted privileges from users. It removes the specified privileges from the user, restricting their access to the database objects. Here's an example of revoking privileges:

```
REVOKE SELECT, INSERT ON customers FROM user1;
```

This statement revokes the SELECT and INSERT privileges on the "customers" table from the user named "user1".

These are basic examples of the GRANT and REVOKE statements. It's important to note that the available privileges and the syntax may vary depending on the specific database management system you are using. Additionally, you may need appropriate permissions to execute these statements, as they often require administrative privileges.

## Transaction Control Language (TCL)

### Begin

The BEGIN statement is used to mark the beginning of a transaction. It indicates that a series of database operations should be treated as a single transaction unit. Here's an example:

```
BEGIN;
```

### Tran

The TRAN statement is a shorthand version of the BEGIN statement. It also marks the beginning of a transaction. Here's an example:

```
TRAN;
```

### Commit

The COMMIT statement is used to save the changes made within a transaction to the database. It marks the successful completion of a transaction and makes the changes permanent. Here's an example:

```
COMMIT;
```

### Rollback

The ROLLBACK statement is used to undo the changes made within a transaction. It cancels the entire transaction and restores the database to its state before the transaction began. Here's an example:

```
ROLLBACK;
```

These are basic examples of the BEGIN, TRAN, COMMIT, and ROLLBACK statements. It's important to note that transactions are typically used in situations where multiple database operations need to be performed atomically, ensuring either all of them succeed or none of them are committed. The exact syntax and behavior of these statements may vary depending on the specific database management system you are using.
