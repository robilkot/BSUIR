import flet as ft
import os
from typing import Callable

class FilePickerWidget:

    def __init__(self, on_file_selected: Callable):
        self.on_file_selected = on_file_selected
        self.file_picker = ft.FilePicker(on_result=self._file_selected)
        self.selected_file_text = ft.Text("Файл не выбран", size=14)

    def _file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            self.selected_file_text.value = f"Выбран: {os.path.basename(file_path)}"
            self.on_file_selected(file_path)

    def pick_files(self, e):
        self.file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["txt", "doc", "docx"]
        )

    def build(self) -> ft.Control:
        return ft.Column([
            ft.Row([
                ft.ElevatedButton(
                    "Выбрать файл",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=self.pick_files,
                ),
                self.selected_file_text,
            ]),
            ft.Text("Поддерживаемые форматы: .txt, .doc, .docx", size=12, color=ft.Colors.GREY)
        ])

    def get_file_picker(self) -> ft.FilePicker:
        return self.file_picker