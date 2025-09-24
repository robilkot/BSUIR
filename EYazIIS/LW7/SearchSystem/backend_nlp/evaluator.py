from dataset_generator import DatasetGenerator
from system_evaluation import evaluate_search_system


def main():
    # Конфигурация
    DATASET_FOLDER = 'D:/indexingTest'
    SEARCH_API_URL = "http://localhost:5054"
    NUM_TEST_QUERIES = 25

    generator = DatasetGenerator(DATASET_FOLDER)

    info = generator.get_dataset_info()
    print(f"\nСгенерировано документов: {info['total_documents']}")
    print(f"Общее количество слов: {info['total_words']}")

    print("\n=== Оценка поисковой системы ===")

    metrics = evaluate_search_system(SEARCH_API_URL, DATASET_FOLDER, NUM_TEST_QUERIES)

    print(metrics)


if __name__ == "__main__":
    main()