import re
from pprint import pprint

from pandas import *


xls = ExcelFile("org_struct.xlsx")
df = xls.parse(xls.sheet_names[0])
dict_total = df.to_dict()


dict_total_my = {}

one = []
two = []
three = []
str_key = ''

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

    # print(exemple_one)

    if exemple_one:
        one_re = exemple_one[0][str(exemple_one).index(" ")-1:]
        one.append(one_re)
        dict_total_my[one[-1]] = {}
        str_key = 'one'

    elif exemple_two:
        two_re = exemple_two[-1][str(exemple_two).index(" ")-1:]
        two.append(two_re)
        dict_total_my[one[-1]][two[-1]] = {}
        str_key = 'two'

    elif exemple_free:
        three_re = exemple_free[0][str(exemple_free).index(" ")-1:]
        three.append(three_re)
        dict_total_my[one[-1]][two[-1]][three[-1]] = {}
        str_key = 'three'

    else:
        if str_key == 'one':
            if org not in dict_total_my[one[-1]].keys():
                dict_total_my[one[-1]][org] = [my_dict_value]
            else:
                dict_total_my[one[-1]][org] += [my_dict_value]
        elif str_key == 'two':
            if org not in dict_total_my[one[-1]][two[-1]].keys():
                dict_total_my[one[-1]][two[-1]][org] = [my_dict_value]
            else:
                dict_total_my[one[-1]][two[-1]][org] += [my_dict_value]
        elif str_key == 'three':
            if org not in dict_total_my[one[-1]][two[-1]][three[-1]].keys():
                dict_total_my[one[-1]][two[-1]][three[-1]][org] = [my_dict_value]
            else:
                dict_total_my[one[-1]][two[-1]][three[-1]][org] += [my_dict_value]

pprint(dict_total_my)

