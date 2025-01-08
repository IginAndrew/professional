import flet as ft
import datetime
from datetime import date
from my_db.select_db import select_user


def card(name:str,email:str,phonenumber:str, post_name:str,birthday:str):
    c = ft.Card(
                ft.Column(
                        [

                        ft.Text(name, style=ft.TextStyle(color="white", size=15)),

                        ft.Text(post_name, style=ft.TextStyle(color="white", size=10)),

                        ft.Text(email, style=ft.TextStyle(color="white", size=10)),

                        ft.Text(phonenumber, style=ft.TextStyle(color="white", size=10)),

                        ft.Text(birthday[:birthday.index(" ")], style=ft.TextStyle(color="white", size=10)),
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
    ]

card_user_ft = ft.Row(scroll=ft.ScrollMode.ALWAYS, controls=card_total_user)

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
                    )
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
                    height=130,
                    margin=10,
                ),
                ft.Row([
                ft.Column([
                    ft.Text("Календарь событий", style=ft.TextStyle(color="black", size=30)),
                    ft.Button(text="Показать календарь",on_click=calc)
                ]),
                    ft.Column([
                        ft.Text("Новости", style=ft.TextStyle(color="black", size=30)),
                    ]),
                    ]),
            ],

        ),
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
