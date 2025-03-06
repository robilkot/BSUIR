class WordToken:
    def __init__(self, text, lemma, pos, feats, bibliographic=None, typological=None, index=None):
        self.text = text              # исходное слово
        self.lemma = lemma            # нормализованная форма
        self.pos = pos                # часть речи
        self.feats = feats            # морфологические признаки (словарь), теперь feats
        self.bibliographic = bibliographic or {}
        self.typological = typological or {}
        self.index = index

    def __repr__(self):
        return f"<WordToken text={self.text} lemma={self.lemma} pos={self.pos} feats={self.feats}>"