import os
from pathlib import Path


def generate_parser():
    """Генерирует парсер из файлов .g4"""

    grammar_dir = Path("grammar")
    if not grammar_dir.exists():
        print("Папка 'grammar' не найдена!")
        return False

    parser_g4 = grammar_dir / "MathLang.g4"

    if not parser_g4.exists():
        print("Файлы .g4 не найдены в папке 'grammar'!")
        return False

    try:
        print("Генерация парсера из .g4 файлов...")

        # Команда для генерации парсера
        cmd = f"antlr4 -Dlanguage=Python3 -o generated {parser_g4}"
        os.system(cmd)

        print("Парсер успешно сгенерирован!")
        return True

    except Exception as e:
        print(f"Ошибка при генерации парсера: {e}")
        return False
