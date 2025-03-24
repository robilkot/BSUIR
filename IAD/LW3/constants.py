MODEL_PATH = "pos_tagger_model.pth"

FILLER = '\0'

POS_MAPPING = {
    'NOUN': 0,
    'VERB': 1,
    'PRON': 2,
    'NUM': 3,
    'ADP': 4,
    'PUNCT': 5,
    'ADV': 6,
    'ADJ': 7,
    'CONJ': 8,
    'PART': 9,
    'LATN': 10,
    'X': 11,
    'H': 12,
    'DET': 13,
    'INTJ': 14,
}

INVERSE_POS_MAPPING = {v: k for k, v in POS_MAPPING.items()}