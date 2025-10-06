###############################
# Лабораторная работа №3 по дисциплине МРЗвИС
# Выполнена студентом группы 221701 БГУИР Робилко Тимуром Марковичем
# Основной файл программы, содержащий реализацию автоэнкодера и класса сжатого изображения
#
import math
from typing import Tuple, Iterator, Callable

import cv2
import numpy as np

from image_preprocessing import preprocess_image, denormalize_image, combine_image


class ImageDataLoader:
    def __init__(self, image_path: str, r: int, m: int) -> None:
        self.items = []

        image = cv2.imread(image_path)
        vectors = preprocess_image(image, r, m)

        for vec in vectors:
            self.items.append(vec)

    def __getitem__(self, idx) -> np.array:
        return self.items[idx]

    def __len__(self) -> int:
        return len(self.items)

    def __iter__(self) -> Iterator[np.array]:
        return iter(self.items)


class AutoEncoder:
    def __init__(self, af_func: Callable[[np.ndarray], float], ab_func: Callable[[np.ndarray], float], dtype):
        self.WF = None
        self.WB = None
        self.__af_func = af_func
        self.__ab_func = ab_func
        self.__dtype = dtype

    def init_weights(self, input_length: int, compression_coef: float, wf: np.ndarray | None = None, wb: np.ndarray | None = None):
        input_layer_size = input_length
        hidden_layer_size = int(input_length / compression_coef)

        self.WF = wf if wf is not None else np.random.uniform(low=-1, high=1, size=(input_layer_size, hidden_layer_size)).astype(self.__dtype)
        self.WB = wb if wb is not None else np.random.uniform(low=-1, high=1, size=(hidden_layer_size, input_layer_size)).astype(self.__dtype)

        print(f"Encoder weights size: {(self.WF.nbytes + self.WB.nbytes) / 1_000:.2f} KB ({self.WF.dtype}, {self.WF.shape})")

    def encode(self, x: np.array) -> np.array:
        return x @ self.WF

    def decode(self, x: np.array) -> np.array:
        return x @ self.WB

    def train(self, data_loader: ImageDataLoader, e_max: float, t_max: int | None = None) -> Iterator[tuple]:
        t = 1

        weight_min = -16.0
        weight_max = 16.0

        ee = float('inf')
        while (math.isnan(ee) or ee > e_max) and (t_max is None or t < t_max):
            for X in data_loader:
                Y = self.encode(X)
                XX = self.decode(Y)
                dX = XX - X

                ab = self.__ab_func(Y)

                # dL/dWB = Y^T * dX
                grad_WB = ab * np.outer(Y, dX)
                self.WB = self.WB - grad_WB

                af = self.__af_func(X)

                # dL/dWF = X^T * (dX * WB^T)
                grad_WF = af * np.outer(X, dX @ self.WB.T)
                self.WF = self.WF - grad_WF

                self.WF = np.clip(self.WF, weight_min, weight_max).astype(self.__dtype)
                self.WB = np.clip(self.WB, weight_min, weight_max).astype(self.__dtype)

            source = np.asarray(data_loader)
            decoded = (source @ self.WF) @ self.WB
            ee = 0.5 * np.sum((decoded - source) ** 2)

            yield t, ee
            t += 1


class CompressedImage:
    def __init__(self, image: np.ndarray, encoder: AutoEncoder, rm: Tuple):
        assert image.ndim == 3

        self.__original_shape = image.shape
        self.__rm = rm
        self.__encoder = encoder

        vectors = preprocess_image(image, self.__rm[0], self.__rm[1])

        self.__data = np.asarray([self.__encoder.encode(x) for x in vectors])

    @property
    def nbytes(self) -> int:
        return self.__data.nbytes + self.__encoder.WB.nbytes + 4 * 2

    def decompress(self) -> np.ndarray:
        decompressed_vectors = np.array([self.__encoder.decode(x) for x in self.__data])
        image = combine_image(decompressed_vectors, self.__original_shape, self.__rm)
        image = denormalize_image(image)

        return image


if __name__ == '__main__':
    (R, M) = (4, 4)
    LEARNING_RATE = 0.1
    COMPRESSION_COEFFICIENT = 6
    T_MAX = 10
    E_MAX = 10


    img_path = 'test_images/blackbuck.bmp'
    img = cv2.imread(img_path, cv2.IMREAD_COLOR_BGR)


    def adaptive_af_func(arr) -> float:
        return 1 / np.dot(arr, arr)

    def adaptive_ab_func(arr) -> float:
        return 1 / np.dot(arr, arr)

    def constant_lr_func(_) -> float:
        return LEARNING_RATE

    auto_encoder = AutoEncoder(adaptive_af_func, adaptive_ab_func, np.float32)
    auto_encoder.init_weights(3 * R * M, COMPRESSION_COEFFICIENT)

    loader = ImageDataLoader(img_path, R, M)

    for epoch, epoch_error in auto_encoder.train(loader, E_MAX, T_MAX):
        print(f"Epoch {epoch}, Error: {epoch_error:.6f}")

    compressed = CompressedImage(img, auto_encoder, (R, M))

    orig_bytes = img.nbytes
    actual_compression_ratio = orig_bytes / compressed.nbytes


    decompressed = compressed.decompress()

    print("Source image bytes: ", orig_bytes)
    print("Compressed image bytes: ", compressed.nbytes)
    print("Actual compression ratio: ", actual_compression_ratio)

    result_vis = cv2.hconcat([img, decompressed])
    cv2.imshow('result', result_vis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
