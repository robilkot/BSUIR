from fs import FileSystem
from model import NLPDatabase
from processor import convert_text_to_db
from tkinter import Menu, messagebox, ttk
import tkinter as tk

from view.table import Table
from view.workspace import Workspace


# Класс, отвечающий за композицию всех компонентов в единое целое
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(expand=True, fill=tk.BOTH)

        self.workspace = Workspace(self.paned_window)
        self.table = Table(self.paned_window)

        self.paned_window.add(self.workspace)
        self.paned_window.add(self.table)

        self.__init_event_handlers()

        self.title("LW1")
        self.geometry('1024x640')
        self.resizable(True, True)
        self.create_widgets()
        self.mainloop()

    def __init_event_handlers(self):
        FileSystem.on_file_opened.append(lambda content: self.set_db(content))

    def create_widgets(self):
        main_menu = Menu(self)

        self.file_menu = Menu(main_menu, tearoff=0)
        self.file_menu.add_command(label="Открыть", command=lambda: FileSystem.open_file())
        self.file_menu.add_command(label="Сохранить как", command=lambda: FileSystem.save_file(content=self.table.db), state='disabled')
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Выход", command=self.quit)

        main_menu.add_cascade(label="Файл", menu=self.file_menu)

        about_menu = Menu(main_menu, tearoff=0)
        about_menu.add_command(label="О программе", command=self.show_about)
        main_menu.add_cascade(label="О программе", menu=about_menu)

        self.config(menu=main_menu)
        self.__center_window(1024, 640)

    def set_db(self, content: NLPDatabase | str):
        if isinstance(content, NLPDatabase):
            db = content
        else:
            db = convert_text_to_db(content)

        if db.source_text == '' or db.source_text is None:
            self.file_menu.entryconfig("Сохранить как", state="disabled")
        else:
            self.file_menu.entryconfig("Сохранить как", state="normal")

        self.workspace.set_db(db)
        self.table.set_db(db)

    def __center_window(self, w, h):
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws / 2) - (w / 2), (hs / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def show_about(self):
        messagebox.showinfo("О программе", "Программа предназначена для базового анализа текстов русского языка "
                                           "(подсчет словоформ, выделение лемм, морфологической информации и количества вхождений в текст). "
                                           "Разработчики: Абушкевич А.А., Робилко Т.М.")
