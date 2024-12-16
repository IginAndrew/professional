import sqlite3
from logging import lastResort


def getconnection():
    con=sqlite3.connect('base.db')
    con.row_factory=sqlite3.Row
    print('connected')
    return con

def create_departament():
    con=getconnection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Departament(
                id INTEGER PRIMARY KEY,
                name TEXT
        )
        ''')
        con.commit()

def create_minidepartament():
    con=getconnection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Mini_departament(
                id INTEGER PRIMARY KEY,
                name TEXT,
                id_departament INTEGER,
                FOREIGN KEY (id_departament) REFERENCES Departament(id)
        )
        ''')
        con.commit()

def create_menegmante():
    con=getconnection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Menegmante(
                id INTEGER PRIMARY KEY,
                name TEXT,
                id_mini_departament INTEGER,
                FOREIGN KEY (id_mini_departament) REFERENCES Mini_departament(id)
        )
        ''')
        con.commit()

def create_post():
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS Post(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    id_departament INTEGER,
                    id_mini_departament INTEGER,
                    id_menegmante INTEGER,
                    FOREIGN KEY (id_menegmante) REFERENCES Menegmante(id)
            )
            ''')
        con.commit()

def create_user():
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS User(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    birthday TEXT,
                    phone TEXT,
                    room TEXT,
                    email TEXT,
                    info TEXT,
                    id_post INTEGER,
                    FOREIGN KEY (id_post) REFERENCES Post(id)
                    
            )
            ''')
        con.commit()

def department_insert(id, name):
        con = getconnection()
        with con:
            c = con.cursor()
            c.execute(
                """
                      INSERT INTO Departament (id, name) values
                      (?,?)
                      """,
                (
                    id,
                    name,
                ),
            )
            con.commit()
        return c.lastrowid


def minidepartment_insert(id, name, id_departament):
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute(
            """
                  INSERT INTO Mini_departament (id, name, id_departament) values
                  (?,?);
                  """,
            (
                id,
                name,
                id_departament,
            ),
        )
        con.commit()
    return c.lastrowid

def managmente_insert(id, name, id_minidepartament):
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute(
            """
                  INSERT INTO Menegmante (id, name, id_minidepartament) values
                  (?,?);
                  """,
            (
                id,
                name,
                id_minidepartament,
            ),
        )
        con.commit()


def post_insert(id, name, id_departament=0, id_mini_departament=0, id_menegmante=0):
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute(
            """
                  INSERT INTO Menegmante (id, name, id_departament, id_mini_departament, id_menegmante) values
                  (?,?,?,?,?);
                  """,
            (
                id,
                name,
                id_departament,
                id_mini_departament,
                id_menegmante,
            ),
        )
        con.commit()
    print(c.lastrowid)
    return c.lastrowid

def user_insert(id,name, birthday,phone,room,email,info,id_post):
    con = getconnection()
    with con:
        c = con.cursor()
        c.execute(
            """
                  INSERT INTO User(id,name,birthday,phone,room,email,info,id_post) values
                  (?,?,?,?,?,?,?,?);
                  """,
            (
                id,
                name,
                birthday,
                phone,
                room,
                email,
                info,
                id_post,
            ),
        )
        con.commit()

if __name__ == '__main__':
    # create_departament()
    # create_minidepartament()
    # create_menegmante()
    # create_post()
    # create_user()
    department_insert(1, 'test')