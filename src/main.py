from database import Database

# Pass your computer password to the pw variable
pw = '11213141'

#
def run():
    creat_db_query = "CREATE DATABASE mydb"

    create_person_table = """CREATE TABLE Person
                        (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(100) NOT NULL UNIQUE,
                        phone VARCHAR(100) NOT NULL UNIQUE,address VARCHAR(100) NOT NULL);"""

    # Create connection to server and create db in it
    connection = Database.create_server_connection("localhost", "root", pw)
    Database.create_database(connection, creat_db_query)

    # # Create connection to db and create table
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    Database.execute_query(connection, create_person_table)


def addPerson():
    # # Add some data¶
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    # #Take Valid Input from user
    name = input("Please enter your name: ")
    phone = input("Please enter your phone: ")
    address = input("Please enter your address: ")
    person_insert_query = "INSERT INTO Person (name,phone,address) VALUES(?,?,?);"
    Database.execute_add_query(connection, person_insert_query,(name, phone, address))
    print('after execute')


def delPerson(by_value):
    print('In delPerson')
    # Deleting Records
    list_query = """SELECT * FROM Person;"""
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    if by_value == '1':
        to_be_deleted = input("Please enter your phone: ")
        delete_query = """DELETE FROM Person WHERE phone = ? ;  """
    else:
        to_be_deleted = input("Please enter your name: ")
        delete_query = """DELETE FROM Person WHERE name = ? ;  """
    Database.execute_add_query(connection, delete_query,(to_be_deleted,))
    results = Database.read_query(connection, list_query)
    Database.formatOutput(results)

def listAll():
    print('In listAll')
    # Read
    list_query = """SELECT * FROM Person;"""
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    results = Database.read_query(connection, list_query)
    Database.formatOutput(results)


