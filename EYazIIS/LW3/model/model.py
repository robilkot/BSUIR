from dataclasses import dataclass
from enum import Enum, auto

from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc, NewsNERTagger

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

class PartOfSpeech(Enum):
    noun = auto() # "Существительное"
    verb = auto() # "Глагол"
    adj = auto() # "Прилагательное"
    adv = auto() # "Наречие"
    pron = auto() # "Местоимение"
    num = auto() # "Числительное"
    adp = auto() # "Предлог"
    conj = auto() # "Союз"
    part = auto() # "Частица"
    intj = auto() # "Междометин"
    det = auto() # "Артикль или указательные слова"
    punct = auto() # "Знаки препинания"
    sym = auto() # "Символы"
    propn = auto() # "Имя собственное"
    x = auto() # "Неопределенная часть речи"

POS_MAPPING = {
    'NOUN': PartOfSpeech.noun,
    'VERB': PartOfSpeech.verb,
    'ADJ': PartOfSpeech.adj,
    'ADV': PartOfSpeech.adv,
    'PRON': PartOfSpeech.pron,
    'NUM': PartOfSpeech.num,
    'ADP': PartOfSpeech.adp,
    'CCONJ': PartOfSpeech.conj,
    'SCONJ': PartOfSpeech.conj,  # If present, treat as conjunction.
    'PART': PartOfSpeech.part,
    'INTJ': PartOfSpeech.intj,
    'DET': PartOfSpeech.det,
    'PUNCT': PartOfSpeech.punct,
    'SYM': PartOfSpeech.sym,
    'PROPN': PartOfSpeech.propn,
    'X': PartOfSpeech.x,
}

SYNTAX_REL_MAPPING = {
        'root': SyntaxRelation.root,
        'nsubj': SyntaxRelation.nsubj,
        'obj': SyntaxRelation.obj,
        'iobj': SyntaxRelation.iobj,
        'ccomp': SyntaxRelation.ccomp,
        'xcomp': SyntaxRelation.xcomp,
        'advmod': SyntaxRelation.advmod,
        'amod': SyntaxRelation.amod,
        'det': SyntaxRelation.det,
        'cc': SyntaxRelation.cc,
        'case': SyntaxRelation.case,
        'obl': SyntaxRelation.obl,
        'appos': SyntaxRelation.appos,
        'conj': SyntaxRelation.conj,
        'nummod': SyntaxRelation.nummod,
        'punct': SyntaxRelation.punct,
        'parataxis': SyntaxRelation.parataxis,
        'acl': SyntaxRelation.acl,
        'nmod': SyntaxRelation.nmod,
    }


@dataclass
class Syntax:
    id: int
    head_id: int
    relation: SyntaxRelation

@dataclass
class Morphology:
    pos: PartOfSpeech
    lemma: str | None = None
    morph_info: dict | None = None

@dataclass
class SentenceToken:
    start_idx: int  # start index in sentence string
    end_idx: int  # end index in sentence string
    syntax: Syntax | None = None
    morphology: Morphology | None = None

@dataclass
class SentenceSyntax:
    tokens: list[Syntax]

@dataclass
class SentenceMorphology:
    tokens: list[Morphology]

@dataclass
class SentenceSemantics:
    entities: list[str]
    core_predicate: str | None = None


@dataclass
class Sentence:
    text: str
    tokens: list[SentenceToken]
    syntax: SentenceSyntax | None = None
    semantics: SentenceSemantics | None = None

    def __str__(self):
        return self.text

def text_to_sentences(text: str) -> list[Sentence]:
    doc = Doc(text)
    doc.segment(segmenter)

    sentences = []
    for sent_idx, sent in enumerate(doc.sents, start=1):
        tokens = []
        for token in sent.tokens:
            start_idx = token.start
            end_idx = token.stop

            tokens.append(
                SentenceToken(
                    start_idx=start_idx,
                    end_idx=end_idx,
                )
            )
        sentence = Sentence(text=sent.text, tokens=tokens)
        sentences.append(sentence)

    return sentences

def parse_morphology(sentence: str) -> SentenceMorphology:
    doc = Doc(sentence)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    morph_tokens = []

    for token in doc.sents[0].tokens:
        token.lemmatize(morph_vocab)

        mtoken = Morphology(
            pos = POS_MAPPING[token.pos],
            lemma = token.lemma,
            morph_info=token.feats
        )
        morph_tokens.append(mtoken)

    return SentenceMorphology(tokens=morph_tokens)

def parse_syntax(sentence: str) -> SentenceSyntax:
    doc = Doc(sentence)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    natasha_sent = list(doc.sents)[0]
    syntax_tokens = []

    for token in natasha_sent.tokens:
        rel = SYNTAX_REL_MAPPING.get(token.rel, SyntaxRelation.nmod)

        head_id = getattr(token, 'head_id', -1)

        stoken = Syntax(
            id=token.id,
            head_id=head_id,
            relation=rel,
        )
        syntax_tokens.append(stoken)

    return SentenceSyntax(tokens=syntax_tokens)


def parse_semantics(sentence: str) -> SentenceSemantics:
    from natasha import NewsNERTagger

    doc = Doc(sentence)
    doc.segment(segmenter)
    doc.tag_ner(NewsNERTagger(embedding))

    print(doc.spans)
    print(doc.spans)
    # entities = [span.text for span in doc.spans] if doc.spans else []

    # core_predicate = None
    # todo repair
    # if sentence.syntax:
    #     for syntax_token in sentence.syntax.tokens:
    #         if syntax_token.relation == SyntaxRelation.root:
    #             token = syntax_token.token
    #             if token.pos == PartOfSpeech.verb:
    #                 core_predicate = token.lemma or sentence.text[token.start_idx:token.end_idx]
    #                 break

    # return SentenceSemantics(entities=entities, core_predicate=core_predicate)


if __name__ == '__main__':
    text = 'Тимур, напоминаю о вреде наркотиков на военном факультете! Новости в Беларуси, новости в мире.'
    sentences = text_to_sentences(text)

    for i, sentence in enumerate(sentences):
        print(sentence)
        sentence.syntax = parse_syntax(sentence.text)

        sentence.semantics = parse_semantics(sentence.text)

        # print(sentence.tokens)
        # print(sentence.syntax)
        # print(sentence.semantics)