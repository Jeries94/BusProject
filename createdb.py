import database_connector


# Creating tables for BusProject
TABLES = {}
TABLES['station'] = (
    "CREATE TABLE `station` ("
    "  `id` int(11) NOT NULL,"
    "  `name` varchar(30) NOT NULL,"
    "  `address` varchar(30),"
    "  `longitude` decimal(11,8) NOT NULL,"
    "  `latitude` decimal(10,8) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ")")

TABLES['bus'] = (
    "CREATE TABLE `bus` ("
    "  `id` int(11) NOT NULL,"
    "  `capacity` int(3) NOT NULL,"
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
    "  CONSTRAINT fk_route_station_source_station_id FOREIGN KEY (source_station_id) REFERENCES station(id),"
    "  CONSTRAINT fk_route_station_destination_station_id FOREIGN KEY (destination_station_id) REFERENCES station(id), "
    "  CONSTRAINT fk_route_bus_bus_id FOREIGN KEY (bus_id) REFERENCES bus(id) "
    ")")

TABLES['schedule'] = (
    "CREATE TABLE `schedule` ("
    "  `id` int(11) NOT NULL,"
    "  `route_id` int(11) NOT NULL,"
    "  `departure_time` datetime NOT NULL,"
    "  `arrival_time` datetime NOT NULL,"
    "  `price` int(7) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  CONSTRAINT fk_schedule_route_route_id FOREIGN KEY (route_id) REFERENCES route(id)"
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
    "  `schedule_id` int(11) NOT NULL,"
    "  `passenger_id` int(11) NOT NULL,"
    "  PRIMARY KEY (`id`),"
    "  CONSTRAINT fk_ticket_schedule_schedule_id FOREIGN KEY (schedule_id) REFERENCES schedule(id),"
    "  CONSTRAINT fk_ticket_passenger_id FOREIGN KEY (passenger_id) REFERENCES passenger(id)"
    ")")

# prepare a cursor object using cursor() method
db=database_connector.connect_db()
cursor = db.cursor()
DB_NAME="busproject"
if db.database == DB_NAME:
    db.database = DB_NAME
else:
    database_connector.create_database(cursor,DB_NAME)
    db.database = DB_NAME

# loop through the tables to create each
for name, table_data in TABLES.iteritems():
   database_connector.create_table(name,table_data,cursor)

# disconnect from server
cursor.close()
db.close()


