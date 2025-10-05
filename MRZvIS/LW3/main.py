###############################
# Лабораторная работа №3 по дисциплине МРЗвИС
# Выполнена студентом группы 221701 БГУИР Робилко Тимуром Марковичем
#
import math
from abc import ABC
from typing import Tuple, Iterator

import cv2
import numpy as np

from image_preprocessing import combine_image, preprocess_image, denormalize_image, split_image


class Dataloader(ABC):
    def __getitem__(self, idx):
        pass

    def __len__(self):
        pass

    def __iter__(self) -> Iterator[np.array]:
        pass


class ImageDataLoader(Dataloader):
    def __init__(self, image_paths: list[str], r, m):
        self.items = []

        for path in image_paths:
            image = cv2.imread(path)
            vectors = preprocess_image(image, r, m)

            for vec in vectors:
                self.items.append(vec)

    def __getitem__(self, idx):
        return self.items[idx]

    def __len__(self):
        return len(self.items)

    def __iter__(self) -> Iterator[np.array]:
        return iter(self.items)


class AutoEncoder:
    def __init__(self):
        self.WF = None
        self.WB = None

    def init_weights(self, input_length: int, compression_coef: float, wf: np.ndarray | None = None, wb: np.ndarray | None = None):
        input_layer_size = input_length
        hidden_layer_size = int(input_length / compression_coef)

        self.WF = wf if wf is not None else np.random.uniform(low=-1, high=1, size=(input_layer_size, hidden_layer_size)).astype(np.float32)
        self.WB = wb if wb is not None else np.random.uniform(low=-1, high=1, size=(hidden_layer_size, input_layer_size)).astype(np.float32)

        print(f"Encoder weights size: {int((self.WF.nbytes + self.WB.nbytes) / 1_000_000)} MB ({self.WF.dtype}, {self.WF.shape})")

    def encode(self, x: np.array) -> np.array:
        assert self.WF is not None
        assert len(x) == self.WF.shape[0], f"{self.WF.shape}, {len(x)}"

        return (x @ self.WF).astype(x.dtype)

    def decode(self, x: np.array) -> np.array:
        assert self.WB is not None
        assert len(x) == self.WB.shape[0], f"{self.WB.shape}, {len(x)}"

        return (x @ self.WB).astype(x.dtype)

    def train(self, data_loader: Dataloader, e_max: float, t_max: int | None = None) -> None:
        assert e_max > 0
        t = 1

        ee = None
        while (ee is None or math.isnan(ee) or ee > e_max) and (t_max is None or t < t_max):
            for X in data_loader:
                Y = self.encode(X)
                XX = self.decode(Y)
                dX = XX - X

                dot_y = np.dot(Y, Y)
                ab = min(1 / dot_y, 1.5)  # Ограничиваем learning rate
                # ab = 0.1

                grad_WB = ab * X * dX
                self.WB = self.WB - np.clip(grad_WB, -1.0, 1.0)

                dot_x = np.dot(X, X)
                af = min(1 / dot_x, 1.5)
                # af = 0.1

                grad_WF = np.transpose(af * X * dX * self.WB)
                self.WF = self.WF - np.clip(grad_WF, -1.0, 1.0)

                self.WF = np.clip(self.WF, -1.0, 1.0)
                self.WB = np.clip(self.WB, -1.0, 1.0)

            # evaluate
            source = np.asarray(data_loader)
            decoded = (source @ self.WF) @ self.WB
            ee = 0.5 * np.sum((decoded - source) ** 2)

            print(f"epoch: {t}, error: {ee}")
            t += 1

        # todo


class CompressedImage:
    def __init__(self, data: np.ndarray, original_shape: Tuple, wb: np.ndarray, rm: Tuple):
        self.original_shape = original_shape
        self.rm = rm
        self.data = data
        self.wb = wb

    @property
    def nbytes(self) -> int:
        return self.data.nbytes + self.wb.nbytes + 4 * 2

    @classmethod
    def create(cls, image: np.ndarray, encoder: AutoEncoder, r, m) -> "CompressedImage":
        assert image.ndim == 3

        original_shape = image.shape[:2]
        vectors = preprocess_image(image, r, m)
        compressed_vectors = np.asarray([encoder.encode(x) for x in vectors])

        return cls(compressed_vectors, original_shape, encoder.WB, (r, m))

    def decompress(self) -> np.ndarray:
        decoder = AutoEncoder()
        decoder.WB = self.wb

        decompressed_vectors = np.array([decoder.decode(x) for x in self.data])
        image = combine_image(decompressed_vectors, self.original_shape, self.rm)
        image = denormalize_image(image)

        return image


if __name__ == '__main__':
    COMPRESSION_COEFFICIENT = 1
    (R, M) = (32, 32)

    img = cv2.imread('512_1.bmp')
    # sh = img.shape[:2]
    #
    # vec = split_image(img, R, M)
    #
    # img = combine_image(vec, sh)
    # cv2.imshow("ds", img)
    # cv2.waitKey(0)
    # exit()

    auto_encoder = AutoEncoder()
    auto_encoder.init_weights(3 * R * M, COMPRESSION_COEFFICIENT)

    image_paths = ['black.png']
    loader = ImageDataLoader(image_paths, R, M)
    auto_encoder.train(loader, 10, 100)

    compressed = CompressedImage.create(img, auto_encoder, R, M)

    orig_bytes = img.astype(np.float32).nbytes
    print(orig_bytes, compressed.nbytes)
    print(orig_bytes / compressed.nbytes)

    decompressed = compressed.decompress()
    # result_vis = cv2.hconcat([img, decompressed])
    cv2.imshow("1", img)
    cv2.imshow("2", decompressed)
    # cv2.imshow('result', result_vis)
    cv2.waitKey(0)
