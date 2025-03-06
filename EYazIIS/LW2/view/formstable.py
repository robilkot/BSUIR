from tkinter import ttk
import tkinter as tk

from dicts import MORPH_FEATURES_TRANSLATIONS, MORPH_VALUES_TRANSLATIONS


# Класс, представляющий таблицу в правой части интерфейса
# и обеспечивающий отображение словаря с информацией о словоформах
class FormsTable(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, side=tk.BOTTOM)

        self.n = 4

        self.db: dict = {}
        self.search_string: tk.StringVar = tk.StringVar()
        self.MORPH_VALUES = {key: values for key, values in MORPH_VALUES_TRANSLATIONS.items() if len(values) > 1}
        for k, v in self.MORPH_VALUES.items():
            v["None"] = "-"

        self.criteria_vars = {key: tk.StringVar(value=list(values.keys())[0])
                              for key, values in self.MORPH_VALUES.items()}

        self.__editing_entry = None

        self.create_table_widgets()

    def search_function(self):
        search_text = self.search_string.get()
        selected_criteria = {key: self.criteria_vars[key].get() for key in self.criteria_vars}
        self.show_filtered_table(search_text)

    def set_data(self, db: dict):
        self.db = db
        self.search_string.set('')
        self.search_function()

    # Функция показа таблицы по заданному критерию поиска
    def show_filtered_table(self, search_string: str):
        for item in self.table.get_children():
            self.table.delete(item)

        search_string = search_string.lower()

        for item in sorted(self.db.items(), key=lambda kvp: kvp[1]['lemma']):
            if item[0].lower().count(search_string) <= 0 and item[1]['lemma'].count(search_string) <= 0:
                continue
            try:
                feats = item[1]['morph']
                self.table.insert('', tk.END, values=(
                    item[0],
                    item[1]['lemma'],
                    item[1]['freq'],
                    self.to_feats_str(feats)
                ))
            except:
                print(item[0], feats)

    def to_feats_str(self, feats_dict) -> str:
        pairs = []

        for feat, value in feats_dict.items():
            key = MORPH_FEATURES_TRANSLATIONS.get(feat, feat)
            values_dict = MORPH_VALUES_TRANSLATIONS.get(feat, {})
            value = values_dict.get(value, value)
            pairs.append(f"{key}: {value}")

        return ", ".join(pairs)

    def create_table_widgets(self):
        frame = tk.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=15)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(0, weight=15)
        frame.pack(fill=tk.X, expand=1)

        search_entry_label = tk.Label(master=frame, text="Поиск по подстроке:")
        search_entry_label.grid(row=0, column=0)

        self.search_entry = tk.Entry(master=frame, textvariable=self.search_string)
        self.search_entry.grid(row=0, column=1, padx=5, pady=2, sticky="NSEW")
        self.search_entry.bind('<Return>', lambda event: self.search_function())

        search_button = tk.Button(master=frame, text="Поиск", command=self.search_function)
        search_button.grid(row=0, column=2, padx=5)

        criteria_frame = tk.Frame(self)
        criteria_frame.pack(fill=tk.X, padx=5, pady=5)

        for index, (criteria, values) in enumerate(self.MORPH_VALUES.items()):
            row = index // self.n  # Определяем строку
            col = (index % self.n) * 2  # Определяем столбец, каждый критерий занимает 2 столбца

            label = tk.Label(master=criteria_frame, text=criteria + ":")
            label.grid(row=row, column=col, sticky="W", padx=5, pady=2)

            dropdown = ttk.Combobox(master=criteria_frame, textvariable=self.criteria_vars[criteria],
                                    values=list(values.keys()), state="readonly")
            dropdown.grid(row=row, column=col + 1, padx=5, pady=2, sticky="W")

        columns = ("Словоформа", "Лемма", "Вхождения", "Морфологическая информация")
        columns_sizes = (100, 100, 20, 200)

        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

        for column, size in zip(columns, columns_sizes):
            self.table.heading(column, text=column)
            self.table.column(column, stretch=True, width=size)
