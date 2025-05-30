import string
from setup import *
from word_token import WordToken

class CorpusEntry:
    def __init__(self, entry_id, text, bibliographic=None, typological=None):
        self.id = entry_id
        self.text = text
        self.bibliographic = bibliographic or {}
        self.typological = typological or {}
        self.tokens = self.analyze_text(text)

    def analyze_text(self, text):
        """
        Анализ текста с использованием Natasha:
         - сегментация, морфологическая разметка, лемматизация.
        """
        doc = Doc(text)
        doc.segment(segmenter)
        doc.tag_morph(morph_tagger)
        tokens = []
        for i, token in enumerate(doc.tokens):
            token.lemmatize(morph_vocab)
            token_data = WordToken(
                text=token.text,
                lemma=token.lemma,
                pos=token.pos,
                feats=token.feats,
                index=i
            )

            if token_data.pos == 'DET':
                token_data.pos = 'PRON'
            elif token_data.pos == 'CCONJ' or token_data.pos == 'SCONJ':
                token_data.pos = 'CONJ'
            elif token_data.pos == 'PROPN':
                token_data.pos = 'NOUN'
            elif token_data.pos == 'AUX':
                token_data.pos = 'VERB'

            token_data.feats['pos'] = token_data.pos

            tokens.append(token_data)
        return tokens

    def __repr__(self):
        return f"<CorpusEntry id={self.id} tokens={self.tokens}>"

    # Функция удаления пунктуации из текста
    def __remove_punctuation(self, text: str):
        translator = str.maketrans('', '', string.punctuation)
        clean_text = text.translate(translator)
        return clean_text