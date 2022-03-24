"""
drawing.py: Drawing class with flood fill functionality
"""
from typing import Sequence

import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import label
from FloodFill.colours import Colours


class Drawing:
    
    def __init__(self, image: np.ndarray):
        self.image = image

    def fill(self, row: int, col: int, rgb: Colours) -> None:
        value = self.image[row, col, :]
        mask = self.get_mask(self.image, value)
        labels, _ = label(mask)
        self.image[labels == labels[row, col]] = rgb.value

    def show(self):
        plt.imshow(self.image)
        plt.show()

    @classmethod
    def from_png(cls, path: str):
        image = imageio.imread(path)
        return cls(image)

    @staticmethod
    def get_mask(image: np.ndarray, value: Sequence) -> np.ndarray:
        if image.shape[-1] != len(value):
            message = "Array dimension mismatch: expected value with " +\
                      f"length {image.shape[-1]}, got {len(value)}"
            raise ValueError(message)
        return np.all(image == value, axis=-1)
