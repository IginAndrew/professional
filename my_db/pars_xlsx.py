from pprint import pprint

from pandas import *

xls=ExcelFile('org_struct.xlsx')
df=xls.parse(xls.sheet_names[0])
dict_total=df.to_dict()

id_departaments=[]
id_minidepartaments=[]
id_managment=[]

last_list = None


for i in range(0,170):
    org=dict_total["Организация"][i]
    name=dict_total["Сотрудники"][i]
    birthday=dict_total["Дата рождения"][i]
    phone=dict_total["Телефон"][i]
    room=dict_total["Кабинет"][i]
    email=dict_total["Коорпоративный email"][i]
    points=org.count('.')
    if points == 1:

        id_dep =

    elif points == 2:
        pass
    elif points == 3:
        pass
    else:
