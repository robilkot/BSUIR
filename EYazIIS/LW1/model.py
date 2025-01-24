from __future__ import annotations


class Form:
    form: str  # Словоформа
    frequency: float  # Частота вхождений
    note: str | None  # Морфологическая информация от пользователя

    def __init__(self, form: str, frequency: float, note: str | None = None):
        self.form = form
        self.frequency = frequency
        self.note = note

    def __repr__(self) -> str:
        return f"{self.form} - {self.frequency} - {self.note}"


class Lemma:
    lemma: str  # Лексема

    def __repr__(self) -> str:
        return self.lemma

    def __init__(self, lemma: str):
        self.lemma = lemma

    def __hash__(self) -> int:
        return self.lemma.__hash__()

    def __eq__(self, other: Lemma) -> bool:
        return self.lemma == other.lemma


# Словарь
class NLPDatabase(dict[Lemma, set[Form]]):
    pass
