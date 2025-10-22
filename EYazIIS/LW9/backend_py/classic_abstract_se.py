import math
import re
from collections import Counter
from string import punctuation

from razdel import sentenize, tokenize

from backend_py.abstract import AbstractGenerator
from backend_py.classic_abstract import ClassicAbstract, ScoredWord, ScoredSentence


class SEClassicAbstractGenerator(AbstractGenerator):
    def __init__(self, language: str = 'russian'):
        """
        Args:
            language: язык текста ('russian' или 'english')
        """
        self.language = language.lower()
        self.stop_words = self._get_stop_words()

    def _get_stop_words(self):
        if self.language == 'english':
            return {
                'a', 'an', 'am', 've', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by',
                'about', 'as', 'into', 'like', 'through', 'after', 'over', 'between', 'out', 'against',
                'during', 'without', 'before', 'under', 'around', 'among', 'i', 'you', 'he', 'she', 'it',
                'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their',
                'mine', 'yours', 'hers', 'ours', 'theirs', 'this', 'that', 'these', 'those', 'is', 'are',
                'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did',
                'doing', 'will', 'would', 'shall', 'should', 'may', 'might', 'must', 'can', 'could', 'what',
                'which', 'who', 'whom', 'whose', 'where', 'when', 'why', 'how', 'all', 'any', 'both', 'each',
                'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
                'so', 'than', 'too', 'very', 'just', 'now', 'then', 'there', 'here', 'when', 'where', 'why',
                'how', 'also', 'even', 'well', 'back', 'down', 'up', 'off', 'on', 'again', 'further', 'then',
                'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'every'
            }
        else:
            return {
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

    def _is_valid_token(self, word: str) -> bool:
        if word in punctuation or word.isdigit():
            return False

        if len(word) <= 1:
            return False

        if word in self.stop_words:
            return False

        if self.language == 'english':
            return bool(re.match(r'^[a-zA-Z]+$', word))
        else:
            return not bool(re.match(r'^[a-zA-Z]+$', word))

    def preprocess_text(self, text: str) -> list[str]:
        """Предобработка текста: токенизация и нормализация"""
        tokens = []
        for token in tokenize(text):
            word = token.text.lower()
            if self._is_valid_token(word):
                tokens.append(word)
        return tokens

    def calculate_tf(self, document_tokens: list[str]) -> dict[str, float]:
        """Вычисление TF для документа"""
        total_words = len(document_tokens)
        word_counts = Counter(document_tokens)
        tf_scores = {}

        for word, count in word_counts.items():
            tf_scores[word] = count / total_words

        return tf_scores

    def calculate_idf(self, documents: list[list[str]]) -> dict[str, float]:
        """Вычисление IDF для коллекции документов"""
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
            return 0.0, []

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
        seen_texts = set()  # Track unique sentence texts

        for i, sentence in enumerate(sentences):
            sentence_text = sentence.strip()

            # Skip duplicate sentences
            if sentence_text in seen_texts:
                continue
            seen_texts.add(sentence_text)

            sentence_tokens = self.preprocess_text(sentence)
            score, scored_words = self.calculate_sentence_score(sentence_tokens, tf_scores, idf_scores)

            scored_sentence = ScoredSentence(
                original_text=sentence_text,
                normalized_text=sentence_text,
                score=score,
                position=i,
                words=scored_words
            )
            scored_sentences.append(scored_sentence)

        # Sort by score and take top sentences
        top_sentences = sorted(scored_sentences, key=lambda x: x.score, reverse=True)[:num_sentences]

        # Sort top sentences by original position to maintain readability
        top_sentences.sort(key=lambda x: x.position)

        total_score = sum(sentence.score for sentence in top_sentences)
        compression_ratio = 1 - len(top_sentences) / len(sentences) if sentences else 0

        return ClassicAbstract(sentences=top_sentences, total_score=total_score, compression_ratio=compression_ratio)


if __name__ == "__main__":
    sample_russian_text = """
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

    sample_english_text = """
    Artificial intelligence represents one of the most promising technologies of our time.
    Machine learning, which is a key component of AI, enables computers to learn from data.
    Deep learning uses neural networks with multiple layers to solve complex problems.
    In recent years, significant progress has been made in natural language processing.
    Transformers have revolutionized the approach to machine translation and text generation.
    Large language models such as GPT demonstrate impressive abilities in understanding context.
    Computer vision is also actively developing thanks to convolutional neural networks.
    Autonomous vehicles use AI for navigation in complex road conditions.
    Ethical issues of artificial intelligence are becoming increasingly relevant.
    Regulation of AI development and application requires careful consideration.
    The security of artificial intelligence systems is a critically important topic.
    The future of artificial intelligence is associated with creating more explainable and reliable systems.
    Research in the field of artificial general intelligence continues to develop.
    Collaboration between humans and AI opens up new possibilities for creativity.
    Educational systems based on AI personalize the learning process.
    Medical diagnostics using artificial intelligence increases the accuracy of analyses.
    Industry is actively implementing AI systems to optimize production processes.
    The financial sector uses machine learning algorithms for market forecasting.
    Cybersecurity is enhanced through the application of artificial intelligence methods.
    The development of quantum computing could significantly accelerate the training of AI models.
    """

    print("=== РУССКИЙ ТЕКСТ ===")
    generator_ru = SEClassicAbstractGenerator(language='russian')
    abstract_ru = generator_ru.generate(sample_russian_text, num_sentences=5)
    abstract_ru.print()

    print("\n" + "=" * 80 + "\n")

    print("=== ENGLISH TEXT ===")
    generator_en = SEClassicAbstractGenerator(language='english')
    abstract_en = generator_en.generate(sample_english_text, num_sentences=5)
    abstract_en.print()