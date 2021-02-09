import mysql.connector
from mysql.connector import Error
import pandas as pd
# import regex
import main


class Database:

    # Connecting to MySQL Server
    def create_server_connection(host_name, user_name, user_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    #Creating a New Database
    def create_database(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            print(f"Error: '{err}'")


    # Connecting to the Database
    def create_db_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                database=db_name
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

    #Creating a Query Execution Function
    def execute_query(connection, query):
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")


    # Reading Data
    def read_query(connection, query):
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")


    # Formatting Output into a pandas DataFrame
    def formatOutput(results):
        from_db = []

        for result in results:
            result = list(result)
            from_db.append(result)


        columns = ["id","name", "phone", "address"]
        df = pd.DataFrame(from_db, columns=columns)
        return df

    if __name__ == "__main__":
        main.run()
