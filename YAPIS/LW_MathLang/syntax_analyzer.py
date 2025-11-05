"""
Синтаксический анализатор для пользовательского языка программирования
"""

import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from generator import generate_parser


class CustomErrorListener(ErrorListener):
    """Кастомный обработчик ошибок для красивого вывода"""

    def __init__(self):
        self.has_errors = False
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_errors = True
        error_msg = f"Syntax error ({line}:{column}): {msg}"
        self.errors.append(error_msg)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


class SyntaxAnalyzer:
    def __init__(self):
        self.error_listener = CustomErrorListener()

    def analyze_file(self, file_path):
        """Анализирует файл на соответствие грамматике"""

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            return False

        # Чтение входного файла
        input_stream = FileStream(file_path, encoding='utf-8')

        # Лексический анализ
        lexer = MathLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(self.error_listener)

        tokens = CommonTokenStream(lexer)

        # Синтаксический анализ
        parser = MathLangParser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(self.error_listener)

        tree = parser.program()

        if self.error_listener.has_errors:
            print(f"\nReport for: {file_path}")
            print(f"Errors count: {len(self.error_listener.errors)}")
            return False
        else:
            print(f"File {file_path} is syntactically correct.")
            return True

    def print_errors(self):
        if self.error_listener.errors:
            print("Errors:")
            for i, error in enumerate(self.error_listener.errors, 1):
                print(f"{i}. {error}")


def main():
    """Основная функция программы"""

    if len(sys.argv) != 2:
        print("No file specified. Using default one.")

    source_file = sys.argv[1] if len(sys.argv) > 1 else 'samples/sample6.ml'

    # Анализируем файл
    analyzer = SyntaxAnalyzer()
    success = analyzer.analyze_file(source_file)

    if not success:
        analyzer.print_errors()
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    generate_parser()

    from generated.grammar.MathLangLexer import MathLangLexer
    from generated.grammar.MathLangParser import MathLangParser

    main()