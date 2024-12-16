from pprint import pprint
from db import *
from pandas import *

xls= ExcelFile('org_struct.xlsx')
parse=xls.parse(xls.sheet_names[0])
dict_parse=parse.to_dict()
# pprint(dict_parse)
id_departament=[]
id_minidepartment=[]
id_manegment=[]

last_list = None

for i in range(0,170):
    org=dict_parse['Организация'][i]
    name = dict_parse["Сотрудник"][i]
    birthday = dict_parse["Дата рождения"][i]
    phone = dict_parse["Телефон рабочий"][i]
    kabinet = dict_parse["Кабинет"][i]
    email = dict_parse["Корпоративный email"][i]

    points = org.count('.')

    if points == 1:

        print(org, "департамент")

        id_dep = department_insert(i, name=org)
        id_departament.append(id_dep)

        last_list = id_departament

    elif points == 2:

        print(org, "минидепартамент")

        id_minidep = mini_department_insert(i, name=org, id_department=id_departament[-1])
        id_minidepartment.append(id_minidep)

        last_list = id_minidepartment

    elif points == 3:

        print(org, "менджмент")

        id_maneg = management_insert(i, name=org, id_mini_departament=id_minidepartment[-1])
        id_manegment.append(id_maneg)

        last_list = id_manegment

    elif points == 0:


        if last_list == id_departament:
            id_post = post_insert(i, name=org, id_department=id_departament[-1])

        elif last_list == id_minidepartment:
            id_post = post_insert(i, name=org, id_mini_departament=id_minidepartment[-1])

        elif last_list == id_manegment:
            id_post = post_insert(i, name=org, id_management=id_manegment[-1])

        user_insert(id=i, name=name, id_post=id_post, birthday=str(birthday), phonenumber=phone, room=kabinet, email=email, info="test info")

        print(org, "неизвестно")