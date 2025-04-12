from dataclasses import dataclass
from enum import Enum, auto

from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc

segmenter = Segmenter()
morph_vocab = MorphVocab()
embedding = NewsEmbedding()
morph_tagger = NewsMorphTagger(embedding)
syntax_parser = NewsSyntaxParser(embedding)


# noinspection SpellCheckingInspection
class SyntaxRelation(Enum):
    root = auto() # "Корень",
    nsubj = auto() # "Подлежащее",
    obj = auto() # "Дополнение",
    iobj = auto() # "Косвенное дополнение",
    ccomp = auto() # "Придаточное дополнительное",
    xcomp = auto() # "Дополнительный предикатив",
    advmod = auto() # "Обстоятельство",
    amod = auto() # "Определение",
    det = auto() # "Определитель",
    cc = auto() # "Сочинительный союз",
    case = auto() # "Предлог",
    obl = auto() # "Обстоятельственное дополнение",
    appos = auto() # "Приложение",
    conj = auto() # "Сочиненное предложение",
    nummod = auto() # "Грамматическое числительное",
    punct = auto() # "Знак препинания",
    parataxis = auto() # "Парцелляция",
    acl = auto() # "Определительное придаточное",
    nmod = auto() # "Именное дополнение"


@dataclass
class SentenceToken:
    start_idx: int  # start index in sentence string
    end_idx: int  # end index in sentence string
    pos: str | None = None  # part of speech. todo: make enum
    lemma: str | None = None
    morph_info: dict | None = None


@dataclass
class SyntaxToken:
    token: SentenceToken
    id: int
    head_id: int
    relation: SyntaxRelation


@dataclass
class SentenceSyntax:
    tokens: list[SyntaxToken]


@dataclass
class SentenceSemantics:
    pass  # todo: implement


@dataclass
class Sentence:
    text: str
    tokens: list[SentenceToken]
    syntax: SentenceSyntax | None = None
    semantics: SentenceSemantics | None = None

    def __str__(self):
        return self.text


def text_to_sentences(text: str) -> list[Sentence]:
    pass
    # todo


def parse_syntax(sentence: Sentence) -> SentenceSyntax:
    pass
    # todo


def parse_semantics(sentence: Sentence) -> SentenceSemantics:
    pass
    # todo


if __name__ == '__main__':
    text = 'Я пришёл домой уставший! Вчера был сложный день.'

    sents = text_to_sentences(text)

    sent = sents[0]

    syntax = parse_syntax(sent)

    print(syntax)
