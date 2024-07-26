import flet as ft
from game.game_board import Main
from game.menu import Menu
from game.login import Login
from game.generatinon_code import GenerationCode
from game.create_player import CreatePlayer
from game.create_or_login_user import LoginOrCreateUser
from game.profile_user import ProfileUser
from game.invite_friend import InviteFriends
from game.friend import Friend

def main(page: ft.Page):

    game = Main(page)
    menu = Menu(page)
    generation_code = GenerationCode()
    player = CreatePlayer()
    login_or_create_user = LoginOrCreateUser(page)
    friend = Friend(page)
    invite_friends = InviteFriends(page, friend)
    profile_user = ProfileUser(page)
    login = Login(page, profile_user, invite_friends, friend)
    page.window_center()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
                    login_or_create_user.view()
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                bgcolor=ft.colors.BLUE_100
            )
        )
        if page.route == '/login':
            page.views.append(
                ft.View(
                    '/login',
                    [
                        login.view()
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )

            )
        if page.route == '/menu':
            page.views.append(
                ft.View(
                    '/menu',
                    [
                        menu.cont
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )
            )
        if page.route == '/profile_user':
            page.views.append(
                ft.View(
                    '/profile_user',
                    [
                        profile_user.view()
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )

            )
        if page.route == '/game':
            page.views.append(
                ft.View(
                    '/game',
                    [
                        game.view()
                    ],
                    horizontal_alignment=ft.alignment.center,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )

            )
        if page.route == '/generation_code':
            page.views.append(
                ft.View(
                    '/generation_code',
                    [
                        generation_code.view(page)
                    ]

                )

            )
        if page.route == '/create_player':
            page.views.append(
                ft.View(
                    '/create_player',
                    [
                        player.view(page)
                    ]
                )

            )
        if page.route == '/invite_friends':
            page.views.append(
                ft.View(
                    '/invite_friends',
                    [
                        invite_friends.view(),

                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )
            )

        if page.route == '/friends':
            page.views.append(
                ft.View(
                    '/friends',
                    [
                        friend.view(),

                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    bgcolor=ft.colors.BLUE_100
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
    print(page.route)
    page.go('/login')
    page.window_width = 400
    page.window_height = 500
    page.window_center()
    page.update()


ft.app(target=main)
