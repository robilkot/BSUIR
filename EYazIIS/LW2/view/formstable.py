from tkinter import ttk
import tkinter as tk


# Класс, представляющий таблицу в правой части интерфейса
# и обеспечивающий отображение словаря с информацией о словоформах
class FormsTable(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, side=tk.BOTTOM)

        self.db: dict = {}
        self.search_string: tk.StringVar = tk.StringVar()
        self.search_string.trace("w", lambda var, index, mode: self.__on_search_string_changed())
        self.__editing_entry = None

        self.create_table_widgets()

    # Обработчик события изменения критерия поиска
    def __on_search_string_changed(self):
        if self.db:
            new_search_string = self.search_string.get()
            self.show_filtered_table(new_search_string)

    # Функция установки базы данных
    def set_data(self, db: dict):
        self.db = db
        self.search_string.set('')
        self.show_filtered_table(self.search_string.get())

    # Функция показа таблицы по заданному критерию поиска
    def show_filtered_table(self, search_string: str):
        for item in self.table.get_children():
            self.table.delete(item)

        search_string = search_string.lower()

        for item in sorted(self.db.items(), key=lambda kvp: kvp[1]['lemma']):
            if item[0].lower().count(search_string) <= 0 and item[1]['lemma'].count(search_string) <= 0:
                continue
            self.table.insert('', tk.END, values=(item[0], item[1]['lemma'], item[1]['freq'], item[1]['morph']))

    def create_table_widgets(self):
        frame = tk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=15)
        frame.rowconfigure(0, weight=15)
        search_entry_label = tk.Label(master=frame, text="Поиск по подстроке:")
        search_entry_label.grid(row=0, column=0)
        frame.pack(fill=tk.X, expand=1)

        self.search_entry = tk.Entry(master=frame, textvariable=self.search_string)
        self.search_entry.grid(row=0, column=1, padx=5, pady=2, sticky="NSEW")
        self.search_entry.bind('')

        columns = ("Словоформа", "Лемма", "Вхождения", "Морфологическая информация")
        columns_sizes = (100, 100, 20, 200)
        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

        for column, size in zip(columns, columns_sizes):
            self.table.heading(column, text=column)
            self.table.column(column, stretch=True, width=size)
