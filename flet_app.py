from db import *

import flet as ft


def main(page: ft.Page):
    page.title = "Дороги России"  # заголовок окна
    page.theme_mode = ft.ThemeMode.LIGHT

    def card(
        otdel: str,
        position: str,
        name: str,
        phone: str,
        mail: str,
        work: str,
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
    card_total_ft = ft.Column(scroll=ft.ScrollMode.ALWAYS, controls=card_total)

    card_total_departament = [
        card(
            otdel=i["departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_departament()
    ]

    card_total_mini_departament = [
        card(
            otdel=i["mini_departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_mini_departament()
    ]

    card_total_managment = [
        card(
            otdel=i["managment_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_managment()
    ]

    card_total_admin_departament = [
        card(
            otdel=i["departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_admin_departament("1. Административный департамент")
    ]

    card_total_academia = [
        card(
            otdel=i["departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_admin_departament("2. Академия Умные дороги")
    ]

    card_total_dogovor = [
        card(
            otdel=i["mini_departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_mini_departament_all("1.2. Договорной отдел")
    ]

    card_total_obsh_otdel = [
        card(
            otdel=i["mini_departament_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_mini_departament_all("1.3. Общий отдел")
    ]

    card_total_license_otdel = [
        card(
            otdel=i["managment_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_managment_all("5.2.1. Лицензионный отдел")
    ]

    card_total_uprav_market = [
        card(
            otdel=i["managment_name"],
            position=i["post_name"],
            name=i["name"],
            phone=i["phone"],
            mail=i["email"],
            work=i["info"],
        )
        for i in select_managment_all("5.2.2. Управление маркетинга")
    ]

    def card_road_of_russia(e):
        card_total.clear()
        card_total.extend(card_total_departament)
        card_total.extend(card_total_mini_departament)
        card_total.extend(card_total_managment)
        card_total_ft.controls = card_total
        page.update()

    def card_admin_departament(e):
        card_total.clear()
        card_total.extend(card_total_admin_departament)
        card_total_ft.controls = card_total
        page.update()

    def card_academia(e):
        card_total.clear()
        card_total.extend(card_total_academia)
        card_total_ft.controls = card_total
        page.update()

    def card_dogovor(e):
        card_total.clear()
        card_total.extend(card_total_dogovor)
        card_total_ft.controls = card_total
        page.update()

    def card_obsh_otdel(e):
        card_total.clear()
        card_total.extend(card_total_obsh_otdel)
        card_total_ft.controls = card_total
        page.update()

    def card_license_otdel(e):
        card_total.clear()
        card_total.extend(card_total_license_otdel)
        card_total_ft.controls = card_total
        page.update()

    def card_uprav_market(e):
        card_total.clear()
        card_total.extend(card_total_uprav_market)
        card_total_ft.controls = card_total
        page.update()

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
                                                    on_click=card_road_of_russia,
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
                                                    on_click=card_admin_departament,
                                                ),
                                                ft.FilledButton(
                                                    "Академия умные дороги",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                    on_click=card_academia,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Container(height=10),
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Договорной отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                    on_click=card_dogovor,
                                                ),
                                                ft.FilledButton(
                                                    "Общий отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                    on_click=card_obsh_otdel,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                        ft.Container(height=10),
                                        ft.Row(
                                            [
                                                ft.FilledButton(
                                                    "Линцензионный отдел",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                    on_click=card_license_otdel,
                                                ),
                                                ft.FilledButton(
                                                    "Управление маркетинга",
                                                    color="black",
                                                    bgcolor="lightgreen",
                                                    on_click=card_uprav_market,
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
