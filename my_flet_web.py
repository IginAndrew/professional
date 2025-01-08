import flet as ft


def main(page: ft.Page):
    page.title = "Дороги России"  # заголовок окна
    page.theme_mode = ft.ThemeMode.LIGHT

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
                )
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
