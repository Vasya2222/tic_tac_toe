import flet as ft
from .profile_user import ProfileUser


class SaveDataUser:
    def __init__(self):
        self.data_user = str()


class Menu(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.data_user = 0
        self.count = 1
        self.check_login = 0
        self.cole = ft.Column()
        self.cont = ft.Container()
        self.add_in_cont()

    def set_data(self, data):
        self.data_user += 1
        self.data_user = data

    def add_in_cont(self):
        btn_start_game = ft.ElevatedButton(content=ft.Text('Начать играть', color='#40FFFF'), on_click=lambda _: self.page.go('/game'),
                                           style=self.btn_style(), width=150)
        with_friend = ft.ElevatedButton(content=ft.Text('С другом', color='#40FFFF'),
                                        on_click=lambda _: self.page.go('/generation_code'),

                                        style=self.btn_style(), width=150)
        with_bot = ft.ElevatedButton(content=ft.Text('С роботом', color='#40FFFF'),
                                        on_click=lambda _: self.page.go('/with_bot'),

                                        style=self.btn_style(), width=150)
        invite_friends = ft.ElevatedButton(content=ft.Text('Пригласить', color='#40FFFF'),
                                           on_click=lambda _: self.page.go('/invite_friends'),
                                           style=self.btn_style(), width=150)
        friends = ft.ElevatedButton(content=ft.Text('Друзья', color='#40FFFF'),
                                    on_click=lambda _: self.page.go('/friends'),
                                           style=self.btn_style(), width=150)
        self.cole.controls.append(
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.ACCOUNT_BOX,
                                            on_click=self.account
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.SETTINGS
                                        )
                                    ], alignment=ft.MainAxisAlignment.CENTER
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    btn_start_game
                                                ]
                                                , alignment=ft.MainAxisAlignment.CENTER)
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    with_friend
                                                ]
                                                , alignment=ft.MainAxisAlignment.CENTER)
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    with_bot
                                                ]
                                                , alignment=ft.MainAxisAlignment.CENTER)
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    invite_friends
                                                ]
                                                , alignment=ft.MainAxisAlignment.CENTER)
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    friends
                                                ]
                                                , alignment=ft.MainAxisAlignment.CENTER)
                                        ]
                                    )
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            ft.Row(
                                                [
                                                    ft.ElevatedButton(content=ft.Text('Выход', color='#40FFFF'),
                                                                      on_click=lambda _: self.page.window_close(),
                                                                      style=self.btn_style(), width=150)
                                                ], alignment=ft.MainAxisAlignment.CENTER
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )

        self.cont = ft.Container(
            content=self.cole,
            bgcolor='#FFC043', width=200, padding=20, border_radius=50
        )
        self.page.update()

    def account(self, e):
        self.page.go('/profile_user')

    def add_data(self, data):
        self.data_user = data.data_user

    def btn_style(self):
        style_for_btn = ft.ButtonStyle(
            bgcolor='#FFAA00'

        )
        self.page.update()
        return style_for_btn
