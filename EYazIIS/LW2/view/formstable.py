from tkinter import ttk
import tkinter as tk

from dicts import MORPH_FEATURES_TRANSLATIONS, MORPH_VALUES_TRANSLATIONS, POS_APPLICABLE_FEATURES

class FormsTable(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, side=tk.BOTTOM)

        self.n = 4

        self.db: dict = {}
        self.search_string: tk.StringVar = tk.StringVar()
        # Фильтруем словарь, оставляя те признаки, где вариантов больше одного
        self.MORPH_VALUES = {key: values for key, values in MORPH_VALUES_TRANSLATIONS.items() if len(values) > 1}
        # Добавляем вариант "None" для каждого признака
        for k, v in self.MORPH_VALUES.items():
            v["None"] = "-"

        # Создаем переменные для хранения выбранных критериев
        self.criteria_vars = {key: tk.StringVar(value="None") for key in self.MORPH_VALUES.keys()}


        # Словарь для хранения ссылок на комбобоксы
        self.criteria_dropdowns = {}

        self.__editing_entry = None

        self.create_table_widgets()

    def search_function(self):
        # Получаем поисковую строку и приводим её к нижнему регистру
        search_text = self.search_string.get().strip().lower()
        # Собираем выбранные критерии; по умолчанию они установлены в "None"
        selected_criteria = {key: self.criteria_vars[key].get() for key in self.criteria_vars}
        self.show_filtered_table(search_text, selected_criteria)

    def set_data(self, db: dict):
        self.db = db
        self.search_string.set('')
        self.search_function()

    # Функция показа таблицы по заданному критерию поиска и выбранным критериям морфологии
    def show_filtered_table(self, search_string: str, criteria: dict):
        # Очистка таблицы
        for item in self.table.get_children():
            self.table.delete(item)

        for item in sorted(self.db.items(), key=lambda kvp: kvp[1]['lemma']):
            wordform = item[0]
            lemma = item[1]['lemma']
            morph = item[1].get('morph', {})

            # Если поисковая строка не пуста, проверяем наличие подстроки в словоформе или лемме
            if search_string:
                if search_string not in wordform.lower() and search_string not in lemma.lower():
                    continue

            # Проверка по выбранным критериям
            criteria_match = True
            for crit, selected_value in criteria.items():
                if selected_value != "None":
                    # Если критерий отсутствует или его значение не совпадает – исключаем запись
                    if crit not in morph or morph[crit] != selected_value:
                        criteria_match = False
                        break

            if not criteria_match:
                continue

            try:
                self.table.insert('', tk.END, values=(
                    wordform,
                    lemma,
                    item[1]['freq'],
                    self.to_feats_str(morph)
                ))
            except Exception as e:
                print(wordform, e)

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

        # Создаем комбобоксы для выбора морфологических критериев
        for index, (criteria, values) in enumerate(self.MORPH_VALUES.items()):
            row = index // self.n  # Определяем строку
            col = (index % self.n) * 2  # Каждый критерий занимает 2 столбца

            label = tk.Label(master=criteria_frame, text=criteria + ":")
            label.grid(row=row, column=col, sticky="W", padx=5, pady=2)

            dropdown = ttk.Combobox(master=criteria_frame, textvariable=self.criteria_vars[criteria],
                                    values=list(values.keys()), state="readonly")
            dropdown.grid(row=row, column=col + 1, padx=5, pady=2, sticky="W")
            self.criteria_dropdowns[criteria] = dropdown

            # Если это критерий для выбора части речи, привязываем обработчик
            if criteria == "pos":
                dropdown.bind("<<ComboboxSelected>>", self.on_pos_change)

        columns = ("Словоформа", "Лемма", "Вхождения", "Морфологическая информация")
        columns_sizes = (100, 100, 20, 200)

        self.table = ttk.Treeview(master=self, columns=columns, show="headings")
        self.table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

        for column, size in zip(columns, columns_sizes):
            self.table.heading(column, text=column)
            self.table.column(column, stretch=True, width=size)

    def on_pos_change(self, event):
        """Обновляет доступность морфологических критериев в зависимости от выбранной части речи."""
        selected_pos = self.criteria_vars["pos"].get()
        # Получаем список применимых признаков для выбранной части речи,
        # если его нет – считаем, что применимы все
        applicable = POS_APPLICABLE_FEATURES.get(selected_pos, list(self.MORPH_VALUES.keys()))
        for feature, dropdown in self.criteria_dropdowns.items():
            # Пропускаем сам критерий "pos"
            if feature == "pos":
                continue
            if feature in applicable:
                dropdown.configure(state="readonly")
            else:
                dropdown.configure(state="disabled")
                # Устанавливаем значение "None" для недоступных признаков
                self.criteria_vars[feature].set("None")
