import mysql.connector
import os
#connect to database
def connect_db():
    user = os.environ.get("db_user")
    password = os.environ.get("db_password")
    database=os.environ.get("db_name")
    db = mysql.connector.connect(user=user, password=password, database=database)
    return db
#create the busproject database if not exist
def create_database(cursor,DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def create_table(name,table_data,cursor):
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(table_data)
    except mysql.connector.Error as err:
        print(err.msg)
    else:
        print("OK")

def insert_passenger(cursor,data_passenger):
    add_passenger = "INSERT INTO passenger " \
                    "VALUES (%s,%s,%s,%s,%s,%s,%s )"
    cursor.execute(add_passenger, data_passenger)