from dataclasses import dataclass, field

from abstract import AbstractGenerator, Abstract


@dataclass
class KeywordPhrase:
    """Класс для представления словосочетания"""
    phrase: str


@dataclass
class KeywordNode:
    """Класс для представления ключевого слова с его словосочетаниями"""
    keyword: str
    frequency: int = 1
    phrases: list[KeywordPhrase] = field(default_factory=list)

    def add_phrase(self, phrase: str):
        for existing_phrase in self.phrases:
            if existing_phrase.phrase == phrase:
                return

        self.phrases.append(KeywordPhrase(phrase))


@dataclass
class KeywordAbstract(Abstract):
    keywords: list[KeywordNode] = field(default_factory=list)

    def add_phrase(self, keyword_lemma: str, phrase: str):
        node = next((kw for kw in self.keywords if kw.keyword == keyword_lemma), None)

        if node is None:
            raise ValueError(f"No keyword found matching '{keyword_lemma}'")

        node.add_phrase(phrase)

    def add_keyword(self, keyword: str):
        for node in self.keywords:
            if node.keyword == keyword:
                node.frequency += 1
                return node

        new_node = KeywordNode(keyword=keyword)
        self.keywords.append(new_node)
        return new_node

    def get_sorted_keywords(self) -> list[KeywordNode]:
        return sorted(self.keywords, key=lambda x: x.frequency, reverse=True)

    def print(self):
        sorted_keywords = self.get_sorted_keywords()
        for i, keyword_node in enumerate(sorted_keywords, 1):
            print(f"{i}. '{keyword_node.keyword}' ({keyword_node.frequency} включений)")

            if keyword_node.phrases:
                sorted_phrases = keyword_node.phrases
                for j, phrase in enumerate(sorted_phrases, 1):
                    print(f"   {j}. '{phrase.phrase}'")


class KeywordAbstractGenerator(AbstractGenerator):
    """
    Генерирует реферат в виде структуры ключевых слов и словосочетаний.

    Args:
        text (str): Исходный текст.
        top_n (int): Количество возвращаемых ключевых элементов.

    Returns:
        KeywordAbstract: Структура ключевых слов и словосочетаний.
    """
    def generate(self, text: str, top_n: int = 20) -> KeywordAbstract:
        pass