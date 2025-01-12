import flet as ft
import datetime
from datetime import date

from CustomCalendar import CustomCalendar
from my_db.select_db import select_user
from request_file import info_user


def card(name: str, email: str, phonenumber: str, post_name: str, birthday: str):
    c = ft.Card(
        ft.Column(
            [
                ft.Text(name, style=ft.TextStyle(color="white", size=15)),
                ft.Text(post_name, style=ft.TextStyle(color="white", size=10)),
                ft.Text(email, style=ft.TextStyle(color="white", size=10)),
                ft.Text(phonenumber, style=ft.TextStyle(color="white", size=10)),
                ft.Text(
                    birthday[: birthday.index(" ")],
                    style=ft.TextStyle(color="white", size=10),
                ),
            ],
        ),
        color="green",
    )

    return c


def card_news(name: str, date: str, text: str):
    c = ft.Card(
        ft.Column(
            [
                ft.Text(name, style=ft.TextStyle(color="white", size=15)),
                ft.Text(text, style=ft.TextStyle(color="white", size=10)),
                ft.Text(date, style=ft.TextStyle(color="white", size=10)),
                ft.Button(text="добавить в календарь"),
            ],
        ),
        color="green",
    )

    return c


def card_big_news(name: str, date: str, text: str):
    c = ft.Card(
        ft.Column(
            [
                ft.Text(name, style=ft.TextStyle(color="white", size=15)),
                ft.Text(text, style=ft.TextStyle(color="white", size=10)),
                ft.Text(date, style=ft.TextStyle(color="white", size=10)),
            ],
        ),
        color="green",
    )

    return c


card_total_user = [
    card(
        name=i["name"],
        email=i["email"],
        phonenumber=i["phonenumber"],
        post_name=i["post_name"],
        birthday=i["birthday"],
    )
    for i in select_user()
]  # функция из request_file.py которая работает с fastapi

card_total_news = [
    card_news(
        "Общее совещание в актовом зале",
        "26.05.2024",
        "Все сотрудника отдела 'Администраторы' собираемся",
    )
    for _ in range(10)
]  # изменить на внешний API


card_total_big_news = [
    ft.Container(
        alignment=ft.alignment.bottom_left,
        width=450,
        height=300,
        bgcolor="#d9d9d9",
        margin=20,
        content=ft.Container(
            alignment=ft.alignment.bottom_left,
            width=450,
            height=100,
            content=card_big_news(
                "Водители на трассе М-12 сыграли 'Полёт шмеля'",
                "04.05.2024",
                """Они ехали-ехали и сыграли! Они ехали-ехали и сыграли! Они ехали ехали и сыграли! Они ехали-ехали и сыграли! Они ехали-ехали и сыграли!""",
            ),
        ),
    )
    for _ in range(5)  # изменить на внешний API
]

card_user_ft = ft.Row(scroll=ft.ScrollMode.ALWAYS, controls=card_total_user)
card_news_ft = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=card_total_news)
ard_big_news_ft = ft.Row(wrap=True, controls=card_total_big_news)
# --------------------------------------------------------------------------
my_calendar = CustomCalendar(
    width=250,
    bgcolor="#71a95a",
    font_color="#ffffff",
    hover_color="#34d409",
    font_color_accent="#84ff17",
    accent_color="#d2334c",
    header_font_color="#ffffff",
)
my_calendar_custom = ft.Row(controls=[my_calendar])


# ------------------------------------------------------------------------
def main(page: ft.Page):
    page.title = "Дороги России"  # заголовок окна
    page.theme_mode = ft.ThemeMode.LIGHT

    def calc(e):
        page.open(
            ft.DatePicker(
                first_date=datetime.datetime(year=2023, month=10, day=1),
                last_date=datetime.datetime(
                    year=int(date.today().strftime("%Y")),
                    month=12,
                    day=31,
                ),
            )
        )
        page.update()

    page.add(
        ft.Column(
            [
                ft.Container(
                    bgcolor="#e1f4c7",
                    height=100,
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        [
                            ft.FilledButton(
                                text="логотип",
                                color="black",
                                bgcolor="#79b14c",
                                style=ft.ButtonStyle(
                                    shape=ft.CircleBorder(), padding=30
                                ),
                            ),
                            ft.TextField(
                                label="Введите для поиска",
                                border_color="white",
                                height=40,
                                width=1000,
                                bgcolor="white",
                                color="black",
                                border_radius=15,
                            ),
                        ],
                        alignment=ft.alignment.center_left,
                    ),
                ),
                ft.Text("Сотрудники", style=ft.TextStyle(color="black", size=30)),
                ft.Container(
                    card_user_ft,
                    height=150,
                    margin=10,
                ),
                ft.Row(
                    [
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Text(
                                        "Календарь событий",
                                        style=ft.TextStyle(color="black", size=30),
                                    ),
                                    my_calendar_custom,
                                    ft.Button(text="Показать календарь", on_click=calc),
                                    ft.Text(
                                        "События",
                                        style=ft.TextStyle(color="black", size=25),
                                    ),
                                    ft.Container(
                                        card_news_ft,
                                        height=850,
                                    ),
                                ],
                            ),
                            width=300,
                        ),
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Text(
                                        "Новости",
                                        style=ft.TextStyle(color="black", size=30),
                                    ),
                                    ard_big_news_ft,
                                ],
                            ),
                            width=1000,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            height=900,
            scroll=ft.ScrollMode.ALWAYS,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
