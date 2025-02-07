from tkinter import ttk
import tkinter as tk

from model import NLPDatabase, FormInfo


# Класс, представляющий таблицу в правой части интерфейса
# и обеспечивающий отображение словаря с информацией о словоформах
class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief=tk.GROOVE)
        self.pack(fill=tk.BOTH, side=tk.BOTTOM)

        self.db: None | NLPDatabase = None
        self.search_string: tk.StringVar = tk.StringVar()
        self.search_string.trace("w", lambda var, index, mode: self.__on_search_string_changed())
        self.__editing_entry = None
        self.__table_entry_mapping: dict[str, FormInfo] = {}

        self.create_table_widgets()

    # Обработчик события изменения критерия поиска
    def __on_search_string_changed(self):
        if self.db:
            new_search_string = self.search_string.get()
            self.show_filtered_table(new_search_string)

    # Функция установки базы данных
    def set_db(self, db: NLPDatabase):
        self.db = db
        self.search_string.set('')
        self.show_filtered_table(self.search_string.get())

    # Функция показа таблицы по заданному критерию поиска
    def show_filtered_table(self, search_string: str):
        self.__table_entry_mapping = {}

        for item in self.table.get_children():
            self.table.delete(item)

        for lemma, forms in sorted(self.db.items(), key=lambda kvp: kvp[0].lemma):
            for f in [form for form in sorted(forms.items(), key=lambda f: f[0]) if form[0].count(search_string) > 0]:
                form = f[0]
                form_info = f[1]
                frequency = form_info.frequency
                morph_info = form_info.note

                item = self.table.insert('', tk.END, values=(form, lemma, morph_info, frequency))
                self.__table_entry_mapping[item] = form_info

    # Функция созданиия элементов UI
    def create_table_widgets(self):
        search_entry_label = tk.Label(master=self, text="Поиск по словоформам:")
        search_entry_label.pack(side=tk.TOP, anchor=tk.W)

        self.search_entry = tk.Entry(master=self, textvariable=self.search_string)
        self.search_entry.pack(side=tk.TOP, fill=tk.X)
        self.search_entry.bind('')

        columns = ("Словоформа", "Лемма", "Морфологическая информация", "Количество вхождений")
        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        for column in columns:
            self.table.heading(column, text=column)
            self.table.column(column, stretch=True, width=100)

        # Привязываем событие двойного щелчка
        self.table.bind("<Double-1>", self.on_double_click)

    # Обработчик двойного нажатия на ячейки таблицы
    def on_double_click(self, event):
        # Получаем выбранный элемент
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            column = self.table.identify_column(event.x)
            col_index = int(column.replace('#', '')) - 1  # Индекс колонки

            if col_index == 2:  # Только морфологическая информация
                # Получаем координаты ячейки
                x, y, width, height = self.table.bbox(selected_item, column)

                # Создаем Entry для редактирования
                self.__editing_entry = tk.Entry(self.table)
                self.__editing_entry.insert(0, item['values'][col_index])
                self.__editing_entry.place(x=x, y=y, width=width, height=height)
                self.__editing_entry.focus()

                # Устанавливаем обработчик для сохранения изменений
                self.__editing_entry.bind("<Return>", lambda e: self.save_changes(selected_item, col_index))
                self.__editing_entry.bind("<FocusOut>", lambda e: self.cancel_edit(selected_item))

    def save_changes(self, selected_item, col_index):
        new_value = self.__editing_entry.get()
        current_values = list(self.table.item(selected_item)['values'])
        current_values[col_index] = new_value

        self.__table_entry_mapping[selected_item[0]].note = new_value

        self.table.item(selected_item, values=current_values)
        self.__editing_entry.destroy()

    def cancel_edit(self, selected_item):
        if self.__editing_entry:
            self.__editing_entry.destroy()
