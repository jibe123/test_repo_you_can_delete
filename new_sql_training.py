import mysql.connector
from sql_2 import UserSQL

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Zsynth91!',
    db='simple_library',
    autocommit=True
)
cursor=DB.cursor()

manager_of_table_user = UserSQL(cursor)
# create_table_user = manager_of_table_user.create_table_user()
add_user_aslan = manager_of_table_user.add_new_user("Sauron", "sauron@lotr.eu", "theringismine89")
# get_user_by_id1 = manager_of_table_user.get_user_by_id(2)
# delete_user = manager_of_table_user.delete_user_by_id(3)
# users = manager_of_table_user.get_all_users()
# update_user = manager_of_table_user.update_user_name_by_id(4, 'Milo')
manager_of_table_user.update_user_email_by_id(5, 'mess_mess@signal.com')
manager_of_table_user.update_user_password_by_id(4, 'milo works at spacex')