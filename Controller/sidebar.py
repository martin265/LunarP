import flet as ft


class SidebarMenu:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
