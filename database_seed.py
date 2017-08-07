from datetime import datetime
import database_connector
#date_of_birth=datetime(1994,8,10).strftime('%m/%d/%Y')



def insert_passenger(cursor):
    print "Please Enter data for new passenger:"
    id = raw_input("\nPlease enter ID:")
    first_name = raw_input("\nPlease enter your first name:")
    if(len(first_name)>10):
        first_name=first_name[:10]
    last_name = raw_input("\nPlease enter your last name:")
    if (len(last_name) > 15):
        last_name=last_name[:15]
    gender = raw_input("\nPlease enter your gender: (M or F)")
    gender.upper()
    while gender !='M' and gender !='F':
        gender = raw_input("\nPlease enter your gender:( M or F)")
        gender.upper()
    date_of_birth_correct=1
    while date_of_birth_correct==1:
        try:
            date_of_birth = datetime.strptime(raw_input("\nPlease enter your date of birth: <YY/MM/DD>"), '%Y/%m/%d')
            date_of_birth_correct=0
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY/MM/DD")
    email = raw_input("\nPlease enter your email:")
    if (len(email) > 25):
        email = email[:25]
    phone = raw_input("\nPlease enter your phone number:")
    while phone.isdigit() != True:
        phone = raw_input("\nPlease enter your phone number:(only digits)")
    if (len(phone) > 15):
        phone = phone[:15]
    data_passenger = (id, first_name, last_name, gender, date_of_birth, email, phone)
    database_connector.insert_passenger(cursor,data_passenger)


def show_menu():
    db = database_connector.connect_db()
    cursor = db.cursor()
    user_in='0'
    while user_in!='2':
        user_in=raw_input("1. Enter new passenger\n "
                "2.Exit\n"
                " Enter your choice:")
        if (user_in=='1'):
            insert_passenger(cursor)
            db.commit()
            cursor.close()
            db.close()


show_menu()

# data_passenger=(500,'Jeries','Nassar','M',datetime(1994,8,10),'jeries.n94@hotmail.com', '0568648989' )

