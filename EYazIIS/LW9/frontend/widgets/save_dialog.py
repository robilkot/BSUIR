import flet as ft
from typing import Callable
from datetime import datetime


class SaveDialog:

    def __init__(self, on_save_complete: Callable):
        self.on_save_complete = on_save_complete
        self.file_picker = ft.FilePicker(on_result=self._file_saved)
        self.save_text = ""

    def _file_saved(self, e: ft.FilePickerResultEvent):
        if e.path:
            try:
                with open(e.path, 'w', encoding='utf-8') as f:
                    f.write(self.save_text)

                self.on_save_complete(e.path)
            except Exception as ex:
                self.on_save_complete(None, str(ex))

    def save_file(self, content: str, suggested_name: str = None):
        self.save_text = content

        if suggested_name is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            suggested_name = f"реферат_{timestamp}.txt"

        self.file_picker.save_file(
            file_name=suggested_name,
            file_type=ft.FilePickerFileType.CUSTOM,
            allowed_extensions=["txt"]
        )

    def get_file_picker(self) -> ft.FilePicker:
        return self.file_picker