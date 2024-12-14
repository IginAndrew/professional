import sqlite3


def get_connection():
    try:
        con = sqlite3.connect("base.db")
        con.row_factory = sqlite3.Row
        print("Успешное подключение!")
        return con
    except Exception as e:
        print(f"Ошибка подключения: {e}")


def create_tables_department():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Department (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            UNIQUE ("name") ON CONFLICT IGNORE
        );
        """
        )
        con.commit()


def department_insert(id, name):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
        c.execute(
            """
                  INSERT INTO Department (id, name) values
                  (?,?);
                  """,
            (
                id,
                name,
            ),
        )
        con.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе sql department_insert", error)


# ----------------------------------------------------------------------------------------------------


def create_tables_mini_department():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Mini_department (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT,
            id_department INTEGER NOT NULL,
            FOREIGN KEY (id_department) REFERENCES Department(id)
            UNIQUE ("name") ON CONFLICT IGNORE
        );
        """
        )
        con.commit()


def mini_department_insert(id, name, id_department):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
        c.execute(
            """
                  INSERT INTO Mini_department (id, name, id_department) values
                  (?,?,?);
                  """,
            (
                id,
                name,
                id_department,
            ),
        )
        con.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе sql mini_department_insert", error)


# -----------------------------------------------------------------------------


def create_tables_management():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Management (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT,
            id_mini_departament INTEGER NOT NULL,
            FOREIGN KEY (id_mini_departament) REFERENCES Mini_department(id)
            UNIQUE ("name") ON CONFLICT IGNORE
        );
        """
        )
        con.commit()


def management_insert(id, name, id_mini_departament):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
        c.execute(
            """
                  INSERT INTO Management (id, name, id_mini_departament) values
                  (?,?,?);
                  """,
            (
                id,
                name,
                id_mini_departament,
            ),
        )
        con.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе sql management_insert", error)


# -------------------------------------
def create_tables_post():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Post (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT,
            id_department INTEGER,
            id_mini_departament INTEGER,
            id_management INTEGER,
            FOREIGN KEY (id_department) REFERENCES Department(id),
            FOREIGN KEY (id_mini_departament) REFERENCES Mini_department(id),
            FOREIGN KEY (id_management) REFERENCES Management(id)
        );
        """
        )
        con.commit()


def post_insert(id, name, id_department=0, id_mini_departament=0, id_management=0):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
        c.execute(
            """
                  INSERT INTO Post (id, name, id_department, id_mini_departament, id_management) values
                  (?,?,?,?,?);
                  """,
            (
                id,
                name,
                id_department,
                id_mini_departament,
                id_management,
            ),
        )
        con.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе sql post_insert", error)


# ----------------------------------------------------------------------


def create_tables_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            id_post INTEGER,
            birthday TEXT,
            phonenumber TEXT,
            room TEXT,
            email TEXT,
            info TEXT,
            FOREIGN KEY (id_post) REFERENCES Post(id)
        );
        """
        )
        con.commit()


def user_insert(
    id, name, id_post, birthday, phonenumber, room, email, info="test info"
):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
        c.execute(
            """
                  INSERT INTO User (id, name, id_post, birthday, phonenumber, room, email, info) values
                  (?,?,?,?,?,?,?,?);
                  """,
            (
                id,
                name,
                id_post,
                birthday,
                phonenumber,
                room,
                email,
                info,
            ),
        )
        con.commit()
    except sqlite3.Error as error:
        print("Ошибка при работе sql user_insert", error)


# ------------------------------------
def create_tables_info_date():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Info_date (
            id INTEGER NOT NULL PRIMARY KEY,
            name TEXT
        );
        """
        )
        con.commit()


def create_tables_id_info_date_id_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
        CREATE TABLE IF NOT EXISTS Id_info_date_id_user (
            id INTEGER NOT NULL PRIMARY KEY,
            id_info_date INTEGER,
            id_user INTEGER,
            id_date INTEGER,
            FOREIGN KEY (id_info_date) REFERENCES Info_date(id),
            FOREIGN KEY (id_user) REFERENCES User(id),
            FOREIGN KEY (id_date) REFERENCES Date(id)
        );
        """
        )
        con.commit()


def create_tables_helper():
    con = get_connection()
    with con:
        c = con.cursor()

        c.execute(
            """
                CREATE TABLE IF NOT EXISTS Helper (
                    id INTEGER NOT NULL PRIMARY KEY,
                    name TEXT
                );
                """
        )
        con.commit()


def create_tables_id_helper_id_user():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS Id_helper_id_user (
                    id INTEGER NOT NULL PRIMARY KEY,
                    id_helper INTEGER,
                    id_user INTEGER,
                    FOREIGN KEY (id_helper) REFERENCES Helper(id),
                    FOREIGN KEY (id_user) REFERENCES User(id)
                );
                """
        )
        con.commit()


def create_tables_date():
    con = get_connection()
    with con:
        c = con.cursor()
        c.execute(
            """
                CREATE TABLE IF NOT EXISTS Date (
                    id INTEGER NOT NULL PRIMARY KEY,
                    date TEXT,
                    info TEXT
                );
                """
        )
        con.commit()


if __name__ == "__main__":
    pass
    create_tables_department()
    create_tables_mini_department()
    create_tables_management()
    create_tables_post()
    create_tables_user()
    create_tables_info_date()
    create_tables_id_info_date_id_user()
    create_tables_helper()
    create_tables_id_helper_id_user()
    create_tables_date()
