from unittest.mock import right

import flet as ft


def main(page: ft.Page):
    page.title = "Дороги России"  # заголовок окна
    page.theme_mode = ft.ThemeMode.LIGHT

    def card(
        otdel: str = "jjj",
        position: str = "dsds",
        name: str = "dsds",
        phone: str = "dsds",
        mail: str = "dsds",
        work: str = "dsds",
    ):
        c = ft.Card(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(otdel, size=10),
                            ft.Text("-"),
                            ft.Text(position, size=10),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text(name, size=15),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text(phone),
                            ft.Text(" "),
                            ft.Text(mail),
                        ]
                    ),
                    ft.Row([ft.Text(work)]),
                ]
            ),
            color="#e1f4c7",
            width=700,
            height=150,
        )
        return c

    card_total = []
    # card_total.append(card())
    card_total_ft = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=card_total)

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
                                label="Организационная структура",
                                border_color="white",
                                height=40,
                                width=1000,
                                bgcolor="white",
                            ),
                        ],
                    ),
                    bgcolor="lightgreen",
                ),
                ft.Container(
                    ft.Row(
                        [
                            ft.Container(
                                ft.Column(
                                    [
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Дороги России",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Container(height=10),
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Административный департамент",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                                ft.FilledButton(
                                                    "Академия умные дороги",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Договорной отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                                ft.FilledButton(
                                                    "Общий отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Линцензионный отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                                ft.FilledButton(
                                                    "Управление маркетинга",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                ),
                                bgcolor="#d9d9d9",
                                height=page.window.height,
                                width=page.window.width / 2.2,
                            ),
                            ft.Container(
                                card_total_ft,
                                bgcolor="#d9d9d9",
                                height=page.window.height,
                                width=page.window.width / 2.2,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ),
            ]
        ),
    ),


if __name__ == "__main__":
    ft.app(main)
