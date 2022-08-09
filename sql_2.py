class UserSQL:
    def __init__(self, cursor_param):
        self.cursor = cursor_param

    def create_table_user(self):
        query = """
        CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
        );
        """
        self.cursor.execute(query)

    def add_new_user(self, name, email, password):
        query = f"INSERT INTO user (name, email, password) VALUES ('{name}', '{email}', '{password}');"
        self.cursor.execute(query)

    def get_user_by_id(self, id):
        query = f"SELECT * FROM user WHERE id = {id};"
        self.cursor.execute(query)
        print(self.cursor.fetchone())

    def get_all_users(self):
        query = f"SELECT * FROM user;"
        self.cursor.execute(query)
        print(self.cursor.fetchall())

    def delete_user_by_id(self, id):
        query = f"DELETE FROM user WHERE id = {id};"
        self.cursor.execute(query)
        print(f"User with id: {id} deleted!")

    def update_user_name_by_id(self, id, new_name):
        query = f"UPDATE user SET name='{new_name}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"User with id: {id} was updated!")

    def update_user_email_by_id(self, id, new_email):
        query = f"UPDATE user SET email='{new_email}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"Email of user with id: {id} was updated!")

    def update_user_password_by_id(self, id, new_password):
        query = f"UPDATE user SET password='{new_password}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"Password of user with id: {id} was updated!")