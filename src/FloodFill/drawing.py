"""
drawing.py: Drawing class with flood fill functionality.
"""
from typing import Sequence

import imageio
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import label

from src.FloodFill.colours import Colours


class Drawing:
    """
    Class that stores an image array and contains flood fill functionality.
    """
    
    def __init__(self, image: np.ndarray):
        self.image = image

    def fill(self, row: int, col: int, colour: Colours) -> None:
        """
        Flood fill the image array, starting from (row, col) coordinate and 
        filling with the specified colour.
        """
        value = self.image[row, col, :]
        mask = self.get_mask(self.image, value)
        labels, _ = label(mask)
        self.image[labels == labels[row, col]] = colour.value

    def show(self):
        """
        Simple imshow of the image array.
        """
        plt.imshow(self.image)
        plt.show()

    @classmethod
    def from_png(cls, path: str):
        """
        Construct a drawing from a png path.
        """
        image = imageio.imread(path)
        return cls(image)

    @staticmethod
    def get_mask(image: np.ndarray, value: Sequence) -> np.ndarray:
        """
        Get a binary mask for all based on comparison with an input value
        """
        if image.shape[-1] != len(value):
            message = "Array dimension mismatch: expected value with " +\
                      f"length {image.shape[-1]}, got {len(value)}"
            raise ValueError(message)
        return np.all(image == value, axis=-1)
