from dataclasses import field, dataclass


@dataclass
class ScoredWord:
    word: str
    tfidf_score: float = 0.0


@dataclass
class ScoredSentence:
    original_text: str
    normalized_text: str = ""
    score: float = 0.0
    position: int = 0
    words: list[ScoredWord] = field(default_factory=list)


@dataclass
class ClassicAbstract:
    sentences: list[ScoredSentence] = field(default_factory=list)
    total_score: float = 0.0
    compression_ratio: float = 0.0

    def print(self):
        print(f"Общий вес: {self.total_score:.3f}")
        print(f"Степень сжатия: {self.compression_ratio:.1%}")
        print(f"Количество предложений: {len(self.sentences)}")
        print("-" * 80)

        for i, sentence in enumerate(self.sentences, 1):
            print(f"{i}. {sentence.original_text}")

            top_words = sorted(sentence.words, key=lambda x: x.tfidf_score, reverse=True)[:3]
            if top_words:
                words_info = ", ".join([f"'{w.word}'(TF-IDF:{w.tfidf_score:.3f})" for w in top_words])
                print(f"   [Вес: {sentence.score:.3f}] Ключевые слова: {words_info}")