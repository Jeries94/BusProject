import mysql.connector
from mysql.connector import errorcode

#connect to database
db=mysql.connector.connect(user="root",password="Jeries",host="localhost")
DB_NAME="busproject"
    # prepare a cursor object using cursor() method
cursor = db.cursor()

# Creating tables for BusProject
TABLES = {}
TABLES['station'] = (
    "CREATE TABLE `station` ("
    "  `id` int(11) NOT NULL,"
    "  `name` varchar(15) NOT NULL,"
    "  `address` varchar(30),"
    "  `longitude` decimal NOT NULL,"
    "  `latitude` decimal NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['bus'] = (
    "CREATE TABLE `bus` ("
    "  `id` int(11) NOT NULL,"
    "  `Capacity` int(3) NOT NULL,"
    "  `plate_number` varchar(10) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['route'] = (
    "CREATE TABLE `route` ("
    "  `id` int(11) NOT NULL,"
    "  `source_station_id` int(11) NOT NULL,"
    "  `destination_station_id` int(11) NOT NULL,"
    "  `bus_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (source_station_id) REFERENCES station(id),"
    "  FOREIGN KEY (destination_station_id) REFERENCES station(id), "
    "  FOREIGN KEY (bus_id) REFERENCES bus(id) "
    ")")

TABLES['route_schedule'] = (
    "CREATE TABLE `route_schedule` ("
    "  `id` int(11) NOT NULL,"
    "  `route_id` int(11) NOT NULL,"
    "  `departure_time` datetime NOT NULL,"
    "  `arrival_time` datetime NOT NULL,"
    "  `wait_time` int(7) NOT NULL,"
    "  `price` int(4) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (route_id) REFERENCES route(id)"
    ")")

TABLES['passenger'] = (
    "CREATE TABLE `passenger` ("
    "  `id` int(11) NOT NULL,"
    "  `first_name` varchar(10) NOT NULL,"
    "  `last_name` varchar(15) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `date_of_birth` date NOT NULL,"
    "  `email` varchar(25),"
    "  `phone` varchar(15),"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['ticket'] = (
    "CREATE TABLE `ticket` ("
    "  `id` int(11) NOT NULL,"
    "  `route_schedule_id` int(11) NOT NULL,"
    "  `passenger_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  FOREIGN KEY (route_schedule_id) REFERENCES route_schedule(id),"
    "  FOREIGN KEY (passenger_id) REFERENCES passenger(id)"
    ")")

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    db.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        db.database = DB_NAME
    else:
        print(err)
        exit(1)


for name, table_data in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(table_data)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
# disconnect from server
db.close()


