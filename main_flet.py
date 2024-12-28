import flet as ft

def main(page: ft.Page):
    # page.window_width = 1000  # ширина окна равна 200 пикселям
    # page.window_height = 600  # высота окна равна 400 пикселям
    # page.window_resizable = False  # размер окна нельзя изменять
    page.title = "Дороги России"  # заголовок окна
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER# вертикальное выравнивание
    # page.horizontal_alignment = ft.MainAxisAlignment.CENTER# горизонтальное выравнивание
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    # page.scroll = "adaptive"

    page.add(
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

                    bgcolor= '#e1f4c7',
                    width=page.window_width,
                    height=100,
                ),
    )


if __name__ == "__main__":
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)
    ft.app(main)
