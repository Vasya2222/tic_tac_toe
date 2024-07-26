import flet as ft


class LoginOrCreateUser(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.check_login = 0

    def view(self):
        return ft.Container(
            content=ft.Column(controls=[
                ft.Row(
                    [ft.ElevatedButton(content=ft.Text('Войти', color='#40FFFF'),
                                       on_click=lambda _: self.page.go('/login'), style=self.btn_style(), width=200),
                     ], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [ft.ElevatedButton(content=ft.Text('Зарегистрироваться', color='#40FFFF'),
                                       on_click=lambda _: self.page.go('/create_player'), style=self.btn_style(),
                                       width=200),
                     ], alignment=ft.MainAxisAlignment.CENTER
                )
            ]
            ),
            bgcolor='#FFC043', width=250, padding=20, border_radius=25
        )

    def btn_style(self):
        style_for_btn = ft.ButtonStyle(
            bgcolor='#FFAA00'

        )
        self.page.update()
        return style_for_btn