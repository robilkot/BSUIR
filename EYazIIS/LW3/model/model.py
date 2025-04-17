from dataclasses import dataclass
from enum import Enum, auto
from html import unescape
from natasha import Segmenter, MorphVocab, NewsEmbedding, NewsMorphTagger, NewsSyntaxParser, Doc, NewsNERTagger
import os
import time
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
from urllib.parse import urljoin

segmenter = Segmenter()
morph_vocab = MorphVocab()
embedding = NewsEmbedding()
morph_tagger = NewsMorphTagger(embedding)
syntax_parser = NewsSyntaxParser(embedding)
ner_tagger = NewsNERTagger(embedding)


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
    aux = auto() # "Вспомогательный глагол"

class NERClass(Enum):
    PER = auto()
    LOC = auto()
    ORG = auto()


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
    'AUX': PartOfSpeech.aux,
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
    id: str
    head_id: str
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
class NamedEntity:
    text: str
    ner_class: NERClass
    normal_form: str | None = None

@dataclass
class ObjectDescription:
    description: str
    images_urls: list[str] | None = None

@dataclass
class Semantics:
    named_entity_info: NamedEntity | None = None
    object_description: ObjectDescription | None = None

@dataclass
class SentenceSemantics:
    tokens: list[Semantics]

@dataclass
class Sentence:
    text: str
    tokens: list[SentenceToken]

    def __str__(self):
        return self.text
    
@dataclass
class WordSemantics:
    word: str
    emph_info: int
    description: str

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
    doc = Doc(sentence)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)

    NERClassDict = {
        'PER': NERClass.PER,
        'LOC': NERClass.LOC,
        'ORG': NERClass.ORG,
    }

    for span in doc.spans:
        span.normalize(morph_vocab)

    # Get spans from NER tagging
    ner_spans = [(span.start, span.stop, span.type, span.normal)
                 for span in doc.spans if span.type != '_']

    print(doc.spans)

    # Create semantics for each token
    semantics_list = []
    for token in doc.sents[0].tokens:
        # Check if token is part of any named entity
        named_entity = None

        # Find matching NER span
        for start, stop, ner_type, normal in ner_spans:
            if start <= token.start < stop:
                named_entity = NamedEntity(
                    text=doc.text[start:stop],
                    ner_class=NERClassDict[ner_type],
                    normal_form=normal
                )
                break

        semantics = Semantics(
            named_entity_info=named_entity,
            object_description=None
        )

        semantics_list.append(semantics)

    return SentenceSemantics(tokens=semantics_list)

def lemmatize_word(word: str) -> str:
    try:
        doc = Doc(word)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        
        if not doc.tokens:
            return word
            
        doc.tokens[0].lemmatize(morph_vocab)
        return doc.tokens[0].lemma.lower()
    
    except Exception:
        return word

def get_words_semantics(query):
    query_lemma = lemmatize_word(query)
    try:
        base_url = "https://www.slovari.ru/search.aspx"
        params = {"s": "0", "p": "3068"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        with requests.Session() as s:
            response = s.get(base_url, params=params, headers=headers)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                return {"error": f"Initial request failed: {response.status_code}"}

            soup = BeautifulSoup(response.text, 'html.parser')
            
            viewstate = soup.find('input', {'id': '__VIEWSTATE'})['value']
            viewstategenerator = soup.find('input', {'id': '__VIEWSTATEGENERATOR'})['value']

            data = {
                '__EVENTTARGET': 'ctl08',
                '__EVENTARGUMENT': 'Search()',
                '__VIEWSTATE': viewstate,
                '__VIEWSTATEGENERATOR': viewstategenerator,
                'query_textfield': 'поиск по сайту',
                'ctl07':'vname',
                'ctl07':'vojsh',
                'ctl08_regime':'simple',
                'ctl08':'query',
                'ctl08_search_query': query_lemma,
            }
            response = s.post(base_url, 
                            params=params,
                            data=data, 
                            headers=headers,
                            allow_redirects=True)

            response.raise_for_status()

        result_soup = BeautifulSoup(response.text, 'html.parser')
        results = result_soup.find('div', class_='searchResultsText')
        
        if not results:
            return "Ничего не найдено"
            
        raw_text = results.get_text(strip=False, separator='\n')
        cleaned_text = ' '.join(raw_text.split())

        first_word = cleaned_text.split()[0] 
        apostrophe_index = first_word.find("'")
        
        if apostrophe_index == -1:
            return WordSemantics(
                word=query_lemma,
                emph_info=0,
                description=cleaned_text
            )

        clean_word = first_word.replace("'", "")
        emph_index = apostrophe_index - 1 

        description = cleaned_text[len(first_word):].strip()

        return WordSemantics(
            word=clean_word,
            emph_info=emph_index,
            description=description
        )

    except requests.exceptions.RequestException as e:
        return f"Ошибка сети: {str(e)}"
    except Exception as e:
        return f"Ошибка: {str(e)}"


if __name__ == "__main__":
    word = "интересы"
    print(get_words_semantics(word))
    # files = os.listdir("./dataset/")
    # content = []
    # for filename in files:
    #     with open(f'./dataset/{filename}', encoding='utf-8') as file:
    #         content.append(file.read())

    # processing_times = []
    # num_sentences_list = []

    # for text in content:
    #     sentences = text_to_sentences(text)
    #     num_sentences = len(sentences)
    #     num_sentences_list.append(num_sentences)

    #     start_time = time.time()
        
    #     for sentence in sentences:
    #         parse_morphology(sentence.text)
    #         sentence.syntax = parse_syntax(sentence.text)
    #         sentence.semantics = parse_semantics(sentence.text)
        
    #     processing_time = time.time() - start_time
    #     processing_times.append(processing_time)

    # plt.figure(figsize=(10, 6))
    # plt.scatter(num_sentences_list, processing_times, alpha=0.7, color='green')
    
    # if len(num_sentences_list) > 1:
    #     z = np.polyfit(num_sentences_list, processing_times, 1)
    #     p = np.poly1d(z)
    #     plt.plot(num_sentences_list, p(num_sentences_list), "r--", 
    #             label=f'Trend: y = {z[0]:.4f}x + {z[1]:.2f}')
    #     plt.legend()

    # plt.title('Зависимость времени обработки от количества предложений')
    # plt.xlabel('Число предложений в тексте')
    # plt.ylabel('Общее время обработки (секунды)')
    # plt.grid(True)
    # plt.show()