import sqlite3


def get_connection():
    c = sqlite3.connect("bd.db")
    c.row_factory = sqlite3.Row
    return c


def create_table_departament():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Departament(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )"""
    )
    c.close()


def insert_departament(name):
    con = get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Departament (name) values
              (?);
              """,
        (name,),
    )
    con.commit()
    return c.lastrowid


def create_table_mini_departament():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Mini_departament(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        departament_id INTEGER,
        FOREIGN KEY (departament_id) REFERENCES Departament(id)
    )"""
    )
    c.close()


def insert_mini_departament(name, departament_id):
    con = get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Mini_departament (name, departament_id) values
              (?,?);
              """,
        (
            name,
            departament_id,
        ),
    )
    con.commit()
    return c.lastrowid


def create_table_managment():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Managment(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mini_departament_id INTEGER,
        FOREIGN KEY (mini_departament_id) REFERENCES Mini_departament(id)
    )"""
    )
    c.close()


def insert_managment(name, mini_departament_id):
    con = get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Managment (name, mini_departament_id) values
              (?,?);
              """,
        (
            name,
            mini_departament_id,
        ),
    )
    con.commit()
    return c.lastrowid


def create_post():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Post(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        id_departament INTEGER,
        id_mini_departament INTEGER,
        id_management INTEGER,
        FOREIGN KEY (id_departament) REFERENCES Departament(id),
        FOREIGN KEY (id_mini_departament) REFERENCES Mini_departament(id),
        FOREIGN KEY (id_management) REFERENCES Management(id)
    )"""
    )
    c.close()


def insert_post(name, id_department=0, id_mini_departament=0, id_management=0):
    con = get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO Post (name, id_departament, id_mini_departament, id_management) values
              (?,?,?,?);
              """,
        (
            name,
            id_department,
            id_mini_departament,
            id_management,
        ),
    )
    con.commit()
    return c.lastrowid


def create_user():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS User(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        birthday TEXT,
        phone TEXT,
        room TEXT,
        info TEXT,
        id_post INTEGER,
        FOREIGN KEY (id_post) REFERENCES Post(id)
    )"""
    )
    c.close()


def insert_user(name, email, birthday, phone, room, info, id_post):
    con = get_connection()
    with con:
        c = con.cursor()
    c.execute(
        """
              INSERT INTO User (name, email, birthday, phone, room, info, id_post) values
              (?,?,?,?,?,?,?);
              """,
        (
            name,
            email,
            birthday,
            phone,
            room,
            info,
            id_post,
        ),
    )
    con.commit()
    return c.lastrowid


# -------------------------------------


def create_helper():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Helper(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )"""
    )
    c.close()


def create_id_user_id_helper():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Id_user_id_helper(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_helper INTEGER,
        FOREIGN KEY (id_user) REFERENCES User(id),
        FOREIGN KEY (id_helper) REFERENCES Helper(id)
    )"""
    )
    c.close()


def create_calendar():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Calendar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT
    )"""
    )
    c.close()


def create_id_user_id_calendar():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Id_user_id_calendar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_user INTEGER,
        id_calendar INTEGER,
        FOREIGN KEY (id_user) REFERENCES User(id),
        FOREIGN KEY (id_calendar) REFERENCES Calendar(id)
    )"""
    )
    c.close()


def create_out():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Out(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_out TEXT,
        info TEXT,
        id_calendar INTEGER,
        FOREIGN KEY (id_calendar) REFERENCES Calendar(id)
    )"""
    )
    c.close()


def create_training():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Training(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_training TEXT,
        info TEXT,
        id_calendar INTEGER,
        FOREIGN KEY (id_calendar) REFERENCES Calendar(id)
    )"""
    )
    c.close()


def create_event():
    c = get_connection()
    c.execute(
        """CREATE TABLE IF NOT EXISTS Event(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_event TEXT,
        type_event TEXT,
        status_event BOOLEAN,
        time_event TEXT,
        responsible_person TEXT,
        info TEXT,
        id_calendar INTEGER,
        FOREIGN KEY (id_calendar) REFERENCES Calendar(id)
    )"""
    )
    c.close()


def select_departament():
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
               SELECT User.name, User.email, User.phone, Post.name as post_name, Departament.name as departament_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Departament ON Post.id_departament = Departament.id
                WHERE Post.id_departament IN (SELECT id FROM Departament) 
                """
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


def select_mini_departament():
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
               SELECT User.name, User.email, User.phone, Post.name as post_name, Mini_departament.name as mini_departament_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Mini_departament ON Post.id_mini_departament = Mini_departament.id
                WHERE Post.id_mini_departament IN (SELECT id FROM Mini_departament) 
                """
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


def select_managment():
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
               SELECT User.name, User.email, User.phone, Post.name as post_name, Managment.name as managment_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Managment ON Post.id_management = Managment.id
                WHERE Post.id_management IN (SELECT id FROM Managment) 
                """
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


def select_admin_departament(name):
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
              SELECT User.name, User.email, User.phone, Post.name as post_name, Departament.name as departament_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Departament ON Post.id_departament = Departament.id
                WHERE Departament.name = ?
                UNION
                SELECT User.name, User.email, User.phone, Post.name as post_name, Mini_departament.name as mini_departament_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Mini_departament ON Post.id_mini_departament = Mini_departament.id
                JOIn Departament ON Mini_departament.departament_id = Departament.id
                WHERE Departament.name = ?
                UNION
                SELECT User.name, User.email, User.phone, Post.name as post_name, Managment.name as managment_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Managment ON Post.id_management = Managment.id
                JOIN Mini_departament ON Managment.mini_departament_id = Mini_departament.id
                JOIN Departament ON Mini_departament.departament_id = Departament.id
                WHERE Departament.name = ?
                """,
            (
                name,
                name,
                name,
            ),
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


def select_mini_departament_all(name):
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
                SELECT User.name, User.email, User.phone, Post.name as post_name, Mini_departament.name as mini_departament_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Mini_departament ON Post.id_mini_departament = Mini_departament.id
                WHERE Mini_departament.name = ?
                UNION
                SELECT User.name, User.email, User.phone, Post.name as post_name, Managment.name as managment_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Managment ON Post.id_management = Managment.id
                JOIN Mini_departament ON Managment.mini_departament_id = Mini_departament.id
                WHERE Mini_departament.name = ?
                """,
            (
                name,
                name,
            ),
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


def select_managment_all(name):
    con = get_connection()
    with con:
        c = con.cursor()
        res = c.execute(
            """
                SELECT User.name, User.email, User.phone, Post.name as post_name, Managment.name as managment_name, User.info FROM User
                JOIN Post ON User.id_post = Post.id
                JOIN Managment ON Post.id_management = Managment.id
                WHERE Managment.name = ?
                """,
            (name,),
        )
        res = res.fetchall()
    if not res:
        print("не найден")
        return False
    return res


if __name__ == "__main__":
    # create_table_departament()
    # create_table_mini_departament()
    # create_table_managment()
    # create_post()
    # create_user()
    # create_helper()
    # create_id_user_id_helper()
    # create_calendar()
    # create_id_user_id_calendar()
    # create_out()
    # create_training()
    # create_event()
    print(select_admin_departament("1. Административный департамент"))
