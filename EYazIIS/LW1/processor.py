import string
from natasha import Doc, MorphVocab, Segmenter, NewsEmbedding, NewsMorphTagger
from model import NLPDatabase, Lemma, FormInfo


# Функция удаления пунктуации из текста
def remove_punctuation(text: str):
    translator = str.maketrans('', '', string.punctuation)
    clean_text = text.translate(translator)
    return clean_text


# Функция лемматизации слов в тексте
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


# Функция перевода документа Natasha в формат лабороторной работы
def to_lw_format(db: NLPDatabase, doc: Doc):
    for token in doc.tokens:
        new_form_info = FormInfo(1, None)

        lemma = Lemma(token.lemma)

        form_dict = db.get(lemma, {})
        form_info = form_dict.get(token.text)

        if form_info is None:
            form_dict[token.text] = new_form_info
        else:
            form_info.frequency += 1

        db[lemma] = form_dict

    db.word_count = len(doc.tokens)


# Функция перевода строки текста в формат лабороторной работы
def convert_text_to_db(text: str) -> NLPDatabase:
    db = NLPDatabase(text)
    text = text.lower()
    clean = remove_punctuation(text)
    doc = lemmatize(clean)
    to_lw_format(db, doc)
    return db
