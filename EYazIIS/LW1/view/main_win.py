from tkinter import ttk
from view.table import Table
from view.workspace import Workspace
import tkinter as tk


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove", borderwidth=1)
        self.pack(expand=True, fill=tk.BOTH)

        self.workspace = Workspace(self)
        self.table = Table(self)
