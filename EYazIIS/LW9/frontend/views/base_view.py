import flet as ft
from abc import ABC, abstractmethod
from typing import List


class BaseView(ABC):

    def __init__(self, page: ft.Page, app_state):
        self.page = page
        self.app_state = app_state
        self.controls_list: List[ft.Control] = []
        self._build_view()

    @abstractmethod
    def _build_view(self):
        pass

    def get_content(self) -> ft.Control:
        return ft.Container(
            content=ft.Column(self.controls_list, scroll=ft.ScrollMode.AUTO),
            padding=20,
            expand=True
        )

    def refresh(self):
        pass

    def show_snackbar(self, message: str):
        self.page.snack_bar = ft.SnackBar(ft.Text(message))
        self.page.snack_bar.open = True
        self.page.update()