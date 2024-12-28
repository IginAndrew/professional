import flet as ft

from my_db.select_db import select_user_management, select_user_department, select_user_mini_department, \
    select_user_admin_department, select_user_admin_mini_department, select_user_management_button


def main(page: ft.Page):
    # page.window_width = 1000  # ширина окна равна 200 пикселям
    # page.window_height = 600  # высота окна равна 400 пикселям
    # page.window_resizable = False  # размер окна нельзя изменять
    page.title = "Дороги России"  # заголовок окна
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER# вертикальное выравнивание
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER# горизонтальное выравнивание
    # page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    # page.scroll = "adaptive"

    add = ft.FloatingActionButton(icon=ft.Icons.ADD, bgcolor=ft.Colors.LIME_100, mini=True)

    def card(otdel: str, position: str, name: str, phone: str, mail: str, work: str):
        c = ft.Column([
            ft.Card(
                ft.Container(
                    ft.Column([
                        ft.Row([
                            ft.Text(otdel, size=10),
                            ft.Text('-'),
                            ft.Text(position, size=10),
                        ]),
                        ft.Row([
                            ft.Text(name, size=15),
                        ]),
                        ft.Row([
                            ft.Text(phone),
                            ft.Text(' '),
                            ft.Text(mail),
                        ]),
                        ft.Row([
                            ft.Text(work)
                        ]),

                    ]),
                    bgcolor='#e1f4c7',
                    width=550,
                    height=150,
                    padding=20,
                )
            ),
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.ALWAYS,
        )
        return c

    card_total = []

    card_total_ft = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        controls=card_total
    )

    card_total_management = [
        card(otdel=i['management_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_management()]

    card_total_department = [
        card(otdel=i['department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_department()]

    card_total_mini_department = [
        card(otdel=i['mini_department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_mini_department()]

    card_total_admin_department = [
        card(otdel=i['department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_admin_department('Административный департамент')]

    card_total_roads = [
        card(otdel=i['department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_admin_department('Академия Умные дороги')]

    card_total_admin_mini_department_dogovor = [
        card(otdel=i['mini_department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_admin_mini_department('Договорной отдел')]

    card_total_admin_mini_department_obshi= [
        card(otdel=i['mini_department_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_admin_mini_department('Общий отдел')]

    card_management_licenz_button = [
        card(otdel=i['management_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_management_button('Лицензионный отдел')]

    card_management_market_button = [
        card(otdel=i['management_name'], position=i['post_name'], name=i['name'], phone=i['phonenumber'],
             mail=i['email'], work=i['info']) for i in select_user_management_button('Управление маркетинга')]

    def roads_of_Russia(e):
        card_total = []
        card_total.extend(card_total_management)
        card_total.extend(card_total_department)
        card_total.extend(card_total_mini_department)
        card_total_ft.controls = card_total
        page.update()

    def admin_deporparment(e):
        card_total = []
        card_total.extend(card_total_admin_department)
        card_total_ft.controls = card_total
        page.update()

    def admin_roads(e):
        card_total = []
        card_total.extend(card_total_roads)
        card_total_ft.controls = card_total
        page.update()

    def admin_dogovor(e):
        card_total = []
        card_total.extend(card_total_admin_mini_department_dogovor)
        card_total_ft.controls = card_total
        page.update()

    def admin_obshi(e):
        card_total = []
        card_total.extend(card_total_admin_mini_department_obshi)
        card_total_ft.controls = card_total
        page.update()

    def management_licenz_button(e):
        card_total = []
        card_total.extend(card_management_licenz_button)
        card_total_ft.controls = card_total
        page.update()

    def management_marketing_button(e):
        card_total = []
        card_total.extend(card_management_market_button)
        card_total_ft.controls = card_total
        page.update()


    page.add(
        ft.Column([
            ft.Container(
                ft.Row(
                    [
                        ft.FilledButton("логотип", color='black', bgcolor='#79b14c',
                                        style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=30), ),
                        ft.TextField(
                            label="Организационная структура",
                            border_color="white",
                            height=40,
                            width=1000,
                            bgcolor="white",
                            color="black",
                        )
                    ],
                    alignment=ft.alignment.center_left,
                ),

                bgcolor='#e1f4c7',
                width=page.window_width,
                height=100,
            ),

            ft.Row(
                [
                    ft.Container(
                        ft.Column([
                            ft.Row([
                                ft.FilledButton("Дороги России", color="black", bgcolor="#e1f4c7", on_click=roads_of_Russia),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text(''),
                            ft.Row([
                                ft.FilledButton(text="Административный департамент", color="black",
                                                bgcolor="#e1f4c7", on_click=admin_deporparment),
                                ft.FilledButton("Академия Умные дороги", color="black", bgcolor="#e1f4c7", on_click=admin_roads),
                            ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Text(''),
                            ft.Row([
                                ft.FilledButton("Договорной отдел", color="black", bgcolor="#e1f4c7", on_click=admin_dogovor),
                                ft.FilledButton("Общий отдел", color="black", bgcolor="#e1f4c7", on_click=admin_obshi),
                            ],
                            ),
                            ft.Text(''),
                            ft.Row([
                                ft.FilledButton("Лицензионный отдел", color="black", bgcolor="#e1f4c7", on_click=management_licenz_button),
                                ft.FilledButton("Управление маркетинга", color="black", bgcolor="#e1f4c7", on_click=management_marketing_button),
                            ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),

                        ],
                        ),
                        bgcolor='#d9d9d9',
                        width=page.window_width / 2 - 20,
                        height=550,
                        margin=20,
                        padding=20,
                    ),
                    ft.Row([
                        add
                    ]),

                    ft.Container(
                        card_total_ft,
                        bgcolor='#d9d9d9',
                        width=page.window_width / 2 - 100,
                        height=550,
                        margin=20,

                    ),


                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),

        ]
        ),

    )


if __name__ == "__main__":
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    ft.app(main)
