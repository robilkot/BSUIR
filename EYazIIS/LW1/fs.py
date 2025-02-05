from tkinter import filedialog
from typing import Callable


def open_file(on_success: Callable):
    file_path = filedialog.askopenfilename(title="Open a file",
                                           filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            on_success(content)


# todo serialize nlpdatabase
def save_file(self, content):
    file_path = filedialog.asksaveasfilename(title="Save a file", defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            print(content)
            file.write(content)
