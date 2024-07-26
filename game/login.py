import flet as ft
from .django_client import DjangoClient
from .menu import Menu


class Login(ft.UserControl):
    def __init__(self, page, obj=None, obj_second=None, obj_three=None):
        super().__init__()
        self.class_profile_user = obj
        self.class_invite_user = obj_second
        self.class_friend = obj_three
        self.page = page
        self.name = ft.TextField(label='Имя', text_size=20, color='#40FFFF', value='vasya')
        self.password = ft.TextField(password=True, label='Пароль', text_size=20, color='#40FFFF', value='123444')
        self.menu = Menu(self.page)

    def view(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([self.name]),
                    ft.Row([self.password]),
                    ft.ElevatedButton('Войти', on_click=self.send_data, style=self.btn_style()),
                    ft.ElevatedButton('Назад', on_click=lambda _: self.page.go('/'), style=self.btn_style())
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            bgcolor='#FFC043', width=350, padding=20, border_radius=25
        )

    def send_data(self, e):
        client = DjangoClient()
        clients = client.send_data('api/player')
        for client in clients:
            if self.name.value == client['nickname'] and self.password.value == client['password']:
                self.class_profile_user.data_user = client
                self.class_invite_user.data_user = client
                self.class_friend.data_user = client
                self.page.go('/menu')
                break

    def btn_style(self):
        style_for_btn = ft.ButtonStyle(
            bgcolor='#FFAA00',
            color='#40FFFF'

        )
        self.page.update()
        return style_for_btn
