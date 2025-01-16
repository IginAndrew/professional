import sqlite3

def get_connection():
    c=sqlite3.connect('bd.db')
    c.row_factory=sqlite3.Row
    return c

def create_table_departament():
    c=get_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS Departament(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )''')
    c.close()

def insert_departament(name):
    con= get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Departament (name) values
              (?);
              """,
        (
            name,
        ),
    )
    con.commit()
    return c.lastrowid

def create_table_mini_departament():
    c=get_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS Mini_departament(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        departament_id INTEGER,
        FOREIGN KEY (departament_id) REFERENCES Departament(id)
    )''')
    c.close()

def insert_mini_departament(name, departament_id):
    con= get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Mini_departament (name, departament_id) values
              (?,?);
              """,
        (
            name, departament_id,
        ),
    )
    con.commit()
    return c.lastrowid

def create_table_managment():
    c=get_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS Managment(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mini_departament_id INTEGER,
        FOREIGN KEY (mini_departament_id) REFERENCES Mini_departament(id)
    )''')
    c.close()

def insert_managment(name, mini_departament_id):
    con= get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Managment (name, mini_departament_id) values
              (?,?);
              """,
        (
            name, mini_departament_id,
        ),
    )
    con.commit()
    return c.lastrowid

def create_post():
    c=get_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS Post(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        id_departament INTEGER,
        id_mini_departament INTEGER,
        id_management INTEGER,
        FOREIGN KEY (id_departament) REFERENCES Departament(id),
        FOREIGN KEY (id_mini_departament) REFERENCES Mini_departament(id),
        FOREIGN KEY (id_management) REFERENCES Management(id)
    )''')
    c.close()

def insert_post(name, id_department=0, id_mini_departament=0, id_management=0):
    con= get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Post (name, id_departament, id_mini_departament, id_management) values
              (?,?,?,?);
              """,
        (
            name, id_department, id_mini_departament, id_management,
        ),
    )
    con.commit()
    return c.lastrowid

def create_user():
    c=get_connection()
    c.execute('''CREATE TABLE IF NOT EXISTS User(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        birthday TEXT,
        phone TEXT,
        room TEXT,
        info TEXT,
        id_post INTEGER,
        FOREIGN KEY (id_post) REFERENCES Post(id)
    )''')
    c.close()

def insert_user(name, email, birthday, phone, room, info, id_post):
    con= get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO User (name, email, birthday, phone, room, info, id_post) values
              (?,?,?,?,?,?,?);
              """,
        (
            name, email, birthday, phone, room, info, id_post,
        ),
    )
    con.commit()
    return c.lastrowid

if __name__ == '__main__':
    create_table_departament()
    create_table_mini_departament()
    create_table_managment()
    create_post()
    create_user()

