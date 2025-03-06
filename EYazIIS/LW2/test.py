import time
import matplotlib.pyplot as plt
import os
from corpus_entry import CorpusEntry

def run_test(entry_id: int, text: str):
    count = len(text)
    start = time.time()
    entry = CorpusEntry(entry_id, text)
    end = time.time()
    processing_time = end - start
    return count, processing_time

if __name__ == '__main__':
    dataset = 'dataset'
    file_paths = sorted([os.path.join(dataset, file) for file in os.listdir(dataset) if file.endswith('.txt')])
    plot_values = []

    print("Running tests with accumulating texts...")

    accumulated_text = ""
    iteration = 0

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_text = f.read()
        accumulated_text += file_text
        iteration += 1

        iterations = 10
        total_processing_time = 0

        for i in range(iterations):
            count, processing_time = run_test(i, accumulated_text)
            total_processing_time += processing_time

        avg_processing_time = total_processing_time / iterations
        plot_values.append((len(accumulated_text), avg_processing_time))
        print(f"Iteration {iteration}: {len(accumulated_text)} символов, среднее время: {avg_processing_time:.4f} с")

    plot_values.sort(key=lambda x: x[0])
    word_counts, processing_times = zip(*plot_values)

    plt.plot(word_counts, processing_times, marker='o')
    plt.xlabel('Количество символов в накопленном тексте')
    plt.ylabel('Время обработки (с)')
    plt.title('Зависимость времени обработки от размера текста')
    plt.grid(True)
    plt.show()
