import sqlite3


def get_connection():
    try:
        con = sqlite3.connect('base.db')
        con.row_factory = sqlite3.Row
        print("Успешное подключение!")
        return con
    except Exception as e:
        print(f"Ошибка подключения: {e}")


def create_tables_department():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Department (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT NOT NULL UNIQUE
        );
        ''')
        con.commit()


def create_tables_mini_department():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Mini_department (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT UNIQUE,
            id_department INTEGER NOT NULL,
            FOREIGN KEY (id_department) REFERENCES Department(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION
        );
        ''')
        con.commit()


def create_tables_management():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Management (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT UNIQUE,
            id_mini_departament INTEGER NOT NULL,
            FOREIGN KEY (id_mini_departament) REFERENCES Mini_department(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION
        );
        ''')
        con.commit()


def create_tables_post():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Post (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT UNIQUE,
            id_department INTEGER,
            id_mini_departament INTEGER,
            id_management INTEGER,
            id_user INTEGER NOT NULL,
            FOREIGN KEY (id_department) REFERENCES Department(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION,
            FOREIGN KEY (id_mini_departament) REFERENCES Mini_department(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION,
            FOREIGN KEY (id_management) REFERENCES Management(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION
        );
        ''')
        con.commit()


def create_tables_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT NOT NULL,
            id_post INTEGER,
            birthday TEXT,
            phonenumber TEXT,
            room TEXT,
            email TEXT,
            info TEXT,
            FOREIGN KEY (id_post) REFERENCES Post(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION
        );
        ''')
        con.commit()


def create_tables_info_date():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Info_date (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            name TEXT
        );
        ''')
        con.commit()


def create_tables_id_info_date_id_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
        CREATE TABLE IF NOT EXISTS Id_info_date_id_user (
            id INTEGER NOT NULL UNIQUE PRIMARY KEY,
            id_info_date INTEGER,
            id_user INTEGER,
            id_date INTEGER,
            FOREIGN KEY (id_info_date) REFERENCES Info_date(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION,
            FOREIGN KEY (id_user) REFERENCES User(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION,
            FOREIGN KEY (id_date) REFERENCES Date(id)
            ON UPDATE NO ACTION ON DELETE NO ACTION
        );
        ''')
        con.commit()


def create_tables_helper():
    con = get_connection()
    with con:
        c = con.cursor()

        c.execute('''
                CREATE TABLE IF NOT EXISTS Helper (
                    id INTEGER NOT NULL UNIQUE PRIMARY KEY,
                    name TEXT
                );
                ''')
        con.commit()

def create_tables_id_helper_id_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS Id_helper_id_user (
                    id INTEGER NOT NULL UNIQUE PRIMARY KEY,
                    id_helper INTEGER,
                    id_user INTEGER,
                    FOREIGN KEY (id_helper) REFERENCES Helper(id)
                    ON UPDATE NO ACTION ON DELETE NO ACTION,
                    FOREIGN KEY (id_user) REFERENCES User(id)
                    ON UPDATE NO ACTION ON DELETE NO ACTION
                );
                ''')
        con.commit()

def create_tables_date():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute('''
                CREATE TABLE IF NOT EXISTS Date (
                    id INTEGER NOT NULL UNIQUE PRIMARY KEY,
                    date TEXT,
                    info TEXT
                );
                ''')
        con.commit()

# create_tables_department()
# create_tables_mini_department()
# create_tables_management()
# create_tables_post()
# create_tables_user()
# create_tables_info_date()
# create_tables_id_info_date_id_user()
# create_tables_helper()
# create_tables_id_helper_id_user()
# create_tables_date()