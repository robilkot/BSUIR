from tkinter import filedialog
from typing import Callable

from model import NLPDatabase


class FileSystem:
    on_file_opened: list[Callable[[str | NLPDatabase], None]] = []

    @staticmethod
    def __on_file_opened(content: str | NLPDatabase) -> None:
        for entry in FileSystem.on_file_opened:
            entry(content)

    @staticmethod
    def open_file():
        file_path = filedialog.askopenfilename(title="Open a file",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                FileSystem.__on_file_opened(content)


    @staticmethod
    # todo serialize nlpdatabase
    def save_file(content):
        file_path = filedialog.asksaveasfilename(title="Save a file", defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                print(content)
                file.write(content)


