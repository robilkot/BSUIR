import flet as ft
from typing import Callable


class ActionButtons:
    """Виджет кнопок действий"""

    def __init__(self, on_generate: Callable, on_save: Callable, on_help: Callable):
        self.on_generate = on_generate
        self.on_save = on_save
        self.on_help = on_help

    def build(self) -> ft.Control:
        """Строит виджет кнопок"""
        return ft.Row([
            ft.ElevatedButton(
                "Сгенерировать заново",
                icon=ft.Icons.REFRESH,
                on_click=self.on_generate,
                style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE)
            ),
            ft.ElevatedButton(
                "Сохранить результаты",
                icon=ft.Icons.SAVE,
                on_click=self.on_save
            ),
            ft.ElevatedButton(
                "Справка",
                icon=ft.Icons.HELP,
                on_click=self.on_help
            ),
        ])