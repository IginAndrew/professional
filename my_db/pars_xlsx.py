from pprint import pprint
from db import *
from pandas import *

xls=ExcelFile('org_struct.xlsx')
df=xls.parse(xls.sheet_names[0])
dict_total=df.to_dict()

id_departaments=[]
id_minidepartaments=[]
id_managments=[]

last_list = None

for i in range(0,170):
    org=dict_total["Организация"][i]
    name=dict_total["Сотрудники"][i]
    birthday=dict_total["Дата рождения"][i]
    phone=dict_total["Телефон"][i]
    room=dict_total["Кабинет"][i]
    email=dict_total["Корпоративный email"][i]

    points=org.count('.')

    if points == 1:

        id_dep = department_insert(i, name=org)
        id_departaments.append(id_dep)

        last_list = id_departaments

    elif points == 2:

        id_minidep = minidepartment_insert(i, name=org, id_departament=id_departaments[-1])
        id_minidepartaments.append(id_minidep)

        last_list = id_minidepartaments

    elif points == 3:

        id_mang= managmente_insert(i, name=org, id_mini_departament=id_minidepartaments[-1])
        id_managments.append(id_mang)

        last_list = id_managments

    else:

        if last_list == id_departaments:
            ip_post= post_insert(i, name=org, id_departament=id_departaments[-1])
        elif last_list == id_minidepartaments:
            ip_post= post_insert(i, name=org,id_mini_departament=id_minidepartaments[-1])
        elif last_list == id_managments:
            ip_post= post_insert(i, name=org,id_menegmante=id_managments[-1])

        user_insert(i, name=name, birthday=str(birthday), phone=phone, room=room, email=email, id_post=ip_post, info="test")

