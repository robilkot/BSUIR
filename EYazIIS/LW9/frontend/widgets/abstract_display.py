# frontend/widgets/abstract_display.py
import flet as ft
from backend_py.classic_abstract import ClassicAbstract
from backend_py.keyword_abstract import KeywordAbstract


class AbstractDisplay:
    """Виджет для отображения рефератов"""

    def __init__(self):
        self.content_area = ft.Column(scroll=ft.ScrollMode.AUTO)
        self.current_classic_abstract = None
        self.current_keyword_abstract = None

    def build(self) -> ft.Control:
        """Строит виджет отображения"""
        return ft.Container(
            content=self.content_area,
            border=ft.border.all(1, ft.Colors.OUTLINE),
            border_radius=10,
            padding=15,
            expand=True
        )

    def show_classic_abstract(self, abstract: ClassicAbstract):
        """Показывает классический реферат"""
        self.current_classic_abstract = abstract

        # Заголовок
        self.content_area.controls.append(
            ft.Text("Классический реферат", size=20, weight=ft.FontWeight.BOLD)
        )

        # Статистика
        self.content_area.controls.append(ft.Column([
            ft.Text(f"Общий вес: {abstract.total_score:.3f}"),
            ft.Text(f"Степень сжатия: {abstract.compression_ratio:.1%}"),
            ft.Text(f"Количество предложений: {len(abstract.sentences)}"),
        ]))

        # Предложения
        for i, sentence in enumerate(abstract.sentences, 1):
            top_words = sorted(sentence.words, key=lambda x: x.tfidf_score, reverse=True)[:3]
            words_text = ""
            if top_words:
                words_text = ", ".join([f"'{w.word}'(TF-IDF:{w.tfidf_score:.3f})" for w in top_words])

            sentence_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"{i}. {sentence.original_text}"),
                        ft.Container(height=5),
                        ft.Row([
                            ft.Text(f"Вес: {sentence.score:.3f}", size=12),
                            ft.Text(f"Ключевые слова: {words_text}", size=12, color=ft.Colors.BLUE)
                        ])
                    ]),
                    padding=10
                )
            )
            self.content_area.controls.append(sentence_card)

        # Добавляем разделитель после классического реферата
        self.content_area.controls.append(ft.Divider())

    def show_keyword_abstract(self, abstract: KeywordAbstract):
        """Показывает реферат ключевых слов"""
        self.current_keyword_abstract = abstract

        self.content_area.controls.append(
            ft.Text("Реферат из ключевых слов", size=20, weight=ft.FontWeight.BOLD)
        )

        sorted_keywords = abstract.get_sorted_keywords()

        for i, keyword_node in enumerate(sorted_keywords, 1):
            phrases_text = ""
            if keyword_node.phrases:
                phrases = [f"   {j}. '{phrase.phrase}'" for j, phrase in enumerate(keyword_node.phrases, 1)]
                phrases_text = "\n".join(phrases)

            keyword_card = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(f"{i}. '{keyword_node.keyword}' ({keyword_node.frequency} включений)"),
                        ft.Text(phrases_text, size=12) if phrases_text else ft.Container()
                    ]),
                    padding=10
                )
            )
            self.content_area.controls.append(keyword_card)

    def clear(self):
        """Очищает содержимое"""
        self.content_area.controls.clear()
        self.current_classic_abstract = None
        self.current_keyword_abstract = None

    def get_save_content(self) -> str:
        """Возвращает содержимое для сохранения в текстовом формате"""
        content_parts = []

        if self.current_classic_abstract:
            content_parts.append(self._format_classic_for_save())

        if self.current_keyword_abstract:
            content_parts.append(self._format_keyword_for_save())

        return "\n\n".join(content_parts)

    def _format_classic_for_save(self) -> str:
        """Форматирует классический реферат для сохранения"""
        abstract = self.current_classic_abstract
        lines = [
            "\nКЛАССИЧЕСКИЙ РЕФЕРАТ",
            "=" * 30,
            f"Общий вес: {abstract.total_score:.3f}",
            f"Степень сжатия: {abstract.compression_ratio:.1%}",
            f"Количество предложений: {len(abstract.sentences)}",
            "",
            "ПРЕДЛОЖЕНИЯ:",
            "-" * 20
        ]

        for i, sentence in enumerate(abstract.sentences, 1):
            lines.append(f"{i}. {sentence.original_text}")

            # Добавляем информацию о ключевых словах
            top_words = sorted(sentence.words, key=lambda x: x.tfidf_score, reverse=True)[:3]
            if top_words:
                words_info = ", ".join([f"'{w.word}'(TF-IDF:{w.tfidf_score:.3f})" for w in top_words])
                lines.append(f"   Вес: {sentence.score:.3f} | Ключевые слова: {words_info}")

            lines.append("")  # Пустая строка между предложениями

        return "\n".join(lines)

    def _format_keyword_for_save(self) -> str:
        """Форматирует реферат ключевых слов для сохранения"""
        abstract = self.current_keyword_abstract
        sorted_keywords = abstract.get_sorted_keywords()

        lines = [
            "\nРЕФЕРАТ ИЗ КЛЮЧЕВЫХ СЛОВ",
            "=" * 30,
            "",
            "КЛЮЧЕВЫЕ СЛОВА:",
            "-" * 20
        ]

        for i, keyword_node in enumerate(sorted_keywords, 1):
            lines.append(f"{i}. '{keyword_node.keyword}' ({keyword_node.frequency} включений)")

            if keyword_node.phrases:
                lines.append("   Словосочетания:")
                for j, phrase in enumerate(keyword_node.phrases, 1):
                    lines.append(f"      {j}. '{phrase.phrase}'")

            lines.append("")  # Пустая строка между ключевыми словами

        return "\n".join(lines)