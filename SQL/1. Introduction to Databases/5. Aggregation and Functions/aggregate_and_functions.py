import sqlite3
import pandas as pd

class AggregateFunctions:
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

    def calculate_total_sales(self):
        query = "SELECT SUM(amount) AS total_sales FROM sales"
        result = self.execute_query(query)
        total_sales = result[0][0]
        return total_sales

    def find_average_age(self):
        query = "SELECT AVG(age) AS average_age FROM users"
        result = self.execute_query(query)
        average_age = result[0][0]
        return average_age

    def extract_month_and_year(self):
        query = "SELECT EXTRACT(MONTH FROM date) AS month, EXTRACT(YEAR FROM date) AS year FROM orders"
        df = self.query_to_dataframe(query)
        return df

if __name__ == "__main__":
    # Create an instance of the AggregateFunctions class
    aggregate_queries = AggregateFunctions("testDB.db")

    # Calculate total sales
    total_sales = aggregate_queries.calculate_total_sales()
    print("Total Sales:", total_sales)

    # Find average age
    average_age = aggregate_queries.find_average_age()
    print("Average Age:", average_age)

    # Extract month and year
    month_year_df = aggregate_queries.extract_month_and_year()
    print("Month and Year:")
    print(month_year_df)

    # Close the database connection
    aggregate_queries.close_connection()
