import flet as ft

import datetime
from datetime import date

from db import *


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

    def card(name: str, position: str, mail: str, phone: str, birthday: str):
        c = ft.Card(
            ft.Column(
                [
                    ft.Text(
                        name,
                        style=ft.TextStyle(color="white", weight=ft.FontWeight.BOLD),
                    ),
                    ft.Text(position, style=ft.TextStyle(color="white")),
                    ft.Text(mail, style=ft.TextStyle(color="white")),
                    ft.Text(phone, style=ft.TextStyle(color="white")),
                    ft.Row(
                        [
                            ft.Text(
                                birthday,
                                style=ft.TextStyle(color="white"),
                            ),
                            ft.FilledButton("QR"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
            ),
            color="lightgreen",
            width=400,
            height=170,
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

    card_total = []

    card_total_all = [
        card(
            name=i["name"],
            position=i["post_name"],
            phone=i["phone"],
            mail=i["email"],
            birthday=i["birthday"],
        )
        for i in select_all()
    ]

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

    card_user_ft = ft.Row(scroll=ft.ScrollMode.ALWAYS, controls=card_total_all)
    card_news_ft = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=card_total_news)
    card_big_news_ft = ft.Row(wrap=True, controls=card_total_big_news)

    page.add(
        ft.Column(
            [
                ft.Container(
                    ft.Row(
                        [
                            ft.FilledButton(
                                "logotip",
                                color="black",
                                bgcolor="green",
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
                            ),
                        ],
                    ),
                    bgcolor="lightgreen",
                ),
            ],
        ),
        ft.Column(
            [
                ft.Text("Сотрудники", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.Container(
                    card_user_ft,
                ),
            ],
        ),
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Календарь событий",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                        ),
                        ft.Button(text="Показать календарь", on_click=calc),
                        ft.Text(
                            "Cобытия",
                            style=ft.TextStyle(weight=ft.FontWeight.BOLD),
                        ),
                        card_news_ft,
                    ]
                ),
                ft.Column(
                    [
                        ft.Text(
                            "Новости", style=ft.TextStyle(weight=ft.FontWeight.BOLD)
                        ),
                        card_big_news_ft,
                    ],
                    width=1000,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
