import matplotlib.pyplot as plt
import numpy as np

from main import ImageDataLoader, AutoEncoder, adaptive_af_func, adaptive_ab_func


def analyze_learning_rate_dependency(
        image_path: str,
        r: int = 4,
        m: int = 4,
        compression_coef: int = 6,
        target_error: float = 10,
        learning_rates: list[float] = None,
        max_iterations: int = 100
) -> None:
    """
    Анализ зависимости количества итераций от коэффициента обучения
    """
    if learning_rates is None:
        learning_rates = [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5]

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
        target_error: float = 10,
        compression_coefs: list[float] = None,
        max_iterations: int = 100
) -> None:
    """
    Анализ зависимости количества итераций от коэффициента сжатия
    """
    if compression_coefs is None:
        compression_coefs = [4.2, 5, 6, 7, 8, 9, 10, 11]

    iterations_data = []

    for comp_coef in compression_coefs:
        auto_encoder = AutoEncoder(adaptive_af_func, adaptive_ab_func, np.float32)
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
        compression_coef: int = 6,
        target_error: float = 100,
        max_iterations: int = 100
) -> None:
    """
    Анализ зависимости количества итераций от типа изображения
    """
    iterations_data = []

    for img_path in image_paths:
        auto_encoder = AutoEncoder(adaptive_af_func, adaptive_ab_func, np.float32)
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
        compression_coef: int = 6,
        error_thresholds: list[float] = None,
        max_iterations: int = 250
) -> None:
    """
    Анализ зависимости количества итераций от величины ошибки
    """
    if error_thresholds is None:
        error_thresholds = [3000, 1500, 1000, 750, 500, 250, 100, 50]

    iterations_data = []

    for error_threshold in error_thresholds:
        auto_encoder = AutoEncoder(adaptive_af_func, adaptive_ab_func, np.float32)
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


def run_comprehensive_analysis():
    """
    Запуск комплексного анализа всех зависимостей
    """
    # Пример использования с разными изображениями
    image_paths = [
        'test_images/blackbuck.bmp',
        'test_images/blackbuck.bmp',  # Замените на другие изображения
        'test_images/blackbuck.bmp',
        'test_images/blackbuck.bmp'
    ]

    image_names = [
        'Простое',
        'Сложное',
        'Текстура',
        'Градиент'
    ]

    print("=== Анализ зависимости от коэффициента обучения ===")
    analyze_learning_rate_dependency('test_images/blackbuck.bmp')

    print("\n=== Анализ зависимости от коэффициента сжатия ===")
    analyze_compression_coef_dependency('test_images/blackbuck.bmp')

    print("\n=== Анализ зависимости от типа изображения ===")
    analyze_image_type_dependency(image_paths, image_names)

    print("\n=== Анализ зависимости от величины ошибки ===")
    analyze_error_threshold_dependency('test_images/blackbuck.bmp')


# Дополнительная функция для анализа прогресса обучения
def analyze_training_progress(
        image_path: str,
        r: int = 4,
        m: int = 4,
        compression_coef: int = 6,
        learning_rate: float = 0.1,
        max_iterations: int = 50
) -> None:
    """
    Анализ прогресса обучения во времени
    """

    def constant_lr_func(_) -> float:
        return learning_rate

    auto_encoder = AutoEncoder(constant_lr_func, constant_lr_func, np.float32)
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

    plt.subplot(1, 2, 1)
    plt.plot(iterations, errors, 'b-', linewidth=2)
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка')
    plt.title('Прогресс обучения')
    plt.grid(True, alpha=0.3)

    plt.subplot(1, 2, 2)
    plt.semilogy(iterations, errors, 'r-', linewidth=2)
    plt.xlabel('Итерация')
    plt.ylabel('Ошибка (лог. шкала)')
    plt.title('Прогресс обучения (лог. шкала)')
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    run_comprehensive_analysis()

    analyze_training_progress('test_images/blackbuck.bmp')