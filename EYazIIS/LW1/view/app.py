from fs import FileSystem
from model import NLPDatabase
from processor import convert_text_to_db
from tkinter import Menu, messagebox
import tkinter as tk

from view.table import Table
from view.workspace import Workspace


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(expand=True, fill=tk.BOTH)

        self.workspace = Workspace(self.paned_window)
        self.table = Table(self.paned_window)

        self.paned_window.add(self.workspace, minsize=200)
        self.paned_window.add(self.table, minsize=200)

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

        file_menu = Menu(main_menu, tearoff=0)
        file_menu.add_command(label="Open", command=lambda: FileSystem.open_file())
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        main_menu.add_cascade(label="File", menu=file_menu)

        about_menu = Menu(main_menu, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about)
        main_menu.add_cascade(label="Help", menu=about_menu)

        self.config(menu=main_menu)
        self.__center_window(1024, 640)

    def set_db(self, content: NLPDatabase | str):
        if isinstance(content, NLPDatabase):
            db = content
        else:
            db = convert_text_to_db(content)

        self.workspace.set_db(db)
        self.table.set_db(db)

    def __center_window(self, w, h):
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws / 2) - (w / 2), (hs / 2) - (h / 2)

        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def show_about(self):
        messagebox.showinfo("About", "праграма для языков чтоб разложить текст")
