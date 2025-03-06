import string
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from corpus_manager import CorpusManager
from view.scrollable_frame import Scrollable
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from view.formstable import FormsTable
from dicts import *

class CorpusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Corpus Manager")
        self.geometry("1200x700")
        self.corpus_manager = CorpusManager()
        self.create_menu()
        self.create_widgets()

        self.entries_dict = {}

        self.add_text_from_file('./dataset/5.txt')
        self.add_text_from_file('./dataset/7.txt')
        self.add_text_from_file('./dataset/11.txt')
        self.add_text_from_file('./dataset/17.txt')
        self.add_text_from_file('./dataset/19.txt')

    def create_menu(self):
        self.menubar = tk.Menu(self)
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="Открыть", command=self.open_file)
        file_menu.add_command(label="Сохранить", command=self.save_file)
        self.menubar.add_cascade(label="Файл", menu=file_menu)
        edit_menu = tk.Menu(self.menubar, tearoff=0)
        edit_menu.add_command(label="Добавить текст из файла", command=self.propmt_user_to_add_text_from_file)
        self.menubar.add_cascade(label="Редактирование", menu=edit_menu)
        self.config(menu=self.menubar)

    def create_widgets(self):
        # Разбивка окна на левую и правую части
        paned_window = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(expand=True, fill=tk.BOTH)

        self.left_frame = tk.Frame(paned_window)
        self.right_frame = tk.Frame(paned_window)

        paned_window.add(self.left_frame)
        paned_window.add(self.right_frame)

        # Левая панель – список записей с вертикальной прокруткой
        self.entry_container = Scrollable(self.left_frame)
        # Правая панель – область для вывода таблиц частотных характеристик и элементов поиска
        self.data_container = Scrollable(self.right_frame)
        data_static_container = tk.Frame(self.data_container)
        self.data_dynamic_container = tk.Frame(self.data_container)

        # Область для конкордансного поиска
        concordance_frame = ttk.LabelFrame(data_static_container, text="Конкордансный поиск")
        concordance_frame.pack(fill=tk.BOTH, padx=5, pady=5, expand=True)
        concordance_frame.columnconfigure(0, weight=1)
        concordance_frame.columnconfigure(1, weight=1)

        self.concordance_entry = ttk.Entry(concordance_frame)
        self.concordance_entry.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.concordance_entry.bind("<Return>", lambda event: self.search_concordance())

        self.concordance_button = ttk.Button(concordance_frame, text="Построить конкорданс", command=self.search_concordance)
        self.concordance_button.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

        self.concordance_results = tk.Frame(concordance_frame)
        self.concordance_results.columnconfigure(0, weight=1)
        self.concordance_results.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        # Область для поиска по морфологическим признакам
        morph_frame = ttk.LabelFrame(data_static_container, text="Поиск по морфологическим признакам")
        morph_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        criteria_frame = tk.Frame(morph_frame)
        criteria_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(criteria_frame, text="Часть речи:").grid(row=0, column=0, padx=2, pady=2)
        self.pos_entry = tk.Entry(criteria_frame)
        self.pos_entry.grid(row=0, column=1, padx=2, pady=2)
        ttk.Label(criteria_frame, text="Род:").grid(row=1, column=0, padx=2, pady=2)
        self.gender_var = tk.StringVar(value="Любой")
        # todo перевести
        gender_options = ["Любой", "Masc", "Fem", "Neut"]
        self.gender_menu = ttk.OptionMenu(criteria_frame, self.gender_var, *gender_options)
        self.gender_menu.grid(row=1, column=1, padx=2, pady=2)
        ttk.Label(criteria_frame, text="Число:").grid(row=2, column=0, padx=2, pady=2)
        self.number_var = tk.StringVar(value="Любой")
        # todo перевести
        number_options = ["Любой", "Sing", "Plur"]
        self.number_menu = ttk.OptionMenu(criteria_frame, self.number_var, *number_options)
        self.number_menu.grid(row=2, column=1, padx=2, pady=2)
        self.morph_search_button = ttk.Button(morph_frame, text="Поиск по критериям", command=self.search_morph)
        self.morph_search_button.pack(padx=5, pady=5)
        self.morph_results_text = tk.Text(morph_frame, height=10)
        self.morph_results_text.pack(fill=tk.BOTH, padx=5, pady=5)

        data_static_container.pack(fill=tk.X, padx=5, pady=5, expand=True)
        self.data_dynamic_container.pack(fill=tk.X, padx=5, pady=5, expand=True)

        self.refresh_entries()
        self.entry_container.update()
        self.data_container.update()

    def refresh_entries(self):
        for widget in self.entry_container.winfo_children():
            widget.destroy()

        for entry_id, entry in self.corpus_manager.entries.items():
            frame = tk.Frame(self.entry_container, bd=1, relief=tk.SOLID, pady=5)
            frame.pack(fill=tk.X, padx=5, pady=5)
            ttk.Label(frame, text=f"ID: {entry_id}").pack(anchor="w", padx=5)
            text_widget = tk.Text(frame, height=10, wrap=tk.WORD)
            text_widget.insert("1.0", entry.text)
            text_widget.configure(state=tk.DISABLED)
            text_widget.pack(fill=tk.X, padx=5, pady=2)
            btn_frame = tk.Frame(frame)
            btn_frame.pack(fill=tk.X, padx=5, pady=2)
            ttk.Button(btn_frame, text="Удалить запись", command=lambda eid=entry_id: self.delete_entry(eid)).pack(side=tk.LEFT, padx=2)
            edit_button = ttk.Button(btn_frame, text="Редактировать")
            edit_button.configure(command=lambda button=edit_button, eid=entry_id, tw=text_widget: self.edit_entry(button, eid, tw))
            edit_button.pack(side=tk.LEFT, padx=2)
            self.entries_dict[entry_id] = text_widget

        self.entry_container.update()


    def delete_entry(self, entry_id):
        if messagebox.askyesno("Подтверждение", "Удалить запись?"):
            self.corpus_manager.delete_entry(entry_id)
            self.refresh_entries()
            self.update_frequencies()

    def edit_entry(self, button, entry_id, text_widget):
        button.configure(state=tk.DISABLED)
        text_widget.configure(state=tk.NORMAL)
        def save_edit():
            new_text = text_widget.get("1.0", tk.END).strip()
            self.corpus_manager.edit_entry(entry_id, new_text)
            text_widget.delete("1.0", tk.END)
            text_widget.insert("1.0", new_text)
            text_widget.configure(state=tk.DISABLED)
            self.update_frequencies()
            save_button.destroy()
            button.configure(state=tk.NORMAL)
        save_button = ttk.Button(text_widget.master, text="Сохранить изменения", command=save_edit)
        save_button.pack(side=tk.RIGHT, padx=2)

    def update_frequencies(self):
        # Очистка панели с таблицами
        for widget in self.data_dynamic_container.winfo_children():
            widget.destroy()

        plt.close('all')

        # Таблица для словоформ
        wordforms_info = self.corpus_manager.get_wordforms_info()
        wordform_frame = ttk.LabelFrame(self.data_dynamic_container, text="Словоформы и леммы")
        wordform_frame.pack(fill=tk.BOTH, padx=5, pady=5)
        table = FormsTable(wordform_frame)
        table.set_data(wordforms_info)
        table.pack(fill=tk.BOTH, expand=True)

        freq = self.corpus_manager.compute_frequency()
        feats_to_skip = [
            "Variant",
            "Aspect",
            "Mood",
            "Polarity",
            "Degree",
            "Foreign",
            "Animacy"
        ]

        feats_with_charts = [
            "pos",
            "Person",
            "Tense",
            "Voice"
        ]
        characteristics = [(feat[0], feat[0] in feats_with_charts) for feat in freq.items() if feat[0] not in feats_to_skip]
        characteristics = sorted(characteristics, key=lambda pair: not pair[1])  # Сперва характеристики с графиками

        total_columns = 4
        column: int = 0
        row: int = 0

        grid = tk.Frame(self.data_dynamic_container)
        for i in range(total_columns):
            grid.columnconfigure(i, weight=1)

        for characteristic, need_plot in characteristics:
            parent = self.data_dynamic_container if need_plot else grid

            table_title = MORPH_FEATURES_TRANSLATIONS[characteristic]
            table_frame = ttk.LabelFrame(parent, text=f"Характеристика: {table_title}")

            tree = ttk.Treeview(table_frame, columns=("pos", "count"), show="headings")
            tree.heading("pos", text=table_title)
            tree.heading("count", text="Количество вхождений")
            if need_plot:
                tree.grid(column=0, row=0, sticky="nsew", padx=5, pady=5)
            else:
                tree.pack(fill=tk.BOTH, padx=5, pady=5)

            for feat, count in freq[characteristic].items():
                readable_feat = MORPH_VALUES_TRANSLATIONS[characteristic].get(feat, feat)
                tree.insert("", tk.END, values=(readable_feat, count))

            if need_plot:
                table_frame.columnconfigure(1, weight=1)
                table_frame.columnconfigure(0, weight=1)
                table_frame.rowconfigure(0, weight=1)

                height_coef = len(freq[characteristic].keys()) / 12 * 3

                labels = [MORPH_VALUES_TRANSLATIONS[characteristic].get(pos, pos) for pos in freq[characteristic].keys()]
                values = list(freq[characteristic].values())

                fig, ax = plt.subplots(figsize=(5, height_coef))
                ax.barh(labels, values, color='orange')
                ax.set_title("Количество вхождений")

                canvas = FigureCanvasTkAgg(fig, master=table_frame)
                canvas_widget = canvas.get_tk_widget()
                canvas_widget.grid(column=1, row=0, sticky="nsew", padx=5, pady=5)
                canvas.draw()
                table_frame.pack(fill=tk.BOTH, padx=5, pady=5)
            else:
                table_frame.grid(sticky='nsew', column=column, row=row)
                column += 1
                if column == total_columns:
                    column = 0
                    row += 1

        grid.pack(fill=tk.BOTH)
        self.data_container.update()

    def search_concordance(self):
        target = self.concordance_entry.get().strip()
        if not target:
            messagebox.showwarning("Внимание", "Введите слово для поиска конкорданса")
            return

        concordances = self.corpus_manager.get_concordance(target)

        for widget in self.concordance_results.winfo_children():
            widget.destroy()

        if concordances:
            for text in self.entries_dict.values():
                text.tag_remove('highlight', 0.0, tk.END)

            for i, c in enumerate(concordances):
                self.concordance_results.rowconfigure(i, weight=1)
                import re

                concordance_text = tk.Text(self.concordance_results, height=2)
                concordance_text.grid(row=i, sticky="we")

                # Метаданные и контекст
                metadata = f"Запись: {c['entry_id']}, позиция: {c['target_index']}\n"
                left = " ".join(c['left_context'])
                right = " ".join(c['right_context'])
                context = f"{left} {c['target']} {right}"

                # Вставка метаданных и текста
                concordance_text.insert(tk.END, metadata, "meta")
                concordance_text.insert(tk.END, context)

                # Оформление метаданных серым цветом
                concordance_text.tag_configure("meta", foreground="gray")

                # Поиск только целых слов (регистронезависимо)
                target_lower = re.escape(c['target'].lower())  # Экранируем спецсимволы
                pattern = rf'\b{target_lower}\b'  # Ограничиваем границами слова

                # Получаем текст без метаданных (начиная со второй строки)
                content = concordance_text.get("2.0", tk.END).lower()

                # Поиск всех вхождений в тексте (с учетом границ слова)
                for match in re.finditer(pattern, content):
                    start_pos = f"2.{match.start()}"
                    end_pos = f"2.{match.end()}"
                    concordance_text.tag_add("highlight", start_pos, end_pos)

                # Настройка выделения
                concordance_text.tag_configure("highlight", background="orange", foreground="black", font="TkFixedFont",
                                               relief="raised")

                concordance_text.config(state="disabled")

                text = self.entries_dict[c['entry_id']]
                text.config(state="normal")
                text.tag_configure("highlight", background="orange", foreground="black", font="TkFixedFont",
                                   relief="raised")

                cur = 1.0  # current position
                length = tk.IntVar()  # num of matched chars
                pattern = f"\m{c["target"]}\M"  # Ensure full word match

                while True:
                    cur = text.search(pattern, cur, tk.END, count=length, regexp=True)
                    if not cur:
                        break

                    matchEnd = f'{cur}+{length.get()}c'
                    text.tag_add('highlight', cur, matchEnd)
                    cur = text.index(matchEnd)

                text.config(state="disabled")

            self.data_container.update()
        else:
            messagebox.showwarning("Внимание", "Совпадений не найдено")

    def search_morph(self):
        criteria = {}

        # Получаем введенное пользователем название части речи
        pos_input = self.pos_entry.get().strip()

        # Обратный словарь для поиска по пользовательскому вводу
        REVERSE_POS_TRANSLATIONS = {v.lower(): k for k, v in POS_TRANSLATIONS.items()}

        # Если введено что-то, пытаемся перевести в сокращение
        if pos_input:
            pos_code = REVERSE_POS_TRANSLATIONS.get(pos_input.lower())
            if pos_code:
                criteria["pos"] = pos_code
            else:
                self.morph_results_text.delete("1.0", tk.END)
                self.morph_results_text.insert(tk.END, "Некорректная часть речи.\n")
                return  # Останавливаем выполнение, если введено что-то неправильное

        gender = self.gender_var.get()
        if gender != "Любой":
            criteria["feats__gender"] = gender
        number = self.number_var.get()
        if number != "Любой":
            criteria["feats__number"] = number

        results = self.corpus_manager.filter_tokens(**criteria)
        self.morph_results_text.delete("1.0", tk.END)

        if results:
            for entry_id, token in results:
                pos_name = POS_TRANSLATIONS.get(token.pos, token.pos)
                morph_details = []
                for feat, value in token.feats.items():
                    feat_ru = MORPH_FEATURES_TRANSLATIONS.get(feat, feat)
                    value_ru = MORPH_VALUES_TRANSLATIONS.get(feat, {}).get(value, value)
                    morph_details.append(f"{feat_ru}: {value_ru}")
                morph_details_str = ", ".join(morph_details)
                line = (f"Запись: {entry_id}, Токен: {token.text}, Лемма: {token.lemma}, "
                        f"Часть речи: {pos_name}, Характеристики: {morph_details_str}\n")
                self.morph_results_text.insert(tk.END, line)
        else:
            self.morph_results_text.insert(tk.END, "Нет результатов.")

    def open_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filepath:
            try:
                self.corpus_manager.load_corpus(filepath)
                self.refresh_entries()
                self.update_frequencies()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл: {e}")

    def save_file(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filepath:
            try:
                self.corpus_manager.save_corpus(filepath)
                messagebox.showinfo("Сохранено", "Файл успешно сохранен.")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")

    def propmt_user_to_add_text_from_file(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if filepath:
            self.add_text_from_file(filepath)

    def add_text_from_file(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            new_id = f"entry{len(self.corpus_manager.entries) + 1}"
            self.corpus_manager.add_entry(new_id, text)
            self.refresh_entries()
            self.update_frequencies()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить текст: {e}")
            raise e