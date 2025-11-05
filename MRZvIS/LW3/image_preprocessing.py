###############################
# Лабораторная работа №3 по дисциплине МРЗвИС
# Выполнена студентом группы 221701 БГУИР Робилко Тимуром Марковичем
# Файл, содержащий функции для перевода входных данных из/в векторное представление для работы с нейросетью
#

import numpy as np


def split_image(image: np.ndarray, r, m) -> np.ndarray:
    assert image.ndim == 3

    h, w = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]

    num_rows = int(np.ceil(h / r))
    num_cols = int(np.ceil(w / m))
    total_rectangles = num_rows * num_cols

    rectangles = np.zeros((total_rectangles, r, m, channels), dtype=image.dtype)


    rect_idx = 0
    for i in range(num_rows):
        row_start = i * r

        if row_start + r > h:
            row_start = h - r

        for j in range(num_cols):
            col_start = j * m

            if col_start + m > w:
                col_start = w - m

            rect_y_end = row_start + r
            rect_x_end = col_start + m

            rect_height = rect_y_end - row_start
            rect_width = rect_x_end - col_start

            rect = np.zeros((r, m, channels), dtype=image.dtype)
            rect[:rect_height, :rect_width, :] = image[row_start:rect_y_end, col_start:rect_x_end, :]

            rectangles[rect_idx] = rect
            rect_idx += 1

    return rectangles


def combine_image(vectors: np.ndarray, shape: tuple, rm: tuple) -> np.ndarray:
    r, m = rm
    h, w = shape[:2]
    channels = 3

    rectangles = vectors.reshape(-1, r, m, channels)

    num_rows = int(np.ceil(h / r))
    num_cols = int(np.ceil(w / m))

    reconstructed = np.zeros((h, w, channels), dtype=vectors.dtype)

    rect_idx = 0
    for i in range(num_rows):
        row_start = i * r
        if row_start + r > h:
            row_start = h - r

        for j in range(num_cols):
            col_start = j * m
            if col_start + m > w:
                col_start = w - m

            rect_y_end = min(row_start + r, h)
            rect_x_end = min(col_start + m, w)

            rect = rectangles[rect_idx]

            reconstructed[row_start:rect_y_end,
            col_start:rect_x_end, :] = rect[:rect_y_end - row_start, :rect_x_end - col_start, :]

            rect_idx += 1

    return reconstructed


def flatten(rectangles: np.ndarray) -> np.ndarray:
    num_rectangles = rectangles.shape[0]
    flattened = rectangles.reshape(num_rectangles, -1)
    return flattened


def preprocess_image(image: np.ndarray, r, m) -> np.ndarray:
    image = normalize_image(image)
    rectangles = split_image(image, r, m)
    flattened = flatten(rectangles)
    return flattened


def normalize_image(image: np.ndarray) -> np.ndarray:
    image = image.astype(np.float32)
    return 2 * image / 255 - 1


def denormalize_image(image: np.ndarray) -> np.ndarray:
    image = (image + 1) * 255 / 2
    image = np.clip(image, 0, 255)
    return image.astype(np.uint8)
