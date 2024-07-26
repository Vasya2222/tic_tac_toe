import flet as ft
from flet_core.control_event import ControlEvent
from .django_client import DjangoClient


class InviteFriends(ft.UserControl):
    def __init__(self, page: ft.Page, main_user=None, obj=None):
        super().__init__()
        self.django_client = DjangoClient()
        self.data_user = dict()
        self.friend_class = obj
        self.page = page
        self.check_login = 0
        self.data_users = {}
        self.friends = ft.ListView(spacing=10, height=300, padding=20)

    def view(self):
        self.add_friends_in_col()
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
        data_users = DjangoClient()
        get_data_users = data_users.send_data('api/player')
        for data_user in get_data_users:
            if data_user != self.data_user:
                self.friends.controls.append(
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    controls=[
                                        ft.Column(
                                            controls=[
                                                ft.Image(src=data_user['image_player'], width=50, height=50,
                                                         border_radius=25),
                                                ft.Text(f'{data_user['nickname']}'),
                                                ft.ElevatedButton(content=ft.Text('Пригласить'), on_click=lambda
                                                    y=ControlEvent, x=data_user: self.check(y, x))
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

    def check(self, e, user):
        print(user['nickname'])
        self.django_client.post_data(url='api/friend', data={'user': self.data_user['id'], 'friend': user['id'],
                                                             'status_invite': 1})
        self.page.update()
