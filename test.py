# # import flet as ft
# #
# # def main(page: ft.Page):
# #     def pick_files_result(e: ft.FilePickerResultEvent):
# #         selected_files.value = (
# #             ','.join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
# #         )
# #         selected_files.update()
# #         img = ft.Image(
# #             src=f"{','.join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"}",
# #             width=100,
# #             height=100,
# #             fit=ft.ImageFit.CONTAIN,
# #         )
# #         images = ft.Row(expand=1, wrap=False)
# #
# #         page.add(img, images)
# #
# #     pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
# #     selected_files = ft.Text()
# #
# #     page.overlay.append(pick_files_dialog)
# #
# #     page.add(
# #         ft.Row(
# #             [
# #                 ft.ElevatedButton(
# #                     "Pick files",
# #                     icon=ft.icons.UPLOAD_FILE,
# #                     on_click=lambda _: pick_files_dialog.pick_files(
# #                         allow_multiple=True
# #                     ),
# #                 ),
# #                 selected_files,
# #             ]
# #         )
# #     )
# #
# # ft.app(target=main)
# from build.windows.Lib.unittest import TestCase
#
#
# # import requests as rs
# #
# # # with open('assets/icon.jpg', 'rb') as f:
# # #     image = {'image_player': f}
# # #     response = rs.post('http://127.0.0.1:8080/api/player/', json={'id': 2, 'nickname': 'Vasya34',
# # #                                                                   'game_id': 'Vasya34', 'create_date': '2024-04-03',
# # #                                                                   'email': 'vasyaryzhov2906@gmail.com',
# # #                                                                   'password': '1234'},
# # #                        files=image)
# # # image = {'image_player': open('assets/icon.jpg', 'rb')}
# # # data = {'nickname': 'vasya', 'game_id': '1234565', 'email': 'vas@gmail.com', 'password': '123444'}
# # # response = rs.post('http://127.0.0.1:8080/api/player/', files=image, data=data)
# # #
# # # print(response.json())
# # # if response.status_code == 200:
# # #     print('Успешно')
# # # else:
# # #     print(False)
# # # dict1 = [{'id': 1, 'image_player': 'http://127.0.0.1:8080/media/players/2024-02-06.png', 'nickname': 'Vasya34',
# # #           'game_id': 'Vasya34', 'create_date': '2024-04-03', 'email': 'vasyaryzhov2906@gmail.com', 'password': '1234'},
# # #          {'id': 2, 'image_player': 'http://127.0.0.1:8080/media/players/icon.jpg', 'nickname': 'vasya',
# # #           'game_id': '1234565',
# # #           'create_date': '2024-04-03', 'email': 'vas@gmail.com', 'password': '123444'},
# # #          {'id': 3, 'image_player': 'http://127.0.0.1:8080/media/players/icon_HFE1x9z.jpg', 'nickname': 'vasya',
# # #           'game_id': '1234565', 'create_date': '2024-04-03', 'email': 'vas@gmail.com', 'password': '123444'},
# # #          {'id': 4, 'image_player': 'http://127.0.0.1:8080/media/players/2024-02-06_PAQ84Eq.png', 'nickname': 'vasss',
# # #           'game_id': 'e8de24fc-f227-40aa-a933-3efd56241102', 'create_date': '2024-04-03', 'email': 'g@gmail.com',
# # #           'password': '55555'},
# # #          {'id': 5, 'image_player': 'http://127.0.0.1:8080/media/players/2024-01-20_1.png', 'nickname': 'vasss',
# # #           'game_id': '84a6ee6c-f11a-4674-95a8-107da957a83b', 'create_date': '2024-04-03', 'email': 'g@gmail.com',
# # #           'password': '33333'},
# # #          {'id': 6, 'image_player': 'http://127.0.0.1:8080/media/players/2024-01-20_1_Tt4HoSf.png', 'nickname': 'vasss',
# # #           'game_id':
# # #               '048813ea-47db-48ab-a921-d9c76fa97a49', 'create_date': '2024-04-03', 'email': 'g@gmail.com',
# # #           'password': '3333'}]
# # #
# # # dict1.remove({'id': 1, 'image_player': 'http://127.0.0.1:8080/media/players/2024-02-06.png', 'nickname': 'Vasya34',
# # #           'game_id': 'Vasya34', 'create_date': '2024-04-03', 'email': 'vasyaryzhov2906@gmail.com', 'password': '1234'})
# # # print(dict1)
# #
# # # import flet as ft
# # #
# # #
# # # def main(page: ft.Page):
# # #     cl = ft.Column(
# # #         spacing=10,
# # #         height=200,
# # #         width=float("inf"),
# # #         scroll=ft.ScrollMode.ALWAYS,
# # #     )
# # #     for i in range(0, 100):
# # #         cl.controls.append(ft.Text(f"Text line {i}", key=str(i)))
# # #
# # #     def scroll_to_offset(e):
# # #         cl.scroll_to(offset=100, duration=1000)
# # #
# # #     def scroll_to_start(e):
# # #         cl.scroll_to(offset=0, duration=1000)
# # #
# # #     def scroll_to_end(e):
# # #         cl.scroll_to(offset=-1, duration=2000, curve=ft.AnimationCurve.EASE_IN_OUT)
# # #
# # #     def scroll_to_key(e):
# # #         cl.scroll_to(key="20", duration=1000)
# # #
# # #     def scroll_to_delta(e):
# # #         cl.scroll_to(delta=40, duration=200)
# # #
# # #     def scroll_to_minus_delta(e):
# # #         cl.scroll_to(delta=-40, duration=200)
# # #
# # #     page.add(
# # #         ft.Container(cl, border=ft.border.all(1)),
# # #         ft.ElevatedButton("Scroll to offset 100", on_click=scroll_to_offset),
# # #         ft.Row(
# # #             [
# # #                 ft.ElevatedButton("Scroll to start", on_click=scroll_to_start),
# # #                 ft.ElevatedButton("Scroll to end", on_click=scroll_to_end),
# # #             ]
# # #         ),
# # #         ft.ElevatedButton("Scroll to key '20'", on_click=scroll_to_key),
# # #         ft.Row(
# # #             [
# # #                 ft.ElevatedButton("Scroll -40", on_click=scroll_to_minus_delta),
# # #                 ft.ElevatedButton("Scroll +40", on_click=scroll_to_delta),
# # #             ]
# # #         ),
# # #     )
# # #
# # #
# # # ft.app(main)
# #
# # import flet as ft
# # from playsound import playsound
# # import simpleaudio.functionchecks as fc
# # import simpleaudio as sa
# #
# # fc.run_all()
# #
# # f_name = 'game/audio/fun_click.mp3'
# #
# # wave_obj = sa.WaveObject.from_wave_file(f_name)
# #
# #
# # def main(page: ft.Page):
# #     audio1 = ft.Audio(
# #         src="audio/fun_click.mp3"
# #     )
# #     def play(e):
# #         audio1.pause()
# #
# #     def play1(e):
# #         play = wave_obj.play()
# #
# #         # To stop after playing the whole audio
# #         play.wait_done()
# #         play.stop()
# #     page.overlay.append(audio1)
# #     page.add(
# #         ft.Text("This is an app with background audio."),
# #         ft.ElevatedButton("Stop playing", on_click=play),
# #         ft.ElevatedButton("Start playing", on_click=play1),
# #     )
# #
# #
# # ft.app(target=main)
#
# # num1 = int(input('Введите 1 число -> '))
# # num2 = int(input('Введите 2 число -> '))
# #
# # if num2 > 500:
# #     num1 = num1 + 50
# # elif num2 > 50:
# #     num1 = num1 - 50
# # else:
# #     num2 *= 2
# #
# # print('Результат =', num1 + num2)
#
# # n = int(input('Введите число -> '))
# # # sum_num = 0
# # #
# # # for i in range(n+1):
# # #     sum_num = sum_num + i
# # #
# # # print(sum_num)
#
# # def sum_two_numbers(num1: int, num2: int) -> int:
# #     return num1 + num2
# #
# # num1 = int(input('Введите 1 число -> '))
# # num2 = int(input('Введите 2 число -> '))
# #
# # print('Результат =', sum_two_numbers(num1, num2))
#
# # a = (1,2,3,4,5,6,7,8,9)
# # a[1]=56
# #
# # print(a)
#
# # class YourTestClass(TestCase):
# #
# #     @classmethod
# #     def setUpTestData(cls):
# #         print("setUpTestData: Run once to set up non-modified data for all class methods.")
# #         pass
# #
# #     def setUp(self):
# #         print("setUp: Run once for every test method to setup clean data.")
# #         pass
# #
# #     def test_false_is_false(self):
# #         print("Method: test_false_is_false.")
# #         self.assertFalse(False)
# #
# #     def test_false_is_true(self):
# #         print("Method: test_false_is_true.")
# #         self.assertTrue(False)
# #
# #     def test_one_plus_one_equals_two(self):
# #         print("Method: test_one_plus_one_equals_two.")
# #         self.assertEqual(1 + 1, 2)
#
# import flet as ft
#
# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#
#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
#
#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()
#
#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()
#
#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )
#
# ft.app(main)
#
# import flet as ft
#
# def main(page: ft.Page):
#     t = ft.Text(value="Hello, world!", color="green")
#     page.controls.append(t)
#     page.update()
#
# ft.app(target=main)
#
# number_1 = 2
# number_2 = 1
# print(number_1 / number_2) #>>> 2.0

# list_1 = [1, 2, 3]
# list_2 = [4, 5, 6]
# 
# print(list_1 == list_2)
