import re
from string import punctuation

from natasha import Doc

from backend_py.keyword_abstract import KeywordAbstract, KeywordAbstractGenerator
from backend_py.nlp_natasha import *


class RUKeywordAbstractGenerator(KeywordAbstractGenerator):
    def generate(self, text: str, top_n: int = 20) -> KeywordAbstract:
        doc = Doc(text)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        doc.parse_syntax(syntax_parser)

        abstract = KeywordAbstract()

        lemmas = []
        for token in doc.tokens:
            if (token.text in punctuation
                    or token.pos in ['ADP', 'CCONJ', 'PART', 'SCONJ', 'PRON', 'DET', 'PUNCT', 'X']
                    or len(token.text) < 3
                    or token.text.isdigit()
                    or bool(re.match(r'^[a-zA-Z]+$', token.text))):
                continue

            token.lemmatize(morph_vocab)
            lemmas.append(token.lemma.lower())

            abstract.add_keyword(token.lemma)

        # Извлечение словосочетаний
        for token in doc.tokens:
            if token.pos == 'NOUN':
                token_case = token.feats.get('Case', None)

                chunk_words = []
                children = [token2 for token2 in doc.tokens if token2.head_id == token.id]
                for child in children:
                    if child.pos not in ['ADJ', 'NOUN']:
                        continue

                    if token_case and child.feats.get('Case', None) and token.lemma == child.lemma:
                        continue

                    chunk_words.append(child)

                chunk_words.append(token)
                chunk_words.sort(key=lambda t: t.start)

                if len(chunk_words) > 1:
                    chunk_words = [t.text for t in chunk_words]
                    chunk_words = ' '.join(chunk_words)
                    if token.lemma is not None:
                        abstract.add_phrase(token.lemma, chunk_words)

        sorted_keywords = abstract.get_sorted_keywords()[:top_n]
        abstract.keywords = sorted_keywords

        return abstract


if __name__ == '__main__':
    text = '''
    fuck you
    Лазер — это устройство, создающее узкий пучок интенсивного света. 
    Лазеры находят применение в самых разных областях: от медицины до телекоммуникаций. 
    Принцип работы лазера основан на явлении вынужденного излучения. 
    Существуют различные типы лазеров, например, газовые лазеры, твердотельные лазеры и полупроводниковые лазеры. 
    Красный лазер часто используется в указателях, в то время как синий лазер обладает большей энергией и применяется в Blu-ray технологиях. 
    Мощность лазерного луча можно регулировать в зависимости от задачи. 
    Устройство лазера включает в себя активную среду, источник накачки и оптический резонатор.
    '''

    abstract = RUKeywordAbstractGenerator().generate(text)
    abstract.print()