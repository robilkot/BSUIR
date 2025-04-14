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
class SentenceToken:
    start_idx: int  # start index in sentence string
    end_idx: int  # end index in sentence string
    pos: PartOfSpeech
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
    doc.tag_morph(morph_tagger)

    sentences = []
    for sent_idx, sent in enumerate(doc.sents, start=1):
        tokens = []
        for token in sent.tokens:
            token.lemmatize(morph_vocab)

            start_idx = token.start
            end_idx = token.stop
            pos_str = token.pos or 'x'
            try:
                pos_enum = PartOfSpeech[pos_str]
            except KeyError:
                pos_enum = PartOfSpeech.x

            morph_info = None
            if token.feats:
                if isinstance(token.feats, str):
                    morph_info = {}
                    feats = token.feats.split('|')
                    for feat in feats:
                        if '=' in feat:
                            key, value = feat.split('=', 1)
                            morph_info[key] = value
                elif isinstance(token.feats, dict):
                    morph_info = token.feats

            tokens.append(
                SentenceToken(
                    start_idx=start_idx,
                    end_idx=end_idx,
                    pos=pos_enum,
                    lemma=token.lemma,
                    morph_info=morph_info
                )
            )
        sentence = Sentence(text=sent.text, tokens=tokens)
        sentences.append(sentence)

    return sentences


def parse_syntax(sentence: Sentence) -> SentenceSyntax:
    doc = Doc(sentence.text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)

    natasha_sent = list(doc.sents)[0]
    syntax_tokens = []

    def find_token(start, stop):
        for token in sentence.tokens:
            if token.start_idx == start and token.end_idx == stop:
                return token
        return None

    for token in natasha_sent.tokens:
        rel = SYNTAX_REL_MAPPING.get(token.rel, SyntaxRelation.nmod)

        matched_token = find_token(token.start, token.stop)
        if matched_token is None:
            matched_token = SentenceToken(
                start_idx=token.start,
                end_idx=token.stop,
                pos=POS_MAPPING.get(token.pos, PartOfSpeech.x),
                lemma=token.lemma,
                morph_info=token.morph.to_dict() if hasattr(token, 'morph') and callable(getattr(token.morph, "to_dict", None)) else None
            )
        else:
            if not matched_token.lemma:
                matched_token.lemma = token.lemma
            if not matched_token.morph_info and hasattr(token, 'morph') and callable(getattr(token.morph, "to_dict", None)):
                matched_token.morph_info = token.morph.to_dict()

        head_id = getattr(token, 'head', -1)

        stoken = SyntaxToken(
            token=matched_token,
            id=token.id,
            head_id=head_id,
            relation=rel,
        )
        syntax_tokens.append(stoken)

    return SentenceSyntax(tokens=syntax_tokens)



def parse_semantics(sentence: Sentence) -> SentenceSemantics:
    from natasha import NewsNERTagger

    doc = Doc(sentence.text)
    doc.segment(segmenter)
    doc.tag_ner(NewsNERTagger(embedding))

    entities = [span.text for span in doc.spans] if doc.spans else []

    core_predicate = None
    if sentence.syntax:
        for syntax_token in sentence.syntax.tokens:
            if syntax_token.relation == SyntaxRelation.root:
                token = syntax_token.token
                if token.pos == PartOfSpeech.verb:
                    core_predicate = token.lemma or sentence.text[token.start_idx:token.end_idx]
                    break

    return SentenceSemantics(entities=entities, core_predicate=core_predicate)


if __name__ == '__main__':
    text = 'Я пришёл домой уставший! Вчера был сложный день. Тимур, напоминаю о вреде наркотиков на военном факультете! Новости в Беларуси, новости в мире.'
    sentences = text_to_sentences(text)

    for i, sentence in enumerate(sentences):
        print(sentence)
        sentence.syntax = parse_syntax(sentence)

        sentence.semantics = parse_semantics(sentence)

        print(sentence.tokens)
        print(sentence.syntax)
        print(sentence.semantics)
        # todo выводитьв человеческом виде