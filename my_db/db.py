import sqlite3

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



if __name__ == '__main__':
    create_departament()
    create_minidepartament()
    create_menegmante()
    create_post()
    create_user()