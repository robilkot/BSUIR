import flet as ft
from frontend.views.base_view import BaseView
from frontend.widgets.abstract_display import AbstractDisplay
from frontend.widgets.action_buttons import ActionButtons
from frontend.widgets.save_dialog import SaveDialog
from backend_py.classic_abstract_se import SEClassicAbstractGenerator
from backend_py.keyword_ru import RUKeywordAbstractGenerator
from backend_py.keyword_en import ENKeywordAbstractGenerator

from backend_py.classic_abstract_llm import LLMClassicAbstractGenerator
from backend_py.keyword_llm import LLMKeywordAbstractGenerator


class ResultView(BaseView):
    """Представление результатов"""

    def _build_view(self):
        # Заголовок
        title = ft.Text(
            "Результаты реферирования",
            size=24,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER
        )

        # Отображение реферата
        self.abstract_display = AbstractDisplay()

        # Диалог сохранения
        self.save_dialog = SaveDialog(on_save_complete=self._on_save_complete)

        # Кнопки действий
        action_buttons = ActionButtons(
            on_generate=self._regenerate_abstract,
            on_save=self._save_results,
            on_help=self._show_help
        )

        back_button = ft.ElevatedButton(
            "Назад",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.page.go("/")
        )

        self.controls_list = [
            title,
            ft.Divider(),
            self.abstract_display.build(),
            ft.Container(height=20),
            action_buttons.build(),
            back_button
        ]

    def refresh(self):
        """Обновление представления при показе"""
        self._generate_abstracts()

    def _generate_abstracts(self):
        """Генерирует рефераты"""
        text = self.app_state.current_text
        language = self.app_state.current_language
        abstract_type = self.app_state.abstract_type

        try:
            # Очищаем предыдущие результаты
            self.abstract_display.clear()

            # Показываем индикатор загрузки
            self.abstract_display.content_area.controls.append(ft.ProgressBar())
            self.page.update()

            # Генерируем рефераты в зависимости от выбранного типа
            if abstract_type in ["classic", "both"]:
                self._generate_classic_abstract(text, language)

            if abstract_type in ["keywords", "both"]:
                self._generate_keyword_abstract(text, language)

            # Сохраняем результаты в состояние
            self.app_state.update_state(
                last_classic_abstract=self.abstract_display.current_classic_abstract,
                last_keyword_abstract=self.abstract_display.current_keyword_abstract
            )

        except Exception as e:
            self.show_snackbar(f"Ошибка генерации реферата: {str(e)}")
        finally:
            # Убираем индикатор загрузки
            if (self.abstract_display.content_area.controls and
                    isinstance(self.abstract_display.content_area.controls[0], ft.ProgressBar)):
                self.abstract_display.content_area.controls.pop(0)
            self.page.update()

    def _generate_classic_abstract(self, text: str, language: str):
        """Генерирует классический реферат"""
        if self.app_state.use_llm:
            generator = LLMClassicAbstractGenerator()
            abstract = generator.generate(text)
            self.abstract_display.show_classic_abstract(abstract)
        else:
            generator = SEClassicAbstractGenerator(language=language)
            abstract = generator.generate(text, num_sentences=10)
            self.abstract_display.show_classic_abstract(abstract)

    def _generate_keyword_abstract(self, text: str, language: str):
        """Генерирует реферат ключевых слов"""
        if self.app_state.use_llm:
            generator = LLMKeywordAbstractGenerator()
        else:
            if language == "russian":
                generator = RUKeywordAbstractGenerator()
            else:
                generator = ENKeywordAbstractGenerator()

        abstract = generator.generate(text, top_n=10)
        self.abstract_display.show_keyword_abstract(abstract)

    def _regenerate_abstract(self, e):
        """Перегенерирует реферат"""
        self._generate_abstracts()

    def _save_results(self, e):
        """Сохраняет результаты в файл"""
        save_content = self.abstract_display.get_save_content()

        if not save_content.strip():
            self.show_snackbar("Нет данных для сохранения")
            return

        # Определяем предлагаемое имя файла на основе типа реферата
        abstract_type = self.app_state.abstract_type
        if abstract_type == "classic":
            suggested_name = "классический_реферат.txt"
        elif abstract_type == "keywords":
            suggested_name = "реферат_ключевых_слов.txt"
        else:
            suggested_name = "полный_реферат.txt"

        # Открываем диалог сохранения
        self.save_dialog.save_file(save_content, suggested_name)

    def _on_save_complete(self, file_path: str, error: str = None):
        """Обрабатывает завершение сохранения"""
        if error:
            self.show_snackbar(f"Ошибка сохранения: {error}")
        elif file_path:
            self.show_snackbar(f"Реферат успешно сохранен: {file_path}")
        else:
            self.show_snackbar("Сохранение отменено")

    def _show_help(self, e):
        self.page.go("/help")

    def get_save_dialog(self):
        return self.save_dialog.get_file_picker()