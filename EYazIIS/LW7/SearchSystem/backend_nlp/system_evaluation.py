import os
import json
import random
from pathlib import Path
from urllib.parse import urlparse

import requests
from typing import List, Dict, Tuple
from dataclasses import dataclass
import statistics


@dataclass
class SearchResult:
    DocumentId: str
    Uri: str
    Title: str
    IndexedAt: str


class SearchEvaluator:
    def __init__(self, base_url: str, dataset_folder: str = "dataset"):
        self.base_url = base_url
        self.dataset_folder = dataset_folder
        self.documents_metadata = self.load_metadata()

    def load_metadata(self) -> List[Dict]:
        """Загружает метаданные датасета"""
        metadata_path = os.path.join(self.dataset_folder, 'metadata.json')
        if not os.path.exists(metadata_path):
            raise FileNotFoundError(f"Метаданные не найдены в {metadata_path}. Сначала сгенерируйте датасет.")

        with open(metadata_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def search_documents(self, text: str, start_date: str = None,
                         end_date: str = None, page_size: int = 0, page: int = 1) -> List[SearchResult]:
        """Выполняет поиск через API"""
        params = {'text': text, 'pageSize': page_size, 'page': page}

        if start_date:
            params['startDate'] = start_date
        if end_date:
            params['endDate'] = end_date

        try:
            response = requests.get(f"{self.base_url}/api/search", params=params, timeout=30)
            response.raise_for_status()

            results = []
            for item in response.json():
                results.append(SearchResult(DocumentId=item["documentId"],
                                            Uri=item["uri"],
                                            Title=item["title"],
                                            IndexedAt=item["indexedAt"]))

            return results
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return []

    def calculate_relevance(self, search_result: SearchResult, query: str, relevant_docs: List[str]) -> bool:
        """Определяет релевантность результата для запроса"""
        # Проверяем по ID документа
        if search_result.DocumentId in relevant_docs:
            return True

        with open(urlparse(search_result.Uri).path[1:], 'r', encoding='utf-8') as f:
            words = query.split()

            for word in words:
                if f.read().__contains__(word):
                    return True

        return False

    def create_test_queries(self, num_queries: int = 10) -> List[Tuple[str, List[str]]]:
        """Создает тестовые запросы на основе датасета"""
        if not self.documents_metadata:
            raise ValueError("Метаданные не загружены")

        test_queries = []

        # Используем ключевые слова из документов для создания запросов
        sample_docs = self.documents_metadata[:min(num_queries * 2, len(self.documents_metadata))]

        for doc in sample_docs:
            if doc['keywords'] and len(test_queries) < num_queries:
                # Берем 1-3 случайных ключевых слова для запроса
                num_keywords = random.randint(1, 3)
                query_words = random.sample(doc['keywords'], min(num_keywords, len(doc['keywords'])))
                query = ' '.join(query_words)

                # Находим документы, которые должны быть релевантными
                relevant_docs = []
                for other_doc in self.documents_metadata:
                    content_lower = other_doc['content'].lower()
                    if any(keyword in content_lower for keyword in query_words):
                        relevant_docs.append(other_doc['id'])

                if relevant_docs:  # Только запросы с релевантными документами
                    test_queries.append((query, relevant_docs))

        return test_queries

    def evaluate_precision_recall(self, results: List[SearchResult], query: str, relevant_docs: List[str]) -> Dict[
        str, float]:
        """Вычисляет precision и recall для одного запроса"""
        if not results:
            return {'precision': 0.0, 'recall': 0.0, 'average_precision': 0.0}

        relevant_found = 0
        precision_at_k = []

        for i, result in enumerate(results):
            is_relevant = self.calculate_relevance(result, query, relevant_docs)

            if is_relevant:
                relevant_found += 1
                # Precision@k
                precision_at_k.append(relevant_found / (i + 1))

        # Вычисляем метрики
        precision = relevant_found / len(results) if results else 0
        recall = relevant_found / len(relevant_docs) if relevant_docs else 0

        # Average Precision
        if precision_at_k and relevant_docs:
            avg_precision = sum(precision_at_k) / len(relevant_docs)
        else:
            avg_precision = 0.0

        return {
            'precision': precision,
            'recall': recall,
            'average_precision': avg_precision,
            'relevant_found': relevant_found,
            'total_relevant': len(relevant_docs),
            'total_results': len(results)
        }

    def evaluate_search(self, test_queries: List[Tuple[str, List[str]]]) -> Dict[str, float]:
        """Оценивает поисковую систему по метрикам"""
        all_metrics = {
            'precision': [],
            'recall': [],
            'average_precision': []
        }

        detailed_results = []

        print(f"Оценка по {len(test_queries)} тестовым запросам...")

        for i, (query, relevant_docs) in enumerate(test_queries):
            results = self.search_documents(query, page_size=0)

            metrics = self.evaluate_precision_recall(results, query, relevant_docs)
            print(metrics)

            all_metrics['precision'].append(metrics['precision'])
            all_metrics['recall'].append(metrics['recall'])
            all_metrics['average_precision'].append(metrics['average_precision'])

            detailed_results.append({
                'query': query,
                'metrics': metrics,
                'relevant_docs_count': len(relevant_docs),
                'results_count': len(results)
            })

        # Усредняем метрики по всем запросам
        final_metrics = {
            'mean_precision': statistics.mean(all_metrics['precision']),
            'mean_recall': statistics.mean(all_metrics['recall']),
            'mean_average_precision': statistics.mean(all_metrics['average_precision']),
            'total_queries': len(test_queries),
            'detailed_results': detailed_results
        }

        return final_metrics

    def run_evaluation(self, num_test_queries: int = 10) -> Dict[str, float]:
        """Запускает полный процесс оценки"""
        print("=== Загрузка датасета ===")
        print(f"Загружено документов: {len(self.documents_metadata)}")

        print("\n=== Создание тестовых запросов ===")
        test_queries = self.create_test_queries(num_test_queries)
        print(f"Создано тестовых запросов: {len(test_queries)}")

        print("\n=== Оценка поисковой системы ===")
        metrics = self.evaluate_search(test_queries)

        return metrics


# Функция для быстрого использования
def evaluate_search_system(base_url: str, dataset_folder: str = "dataset", num_queries: int = 10) -> Dict[str, float]:
    """Быстрая функция для оценки поисковой системы"""
    evaluator = SearchEvaluator(base_url, dataset_folder)
    metrics = evaluator.run_evaluation(num_queries)
    return metrics
