import re
from pprint import pprint

from pandas import *

from my_db.db import department_insert, mini_department_insert, management_insert, post_insert, user_insert

xls = ExcelFile("my_db/org_struct.xlsx")
df = xls.parse(xls.sheet_names[0])
dict_total = df.to_dict()


dict_total_my = {}

one = []
one_id = []
two = []
two_id = []
three = []
three_id = []
post_id = []
str_key = ""

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
    exemple_one = re.findall(r"^\d{,2}\.\s\D+", org)
    exemple_two = re.findall(r"^\d{,2}\.\d{,1}\.\s\D+", org)
    exemple_free = re.findall(r"^\d{,2}\.\d{,1}\.\d{,1}\.\s\D+", org)

    if exemple_one:
        one_re = exemple_one[0][str(exemple_one).index(" ") - 1 :]
        one.append(one_re)
        one_id.append(i + 1)
        dict_total_my[one[-1]] = {}
        str_key = "one"
        department_insert(one_id[-1], one[-1])#db

    elif exemple_two:
        two_re = exemple_two[-1][str(exemple_two).index(" ") - 1 :]
        two.append(two_re)
        two_id.append(i + 1)
        dict_total_my[one[-1]][two[-1]] = {}
        str_key = "two"
        mini_department_insert(two_id[-1], two[-1], one_id[-1])#db

    elif exemple_free:
        three_re = exemple_free[0][str(exemple_free).index(" ") - 1 :]
        three.append(three_re)
        three_id.append(i + 1)
        dict_total_my[one[-1]][two[-1]][three[-1]] = {}
        str_key = "three"
        management_insert(three_id[-1], three[-1], two_id[-1])#db

    else:
        if str_key == "one":
            if org not in dict_total_my[one[-1]].keys():
                dict_total_my[one[-1]][org] = [my_dict_value]
                post_id.append(i + 1)
                post_insert(id=post_id[-1], name=org, id_department=one_id[-1])#db
            else:
                dict_total_my[one[-1]][org] += [my_dict_value]

        elif str_key == "two":
            if org not in dict_total_my[one[-1]][two[-1]].keys():
                dict_total_my[one[-1]][two[-1]][org] = [my_dict_value]
                post_id.append(i + 1)
                post_insert(
                    id=post_id[-1],
                    name=org,
                    id_mini_departament=two_id[-1],
                )#db

            else:
                dict_total_my[one[-1]][two[-1]][org] += [my_dict_value]

        elif str_key == "three":
            if org not in dict_total_my[one[-1]][two[-1]][three[-1]].keys():
                dict_total_my[one[-1]][two[-1]][three[-1]][org] = [my_dict_value]
                post_id.append(i + 1)
                post_insert(id=post_id[-1], name=org, id_management=three_id[-1])#db

            else:
                dict_total_my[one[-1]][two[-1]][three[-1]][org] += [my_dict_value]

        user_insert(
            id=i + 1,
            name=name,
            id_post=post_id[-1],
            birthday=str(birthday),
            phonenumber=str(phone),
            room=str(kabinet),
            email=email,
        )#db


pprint(dict_total_my)
