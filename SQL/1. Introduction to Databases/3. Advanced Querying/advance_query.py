import sqlite3
import pandas as pd

class AdvanceQueryHandler:
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

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE {table_name} ({columns})"
        self.execute_query(query)
        print(f"Table '{table_name}' created successfully.")

    def alter_table(self, table_name, alteration):
        query = f"ALTER TABLE {table_name} {alteration}"
        self.execute_query(query)
        print(f"Table '{table_name}' altered successfully.")

    def drop_table(self, table_name):
        query = f"DROP TABLE {table_name}"
        self.execute_query(query)
        print(f"Table '{table_name}' dropped successfully.")

    def grant_privileges(self, table_name, privileges, user):
        query = f"GRANT {privileges} ON {table_name} TO {user}"
        self.execute_query(query)
        print(f"Privileges granted successfully.")

    def revoke_privileges(self, table_name, privileges, user):
        query = f"REVOKE {privileges} ON {table_name} FROM {user}"
        self.execute_query(query)
        print(f"Privileges revoked successfully.")

    def begin_transaction(self):
        query = "BEGIN"
        self.execute_query(query)
        print("Transaction started.")

    def commit_transaction(self):
        query = "COMMIT"
        self.execute_query(query)
        print("Transaction committed successfully.")

    def rollback_transaction(self):
        query = "ROLLBACK"
        self.execute_query(query)
        print("Transaction rolled back.")

if __name__ == "__main__":
    # Create an instance of the AdvanceQueryHandler class
    advance_queries = AdvanceQueryHandler("testDB.db")

    # Create table query
    do_create_table = False
    if do_create_table:
        table_name = "wishes"
        columns = "wish_id INT PRIMARY KEY, customer_id INT, wish_date DATE"
        advance_queries.create_table(table_name, columns)

    # Alter table query
    do_alter_table = False
    if do_alter_table:
        table_name = "wishes"
        alteration = "ADD COLUMN total_amount FLOAT"
        advance_queries.alter_table(table_name, alteration)

    # Drop table query
    do_drop_table = False
    if do_drop_table:
        table_name = "wishes"
        advance_queries.drop_table(table_name)

    # Grant privileges query
    do_grant_privileges = False
    if do_grant_privileges:
        table_name = "wishes"
        privileges = "SELECT, INSERT"
        user = "user1"
        advance_queries.grant_privileges(table_name, privileges, user)

    # Revoke privileges query
    do_revoke_privileges = False
    if do_revoke_privileges:
        table_name = "wishes"
        privileges = "SELECT, INSERT"
        user = "user1"
        advance_queries.revoke_privileges(table_name, privileges, user)

    # Begin transaction query
    do_begin_transaction = False
    if do_begin_transaction:
        advance_queries.begin_transaction()

    # Commit transaction query
    do_commit_transaction = False
    if do_commit_transaction:
        advance_queries.commit_transaction()

    # Rollback transaction query
    do_rollback_transaction = False
    if do_rollback_transaction:
        advance_queries.rollback_transaction()

    # Close the database connection
    advance_queries.close_connection()
