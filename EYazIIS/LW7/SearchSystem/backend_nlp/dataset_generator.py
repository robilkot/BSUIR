import os
import uuid
import random
import json
from datetime import datetime, timedelta
from typing import List, Dict


class DatasetGenerator:
    def __init__(self, dataset_folder: str = "dataset"):
        self.dataset_folder = dataset_folder
        self.documents_metadata = []

        # Русские слова в разных формах для генерации контента
        self.russian_words = {
            'существительные': [
                'компьютер', 'программа', 'данные', 'система', 'информация',
                'разработка', 'технология', 'алгоритм', 'база', 'сеть',
                'пользователь', 'интерфейс', 'код', 'файл', 'папка',
                'проект', 'команда', 'решение', 'задача', 'метод',
                'город', 'студент', 'университет', 'преподаватель', 'экзамен',
                'книга', 'библиотека', 'исследование', 'наука', 'лаборатория',
                'компания', 'рынок', 'бизнес', 'продукт', 'услуга',
                'искусство', 'музыка', 'живопись', 'литература', 'культура'
            ],
            'прилагательные': [
                'новый', 'эффективный', 'быстрый', 'надежный', 'современный',
                'цифровой', 'автоматический', 'интеллектуальный', 'оптимальный',
                'уникальный', 'основной', 'дополнительный', 'важный', 'сложный',
                'российский', 'федеральный', 'городской', 'местный', 'центральный',
                'технический', 'научный', 'академический', 'образовательный', 'учебный',
                'коммерческий', 'финансовый', 'экономический', 'производственный'
            ],
            'глаголы': [
                'работать', 'создавать', 'использовать', 'разрабатывать', 'анализировать',
                'обрабатывать', 'хранить', 'передавать', 'получать', 'изучать',
                'тестировать', 'оптимизировать', 'внедрять', 'управлять', 'контролировать',
                'обучать', 'исследовать', 'экспериментировать', 'доказывать', 'обсуждать',
                'продавать', 'покупать', 'инвестировать', 'производить', 'распространять'
            ]
        }

        # Тематики для документов
        self.topics = [
            "технологии и программирование",
            "наука и исследования",
            "бизнес и управление",
            "образование и обучение",
            "искусство и культура",
            "городское развитие и инфраструктура",
            "медицина и здоровье",
            "спорт и активный образ жизни"
        ]

    def generate_russian_text(self, min_words: int = 50, max_words: int = 300) -> str:
        """Генерирует русский текст со случайными словами"""
        words_count = random.randint(min_words, max_words)
        words = []

        for _ in range(words_count):
            word_type = random.choice(list(self.russian_words.keys()))
            word = random.choice(self.russian_words[word_type])

            words.append(word)

        # Формируем предложения
        sentences = []
        current_sentence = []

        for i, word in enumerate(words):
            current_sentence.append(word)
            if len(current_sentence) >= random.randint(5, 15) or i == len(words) - 1:
                sentence = ' '.join(current_sentence).capitalize()
                if not sentence.endswith('.'):
                    sentence += '.'
                sentences.append(sentence)
                current_sentence = []

        return ' '.join(sentences)

    def extract_keywords(self, text: str, max_keywords: int = 5) -> List[str]:
        """Извлекает ключевые слова из текста"""
        words = text.lower().split()
        word_freq = {}

        for word in words:
            # Игнорируем короткие слова и некоторые служебные
            if len(word) > 4 and not word.endswith(('ные', 'овые', 'ение')):
                word_freq[word] = word_freq.get(word, 0) + 1

        # Сортируем по частоте и берем топ ключевых слов
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:max_keywords]]

    def generate_document(self, index: int) -> Dict:
        """Генерирует один документ с метаданными"""
        doc_id = str(uuid.uuid4())
        filename = f"document_{index + 1:04d}.txt"
        filepath = os.path.join(self.dataset_folder, filename)
        topic = random.choice(self.topics)

        # Генерируем дату создания (в пределах последнего года)
        base_date = datetime.now() - timedelta(days=365)
        created_date = base_date + timedelta(days=random.randint(0, 365))

        # Генерируем содержимое
        content = self.generate_russian_text()
        keywords = self.extract_keywords(content)

        # Сохраняем файл
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"{content}")

        return {
            'id': doc_id,
            'filename': filename,
            'filepath': filepath,
            'content': content,
            'created_date': created_date.isoformat(),
            'keywords': keywords,
            'topic': topic
        }

    def generate_dataset(self, num_documents: int = 100) -> str:
        """Генерирует датасет документов и возвращает путь к папке"""
        if not os.path.exists(self.dataset_folder):
            os.makedirs(self.dataset_folder)

        self.documents_metadata = []

        print(f"Генерация {num_documents} документов...")
        for i in range(num_documents):
            doc_metadata = self.generate_document(i)
            self.documents_metadata.append(doc_metadata)

            if (i + 1) % 10 == 0:
                print(f"Создано документов: {i + 1}/{num_documents}")

        # Сохраняем метаданные для использования в оценке
        metadata_path = os.path.join(self.dataset_folder, 'metadata.json')
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.documents_metadata, f, ensure_ascii=False, indent=2, default=str)

        print(f"Датасет создан в папке: {os.path.abspath(self.dataset_folder)}")
        print(f"Метаданные сохранены в: {metadata_path}")

        return self.dataset_folder

    def get_dataset_info(self) -> Dict:
        """Возвращает информацию о сгенерированном датасете"""
        if not self.documents_metadata:
            metadata_path = os.path.join(self.dataset_folder, 'metadata.json')
            if os.path.exists(metadata_path):
                with open(metadata_path, 'r', encoding='utf-8') as f:
                    self.documents_metadata = json.load(f)

        if not self.documents_metadata:
            return {"error": "Датасет не найден или не сгенерирован"}

        total_words = sum(len(doc['content'].split()) for doc in self.documents_metadata)
        unique_keywords = set(keyword for doc in self.documents_metadata for keyword in doc['keywords'])

        return {
            "total_documents": len(self.documents_metadata),
            "total_words": total_words,
            "unique_keywords": len(unique_keywords),
            "topics": list(set(doc['topic'] for doc in self.documents_metadata)),
            "date_range": {
                "min": min(doc['created_date'] for doc in self.documents_metadata),
                "max": max(doc['created_date'] for doc in self.documents_metadata)
            }
        }


# Функция для быстрого использования
def generate_dataset(dataset_folder: str = "dataset", num_documents: int = 100) -> str:
    """Быстрая функция для генерации датасета"""
    generator = DatasetGenerator(dataset_folder)
    return generator.generate_dataset(num_documents)


if __name__ == "__main__":
    # Пример использования
    generator = DatasetGenerator("D:/indexingTest")
    dataset_path = generator.generate_dataset(250)

    info = generator.get_dataset_info()
    print("\nИнформация о датасете:")
    print(f"Документов: {info['total_documents']}")
    print(f"Слов: {info['total_words']}")
    print(f"Уникальных ключевых слов: {info['unique_keywords']}")
    print(f"Темы: {', '.join(info['topics'])}")
