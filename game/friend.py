import flet as ft
from flet_core.control_event import ControlEvent

class Friend(ft.UserControl):
    def __init__(self, page: ft.Page, obj=None):
        super().__init__()
        self.page = page
        self.data_user = str()
        self.friends = ft.ListView(spacing=10, height=300, padding=20)

    def view(self):
        return ft.Container(
            content=ft.Column(
                [
                    self.friends,
                    ft.ElevatedButton(content=ft.Text('Назад'), style=ft.ButtonStyle(bgcolor='#FFAA00'),
                                      on_click=lambda _: self.page.go('/menu'))
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ), bgcolor='#FFC043',
            width=250, alignment=ft.alignment.center, border_radius=25, padding=20
        )

    def add_friends_in_col(self):
        for friend in self.friend:
            self.friends.controls.append(
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Image(src=friend['image_player'], width=50, height=50,
                                                     border_radius=25),
                                            ft.Text(f'{friend['nickname']}'),
                                            ft.ElevatedButton(content=ft.Text('Пригласить'), on_click=lambda
                                                y=ControlEvent, x=friend: self.check(y, x))
                                        ], alignment=ft.MainAxisAlignment.CENTER
                                    )

                                ], alignment=ft.MainAxisAlignment.CENTER
                            )
                        ], alignment=ft.MainAxisAlignment.CENTER
                    ), bgcolor='#FFAA00', padding=20,
                    width=210, border_radius=25
                )
            )
            self.page.update()

