import string
from natasha import Doc, MorphVocab, Segmenter, NewsEmbedding, NewsMorphTagger
from model import NLPDatabase, Lemma, Form


def remove_punctuation(text: str):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    return clean_text


def lemmatize(text: str) -> Doc:
    segmenter = Segmenter()
    morph_vocab = MorphVocab()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)

    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    for token in doc.tokens:
        token.lemmatize(morph_vocab)

    return doc


def to_lw_format(doc: Doc) -> NLPDatabase:
    db = NLPDatabase(doc.text)

    for token in doc.tokens:
        form = Form(token.text, 0, None)

        item = Lemma(token.lemma)

        set_ = db.get(item, set())
        set_.add(form)

        db[item] = set_

    return db


def convert_text_to_db(text: str) -> NLPDatabase:
    clean = remove_punctuation(text)
    doc = lemmatize(clean)
    db = to_lw_format(doc)
    return db