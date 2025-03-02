import time
import matplotlib.pyplot as plt
from processor import convert_text_to_db
import os

def run_test(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()

    start = time.time()
    db = convert_text_to_db(text)
    end = time.time()

    processing_time = end - start
    count = db.word_count
    return count, processing_time

if __name__ == '__main__':
    dataset = 'dataset'
    texts = [os.path.join(dataset, file) for file in os.listdir(dataset) if file.endswith('.txt')]
    plot_values = []

    print("running tests")

    for filename in texts:
        iterations = 10
        count: int = 0
        total_processing_time: float = 0

        for i in range(iterations):
            count, processing_time = run_test(filename)
            total_processing_time += processing_time

        plot_values.append((count, total_processing_time / iterations))
        print(total_processing_time / iterations)

    plot_values.sort(key=lambda x: x[0])
    word_counts, processing_times = zip(*plot_values)

    plt.plot(word_counts, processing_times, marker='o')
    plt.xlabel('Количество слов в тексте')
    plt.ylabel('Время обработки (с)')
    plt.title('Зависимость времени обработки от количества слов')
    plt.grid(True)
    plt.show()
