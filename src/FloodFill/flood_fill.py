"""
flood_fill.py: Implement flood fill algorithm
"""
import numpy as np
from typing import Sequence


def get_mask(image: np.array, value: Sequence):
    mask = np.ones(image.shape[1:], dtype=bool)
    for img, val in zip(image, value):
        mask &= img == val
    return mask