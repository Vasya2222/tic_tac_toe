import flet as ft
import uuid
from .django_client import DjangoClient


class CreatePlayer(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.file_path = str()
        self.image_avatar = ft.FilePicker(on_result=self.result_choose_image_for_player)
        self.name = ft.TextField()
        self.email = ft.TextField()
        self.password = ft.TextField(password=True)
        self.choose_image = ft.ElevatedButton(
            content=ft.Text('Выберите вашу аватарку'),
            on_click=lambda _: self.image_avatar.pick_files()
        )

    def view(self, page):
        self.page = page
        page.overlay.append(self.image_avatar)
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row([self.choose_image]),
                    ft.Row([ft.Text('Имя'), self.name]),
                    ft.Row([ft.Text('Email'), self.email]),
                    ft.Row([ft.Text('Пароль'), self.password]),
                    ft.ElevatedButton('Создать аккаунт', on_click=self.send_data),
                    ft.ElevatedButton('Назад', on_click=lambda _: page.go('/'))
                ]
            )
        )

    def send_data(self, e):
        data = {
            'nickname': self.name.value,
            'game_id': str(uuid.uuid4()),
            'email': self.email.value,
            'password': self.password.value
        }
        image = {"image_player": open(str(self.file_path), 'rb')}
        client = DjangoClient()
        client.post_data('api/player', data, image)

    def result_choose_image_for_player(self, e):
        self.file_path = (
            ','.join(map(lambda f: f.path, e.files))
        )
        self.file_name = (
            ','.join(map(lambda f: f.name, e.files))
        )
        print(self.image_avatar)
        print(self.file_path)
        self.choose_image.content = ft.Image(src=self.file_path, width=100,
                                             height=100)
        self.page.update()
