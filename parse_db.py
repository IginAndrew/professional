from pprint import pprint

from pandas import *

from db import *

xls=ExcelFile('users.xlsx')
df = xls.parse(xls.sheet_names[0])
dict_total = df.to_dict()
dict_total_my = {}
pprint(dict_total)

id_deps = []
id_minideps= []
id_mng = []

last_id = None

for i in range(0, 170):
    org = dict_total["Организация"][i]
    name = dict_total["Сотрудник"][i]
    birthday = dict_total["Дата рождения"][i]
    phone = dict_total["Телефон рабочий"][i]
    kabinet = dict_total["Кабинет"][i]
    email = dict_total["Корпоративный email"][i]
    my_dict_value = {
        "Сотрудник": name,
        "Дата рождения": str(birthday),
        "Телефон рабочий": phone,
        "Кабинет": kabinet,
        "Корпоративный email": email,
    }

    points=org.count('.')


    if points == 1:
        id_dep = insert_departament(org)
        id_deps.append(id_dep)
        last_id = id_dep
    elif points == 2:
        id_mini_dep = insert_mini_departament(org,id_deps[-1])
        id_minideps.append(id_mini_dep)
        last_id = id_mini_dep
    elif points == 3:
        id_mang = insert_managment(org,id_minideps[-1])
        id_mng.append(id_mang)
        last_id = id_mang
    else:
        if last_id == id_dep:
            post_id = insert_post(name=org,id_department=last_id)
        elif last_id == id_mini_dep:
            post_id = insert_post(name=org,id_mini_departament=last_id)
        elif last_id == id_mang:
            post_id = insert_post(name=org,id_management=last_id)

        insert_user(name=name,email=email,birthday=str(birthday),phone=phone,room=kabinet,info='test',id_post=post_id)



