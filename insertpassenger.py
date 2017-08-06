from datetime import date, datetime, timedelta
import mysql.connector

db = mysql.connector.connect(user='root', password="Jeries", database='busproject')
cursor = db.cursor()
#date_of_birth=datetime(1994,8,10).strftime('%m/%d/%Y')

data_passenger=(500,'Jeries','Nassar','M',datetime(1994,8,10),'jeries.n94@hotmail.com', '0568648989' )
add_passenger="INSERT INTO passenger "\
               "VALUES (%s,%s,%s,%s,%s,%s,%s )"

cursor.execute(add_passenger,data_passenger)
db.commit()
cursor.close()
db.close()
