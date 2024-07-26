import flet as ft


class ProfileUser(ft.UserControl):
    def __init__(self, page, class_profile_user=None):
        super().__init__()
        self.page = page
        self.class_profile_user = class_profile_user
        self.data_user = dict()


    def view(self):
        return ft.Container(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Text('Профиль', size=20, color='#B9F73E')
                            ], alignment=ft.MainAxisAlignment.CENTER)
                    ),
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Image(
                                                                        src=self.data_user['image_player'],
                                                                        width=100, height=100, border_radius=50,

                                                                    )

                                                                ], alignment=ft.MainAxisAlignment.CENTER

                                                            )
                                                        ], width=210
                                                    ),
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'Псевдоним',
                                                                            color="#512EC2", size=20)
                                                                ],
                                                                alignment=ft.MainAxisAlignment.CENTER
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'{self.data_user['nickname']}',
                                                                            color='#40FFFF', size=20),
                                                                    ft.IconButton(icon=ft.icons.COPY,
                                                                                  on_click=self.copy_nickname)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            )
                                                        ], width=210
                                                    ), bgcolor='#FFAA00', border_radius=50
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'Идентификатор',
                                                                            color="#512EC2", size=20)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'{self.data_user['game_id']}',
                                                                            color='#40FFFF', size=20),
                                                                    ft.IconButton(icon=ft.icons.COPY,
                                                                                  on_click=self.copy_game_id)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            )
                                                        ], width=210
                                                    ), bgcolor='#FFAA00', border_radius=50
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'Эл. почта.',
                                                                            color="#512EC2", size=20)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'{self.data_user['email']}',
                                                                            color='#40FFFF', size=20),
                                                                    ft.IconButton(icon=ft.icons.COPY,
                                                                                  on_click=self.copy_email)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            )
                                                        ], width=210
                                                    ), bgcolor='#FFAA00', border_radius=50
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Column(

                                                        controls=[
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'Дата создания',
                                                                            color="#512EC2", size=20)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            ),
                                                            ft.Row(
                                                                controls=[
                                                                    ft.Text(f'{self.data_user['create_date']}',
                                                                            color='#40FFFF', size=20),
                                                                    ft.IconButton(icon=ft.icons.COPY,
                                                                                  on_click=self.copy_date_create)
                                                                ], alignment=ft.MainAxisAlignment.CENTER
                                                            )
                                                        ], width=210
                                                    ), bgcolor='#FFAA00', border_radius=50
                                                )
                                            ]
                                        )

                                    ]
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.ElevatedButton(content=ft.Text('Назад'), style=ft.ButtonStyle(bgcolor='#FFAA00'),
                                                  on_click=lambda _: self.page.go('/menu'))
                            ], width=210, horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS, height=400
            ),
            bgcolor='#FFC043',
            width=250, alignment=ft.alignment.center, border_radius=25, padding=20,
        )

    def copy_nickname(self, x):
        import pyperclip as clipboard

        clipboard.copy(self.data_user['nickname'])

    def copy_game_id(self, x):
        import pyperclip as clipboard

        clipboard.copy(self.data_user['game_id'])

    def copy_email(self, x):
        import pyperclip as clipboard

        clipboard.copy(self.data_user['email'])

    def copy_date_create(self, x):
        import pyperclip as clipboard

        clipboard.copy(self.data_user['create_date'])