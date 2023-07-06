import sqlite3
import pandas as pd

class QueryHandler:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def query_to_dataframe(self, query):
        df = pd.read_sql_query(query, self.conn)
        return df

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    # Create an instance of the BasicQueries class
    basic_queries = QueryHandler("testDB.db")
    
    # SELECT queries
    do_query1 = False
    if do_query1:
        query1 = "SELECT * FROM customers"
        result1 = basic_queries.execute_query(query1)
        print("Query 1 Result:")
        for row in result1:
            print(row)
        print()

    do_query2 = True
    if do_query2:
        query2 = "SELECT item_name FROM items WHERE remaining_stock > 50"
        df2 = basic_queries.query_to_dataframe(query2)
        print("Query 2 Result:")
        print(df2)
        print()

    # INSERT queries
    do_query3 = False
    if do_query3:
        query3 = "INSERT INTO customers (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com')"
        basic_queries.execute_query(query3)
        print("New customer inserted successfully.")
        print()

    do_query4 = False
    if do_query4:
        query4 = "INSERT INTO items (item_name, item_type, item_price, remaining_stock) VALUES ('Phone', 'Electronics', 599.99, 10)"
        basic_queries.execute_query(query4)
        print("New item inserted successfully.")
        print()

    # UPDATE queries
    do_query5 = False
    if do_query5:
        query5 = "UPDATE customers SET email = 'newemail@example.com' WHERE customer_id = 1"
        basic_queries.execute_query(query5)
        print("Email updated successfully.")
        print()

    do_query6 = False
    if do_query6:
        query6 = "UPDATE items SET item_price = 499.99 WHERE item_id = 1"
        basic_queries.execute_query(query6)
        print("Item price updated successfully.")
        print()

    # DELETE queries
    do_query7 = False
    if do_query7:
        query7 = "DELETE FROM customers WHERE customer_id = 2"
        basic_queries.execute_query(query7)
        print("Customer deleted successfully.")
        print()

    do_query8 = False
    if do_query8:
        query8 = "DELETE FROM items WHERE item_id = 2"
        basic_queries.execute_query(query8)
        print("Item deleted successfully.")
        print()
    
    # Other sample queries
    do_query9 = True

    if do_query9:
        query9 = "SELECT * FROM items WHERE remaining_stock < 50"
        df9 = basic_queries.query_to_dataframe(query9)
        print("Query 9 Result:")
        print(df9.shape)
        print(df9)
        print()

    do_query10 = False

    if do_query10:
        query10 = "SELECT * FROM items WHERE remaining_stock > 50"
        df10 = basic_queries.query_to_dataframe(query10)
        print("Query 10 Result:")
        print(df10.shape)
        print(df10)
        print()

    do_query11 = False

    if do_query11:
        query11 = "SELECT customer_id, first_name, last_name FROM customers WHERE first_name = 'John'"
        df11 = basic_queries.query_to_dataframe(query11)
        print("Query 11 Result:")
        print(df11)
        print()

    # Close the database connection
    basic_queries.close_connection()
