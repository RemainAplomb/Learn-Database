# Since we have an empty database, let's populate it with random data

from faker import Faker
import sqlite3
import time
import csv
import pandas as pd

class Database:
    def __init__(self, db_name):
        self.start_database(db_name)
    
    def start_database(self, db_name):
        # Connect to the database
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create an instance of the Faker class
        self.fake = Faker()
    
    def close_database(self):
        # Commit the changes and close the connection
        self.conn.commit()
        self.conn.close()

    def populate_people(self, num_records, delete_prev=True, target= "customers"):
        if delete_prev:
            # Delete previous data from the "customers" table
            self.cursor.execute(f"DELETE FROM {target};")
            # Introduce a delay of 1 second
            time.sleep(1)

        # Generate and insert random data into the "customers" table
        records = []
        for _ in range(num_records):
            first_name = self.fake.first_name()
            middle_name = self.fake.first_name()  # Generating a random first name as middle name
            last_name = self.fake.last_name()
            email = self.fake.email()
            contact_number = self.fake.phone_number()

            records.append((first_name, middle_name, last_name, email, contact_number))

        self.cursor.executemany(f"INSERT INTO {target} (first_name, middle_name, last_name, email, contact_number) "
                                "VALUES (?, ?, ?, ?, ?)", records)

        return
    
    def populate_items(self, num_records, delete_prev=True):
        if delete_prev:
            # Delete previous data from the "items" table
            self.cursor.execute("DELETE FROM items;")
            # Introduce a delay of 1 second
            time.sleep(1)

        # Generate and insert random data into the "items" table
        for _ in range(num_records):
            item_name = str(self.fake.word())
            item_description = str(self.fake.sentence())
            item_type = str(self.fake.random_element(['Electronics', 'Clothing', 'Home Decor', 'Books']))
            item_price = float(self.fake.pydecimal(left_digits=3, right_digits=2, positive=True))
            remaining_stock = int(self.fake.random_int(min=0, max=100))
            # print(item_name)
            # print(item_description)
            # print(item_type) 
            # print(item_price)
            # print(remaining_stock)

            self.cursor.execute("INSERT INTO items (item_name, item_description, item_type, item_price, remaining_stock) "
                                "VALUES (?, ?, ?, ?, ?)",
                                (item_name, item_description, item_type, item_price, remaining_stock))

    def populate_orders(self, num_records, max_id_num = 1000, delete_prev=True):
        if delete_prev:
            # Delete previous data from the "orders" table
            self.cursor.execute("DELETE FROM orders;")
            # Introduce a delay of 1 second
            time.sleep(1)

        # Generate and insert random data into the "orders" table
        for _ in range(num_records):
            seller_id = self.fake.random_int(min=1, max=max_id_num)  # Assuming seller_id exists in the sellers table
            item_id = self.fake.random_int(min=1, max=max_id_num)  # Assuming item_id exists in the items table
            customer_id = self.fake.random_int(min=1, max=max_id_num)  # Assuming customer_id exists in the customers table
            address = self.fake.address()
            date = self.fake.date_this_decade()

            self.cursor.execute("INSERT INTO orders (seller_id, item_id, customer_id, address, date) "
                                "VALUES (?, ?, ?, ?, ?)",
                                (seller_id, item_id, customer_id, address, date))
    

    def export_table_to_csv(self, table_name, file_name):
        # Fetch all records from the specified table
        self.cursor.execute(f"SELECT * FROM {table_name}")
        records = self.cursor.fetchall()

        # Get the column names
        self.cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in self.cursor.fetchall()]

        # Write the records to a CSV file
        with open(file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(columns)  # Write the column names as the header
            writer.writerows(records)

        print(f"Data from table '{table_name}' exported to '{file_name}' successfully.")
        return


    def query_to_dataframe(self, query):
        df = pd.read_sql_query(query, self.conn)
        return df


    def populate_table_from_csv(self, csv_file, table_name, statement="UPDATE"):
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file)
            header = next(csv_data)  # Read the header row

            # Iterate over the rows in the CSV file
            for row in csv_data:
                # Check if the statement is "INSERT" or "UPDATE"
                if statement.upper() == "INSERT":
                    # Prepare the SQL INSERT statement
                    placeholders = ','.join(['?'] * len(header))
                    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                    self.cursor.execute(query, row)
                elif statement.upper() == "UPDATE":
                    # Prepare the SQL UPDATE statement
                    update_query = f"UPDATE {table_name} SET "
                    update_query += ", ".join([f"{column} = ?" for column in header[1:]])  # Exclude the customer_id column
                    
                    customer_id = row[0]  # Assuming customer_id is the first column in the CSV file
                    values = row[1:]  # Assuming the remaining columns in the CSV file match the table structure

                    update_query += f" WHERE customer_id = ?"
                    values.append(customer_id)

                    self.cursor.execute(update_query, values)
                else:
                    print("Invalid statement specified.")
        print(f"{csv_file} imported successfully to {table_name}")

        return




if __name__ == "__main__":
    # Initialize our database
    our_db = Database("testDB.db")

    # Define the number of records to generate
    num_records = 1000

    populate = False

    if populate:
        # Populate Customers
        our_db.populate_people(num_records)

        # Populate Sellers
        our_db.populate_people(num_records, target = "sellers")

        # Populate Items
        our_db.populate_items(num_records)

        # Populate Orders
        our_db.populate_orders(num_records)

    # To check result, you can do this
    # SELECT * FROM customers; 
    # SELECT COUNT(*) FROM customers; 
    # SELECT * FROM sellers;
    # SELECT COUNT(*) FROM sellers;
    # SELECT * FROM items;
    # SELECT COUNT(*) FROM items;
    # SELECT * FROM orders;
    # SELECT COUNT(*) FROM orders;

    export = False

    if export:
        # Export the customers table to a CSV file
        our_db.export_table_to_csv('customers', 'testDB_customers.csv')

        # Export the sellers table to a CSV file
        our_db.export_table_to_csv('sellers', 'testDB_sellers.csv')

        # Export the items table to a CSV file
        our_db.export_table_to_csv('items', 'testDB_items.csv')

        # Export the orders table to a CSV file
        our_db.export_table_to_csv('orders', 'testDB_orders.csv')
    
    send_query = True

    if send_query:
        query = "SELECT * FROM orders" 
        result_df = our_db.query_to_dataframe(query)
        print(result_df.head(20))
    

    import_csv = True

    if import_csv:
        csv_file = 'testDB_customers.csv'  # Replace with the path to your CSV file
        table_name = 'customers'  # Replace with the actual table name in your database
        our_db.populate_table_from_csv(csv_file, table_name)

    # Close Database
    our_db.close_database()