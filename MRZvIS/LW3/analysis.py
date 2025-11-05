###############################
# Лабораторная работа №3 по дисциплине МРЗвИС
# Выполнена студентом группы 221701 БГУИР Робилко Тимуром Марковичем
# Файл, содержащий функции построения графиков для оценки работы нейросети
#
import matplotlib.pyplot as plt
import numpy as np

from main import ImageDataLoader, AutoEncoder, adaptive_a_func


def analyze_learning_rate_dependency(
        image_path: str,
        r: int = 12,
        m: int = 12,
        compression_coef: int = 6,
        target_error: float = 500,
        learning_rates: list[float] = None,
        max_iterations: int = 100
) -> None:
    """
    Анализ зависимости количества итераций от коэффициента обучения
    """
    print("=== Анализ зависимости от коэффициента обучения ===")

    if learning_rates is None:
        learning_rates = [0.005, 0.003, 0.001, 0.0005, 0.0001]

    iterations_data = []

    for lr in learning_rates:
        def constant_lr_func(_) -> float:
            return lr

        auto_encoder = AutoEncoder(constant_lr_func, constant_lr_func, np.float32)
        auto_encoder.init_weights(3 * r * m, compression_coef)

        loader = ImageDataLoader(image_path, r, m)

        iterations = 0
        for epoch, epoch_error in auto_encoder.train(loader, target_error, max_iterations):
            iterations = epoch
            if epoch_error <= target_error:
                break

        iterations_data.append(iterations)
        print(f"Learning rate: {lr:.3f}, Iterations: {iterations}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(learning_rates, iterations_data, 'bo-', linewidth=2, markersize=8)
    plt.xscale('log')
    plt.xlabel('Коэффициент обучения')
    plt.ylabel('Количество итераций')
    plt.title('Зависимость количества итераций от коэффициента обучения')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def analyze_compression_coef_dependency(
        image_path: str,
        r: int = 4,
        m: int = 4,
        target_error: float = 500,
        compression_coefs: list[float] = None,
        max_iterations: int = 100
) -> None:
    """
    Анализ зависимости количества итераций от коэффициента сжатия
    """
    print("\n=== Анализ зависимости от коэффициента сжатия ===")

    if compression_coefs is None:
        compression_coefs = [4.2, 5, 5.5, 6, 6.5, 7, 7.5, 8]

    iterations_data = []

    for comp_coef in compression_coefs:
        auto_encoder = AutoEncoder(adaptive_a_func, adaptive_a_func, np.float32)
        auto_encoder.init_weights(3 * r * m, comp_coef)

        loader = ImageDataLoader(image_path, r, m)

        iterations = 0
        for epoch, epoch_error in auto_encoder.train(loader, target_error, max_iterations):
            iterations = epoch
            if epoch_error <= target_error:
                break

        iterations_data.append(iterations)
        print(f"Compression coefficient: {comp_coef}, Iterations: {iterations}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(compression_coefs, iterations_data, 'ro-', linewidth=2, markersize=8)
    plt.xlabel('Коэффициент сжатия')
    plt.ylabel('Количество итераций')
    plt.title('Зависимость количества итераций от коэффициента сжатия')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def analyze_image_type_dependency(
        image_paths: list[str],
        image_names: list[str],
        r: int = 4,
        m: int = 4,
        compression_coef: int = 4,
        target_error: float = 1000,
        max_iterations: int = 50
) -> None:
    """
    Анализ зависимости количества итераций от типа изображения
    """
    print("\n=== Анализ зависимости от типа изображения ===")

    iterations_data = []

    for img_path in image_paths:
        auto_encoder = AutoEncoder(adaptive_a_func, adaptive_a_func, np.float32)
        auto_encoder.init_weights(3 * r * m, compression_coef)

        loader = ImageDataLoader(img_path, r, m)

        iterations = 0
        for epoch, epoch_error in auto_encoder.train(loader, target_error, max_iterations):
            iterations = epoch
            if epoch_error <= target_error:
                break

        iterations_data.append(iterations)
        print(f"Image: {img_path}, Iterations: {iterations}")

    # Построение графика
    plt.figure(figsize=(12, 6))
    bars = plt.bar(image_names, iterations_data, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
    plt.xlabel('Тип изображения')
    plt.ylabel('Количество итераций')
    plt.title('Зависимость количества итераций от типа изображения')

    # Добавление значений на столбцы
    for bar, value in zip(bars, iterations_data):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 str(value), ha='center', va='bottom')

    plt.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    plt.show()


def analyze_error_threshold_dependency(
        image_path: str,
        r: int = 4,
        m: int = 4,
        compression_coef: int = 5,
        error_thresholds: list[float] = None,
        max_iterations: int = 50
) -> None:
    """
    Анализ зависимости количества итераций от величины ошибки
    """
    print("\n=== Анализ зависимости от величины ошибки ===")

    if error_thresholds is None:
        error_thresholds = [2000, 1600, 1300, 1100, 900, 700, 500, 300]

    iterations_data = []

    for error_threshold in error_thresholds:
        auto_encoder = AutoEncoder(adaptive_a_func, adaptive_a_func, np.float32)
        auto_encoder.init_weights(3 * r * m, compression_coef)

        loader = ImageDataLoader(image_path, r, m)

        iterations = 0
        for epoch, epoch_error in auto_encoder.train(loader, error_threshold, max_iterations):
            iterations = epoch
            if epoch_error <= error_threshold:
                break

        iterations_data.append(iterations)
        print(f"Error threshold: {error_threshold}, Iterations: {iterations}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(error_thresholds, iterations_data, 'go-', linewidth=2, markersize=8)
    plt.xlabel('Порог ошибки')
    plt.ylabel('Количество итераций')
    plt.title('Зависимость количества итераций от величины ошибки')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


# Дополнительная функция для анализа прогресса обучения
def analyze_training_progress(
        image_path: str,
        r: int = 4,
        m: int = 4,
        compression_coef: int = 4,
        max_iterations: int = 50
) -> None:
    """
    Анализ прогресса обучения во времени
    """

    auto_encoder = AutoEncoder(adaptive_a_func, adaptive_a_func, np.float32)
    auto_encoder.init_weights(3 * r * m, compression_coef)

    loader = ImageDataLoader(image_path, r, m)

    iterations = []
    errors = []

    for epoch, epoch_error in auto_encoder.train(loader, 0.1, max_iterations):
        iterations.append(epoch)
        errors.append(epoch_error)
        print(f"Epoch {epoch}, Error: {epoch_error:.6f}")

    # Построение графика прогресса обучения
    plt.figure(figsize=(12, 5))

    plt.plot(iterations, errors, 'b-', linewidth=2)
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка')
    plt.title('Прогресс обучения')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # analyze_learning_rate_dependency('test_images/lena.bmp', r=10, m=10, target_error=500, max_iterations=200, learning_rates=[0.0095, 0.007, 0.0035, 0.001, 0.00075, 0.0005, 0.00025])
    # analyze_compression_coef_dependency('test_images/blackbuck.bmp', r=10, m=10, target_error=750, compression_coefs=[4, 7, 10, 13, 16, 19])
    # analyze_error_threshold_dependency('test_images/lena.bmp', r=10, m=10, max_iterations=200, compression_coef=10)

    image_paths = [
        'test_images/solid_color.png',
        'test_images/lena.bmp',
        'test_images/golub.png',
        'test_images/two_colors.png',
        'test_images/52.jpg'
    ]
    image_names = [
        'Простое',
        'Простое',
        'Среднее',
        'Сложное',
        'Высокое разрешение'
    ]
    # analyze_image_type_dependency(image_paths, image_names)


    # analyze_training_progress('test_images/52.jpg')
    # analyze_training_progress('test_images/snail.bmp')
    analyze_training_progress('test_images/lena.bmp', r=10, m=10)
    # analyze_training_progress('test_images/blackbuck.bmp')
    # analyze_training_progress('test_images/golub.png')