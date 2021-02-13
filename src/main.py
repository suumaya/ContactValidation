from database import Database
import re
# Pass your computer password to the pw variable
pw = 'mypassword'

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
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    person_insert_query = "INSERT INTO Person (name,phone,address) VALUES(?,?,?);"
    name_regex = r'(([a-zA-Z]{2,})?(\s?[a-zA-Z]\'{1}[a-zA-Z]{2,})?\,?\s?([a-zA-Z]{2,})?(\-|\s)?[a-zA-Z]{0,}?\.?)$'
    phone_regex = r'^[1-3]{0,1}([+][1-3]{1,2})?\s{0,1}(([(]{0,1}(703){0,1}[)])|([(]{0,1}(21){0,1}[)]){0,1})\s{0,1}[-\s\.0-6]{1}[-\s\.0-9]{4,}$'
    address_regex =  r'^[0-9]{3,4}[a-zA-Z]?\s[0-9]?[a-zA-Z]+\s[a-zA-Z]+\,?\s[a-zA-Z]*[#\s\d\]?\.?\,\s[a-zA-Z]+\,?\s[a-zA-Z]+\s?[0-9]{5}\-?[0-9]{0,4}'

    # #Take Valid Input from user
    name = input("Please enter your name: ")
    while not re.match(name_regex, name):
        name = input("Oops! Please enter a valid name: ")
    else:
        phone = input("Please enter your phone: ")
        while not re.match(phone_regex, phone):
            phone = input("Oops! Please enter a valid phone number: ")
        else:
            address = input("Please enter your address: ")
            while not re.match(address_regex, address):
                address = input("Oops! Please enter a valid address: ")
            else:
                Database.execute_add_query(connection, person_insert_query,(name, phone, address))

    # print('after execute')


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


def resetAll():
    drob_db = """DROP DATABASE mydb;"""
    connection = Database.create_db_connection("localhost", "root", pw, 'mydb')
    Database.execute_query(connection, drob_db)
