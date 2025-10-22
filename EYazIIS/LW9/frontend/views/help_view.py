# frontend/views/help_view.py
import flet as ft
from frontend.views.base_view import BaseView


class HelpView(BaseView):

    def _build_view(self):
        title = ft.Text("Справка", size=24, weight=ft.FontWeight.BOLD)

        help_content = self._build_help_content()

        back_button = ft.ElevatedButton(
            "Назад",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.page.go("/")
        )

        self.controls_list = [
            title,
            ft.Divider(),
            help_content,
            ft.Container(height=20),
            back_button
        ]

    def _build_help_content(self) -> ft.Control:
        return ft.Column([
            ft.Text("Руководство пользователя", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("""
            Система автоматического реферирования текста позволяет создавать рефераты 
            научных статей по медицине и критики изобразительного искусства.
            """),

            ft.Text("Шаги работы:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("1. Выберите язык текста (русский или английский)"),
            ft.Text("2. Выберите тип реферата:"),
            ft.Text("   - Классический: выделение ключевых предложений"),
            ft.Text("   - Ключевые слова: список значимых терминов"),
            ft.Text("   - Оба типа: комбинированный результат"),
            ft.Text("3. Введите текст или загрузите файл (.txt, .doc, .docx)"),
            ft.Text("4. Нажмите 'Сгенерировать реферат'"),
            ft.Text("5. Просмотрите, сохраните или распечатайте результат"),

            ft.Text("Требования к тексту:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("• Объем: до 10 страниц формата А4"),
            ft.Text("• Язык: русский или английский"),
            ft.Text("• Тематика: научные статьи по медицине или критика искусства"),

            ft.Text("Поддерживаемые форматы:", size=16, weight=ft.FontWeight.BOLD),
            ft.Text("• Текстовые файлы (.txt)"),
            ft.Text("• Документы Word (.doc, .docx)"),
        ], scroll=ft.ScrollMode.AUTO)