from pprint import pprint

import requests


def users_departament_req():
    url = "http://127.0.0.1:8000/users_departament"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


def users_minidepartament_req():
    url = "http://127.0.0.1:8000/users_minidepartament"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


def users_managment_req():
    url = "http://127.0.0.1:8000/users_management"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


def users_admin_departament_req(name):
    url = f"http://127.0.0.1:8000/users_admin_departament?name={name}"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


def select_mini_departament_all_req(name):
    url = f"http://127.0.0.1:8000/select_mini_departament_all?name={name}"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


def select_managment_all_req(name):
    url = f"http://127.0.0.1:8000/select_managment_all?name={name}"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res


if __name__ == "__main__":
    pprint(users_departament_req())
    pprint(users_admin_departament_req("1. Административный департамент"))
