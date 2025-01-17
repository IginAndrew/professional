import requests
from pprint import pprint


def data():
    url = "https://andrew79.pythonanywhere.com/d/python_request.zip"
    response = requests.get(url)
    with open("python_request.zip", "wb") as code:
        code.write(response.content)

#-------------------------------4 сессия-------------------------------

def info_user():
    url = "http://127.0.0.1:8000/user_work"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res

def info_news():
    url = "https://192.168.1.85:5000/swagger"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res

#-------------------5 сессия-------------------------------

def info_calendar():
    url = "http://127.0.0.1:8000/calendar"
    response = requests.get(url)
    dict_res = response.json()
    return dict_res




if __name__ == "__main__":
    pass
    data()
    # print(info_news())
    # print([i['date_training'] for i in info_calendar()])