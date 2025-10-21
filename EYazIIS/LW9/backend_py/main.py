from dataclasses import dataclass, field
from string import punctuation

from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)


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
class KeywordStructure:
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

    def print(self, max_phrases_per_keyword: int = 5):
        sorted_keywords = self.get_sorted_keywords()
        for i, keyword_node in enumerate(sorted_keywords, 1):
            print(f"{i}. {keyword_node.keyword} ({keyword_node.frequency} включений)")

            if keyword_node.phrases:
                sorted_phrases = keyword_node.phrases
                for j, phrase in enumerate(sorted_phrases, 1):
                    print(f"   {j}. {phrase.phrase}")


def generate_keyword_abstract(text, top_n=20, min_word_length=2):
    """
    Генерирует реферат в виде структуры ключевых слов и словосочетаний.

    Args:
        text (str): Исходный текст.
        top_n (int): Количество возвращаемых ключевых элементов.
        min_word_length (int): Минимальная длина слова для учета.

    Returns:
        KeywordStructure: Структура ключевых слов и словосочетаний.
    """

    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)


    keyword_structure = KeywordStructure()

    # Лемматизация и сбор статистики по отдельным словам
    lemmas = []
    for token in doc.tokens:
        if (token.text in punctuation
                or token.pos in ['ADP', 'CCONJ', 'PART', 'SCONJ', 'PRON', 'DET']
                or len(token.text) < min_word_length
                or token.text.isdigit()):
            continue

        token.lemmatize(morph_vocab)
        lemmas.append(token.lemma.lower())

        keyword_structure.add_keyword(token.lemma)

    # Извлечение словосочетаний
    for token in doc.tokens:
        if token.pos == 'NOUN':
            token_case = token.feats['Case']

            chunk_words = []
            children = [token2 for token2 in doc.tokens if token2.head_id == token.id]
            for child in children:
                if child.pos not in ['ADJ', 'NOUN']:
                    continue

                if token_case and child.feats['Case'] and token.lemma == child.lemma:
                    continue

                chunk_words.append(child)

            chunk_words.append(token)
            chunk_words.sort(key=lambda t: t.start)

            if len(chunk_words) > 1:
                chunk_words = [t.text for t in chunk_words]
                chunk_words = ' '.join(chunk_words)
                keyword_structure.add_phrase(token.lemma, chunk_words)

    sorted_keywords = keyword_structure.get_sorted_keywords()[:top_n]
    keyword_structure.keywords = sorted_keywords

    return keyword_structure


if __name__ == '__main__':
    sample_text = """
    Лазер — это устройство, создающее узкий пучок интенсивного света. 
    Лазеры находят применение в самых разных областях: от медицины до телекоммуникаций. 
    Принцип работы лазера основан на явлении вынужденного излучения. 
    Существуют различные типы лазеров, например, газовые лазеры, твердотельные лазеры и полупроводниковые лазеры. 
    Красный лазер часто используется в указателях, в то время как синий лазер обладает большей энергией и применяется в Blu-ray технологиях. 
    Мощность лазерного луча можно регулировать в зависимости от задачи. 
    Устройство лазера включает в себя активную среду, источник накачки и оптический резонатор.
    """

    print("Реферат в виде структуры ключевых слов:")
    print("=" * 50)

    keyword_structure = generate_keyword_abstract(sample_text, top_n=10)
    keyword_structure.print(max_phrases_per_keyword=10)
