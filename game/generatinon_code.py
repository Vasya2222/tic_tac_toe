from random import randint
import flet as ft
import asyncio

from .django_client import DjangoClient


class GenerationCode(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.code = 0

    def view(self, page):
        self.update_code()
        # asyncio.run(self.main())
        client = DjangoClient()
        client.send_data('send_data', {'data': self.code}, 0)
        return ft.Container(

            content=ft.Column(
                controls=[
                    ft.Text(f'{self.code}'),
                    ft.ElevatedButton('Назад', on_click=lambda _: page.go('/')),
                ]
            )
        )


    def update_code(self):
        self.code = randint(1000, 9999)


    # async def send_data_to_server(self, data, url):
    #     async with aiohttp.ClientSession() as session:
    #         async with session.post(url, data=data) as response:
    #             return await response.text()
    #
    # async def main(self):
    #     url = 'http://localhost:8080/send_data/'
    #     data = {'data': self.code}
    #
    #     response = await self.send_data_to_server(data, url)
    #     print(response)

