import sqlite3

class SQLJoin:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.conn.close()

    def inner_join_example(self):
        query = '''
        SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        '''
        result = self.execute_query(query)
        print("Inner Join Example:")
        for row in result:
            print(row)
        print()

    def left_join_example(self):
        query = '''
        SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
        FROM customers
        LEFT JOIN orders ON customers.customer_id = orders.customer_id
        '''
        result = self.execute_query(query)
        print("Left Join Example:")
        for row in result:
            print(row)
        print()

    def right_join_example(self):
        query = '''
        SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
        FROM customers
        RIGHT JOIN orders ON customers.customer_id = orders.customer_id
        '''
        result = self.execute_query(query)
        print("Right Join Example:")
        for row in result:
            print(row)
        print()

    def full_join_example(self):
        query = '''
        SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
        FROM customers
        FULL JOIN orders ON customers.customer_id = orders.customer_id
        '''
        result = self.execute_query(query)
        print("Full Join Example:")
        for row in result:
            print(row)
        print()

    def cross_join_example(self):
        query = '''
        SELECT customers.customer_id, customers.first_name, orders.order_id, orders.order_date
        FROM customers
        CROSS JOIN orders
        '''
        result = self.execute_query(query)
        print("Cross Join Example:")
        for row in result:
            print(row)
        print()


if __name__ == "__main__":
    # Create an instance of the SQLJoinExample class
    join_example = SQLJoin("testDB.db")

    # Perform different join examples
    join_example.inner_join_example()
    join_example.left_join_example()
    join_example.right_join_example()
    join_example.full_join_example()
    join_example.cross_join_example()

    # Close the database connection
    join_example.close_connection()
