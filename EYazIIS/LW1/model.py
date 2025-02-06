from __future__ import annotations


class FormInfo:
    def __init__(self, frequency: float, note: str | None = None):
        self.frequency: float = frequency
        self.note: str | None = note

    def __repr__(self) -> str:
        return f"{self.frequency} - {self.note}"


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


class NLPDatabase(dict[Lemma, dict[str, FormInfo]]):
    def __init__(self, text):
        super().__init__()
        self.source_text = text
        self.word_count = 0
