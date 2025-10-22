import flet as ft

from frontend.views.base_view import BaseView
from frontend.widgets.action_buttons import ActionButtons
from frontend.widgets.file_picker import FilePickerWidget
from frontend.widgets.language_selector import LanguageSelector


class InputView(BaseView):

    def _build_view(self):
        title = ft.Text(
            "Система автоматического реферирования текста",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        language_selector = LanguageSelector(self.app_state)

        abstract_type_selector = self._build_abstract_type_selector()

        self.file_picker_widget = FilePickerWidget(self._on_file_selected)

        self.text_field = ft.TextField(
            label="Введите текст для реферирования",
            multiline=True,
            min_lines=10,
            max_lines=15,
            expand=True,
            on_change=self._on_text_change
        )

        action_buttons = ActionButtons(
            on_generate=self._generate_abstract,
            on_save=None,
            on_help=self._show_help
        )

        self.controls_list = [
            title,
            ft.Divider(),
            language_selector.build(),
            abstract_type_selector,
            ft.Divider(),
            ft.Text("Ввод текста:", size=18, weight=ft.FontWeight.BOLD),
            self.file_picker_widget.build(),
            self.text_field,
            action_buttons.build()
        ]

    def _build_abstract_type_selector(self) -> ft.Control:
        return ft.Row([
            ft.Text("Тип реферата:", size=16),
            ft.Dropdown(
                width=200,
                value=self.app_state.abstract_type,
                options=[
                    ft.dropdown.Option("classic", "Классический реферат"),
                    ft.dropdown.Option("keywords", "Ключевые слова"),
                    ft.dropdown.Option("both", "Оба типа"),
                ],
                on_change=self._on_abstract_type_change
            )
        ], alignment=ft.MainAxisAlignment.START)

    def _on_text_change(self, e):
        self.app_state.update_state(current_text=e.control.value)

    def _on_file_selected(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            self.text_field.value = text
            self.text_field.update()
            self.app_state.update_state(current_text=text, file_path=file_path)
        except Exception as e:
            self.show_snackbar(f"Ошибка чтения файла: {str(e)}")

    def _on_abstract_type_change(self, e):
        self.app_state.update_state(abstract_type=e.control.value)

    def _generate_abstract(self, e):
        if not self.app_state.current_text.strip():
            self.show_snackbar("Введите текст для реферирования")
            return
        self.page.go("/results")

    def _show_help(self, e):
        self.page.go("/help")

    def get_file_picker(self):
        return self.file_picker_widget.get_file_picker()