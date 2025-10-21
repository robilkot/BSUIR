from string import punctuation

import spacy

from keyword_abstract import KeywordAbstract, KeywordAbstractGenerator


class ENKeywordAbstractGenerator(KeywordAbstractGenerator):
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(spacy.lang.en.stop_words.STOP_WORDS)
        self.ignore_pos = {'ADP', 'CCONJ', 'PART', 'SCONJ', 'PRON', 'DET', 'AUX', 'SYM', 'X', 'SPACE'}

    def is_valid_token(self, token) -> bool:
        return (token.text not in punctuation and
                not token.is_digit and
                not token.is_space and
                token.pos_ not in self.ignore_pos and
                token.lemma_.lower() not in self.stop_words and
                len(token.text) > 1 and
                not token.is_punct)


    def generate(self, text: str, top_n: int = 20) -> KeywordAbstract:
        doc = self.nlp(text)

        keyword_structure = KeywordAbstract()

        for token in doc:
            if self.is_valid_token(token):
                lemma = token.lemma_.lower()
                keyword_structure.add_keyword(lemma)

        chunks = []
        for chunk in doc.noun_chunks:
            chunk_tokens = [token for token in chunk if self.is_valid_token(token)]

            if any(token.pos_ in {'NOUN', 'PROPN', 'ADJ'} for token in chunk_tokens):
                if len(chunk) > 1:
                    chunks.append(chunk_tokens)

        for chunk in chunks:
            chunk_text = ' '.join([token.text for token in chunk]).lower()

            for token in chunk:
                lemma_word = token.lemma_.lower()
                if any(node.keyword == lemma_word for node in keyword_structure.keywords):
                    keyword_structure.add_phrase(lemma_word, chunk_text)

        sorted_keywords = keyword_structure.get_sorted_keywords()[:top_n]
        keyword_structure.keywords = sorted_keywords

        return keyword_structure


# Пример использования
if __name__ == "__main__":
    # Пример английского текста
    sample_text = """
    Artificial intelligence is one of the most promising technologies of our time. 
    Machine learning, which is a key component of AI, enables computers to learn from data. 
    Deep learning uses neural networks with multiple layers to solve complex problems. 
    In recent years, significant progress has been made in natural language processing. 
    Transformers have revolutionized the approach to machine translation and text generation. 
    Large language models such as GPT demonstrate impressive abilities in understanding context. 
    Computer vision is also actively developing thanks to convolutional neural networks. 
    Autonomous vehicles use AI for navigation in complex road conditions. 
    Ethical issues of artificial intelligence are becoming increasingly relevant. 
    Regulation of AI development and application requires careful consideration. 
    The safety of artificial intelligence systems is a critically important topic. 
    The future of artificial intelligence is associated with creating more explainable and reliable systems. 
    Research in the field of artificial general intelligence continues to develop. 
    Collaboration between humans and AI opens up new opportunities for creativity. 
    Educational systems based on AI personalize the learning process. 
    Medical diagnostics using artificial intelligence improves the accuracy of analyses. 
    Industry is actively implementing AI systems to optimize production processes. 
    The financial sector uses machine learning algorithms to predict markets. 
    Cybersecurity is enhanced through the application of artificial intelligence methods. 
    The development of quantum computing can significantly accelerate AI model training.
    """

    keyword_abstract = ENKeywordAbstractGenerator().generate(sample_text, top_n=10)
    keyword_abstract.print()