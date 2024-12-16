from pprint import pprint

from pandas import *

xls= ExcelFile('org_struct.xlsx')
parse=xls.parse(xls.sheet_names[0])
dict_parse=parse.to_dict()
# pprint(dict_parse)
id_departament=[]

for i in range(0,170):
    org=dict_parse['Организация'][i]

    points = org.count('.')

    if points == 1:

        print(org, "департамент")

    elif points == 2:

        print(org, "минидепартамент")

    elif points == 3:

        print(org, "менджмент")

    elif points == 0:

        print(org, "неизвестно")