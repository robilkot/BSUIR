from natasha import Segmenter, NewsEmbedding, NewsMorphTagger, MorphVocab, Doc

segmenter = Segmenter()
embedding = NewsEmbedding()
morph_tagger = NewsMorphTagger(embedding)
morph_vocab = MorphVocab()
