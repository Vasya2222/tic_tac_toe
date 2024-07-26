# import time
#

import asyncio
from random import random, choice

import flet as ft
from playsound import playsound


class GameWithBotAndPlayer(ft.UserControl):
    WIN = (
        # колоны
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        # ряда
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        # диагонали

        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    )

    def __init__(self, page: ft.Page):
        super().__init__()
        self.dlg = ft.AlertDialog()
        self.button_fields = list()
        self.move = 'X'
        self.fields = [[0 for _ in range(3)] for _ in range(3)]
        self.style_for_btn = str()
        self.page = page
        self.count = 0
        self.cole = ft.Column()
        self.cont = ft.Container(
            bgcolor=ft.colors.BLUE_100,
            alignment=ft.alignment.center
        )
        self.buttons()
        self.play_audio = ft.Audio(
            src='../audio/funClick.mp3'
        )
        self.win_audio = ft.Audio(
            src='../audio/you_win.wav'
        )
        self.page.overlay.append(self.play_audio)
        self.page.overlay.append(self.win_audio)

    def view(self):
        return self.cont

    def change_page(self, e, page: ft.Page):
        page.go('/')
        page.update()

    def move_player(self):
        if self.move == 'X':
            self.move = 'O'
            return 'O'
        else:
            self.move = 'X'
            return 'X'

    def click(self, button):
        self.play_audio.play()
        button.control.content = ft.Text(self.move, size=50)
        button.control.animate_size = 15
        button.control.style = self.btn_style_after_click()

        row, col = button.control.data
        self.fields[row][col] = self.move
        button.control.disabled = True
        self.alert_dialog()
        self.check_win()
        self.move_player()
        self.page.update()
        self.bot_move()

    def buttons(self):
        for row in range(3):
            list_buttons = list()
            for col in range(3):
                button = ft.ElevatedButton(
                    content=ft.Text('', size=20), style=self.btn_style(), data=[row, col],
                    on_click=self.click, width=100, height=100
                )
                list_buttons.append(button)
            self.button_fields.append(list_buttons)
        for list_buttons in self.button_fields:
            self.cole.controls.append(ft.Row(list_buttons, alignment=ft.MainAxisAlignment.CENTER))

        self.cole.controls.append(ft.Row([
            ft.TextButton(text='новая игра', on_click=self.new_game, style=self.btn_new_game())
        ], expand_loose=True, alignment=ft.MainAxisAlignment.CENTER)
        )
        self.cole.controls.append(ft.Row([
            ft.TextButton(text='Назад', on_click=lambda _: self.page.go('/menu'), style=self.btn_new_game())
        ], expand_loose=True, alignment=ft.MainAxisAlignment.CENTER)
        )
        self.cont = ft.Container(content=self.cole)

    def new_game(self, e):

        for list_buttons in self.button_fields:
            for button in list_buttons:
                button.content = ft.Text('')
                button.disabled = False
        self.page.update()
        self.fields = [[0 for _ in range(3)] for _ in range(3)]
        self.move = 'X'

    def bot_move(self):
        empty_indexes = list()
        for index, el in enumerate(self.fields):
            if el == 0:
                empty_indexes.append(index)
        if empty_indexes:
            index = choice(empty_indexes)



    def check_win(self):
        for win in self.WIN:
            if self.fields[win[0][0]][win[0][1]] == self.fields[win[1][0]][win[1][1]] == self.fields[win[2][0]][
                win[2][1]] \
                    and (self.fields[win[0][0]][win[0][1]] != 0 and self.fields[win[1][0]][win[1][1]] != 0 and
                         self.fields[win[2][0]][win[2][1]] != 0):
                for list_buttons in self.button_fields:
                    for button in list_buttons:
                        button.disabled = True
                self.page.update()
                self.open_dialog()
                self.win_audio.play()
                print("победил -> ", self.move)

    def alert_dialog(self):
        print(self.move)
        self.dlg = ft.AlertDialog(
            title=ft.Text(f'Победил игрок -> {self.move}', size=10), on_dismiss=lambda e: print('open'),
            shape=ft.RoundedRectangleBorder(radius=6), actions_padding=0,

        )

    def open_dialog(self):
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()

    # Стили для кнопок

    def btn_style_after_click(self):
        return ft.ButtonStyle(
            color={
                ft.MaterialState.DISABLED: ft.colors.YELLOW if self.move == 'O' else ft.colors.RED
            },
            bgcolor={
                ft.MaterialState.DEFAULT: '#DAFB3F',
                ft.MaterialState.DISABLED: '#1240AB'
            },
            animation_duration=500,
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
            },
            shape={
                ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
            },

        )

    def btn_style(self):
        style_for_btn = ft.ButtonStyle(
            bgcolor={
                ft.MaterialState.DEFAULT: '#DAFB3F',
                ft.MaterialState.DISABLED: '#1240AB'
            },
            animation_duration=500,
            side={
                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
            },
            shape={
                ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
            },

        )
        self.page.update()
        self.update()
        return style_for_btn

    def btn_new_game(self):
        style_for_btn = ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_ACCENT,
            color=ft.colors.ORANGE_300
        )
        return style_for_btn
