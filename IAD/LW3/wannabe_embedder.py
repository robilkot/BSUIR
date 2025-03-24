import math

import numpy as np

from constants import POS_MAPPING


def make_embeddings_and_outputs(corpus, symbols_count) -> (np.ndarray, np.ndarray):
    embeddings = []
    outputs = []
    indexes_in_corpus = []

    for index, pair in enumerate(corpus):
        word = corpus[index][0]

        embedding = embed_word(word, symbols_count)

        indexes_in_corpus.append(index)
        embeddings.append(embedding)

        try:
            outputs.append(POS_MAPPING[corpus[index][1]])
        except:
            print('Unknown key: ', corpus[index])
            outputs.append(11)

    indexes_in_corpus = np.array(indexes_in_corpus, dtype='uint32')
    embeddings = np.array(embeddings, dtype='uint8')
    outputs = np.array(outputs, dtype='uint8')

    return indexes_in_corpus, embeddings, outputs


def embed_word(word, n_symbols) -> np.ndarray:
    padded: str = word.rjust(n_symbols, '\0')[-n_symbols:]

    try:
        encoded = padded.encode('iso-8859-5')
    except:
        try:
            encoded = padded.replace('—', '-').replace('…', '.').encode('iso-8859-5')
        except:
            print(word)
            raise

    embedding = np.frombuffer(encoded, dtype=np.uint8)
    return embedding
