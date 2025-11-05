import os
import shutil
from pathlib import Path


def generate_parser():
    """Генерирует парсер из файлов .g4"""
    grammar_dir = Path("grammar")
    generated_dir = Path("generated")

    shutil.rmtree(generated_dir, ignore_errors=True)
    os.makedirs(generated_dir, exist_ok=True)

    parser_g4 = grammar_dir / "MathLang.g4"

    try:
        print("Генерация парсера из .g4 файлов...")

        # Команда для генерации парсера
        cmd = f"antlr4 -Dlanguage=Python3 -visitor -o {generated_dir} {parser_g4}"
        os.system(cmd)

        print("Парсер успешно сгенерирован!")
        return True

    except Exception as e:
        print(f"Ошибка при генерации парсера: {e}")
        return False


if __name__ == "__main__":
    generate_parser()
