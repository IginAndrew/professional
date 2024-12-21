import requests


def date():
    url = "https://andrew79.pythonanywhere.com/download/python_request.zip"
    response = requests.get(url)
    with open("python_request.zip", "wb") as code:
        code.write(response.content)

if __name__ == "__main__":
    date()