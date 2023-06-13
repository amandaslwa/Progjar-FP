import flet as ft
from chat_message import *
class GroupMessage():
    def __init__(self,group:str,user:str,text:str,message_type:str):
        self.group=group
        self.user=user
        self.text=text
        self.message_type=message_type

class ChatGroupMessage(ft.Row):
    def __init__(self, message: GroupMessage):
        super().__init__()
        self.vertical_alignment="start"
        self.controls=[
            ft.CircleAvatar(
                bgcolor=self.get_avatar_color(message.group)
            ),
            ft.Column(
                [
                    ft.Text(message.group, weight="bold"),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def get_avatar_color(self, group: str):
        colors_lookup = [
            ft.colors.AMBER,
            ft.colors.BLUE,
            ft.colors.BROWN,
            ft.colors.CYAN,
            ft.colors.GREEN,
            ft.colors.INDIGO,
            ft.colors.LIME,
            ft.colors.ORANGE,
            ft.colors.PINK,
            ft.colors.PURPLE,
            ft.colors.RED,
            ft.colors.TEAL,
            ft.colors.YELLOW,
        ]
        return colors_lookup[hash(group) % len(colors_lookup)]