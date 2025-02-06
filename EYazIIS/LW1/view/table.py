from tkinter import ttk
import tkinter as tk

from model import NLPDatabase


class Table(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief="groove")
        self.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)
        self.create_table_widgets()
        self.db: None | NLPDatabase = None
        self.editing_entry = None  # Для хранения виджета Entry

    def set_db(self, db: NLPDatabase):
        self.db = db
        for item in self.table.get_children():
            self.table.delete(item)

        for lemma, forms in sorted(db.items(), key=lambda kvp: kvp[0].lemma):
            for form in sorted(forms.items(), key=lambda f: f[0]):
                frequency = form[1].frequency
                morph_info = form[1].note

                self.table.insert('', tk.END, values=(form[0], lemma, morph_info, frequency))

    def create_table_widgets(self):
        columns = ("Словоформа", "Лемма", "Морфологическая информация", "Частота появления")
        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        for column in columns:
            self.table.heading(column, text=column)
            self.table.column(column, stretch=True, width=100)

        # Привязываем событие двойного щелчка
        self.table.bind("<Double-1>", self.on_double_click)

    def on_double_click(self, event):
        # Получаем выбранный элемент
        selected_item = self.table.selection()
        if selected_item:
            item = self.table.item(selected_item)
            column = self.table.identify_column(event.x)
            col_index = int(column.replace('#', '')) - 1  # Индекс колонки

            # Получаем координаты ячейки
            x, y, width, height = self.table.bbox(selected_item, column)

            # Создаем Entry для редактирования
            self.editing_entry = tk.Entry(self)
            self.editing_entry.insert(0, item['values'][col_index])
            self.editing_entry.place(x=x, y=y, width=width, height=height)
            self.editing_entry.focus()

            # Устанавливаем обработчик для сохранения изменений
            self.editing_entry.bind("<Return>", lambda e: self.save_changes(selected_item, col_index))
            self.editing_entry.bind("<FocusOut>", lambda e: self.cancel_edit(selected_item))

    def save_changes(self, selected_item, col_index):
        new_value = self.editing_entry.get()
        current_values = list(self.table.item(selected_item)['values'])
        current_values[col_index] = new_value
        self.table.item(selected_item, values=current_values)
        self.editing_entry.destroy()

    def cancel_edit(self, selected_item):
        if self.editing_entry:
            self.editing_entry.destroy()