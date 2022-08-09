import mysql.connector
DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Zsynth91!',
    db='test_db'
)
cursor = DB.cursor()
# cursor.execute("SELECT * FROM table_name;")
# print(cursor.fetchall())
# print(cursor.fetchone())
while True:
    answer_to_exit = input('Do you want to exit?\n Please enter yes (y) or no (n)\n Your answer: ').lower()
    if answer_to_exit in ['yes', 'y']:
        break
    name = input('name: ')
    email = input('email: ')
    password = input('password: ')
    query = f"INSERT INTO user (name, email, password)" \
            f"VALUES" \
            f"('{name}', '{email}', '{password}');"
    cursor.execute(query)
    DB.commit()

cursor.execute('SELECT * FROM user;')
print(cursor.fetchall())