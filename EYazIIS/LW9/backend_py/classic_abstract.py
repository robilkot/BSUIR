import math
import re
from collections import Counter
from dataclasses import dataclass, field
from string import punctuation

from razdel import sentenize, tokenize

from abstract import AbstractGenerator


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
            print()


class ClassicAbstractGenerator(AbstractGenerator):
    """Генератор классического реферата методом sentence extraction"""
    def __init__(self):
        self.stop_words = {
            'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она',
            'так', 'его', 'но', 'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее',
            'мне', 'было', 'вот', 'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда',
            'даже', 'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 'него', 'до',
            'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом', 'себя', 'ничего', 'ей',
            'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их', 'чем',
            'была', 'сам', 'чтоб', 'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет',
            'ж', 'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним',
            'здесь', 'этом', 'один', 'почти', 'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда',
            'зачем', 'всех', 'никогда', 'можно', 'при', 'наконец', 'два', 'об', 'другой', 'хоть',
            'после', 'над', 'больше', 'тот', 'через', 'эти', 'нас', 'про', 'всего', 'них', 'какая',
            'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой', 'перед',
            'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно',
            'всю', 'между'
        }

    def preprocess_text(self, text: str) -> list[str]:
        """Предобработка текста: токенизация и нормализация"""
        tokens = []
        for token in tokenize(text):
            word = token.text.lower()
            # Удаляем пунктуацию, числа, латинские буквы и стоп-слова
            if (word not in punctuation and
                    not word.isdigit() and
                    not re.match(r'^[a-zA-Z]+$', word) and
                    word not in self.stop_words and
                    len(word) > 1):
                tokens.append(word)
        return tokens

    def calculate_tf(self, document_tokens: list[str]) -> dict[str, float]:
        """Вычисление TF (Term Frequency) для документа"""
        total_words = len(document_tokens)
        word_counts = Counter(document_tokens)
        tf_scores = {}

        for word, count in word_counts.items():
            tf_scores[word] = count / total_words

        return tf_scores

    def calculate_idf(self, documents: list[list[str]]) -> dict[str, float]:
        """Вычисление IDF (Inverse Document Frequency) для коллекции документов"""
        num_documents = len(documents)
        idf_scores = {}

        all_words = set()
        for doc in documents:
            all_words.update(doc)

        for word in all_words:
            doc_count = sum(1 for doc in documents if word in doc)
            idf_scores[word] = math.log(num_documents / (doc_count + 1)) + 1  # +1 для сглаживания

        return idf_scores

    def calculate_sentence_score(self, sentence_tokens: list[str],
                                 tf_scores: dict[str, float],
                                 idf_scores: dict[str, float]) -> (float, list):
        """Вычисление веса предложения на основе TF-IDF слов"""
        if not sentence_tokens:
            return 0.0

        total_score = 0.0
        scored_words = []

        for token in sentence_tokens:
            tf = tf_scores.get(token, 0.0)
            idf = idf_scores.get(token, 0.0)
            word_score = tf * idf
            total_score += word_score
            scored_words.append(ScoredWord(word=token, tfidf_score=word_score))

        # Нормализуем по длине предложения
        normalized_score = total_score / len(sentence_tokens)

        return normalized_score, scored_words

    def generate(self, text: str, num_sentences: int = 10) -> ClassicAbstract:
        sentences = [sentence.text for sentence in sentenize(text)]

        all_tokens = self.preprocess_text(text)

        # Создаем "документы" для IDF (каждое предложение - отдельный документ)
        sentence_documents = []
        for sentence in sentences:
            sentence_tokens = self.preprocess_text(sentence)
            sentence_documents.append(sentence_tokens)

        tf_scores = self.calculate_tf(all_tokens)
        idf_scores = self.calculate_idf(sentence_documents)

        scored_sentences = []
        for i, sentence in enumerate(sentences):
            sentence_tokens = self.preprocess_text(sentence)
            score, scored_words = self.calculate_sentence_score(sentence_tokens, tf_scores, idf_scores)

            scored_sentence = ScoredSentence(
                original_text=sentence.strip(),
                normalized_text=sentence.strip(),
                score=score,
                position=i,
                words=scored_words
            )
            scored_sentences.append(scored_sentence)

        top_sentences = sorted(scored_sentences, key=lambda x: x.score, reverse=True)[:num_sentences]

        total_score = sum(sentence.score for sentence in top_sentences)
        compression_ratio = 1 - len(top_sentences) / len(sentences) if sentences else 0

        return ClassicAbstract(sentences=top_sentences, total_score=total_score, compression_ratio=compression_ratio)


if __name__ == "__main__":
    sample_text = """
    Искусственный интеллект представляет собой одну из наиболее перспективных технологий современности. 
    Машинное обучение, являющееся ключевой составляющей ИИ, позволяет компьютерам обучаться на основе данных. 
    Глубокое обучение использует нейронные сети с множеством слоев для решения сложных задач. 
    В последние годы достигнут значительный прогресс в области обработки естественного языка. 
    Трансформеры революционизировали подход к машинному переводу и генерации текста. 
    Большие языковые модели, такие как GPT, демонстрируют впечатляющие способности в понимании контекста. 
    Компьютерное зрение также активно развивается благодаря сверточным нейронным сетям. 
    Автономные транспортные средства используют ИИ для навигации в сложных дорожных условиях. 
    Этические вопросы искусственного интеллекта становятся все более актуальными. 
    Регулирование разработки и применения ИИ требует внимательного подхода. 
    Безопасность систем искусственного интеллекта является критически важной темой. 
    Будущее искусственного интеллекта связано с созданием более объяснимых и надежных систем. 
    Исследования в области искусственного общего интеллекта продолжают развиваться. 
    Коллаборация между человеком и ИИ открывает новые возможности для творчества. 
    Образовательные системы на основе ИИ персонализируют процесс обучения. 
    Медицинская диагностика с использованием искусственного интеллекта повышает точность анализов. 
    Промышленность активно внедряет системы ИИ для оптимизации производственных процессов. 
    Финансовый сектор использует алгоритмы машинного обучения для прогнозирования рынков. 
    Кибербезопасность усиливается за счет применения методов искусственного интеллекта. 
    Развитие квантовых вычислений может значительно ускорить тренировку моделей ИИ.
    """

    generator = ClassicAbstractGenerator()
    abstract = generator.generate(sample_text, num_sentences=10)

    abstract.print()
