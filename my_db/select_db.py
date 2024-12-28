import sqlite3

from my_db.db import get_connection

def select_user_management():
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
           SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Management.name as  management_name, User.info
           FROM User
            JOIN Post ON User.id_post = Post.id
            JOIN Management ON Post.id_management = Management.id
            WHERE Post.id_management IN (SELECT id FROM Management) 
            ''')
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def select_user_department():
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
           SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Department.name as  department_name, User.info
           FROM User
            JOIN Post ON User.id_post = Post.id
            JOIN Department ON Post.id_department = Department.id
            WHERE Post.id_department IN (SELECT id FROM Department) 
            ''')
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def select_user_mini_department():
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
          SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Mini_department.name as  mini_department_name, User.info
           FROM User
            JOIN Post ON User.id_post = Post.id
            JOIN Mini_department ON Post.id_mini_departament = Mini_department.id
            WHERE Post.id_mini_departament IN (SELECT id FROM Mini_department) 
            ''')
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def select_user_admin_department(name):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
          SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Department.name as department_name, User.info FROM User
JOIN Post ON User.id_post = Post.id
JOIN Department ON Post.id_department = Department.id
WHERE Department.name = ?
UNION
SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Mini_department.name as  mini_department_name, User.info FROM User
JOIN Post ON User.id_post = Post.id
JOIN Mini_department ON Post.id_mini_departament = Mini_department.id
JOIN Department ON Mini_department.id_department = Department.id
WHERE Department.name = ?
UNION
SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Management.name as  management_name, User.info FROM User
JOIN Post ON User.id_post = Post.id
JOIN Management ON Post.id_management = Management.id
JOIN Mini_department ON Management.id_mini_departament = Mini_department.id
JOIN Department ON Mini_department.id_department = Department.id
WHERE Department.name = ? 
            ''', (name, name, name,))
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def select_user_admin_mini_department(name):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Mini_department.name as  mini_department_name, User.info FROM User
JOIN Post ON User.id_post = Post.id
JOIN Mini_department ON Post.id_mini_departament = Mini_department.id
JOIN Department ON Mini_department.id_department = Department.id
WHERE Department.name = 'Административный департамент' AND Mini_department.name = ?
            ''', (name,))
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)

def select_user_management_button(name):
    try:
        con = get_connection()
        with con:
            c = con.cursor()
            res = c.execute('''
SELECT User.name, User.email, User.phonenumber, Post.name as post_name, 
           Management.name as  management_name, User.info FROM User
JOIN Post ON User.id_post = Post.id
JOIN Management ON Post.id_management = Management.id
JOIN Mini_department ON Management.id_mini_departament = Mini_department.id
JOIN Department ON Mini_department.id_department = Department.id
WHERE Management.name = ?
            ''', (name,))
            res = res.fetchall()
        # print(res)
        if not res:
            print("не найден")
            return False
        return res
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)


if __name__ == '__main__':
    print([i['name'] for i in select_user_management()])