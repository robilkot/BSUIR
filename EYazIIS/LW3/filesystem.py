# import sys
# from io import StringIO
#
# from natasha import Doc
#
#
# def save_syntax(filepath, doc: Doc):
#     original_stdout = sys.stdout
#     sys.stdout = StringIO()
#
#     with open(filepath, "w", encoding="utf-8") as file:
#         for sentence in doc.sents:
#             sentence.syntax.print()
#             file.write(sys.stdout.getvalue())
#             sys.stdout.truncate(0)
#             sys.stdout.seek(0)
#
#     sys.stdout = original_stdout
#
#
# def open_text(filepath) -> Doc:
#     with open(filepath, "r", encoding="utf-8") as file:
#         text = file.read()
#
#     doc = Doc(text)
#     return doc
