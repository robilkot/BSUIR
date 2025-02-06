from tkinter import filedialog
from typing import Callable
import json
import jsonpickle
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
                                               filetypes=[("Text files", "*.txt"), ("NLP Files", "*.nlp"), ("All files", "*.*")])
        if file_path:
            if file_path.endswith(".txt"):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    FileSystem.__on_file_opened(content)
            if file_path.endswith(".nlp"):
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    content = json.load(json_file)
                    FileSystem.__on_file_opened(content)


    @staticmethod
    # todo serialize nlpdatabase
    def save_file(content):
        file_path = filedialog.asksaveasfilename(title="Save a file", defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("NLP Files", "*.nlp"), ("All files", "*.*")])
        if file_path:
            if file_path.endswith(".txt"):
                with open(file_path, 'w', encoding='utf-8') as file:
                    print(content)
                    file.write(content)
            if file_path.endswith(".nlp"):
                with open(file_path, 'w', encoding='utf-8') as json_file:
                    content = jsonpickle.encode(content)
                    print(content)
                    json.dump(content, json_file)



