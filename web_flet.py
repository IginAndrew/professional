import flet as ft

from db import *


def main(page: ft.Page):
    page.title = "Дороги России"  # заголовок окна
    page.theme_mode = ft.ThemeMode.LIGHT

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

    card_user_ft = ft.Row(scroll=ft.ScrollMode.ALWAYS, controls=card_total_all)

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
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
