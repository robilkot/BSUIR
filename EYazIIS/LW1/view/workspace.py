import tkinter as tk
from tkinter import ttk
from typing import Callable

import fs


class Workspace(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.__text: tk.Text = None
        self.__open_text_button: tk.Button = None
        self.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.create_workspace_widgets()
        self.on_text_changed: list[Callable] = []

    def set_text(self, text: str):
        self.__text.config(state=tk.NORMAL)
        self.__text.delete(1.0, tk.END)
        self.__text.insert(tk.END, text)
        self.__text.config(state=tk.DISABLED)

        if text == '' or text is None:
            self.__open_text_button.pack()
            self.__text.pack_forget()
        else:
            self.__open_text_button.pack_forget()
            self.__show_text()

        for func in self.on_text_changed:
            func(text)

    def __show_text(self):
        self.__text.pack(expand=True, fill=tk.BOTH)

    def create_workspace_widgets(self):
        self.__text = tk.Text(self)
        self.__text.config(state=tk.DISABLED)

        self.__open_text_button = tk.Button(self, text="Открыть файл",
                                            command=lambda: fs.open_file(lambda content: self.set_text(content)))
        self.__open_text_button.pack()

        state_footer = ttk.Frame(self, relief="groove", borderwidth=1)
        state_footer.pack(side=tk.BOTTOM, expand=False, anchor=tk.W)

        curr_file = tk.Label(state_footer, text="Текущий файл:")
        curr_file.pack(side=tk.LEFT, anchor=tk.W)

        words_num = tk.Label(state_footer, text="Количество слов:")
        words_num.pack(side=tk.LEFT, anchor=tk.W)

        other_label = tk.Label(state_footer, text="Количество ещё чего-нибудь:")
        other_label.pack(side=tk.LEFT, anchor=tk.W)
