from database import Database

creat_db_query = "CREATE DATABASE mydb"

create_person_table = """
                                CREATE TABLE Person (
                                  id INT PRIMARY KEY,
                                  name VARCHAR(100) NOT NULL UNIQUE,
                                  phone VARCHAR(100) NOT NULL UNIQUE,
                                  address VARCHAR(100) NOT NULL
                                  );
                                 """
person_insert_query = """
                                INSERT INTO Person VALUES
                                (1,'Bruce Schneier', '12345', '795 E DRAGRAM Drive, TUCSON, AZ 85705-7598'),
                                (2,'Schneier, Bruce', '(703)111-2121', '795 E DRAGRAM Dr., TUCSON, AZ 85705'), 
                                (3,'Schneier, Bruce Wayne', '123-1234', '770W DRAGRAM Drive # 321, TUCSON, AZ 85703');
                                """
list_query = """
                                SELECT * FROM Person;
                                """
delete_query = """
                                DELETE FROM Person 
                                WHERE name = 'Schneier, Bruce';
                                """

def run():

    print('in main')

    # Pass your computer password to the pw variable
    pw = '11213141'
    connection = Database.create_server_connection("localhost", "root", pw)
    Database.create_database(connection, creat_db_query)
    #
    # # Creating Tables
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    Database.execute_query(connection, create_person_table)
    #
    # # Add some data¶
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    Database.execute_query(connection, person_insert_query)

    # Read
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    results = Database.read_query(connection, list_query)
    Database.formatOutput(results)

    # Deleting Records
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    Database.execute_query(connection, delete_query)
    results = Database.read_query(connection, list_query)
    Database.formatOutput(results)

    # #Take Valid Input from user
    # name = input("Please enter your name: ")
    # phone = input("Please enter your phone: ")
    # address = input("Please enter your address: ")
    #
    # #Take Inalid Input from user
    # invalid_name = input("Please enter your name: ")
    # invalid_phone = input("Please enter your phone: ")
    # invalid_address = input("Please enter your address: ")