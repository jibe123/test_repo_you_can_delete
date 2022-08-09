class AuthorSQL:
    def __init__(self, cursor_param):
        self.cursor = cursor_param

    def create_table_author(self):
        query = """
        CREATE TABLE author (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        lastname VARCHAR(100) NOT NULL,
        country VARCHAR(100) NOT NULL
        );
        """
        self.cursor.execute(query)

    def add_new_author(self, name, lastname, country):
        query = f"INSERT INTO author (name, lastname, country) VALUES ('{name}', '{lastname}', '{country}');"
        self.cursor.execute(query)

    def get_author_by_id(self, id):
        query = f"SELECT * FROM author WHERE id = {id};"
        self.cursor.execute(query)
        print(self.cursor.fetchone())

    def get_all_authors(self):
        query = f"SELECT * FROM author;"
        self.cursor.execute(query)
        print(self.cursor.fetchall())

    def delete_author_by_id(self, id):
        query = f"DELETE FROM author WHERE id = {id};"
        self.cursor.execute(query)
        print(f"Author with id: {id} deleted!")

    def update_author_name_by_id(self, id, new_name):
        query = f"UPDATE author SET name='{new_name}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"Author with id: {id} was updated!")

    def update_author_lastname_by_id(self, id, new_lastname):
        query = f"UPDATE author SET lastname='{new_lastname}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"Lastname of author with id: {id} was updated!")

    def update_author_country_by_id(self, id, new_country):
        query = f"UPDATE author SET country='{new_country}' WHERE id={id};"
        self.cursor.execute(query)
        print(f"Password of user with id: {id} was updated!")