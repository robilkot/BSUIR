import flet as ft
from frontend.models.app_state import AppState

class LanguageSelector:

    def __init__(self, app_state: AppState):
        self.app_state = app_state
        self.dropdown = ft.Dropdown(
            width=150,
            value=self.app_state.current_language,
            options=[
                ft.dropdown.Option("russian", "Русский"),
                ft.dropdown.Option("english", "English"),
            ],
            on_change=self._on_language_change
        )

    def _on_language_change(self, e):
        self.app_state.update_state(current_language=e.control.value)

    def build(self) -> ft.Control:
        return ft.Row([
            ft.Text("Язык текста:", size=16),
            self.dropdown,
        ], alignment=ft.MainAxisAlignment.START)