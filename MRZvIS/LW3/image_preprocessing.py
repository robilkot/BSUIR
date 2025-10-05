from typing import Tuple

import numpy as np


def split_image(image: np.ndarray, r, m) -> np.ndarray:
    assert image.ndim == 3

    H, W = image.shape[:2]
    channels = 1 if len(image.shape) == 2 else image.shape[2]

    # Calculate number of rectangles needed
    num_rows = int(np.ceil(H / r))
    num_cols = int(np.ceil(W / m))
    total_rectangles = num_rows * num_cols

    # Initialize array to store rectangles
    rectangles = np.zeros((total_rectangles, r, m, channels), dtype=image.dtype)


    rect_idx = 0
    for i in range(num_rows):
        row_start = i * r

        if row_start + r > H:
            row_start = H - r

        for j in range(num_cols):
            col_start = j * m

            if col_start + m > W:
                col_start = W - m

            rect_y_end = row_start + r
            rect_x_end = col_start + m

            rect_height = rect_y_end - row_start
            rect_width = rect_x_end - col_start

            rect = np.zeros((r, m, channels), dtype=image.dtype)
            rect[:rect_height, :rect_width, :] = image[row_start:rect_y_end,
                                                 col_start:rect_x_end, :]

            rectangles[rect_idx] = rect
            rect_idx += 1

    return rectangles


def combine_image(vectors: np.ndarray, shape: Tuple, rm: Tuple) -> np.ndarray:
    """
    Combines rectangular patches back into a complete image.

    Args:
        vectors: Array containing the rectangular patches to combine
        shape: Original shape of the image (height, width, channels)
        rm: Tuple containing (rows, cols) for rectangle dimensions

    Returns:
        Reconstructed image as a numpy array
    """
    r, m = rm
    H, W = shape[:2]
    channels = 1 if len(shape) == 2 else shape[2]

    # Reshape vectors back to rectangles
    rectangles = vectors.reshape(-1, r, m, channels)

    # Calculate grid dimensions
    num_rows = int(np.ceil(H / r))
    num_cols = int(np.ceil(W / m))

    # Initialize empty image
    reconstructed = np.zeros((H, W, channels), dtype=vectors.dtype)

    # Fill in rectangles
    rect_idx = 0
    for i in range(num_rows):
        row_start = i * r
        if row_start + r > H:
            row_start = H - r

        for j in range(num_cols):
            col_start = j * m
            if col_start + m > W:
                col_start = W - m

            rect_y_end = min(row_start + r, H)
            rect_x_end = min(col_start + m, W)

            # Extract current rectangle
            rect = rectangles[rect_idx]

            # Place rectangle in correct position
            reconstructed[row_start:rect_y_end,
            col_start:rect_x_end, :] = \
                rect[:rect_y_end - row_start,
                :rect_x_end - col_start, :]

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
    return image.astype(np.uint8)
