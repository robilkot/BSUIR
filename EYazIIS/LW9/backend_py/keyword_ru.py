from string import punctuation

from natasha import Doc

from keyword_abstract import KeywordAbstract, KeywordAbstractGenerator
from nlp_natasha import *


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
                    or token.pos in ['ADP', 'CCONJ', 'PART', 'SCONJ', 'PRON', 'DET', 'PUNCT']
                    or token.text.isdigit()):
                continue

            token.lemmatize(morph_vocab)
            lemmas.append(token.lemma.lower())

            abstract.add_keyword(token.lemma)

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
                    abstract.add_phrase(token.lemma, chunk_words)

        sorted_keywords = abstract.get_sorted_keywords()[:top_n]
        abstract.keywords = sorted_keywords

        return abstract
